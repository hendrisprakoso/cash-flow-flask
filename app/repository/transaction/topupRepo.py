from app import mysql
from app.utility.response import rows_to_list

def topupSaldoUser(p_topup, p_id_account):
	try:
		cur = mysql.connection.cursor()
		sql_query_topup = '''
								update account_detail set 
									balance = balance + {}, 
									last_modified = curdate()
								where id_account = {}
						'''.format(p_topup, p_id_account)
		cur.execute(sql_query_topup)
		
		sql_query_log = '''
							INSERT INTO cash_flow.cash_flow
							(`type`, credit, id_account, notes)
							VALUES('5', {}, {}, 'TOPUP')

						'''.format(p_topup, p_id_account)
		cur.execute(sql_query_log)
		
		cur.connection.commit()
		return True
	except Exception as error:
		raise error
	finally:
		if(cur):
			cur.close()

def paymentProduct(p_payment_method, p_tot_payment, p_id_account, p_destination, p_notes, p_category):
	try:
		cur = mysql.connection.cursor()
		sql_query_topup = '''
								update account_detail set 
									balance = balance - {}, 
									last_modified = curdate()
								where id_account = {}
						'''.format(p_tot_payment, p_id_account)
		cur.execute(sql_query_topup)
		
		sql_query_log = '''
							INSERT INTO cash_flow.cash_flow
							(`type`, destination, debit, id_account, notes, category)
							VALUES('{}', '{}', {}, {}, '{}', {})

						'''.format(p_payment_method, p_destination, p_tot_payment, p_id_account, p_notes, p_category)
		cur.execute(sql_query_log)
		
		cur.connection.commit()
		return True
	except Exception as error:
		raise error
	finally:
		if(cur):
			cur.close()