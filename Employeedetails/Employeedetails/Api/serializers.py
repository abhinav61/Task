from django.contrib.auth.models import User
from rest_framework import serializers
from .views import profile_reg
from rest_auth.serializers import PasswordResetSerializer


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['first_name','last_name','company_name','email_id','phone_number','password','confirm_password']
        extra_kwargs = {'password':{'write_only':True,'required':True},'confirm_password':{'write_only':True,'required':True}}

        def create(Self,validated_data):
            user = User.objects.create_user(**validated_data)
            return user
class CustomPasswordResetSerializer(PasswordResetSerializer):
    email = serializers.EmailField()
    password_reset_form_class = ResetPasswordForm

    def validate_email(self, value):
        # Create PasswordResetForm with the serializer
        self.reset_form = self.password_reset_form_class(data=self.initial_data)
        if not self.reset_form.is_valid():
            raise serializers.ValidationError(self.reset_form.errors)

        ###### FILTER YOUR USER MODEL ######
        if not get_user_model().objects.filter(email=value).exists():
            raise serializers.ValidationError(_('Invalid e-mail address'))

        return value

    def save(self):
        request = self.context.get('request')
        # Set some values to trigger the send_email method.
        opts = {
            'use_https': request.is_secure(),
            'from_email': getattr(settings, 'DEFAULT_FROM_EMAIL'),
            'request': request,
        }
        opts.update(self.get_email_options())
        self.reset_form.save(**opts)