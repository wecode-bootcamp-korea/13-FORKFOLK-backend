import json
import bcrypt
import jwt
import re

from django.db.models import Q
from django.views     import View
from django.http      import JsonResponse,HttpResponse

from user.models      import User
from my_settings      import SECRET,ALGORITHM
from user.utils       import user_decorator     

class SignUpView(View):
    def post(self,request):
        try:
            data     = json.loads(request.body)
            email    = data['email']
            password = data['password']

            if User.objects.filter(email=email).exists():
                return JsonResponse({'message':'Existing user.'},status=409)

            if not re.match('^[a-zA-Z0-9+-_.]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$', email):
                return JsonResponse({'message':'Invalid Email'},status=400)

            hashed_password  = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
            decoded_password = hashed_password.decode('utf-8')

            User.objects.create(
                email    = email,
                password = decoded_password
            )

            return JsonResponse({'message':'SUCCESS'},status=201)

        except KeyError:
            return JsonResponse({'message': 'KEY_ERROR'}, status=400)
        except ValueError:
            return JsonResponse({'message':'VALUE_ERROR'},status=400)
        except:
            return jsonResponse({'dd':'dd'},status=400)

class SignInView(View):
    def post(self,request):
        try:
            data = json.loads(request.body)

            if User.objects.filter(email=data['email']).exists():
                user = User.objects.get(email=data['email'])
                password = data['password']
                db_password = user.password.encode()

                if bcrypt.checkpw(password.encode(),db_password):
                    access_token = jwt.encode({'id':user.id},SECRET['secret'],ALGORITHM['algorithm'])
                    decoded_token = access_token.decode()

                    return JsonResponse(
                    {'message':'SUCCESS','TOKEN':decoded_token}, status=201)

                else:
                    return JsonResponse({'message':'PASSWORD_ERROR'}, status=400)

            else:
                return JsonResponse({'message':'INVALID_USER'}, status=401)

        except KeyError:
            return JsonResponse({'message': 'KEY_ERROR'}, status=400)

        except ValueError:
            return JsonResponse({'message': 'VALUE_ERROR'}, status=400)
