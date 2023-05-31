import requests
from app import app
from flask import request

from app.utility.response import responseJson
from app.repository.report.reportTransactionRepo import *
from app.repository.users.usersRepo import userIsExist

@app.route('/report', methods=['POST'])
def reportTransactions():
    try:
        request_json = request.get_json()

        check_data_exists = userIsExist(request_json['username'])[0]
        if check_data_exists['is_exists'] == 0:
            return responseJson(200, {'method' : request.method, 'status' : False, 'message' : 'Username is not Exists!'})    
        else:
            data_report_transaction = getDataReportTransaction(request_json['account_id'])
                        
            return responseJson(200, {'method' : request.method, 'status' : True, 'message' : f'Topup Successfully!', 'data' : data_report_transaction})
    except Exception as error:
        return responseJson(500, {'method' : request.method, 'status' : False, 'message' : f'[ERROR] : {str(error)}', 'data' : []})
