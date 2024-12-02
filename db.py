mport psycopg2

def criar_conexao ():
    try:
        conn = psycopg2.connect(
            dbname='postgres',
            user='postgres',
            password='postgre',
            host='localhost',
            port='5432'
        )
        print("Conexao realizada com sucesso!")
        return conn
    except Exception as e:
        print(f'Erro ao conectar com o banco de dados>: {e}')
        return None
