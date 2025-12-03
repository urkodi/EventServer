from rest_framework.exceptions import AuthenticationFailed
from rest_framework_simplejwt.tokens import AccessToken
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.exceptions import InvalidToken, TokenError
from users.models import User

class JWTCookieAuthentication(JWTAuthentication):
    def authenticate(self, request):
        access_token = request.COOKIES.get("access_token")
        
        if not access_token:
            return None

        request.META["HTTP_AUTHORIZATION"] = f"Bearer {access_token}"

        try:
            token = AccessToken(access_token)

            try:
                user = User.objects.get(id=token['user_id'])
            except User.DoesNotExist:
                raise AuthenticationFailed('User not found', code='user_not_found')
            
            return (user, token)
        except (InvalidToken, TokenError, AuthenticationFailed) as e:
            raise e
