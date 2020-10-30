import cx_Oracle

from Class_Test.db_connection4 import cur


class Ora_Connection():
    def __init__(self):
        temp = 'test'
        print('Ora_Connection contruct called')

    def new_conn(self):
        print('new connection called with self new_conn1')
        qry1 = 'select * from person where id = 1'
        rec1 = cur.execute(qry1).fetchone()
        print(rec1)
        print(rec1[1])


def main():
    temp = Ora_Connection()
    temp.new_conn()


if __name__ == '__main__':
    main()
