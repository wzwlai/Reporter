import re
from rest_framework import serializers
from .models import Reporters
from rest_framework_jwt.settings import api_settings
from django.conf import settings


class CreateUserSerializer(serializers.ModelSerializer):
    """创建用户序列化器"""

    password2 = serializers.CharField(label='确定密码', write_only=True)
    token = serializers.CharField(label='登录状态token', read_only=True)  # 增加token字段

    class Meta:
        model = Reporters
        fields = ('id', 'name', 'password', 'password2', 'mobile', 'token')
        extra_kwargs = {
            'username': {
                'min_length': 3,
                'max_length': 10,
                'error_messages': {
                    'min_length': '仅允许3-10个字符的用户名',
                    'max_length': '仅允许3-10个字符的用户名'
                }
            },
            'password': {
                'write_only': True,
                'min_length': 8,
                'max_length': 20,
                'error_messages': {
                    'min_length': '仅允许8-20个字符的密码',
                    'max_length': '仅允许8-20个字符的密码',
                }
            }
        }

    def validate_mobile(self, value):
        """验证手机号"""
        # value会自动获取方法名后的mobile
        if not re.match(r'^1[3-9]\d{9}$', value):
            raise serializers.ValidationError('手机号格式错误')
        return value

    def validate(self, attrs):
        # 判断两次密码
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError('两次密码不一致')

        return attrs

    def create(self, validated_data):
        """创建用户"""
        # 移除数据库模型类中不存在的属性
        del validated_data['password2']
        user = super().create(validated_data)

        # 调用django的认证系统加密密码
        user.set_password(validated_data['password'])
        user.save()

        # 补充生成记录登录状态的token
        jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
        jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER
        payload = jwt_payload_handler(user)
        token = jwt_encode_handler(payload)
        user.token = token

        return user


class UserDetailSerializer(serializers.ModelSerializer):
    """用户详细信息序列化器"""
    class Meta:
        model = Reporters
        fields = ('id', 'name', 'mobile')


class UserQuerySerializer(serializers.ModelSerializer):
    """通过记者查询的序列化器"""
    searchTerm = serializers.CharField(label='记者名', write_only=True)

    class Meta:
        model = Reporters
        fields = ('id', 'name', 'mobile', 'Industry_Id', 'Company_Id', 'Manuscript_Id')

        def validate_user_id(self, value):
            try:
                reporter = Reporters.objects.filter(name=value['searchTerm'])
                if len(reporter)==0:
                    reporter = Reporters.objects.filter(mobile=value['searchTerm'])
            except Exception as f:
                raise serializers.ValidationError('用户不存在')

            # for industryId in reporter:

