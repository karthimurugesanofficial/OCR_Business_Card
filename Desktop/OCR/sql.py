from sqlalchemy import create_engine, text
from urllib.parse import quote_plus

connection = {
    'port': 5432,
    'host': 'localhost',
    'password': 'Murugesan@1965',
    'username': 'postgres',  
    'database': 'OCR'}

password = quote_plus(connection['password'])

engine_url = f"postgresql+psycopg2://{connection['username']}:{password}@{connection['host']}:{connection['port']}/{connection['database']}"

engine = create_engine(engine_url)

with engine.connect() as conn:
    db_check=text("SELECT 1 FROM pg_database WHERE datname='OCR'")
    db_exists=conn.execute(db_check).scalar()
    if not db_exists:
        create_db=text('''CREATE DATABASE OCR''')
        conn.execute(create_db)
        print("database created")
    else:
        print("database already exists")

    #conn.execute(text("USE OCR"))
    try:
        create_table=text('''CREATE TABLE IF NOT EXISTS BUSINESS_CARD(
                        NAME VARCHAR(50),
                        DESIGNATION VARCHAR(50),
                        COMPANY_NAME VARCHAR(50),
                        CONTACT VARCHAR(50),
                        EMAIL VARCHAR(50),
                        WEBSITE VARCHAR(100),
                        ADDRESS TEXT,
                        PINCODE VARCHAR(100))''')
        conn.execute(create_table)
        print("table created successfully")
    except Exception as e:
        print(f"Error creating table: {e}")

