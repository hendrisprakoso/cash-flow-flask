from app import mysql
from app.utility.response import rows_to_list


def getDataUsers(p_fil_role, p_fil_status):
	try:
		cur = mysql.connection.cursor()

		str_fil_status = ''
		if p_fil_role not in ('', None):
			str_fil_status += ''' where al.status = {} '''.format(p_fil_status)

		str_fil_role = ''
		if p_fil_role not in ('', None):
			str_fil_role += ''' AND al.role = {} '''.format(p_fil_role)

		sql_query = '''
						select
							al.id_account as account_id,
							al.username as account_username,
							al.name as account_name,
							al.status as account_status,
							al.`role` as account_role,
							ar.desc_role as role_desc,
							ad.balance as balance
						from
							account_list al
						left join account_role ar on
							al.`role` = ar.`role`
						left join account_detail ad on
							al.id_account = ad.id_account
						{}{}
					'''.format(str_fil_status, str_fil_role)

		cur.execute(sql_query)
		return rows_to_list(cur.description, cur.fetchall())
	except Exception as error:
		raise error
	finally:
		if(cur):
			cur.close()

def getDataUserByUsername(p_username):
	try:
		cur = mysql.connection.cursor()
		sql_query = '''
						select
							al.id_account as account_id,
							al.username as account_username,
							al.password as account_password,
							al.name as account_name,
							al.status as account_status,
							al.`role` as account_role,
							ar.desc_role as role_desc,
							ad.balance as balance
						from
							account_list al
						left join account_role ar on
							al.`role` = ar.`role`
						left join account_detail ad on
							al.id_account = ad.id_account
						where username = %s
					'''
		cur.execute(sql_query, (p_username, ))
		return rows_to_list(cur.description, cur.fetchall())
	except Exception as error:
		raise error
	finally:
		if(cur):
			cur.close()

def userIsExist(p_username):
	try:
		cur = mysql.connection.cursor()
		sql_query = '''
						select
							case
								when count(0) >= 1 then true
								else false
							end as is_exists
						from
							account_list
						where
							username = %s
					'''
		cur.execute(sql_query, (p_username,))
		return rows_to_list(cur.description, cur.fetchall())
	except Exception as error:
		raise error
	finally:
		if(cur):
			cur.close()

def insertDataUser(p_username, p_password, p_name, p_role):
	try:
		cur = mysql.connection.cursor()
		sql_query = '''
						INSERT INTO account_list
						(username, password, name, status, `role`, created_date)
						VALUES(%s, %s, %s, 1, %s, now())
					'''
		cur.execute(sql_query, (p_username, p_password, p_name, p_role))
		cur.connection.commit()
		return True
	except Exception as error:
		raise error
	finally:
		if(cur):
			cur.close()


def updateDataUser(p_password, p_name, p_status, p_role, p_username):
	try:
		cur = mysql.connection.cursor()
		sql_query = '''
						UPDATE cash_flow.account_list SET 
							password = %s, 
							name = %s, 
							status = %s, 
							`role` = %s
						WHERE username = %s
					'''
		cur.execute(sql_query, (p_password, p_name, p_status, p_role, p_username))
		cur.connection.commit()
		return True
	except Exception as error:
		raise error
	finally:
		if(cur):
			cur.close()

def deleteDataUser(p_username):
	try:
		cur = mysql.connection.cursor()
		sql_query = '''
						DELETE FROM cash_flow.account_list
						WHERE username = %s
					'''
		cur.execute(sql_query, (p_username,))
		cur.connection.commit()
		return True
	except Exception as error:
		raise error
	finally:
		if(cur):
			cur.close()