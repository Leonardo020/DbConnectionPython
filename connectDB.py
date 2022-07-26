
import psycopg2
from tabulate import tabulate
import json 

users = []

id = int(input('Insira o id: '))
nome = input('Insira o nome: ')
senha = input('Insira a senha: ')

def connect():
    """ Connect to the PostgreSQL database server """
    conn = None
    try:
        # read connection parameters

        # connect to the PostgreSQL server
        print('Connecting to the PostgreSQL database...')
        conn = psycopg2.connect(
                host="ec2-44-195-162-77.compute-1.amazonaws.com",
                database="d9eb9q6echr6sh",
                user="kqwqaiwbcfmhlv",
                password="dd35bbd8064b1a0c26cb9369966d2be6a693a3623e084c25c961efc68e17b369")
		
        # create a cursor
        cur = conn.cursor()
        
	# execute a statement
        print('PostgreSQL database version:')
        postgres_insert_query = """ INSERT INTO tbLogin VALUES (%s,%s,%s)"""
        record_to_insert = (id, nome, senha)
        cur.execute(postgres_insert_query, record_to_insert)
        conn.commit()
        
        cur.execute('SELECT * FROM tbLogin')

        # display the PostgreSQL database server version
        users = cur.fetchall()
     
        print(tabulate(users, headers=['Id', 'Usuário', 'Senha']))
        print(json.dumps(users, ensure_ascii=False).encode('utf8').decode())
        # for user in users:
        #     print('O usuário da vez é: {} de id {}, que possui a senha {}'.format(user[1], user[0], user[2]))
        
        
        
       
	# close the communication with the PostgreSQL
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            print('Database connection closed.')


if __name__ == '__main__':
    connect()
