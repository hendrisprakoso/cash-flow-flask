import requests
from app import app
from flask import request

from app.utility.response import responseJson
from app.repository.users.usersRepo import *
from app.middleware.encrypt import encryptPassword


def passwordIsCorrect(p_username, p_password):
    try:
        user = getDataUserByUsername(p_username)
        if len(user) > 0:
            v_password = user[0]['account_password']
            if v_password == encryptPassword(p_password):
                return {'status' : True, 'status_code' : 200, 'message' : f'Password is Match!', 'data' : user}
            else:
                return {'status' : False, 'status_code' : 401, 'message' : f'Username and Password is not Match!', 'data' : []}
        else:
            return {'status' : False, 'status_code' : 404, 'message' : f'Account is not found!', 'data' : []}
            
    except Exception as error:
        return {'status' : False, 'message' : f'[ERROR] check password Failed! {str(error)}'}


@app.route('/users', methods=['GET', 'POST', 'PUT', 'DELETE'])
@app.route('/users/', methods=['GET', 'POST', 'PUT', 'DELETE'])
def usersController():
    if request.method == 'GET':
        try:

            v_fil_role = request.args.get("role", None)
            v_fil_status = request.args.get("status", None)

            if v_fil_role not in (None, '') and v_fil_status in ('', None):
                return responseJson(200, {'method' : request.method, 'status' : False, 'message' : f'Pastikan status juga terisi!', 'data' : []})

            data_user = getDataUsers(v_fil_role, v_fil_status)

            return responseJson(200, {'method' : request.method, 'status' : True, 'message' : 'in users controller!', 'data' : data_user})
        except Exception as error:
            return responseJson(500, {'method' : request.method, 'status' : False, 'message' : f'[ERROR] : {str(error)}', 'data' : []})

    elif request.method == 'POST':
        try:            
            request_json = request.get_json()

            check_data_exists = userIsExist(request_json['username'])[0]
            if check_data_exists['is_exists'] == 1:
                return responseJson(200, {'method' : request.method, 'status' : False, 'message' : 'Username is Exists!'})    
            else:
                ins_user = insertDataUser(request_json['username'], encryptPassword(request_json['password']), request_json['name'], request_json['role'])
                if ins_user:
                    return responseJson(200, {'method' : request.method, 'status' : True, 'message' : 'Add account Successfully!'})        
                else:
                    return responseJson(200, {'method' : request.method, 'status' : False, 'message' : 'Failed! Error Database.'})
        except Exception as error:
            return responseJson(500, {'method' : request.method, 'status' : False, 'message' : f'[ERROR] : {str(error)}', 'data' : []})

    elif request.method == 'PUT':
        try:
            request_json = request.get_json()

            check_data_exists = userIsExist(request_json['username'])[0]
            if check_data_exists['is_exists'] == 0:
                return responseJson(200, {'method' : request.method, 'status' : False, 'message' : 'Username is not Exists!'})    
            else:
                upd_user = updateDataUser(encryptPassword(request_json['password']), request_json['name'], request_json['status'], request_json['role'], request_json['username'])
                if upd_user:
                    return responseJson(200, {'method' : request.method, 'status' : True, 'message' : 'Update account Successfully!'})        
                else:
                    return responseJson(200, {'method' : request.method, 'status' : False, 'message' : 'Failed! Error Database.'})
        except Exception as error:
            return responseJson(500, {'method' : request.method, 'status' : False, 'message' : f'[ERROR] : {str(error)}', 'data' : []})

    elif request.method == 'DELETE':
        try:
            request_json = request.get_json()

            del_user = deleteDataUser(request_json['username'])
            if del_user:
                return responseJson(200, {'method' : request.method, 'status' : True, 'message' : 'Account Deleted! Successfully.'})        
            else:
                return responseJson(200, {'method' : request.method, 'status' : False, 'message' : 'Failed! Error Database.'})
            
        except Exception as error:
            return responseJson(500, {'method' : request.method, 'status' : False, 'message' : f'[ERROR] : {str(error)}', 'data' : []})
    
    else:
        return responseJson(405, {'message' : 'Method not allowed!'})


@app.route('/users/<id>', methods=['POST'])
def userControllerbyId(id):
    data_user = getDataUserByUsername(id)
    return responseJson(200, {'status' : True, 'message': 'success', 'data' : data_user})


@app.route('/user/login', methods=['POST'])
@app.route('/user/login/', methods=['POST'])
def userLogin():
    request_json = request.get_json()

    passwrod_is_correct = passwordIsCorrect(request_json['username'], request_json['password'])
    if passwrod_is_correct['status_code'] == 401:
        return responseJson(401, {'status' : False, 'message' : passwrod_is_correct['message']})
    
    elif passwrod_is_correct['status_code'] == 404:
        return responseJson(404, {'status' : False, 'message' : passwrod_is_correct['message']})
    
    else:
        return responseJson(passwrod_is_correct['status_code'], {'status' : False, 'message' : passwrod_is_correct['message'], 'data' : passwrod_is_correct['data']})

