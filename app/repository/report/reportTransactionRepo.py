from app import mysql
from app.utility.response import rows_to_list


def getDataReportTransaction(p_id_account, p_category, p_date):
	try:
		cur = mysql.connection.cursor()

		sql_fil_by_category = ""
		sql_fil_by_date = ""

		if p_category not in ('', None, "None", 'null'):
			sql_fil_by_category = """AND cf.category = {}""".format(p_category)

		if p_date not in ('', None, "None", 'null'):
			sql_fil_by_date = """ and cast(cf.`date` as date) = '{}' """.format(p_date)

		sql_query = '''
						select
							cast(cf.date as char) as tanggal_transaksi,
							tt.desc_type as type_transaksi, al.name, coalesce(cf.debit, 0) as pengeluaran, cf.category as kategori, ct.desc_category as des_kategori,
							coalesce(cf.credit, 0) as pemasukan,  cf.notes as keterangan
						from
							cash_flow cf
						left join type_transaction tt on
							cf.`type` = tt.id_type
						left join account_list al on
							al.id_account = cf.id_account
						left join category_transaction ct on 
							cf.category = ct.id_category 
                        where
                            cf.id_account = {} {} {}
                        order by
                            cf.id desc
					'''.format(p_id_account, sql_fil_by_category, sql_fil_by_date)

		cur.execute(sql_query)
		return rows_to_list(cur.description, cur.fetchall())
	except Exception as error:
		raise error
	finally:
		if(cur):
			cur.close()