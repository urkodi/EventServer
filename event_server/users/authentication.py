from rest_framework.exceptions import AuthenticationFailed
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.exceptions import InvalidToken, TokenError


class JWTCookieAuthentication(JWTAuthentication):
    def authenticate(self, request):
        access_token = request.COOKIES.get("access_token")

        if access_token:
            request.META["HTTP_AUTHORIZATION"] = f"Bearer {access_token}"

        try:
            return super().authenticate(request)
        except (InvalidToken, TokenError, AuthenticationFailed) as e:
            raise e
