from rest_framework.authentication import TokenAuthentication
from rest_framework.exceptions import AuthenticationFailed


class CustomTokenAuthentication(TokenAuthentication):
    def has_permission(self, request, view):
        if not request.user.is_authenticated:
            raise AuthenticationFailed('You must be authenticated to access this resource.')

        return True
