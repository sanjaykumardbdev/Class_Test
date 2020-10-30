import cx_Oracle

from Class_Test.db_connection import cur


class exec_Connection():
    def ora_conn(self):
        print('parent calls')
        dsn_tns = cx_Oracle.makedsn('localhost', '1521', service_name='XE')
        conn = cx_Oracle.connect(user='scott', password='tiger', dsn=dsn_tns)
        cur = conn.cursor()
        temp = 'hello world'


class Ora_Connection(exec_Connection):
    def __init__(self):
        temp = 'test'
        print('Ora_Connection contruct called')
        print(temp)

    def new_conn(self):
        print('new connection called with self new_conn1')
        qry1 = 'select * from person where id = 1';
        rec1 = cur.execute(qry1).fetchone()
        print(rec1)
        print(rec1[1])


def main():
    temp1 = Ora_Connection()
    # temp.new_conn()


if __name__ == '__main__':
    main()
