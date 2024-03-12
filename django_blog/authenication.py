from django.contrib.auth.backends import BaseBackend
from django.contrib.auth import get_user_model
from django.db.models import Q
User = get_user_model()

class EmailBackend(BaseBackend):
    def authenticate(self, request, email=None, password=None, **kwargs):
        user = User.objects.filter(Q(email=email) | Q(username=email)).first()

        if user is not None and user.check_password(password):
            return user

        return None

    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None