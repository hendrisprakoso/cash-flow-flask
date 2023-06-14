import jwt
from flask import request
from functools import wraps
from datetime import datetime

from app import app
from app.utility.response import responseJson
from app.repository.users.usersRepo import getDataUserByUsername


def token_validation(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        try:
            
            ''' GET Request Header '''
            token = request.headers.get('token', None)
            print('token : ', token)

            ''' Process Authorized '''
            token_decode = jwt.decode(token, app.config['SALT_JWT_CF'], app.config['JWT_ALGORITHM'])
            print('token_decode : ', token_decode)

            ''' Check Expired Token '''
            expired_date = datetime.strptime(token_decode['expired'], '%d-%m-%Y %H:%M')
            if datetime.now() > expired_date:
                return responseJson(401, {'status' : False, 'message' : f'Token is expired!'})

            ''' Check Account is available '''
            check_user = getDataUserByUsername(token_decode['username'])
            print('check_user : ', check_user)
            if len(check_user) == 0:
                return responseJson(404, {'status' : False, 'message' : f'Account is not found!'})
            
            elif len(check_user) > 0 and check_user[0]['account_status'] != 1:
                return responseJson(404, {'status' : False, 'message' : f'Account is not active!'})
            
            elif check_user[0]['account_id'] != token_decode['account_id']:
                return responseJson(404, {'status' : False, 'message' : f'Account is not valid!'})

        except Exception as error:
            return responseJson(500, {'status' : False, 'message' : f'[ERROR] token validation : {str(error)}'})
        
        return f(*args, **kwargs)
    return wrapper