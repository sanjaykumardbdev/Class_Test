import cx_Oracle


class exec_Connection():

    dsn_tns = cx_Oracle.makedsn('localhost', '1521', service_name='XE')
    conn = cx_Oracle.connect(user='scott', password='tiger', dsn=dsn_tns)
    cur = conn.cursor()
    temp = 'hello world'


class Ora_Connection(exec_Connection):

    def __init__(self):
        print('Ora_Connection contruct called')
        print(Ora_Connection.temp)

    def new_conn(self):
        print('new connection called')

    def new_conn1(self):
        print('new connection called with self new_conn1')
        qry1 = 'select * from person where id = 1';
        rec1 = Ora_Connection.cur.execute(qry1).fetchone()
        print(rec1)
        # print(rec1[1])

    def new_conn2(self):
        print('new connection called with self new_conn2')
        qry1 = 'select * from person where id = 2';
        rec1 = Ora_Connection.cur.execute(qry1).fetchone()
        print(rec1)

    def exe_select_qry(self):
        qry1 = 'select * from person where id = 1';
        Ora_Connection.cur.execute(qry1).fetchone()

def main():
    temp = Ora_Connection()
    temp.new_conn()

    print('***************-------------')
    temp.new_conn1()

    print('***************-------------')
    temp.new_conn2()

    temp.exe_select_qry()


if __name__ == '__main__':
    main()
