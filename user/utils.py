import jwt
import json

from django.http            import JsonResponse
from django.core.exceptions import ObjectDoesNotExist

from my_settings import SECRET,ALGORITHM
from user.models import User

def user_decorator(func):
    def wrapper(self,request, *args, **kwargs):
        try:
            token = request.headers.get('Authorization', None)
            payload = jwt.decode(token, SECRET["secret"], ALGORITHM["algorithm"])
            user = User.objects.get(email=payload['email'])
            request.user = user

        except jwt.exceptions.DecodeError:
            return JsonResponse({'message' : 'INVALID_TOKEN' }, status=400)

        except User.DoesNotExist:
            return JsonResponse({'message' : 'INVALID_USER'}, status=400)

        return func(self, request, *args, **kwargs)

    return wrapper
