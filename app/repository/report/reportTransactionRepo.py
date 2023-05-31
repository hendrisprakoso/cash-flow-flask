from app import mysql
from app.utility.response import rows_to_list


def getDataReportTransaction(p_id_account):
	try:
		cur = mysql.connection.cursor()
		sql_query = '''
						select
                            cf.`date` as tanggal_transaksi, tt.desc_type as type_transaksi, al.name, coalesce(cf.debit, 0) as pengeluaran, 
			                coalesce(cf.credit, 0) as pemasukan,  cf.notes as keterangan
                        from
                            cash_flow cf
                        left join type_transaction tt on
                            cf.`type` = tt.id_type
                        left join account_list al on
                            al.id_account = cf.id_account
                        where
                            cf.id_account = {}
                        order by
                            cf.id desc
					'''.format(p_id_account)
		cur.execute(sql_query)
		return rows_to_list(cur.description, cur.fetchall())
	except Exception as error:
		raise error
	finally:
		if(cur):
			cur.close()