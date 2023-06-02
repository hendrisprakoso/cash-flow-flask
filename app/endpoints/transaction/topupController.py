import requests
from app import app
from flask import request

from app.utility.response import responseJson
from app.repository.transaction.topupRepo import *
from app.middleware.token import token_validation

@app.route('/topup-saldo', methods=['POST'])
@token_validation
def topupController():
    try:

        request_json = request.get_json()

        print('request_json : ', request_json)
        topup = topupSaldoUser(request_json['topup'], request_json['account_id'])
        print('topup : ', topup)
        if topup :
            return responseJson(200, {'method' : request.method, 'status' : True, 'message' : f'Topup Successfully!'})
        
        return responseJson(500, {'method' : request.method, 'status' : True, 'message' : f'Topup Failed! {str(error)}'})
    except Exception as error:
        return responseJson(500, {'method' : request.method, 'status' : False, 'message' : f'[ERROR] : {str(error)}', 'data' : []})


@app.route('/payment', methods=['POST'])
@token_validation
def paymentProcess():
    try:

        request_json = request.get_json()
        print('request_json : ', request_json)

        payment = paymentProduct(request_json['payment_method'], request_json['payment'], request_json['account_id'],
                                request_json['payment_receipt'], request_json['notes'])
        print('payment : ', payment)
        if payment:
            return responseJson(200, 
                                {'method' : request.method, 'status' : True, 
                                 'message' : f'Payment Successfully!'})
        else:
            return responseJson(500, 
                                {'method' : request.method, 'status' : True, 
                                 'message' : f'Payment Failed! {str(error)}'})
    except Exception as error:
        return responseJson(500, 
                            {'method' : request.method, 'status' : False, 
                             'message' : f'[ERROR] : {str(error)}', 'data' : []})