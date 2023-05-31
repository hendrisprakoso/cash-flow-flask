from flask import make_response

def responseJson(p_status_code, p_data):
    return make_response(p_data, p_status_code)

def rows_to_list(description, rows):
    columns = [i[0].lower() for i in description]
    return [dict(zip(columns, row)) for row in rows]

def row_to_dict(description, row):
    columns = [i[0].lower() for i in description]
    return dict(zip(columns, row)) if row is not None else dict(zip(columns, ['' for _ in description]))