""" fungsi untuk membuat konek ke database """
def dbConnect():
    

    
    db_uri = "postgresql://{uname}:{pwd}@/{db}?host={host}&port={port}".format(uname=app.config["POSTGRES_USER"], pwd=urllib.parse.quote_plus(app.config["POSTGRES_PW"]), db=app.config["POSTGRES_DB"], host=app.config["POSTGRES_HOST"], port=app.config["POSTGRES_PORT"]) #cloudSQL GCP
    connection = psycopg2.connect(db_uri)
    return connection