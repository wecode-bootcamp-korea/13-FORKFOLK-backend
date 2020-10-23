import json
import bcrypt
import jwt

from django.views import View
from django.http  import JsonResponse,HttpResponse

from user.models  import User


class SignUpView(View):
    def post(self,request):
        try:
            data     = json.loads(request.body)
            name     = data['name']
            email    = data['email']
            password = data['password']
            if re.match('^[a-zA-Z0-9+-_.]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$', email) == None:
                return JsonResponse({"message":"User is not valid."},status=400)
            else:
                hashed_password  = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
            decoded_password = hashed_password.decode('utf-8') 

            User(
                name     = name,
                email    = email,
                password = decoded_password
                ).save()
            return JsonResponse({'message':'SUCCESS'},status=200)

        except KeyError:
            return JsonResponse({"message": "KEY_ERROR"}, status=400)
