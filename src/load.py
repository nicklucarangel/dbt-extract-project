from config.database import get_engine
import psycopg2

engine = get_engine()

def salvar_no_postgres(df,schema='public'):
    df.to_sql('commodities',engine,if_exists='replace',index=True,index_label='Date',schema=schema)


