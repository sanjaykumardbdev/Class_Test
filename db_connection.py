import cx_Oracle

dsn_tns = cx_Oracle.makedsn('localhost', '1521', service_name='XE')
conn = cx_Oracle.connect(user='scott', password='tiger', dsn=dsn_tns)
cur = conn.cursor()


class Ora_Connection():
    # dsn_tns = cx_Oracle.makedsn('localhost', '1521', service_name='XE')
    # conn = cx_Oracle.connect(user='scott', password='tiger', dsn=dsn_tns)
    # cur = conn.cursor()

    def __init__(self):
        print('Ora_Connection contruct called')

    def new_conn():
        print('new connection called')
        # new_val = 10
        # new_val1 = 'test'

    def new_conn1(self):
        print('new connection called with self')
        qry1 = 'select * from person where id = 1';
        rec1 = cur.execute(qry1).fetchone()
        print(rec1)
        # print(rec1[1])

    def new_conn2(self):
        print('new connection called with self')
        qry1 = 'select * from person where id = 2';
        rec1 = cur.execute(qry1).fetchone()
        print(rec1)


    def exe_select_qry(self):
        qry1 = 'select * from person where id = 1';
        # getattr(Ora_Connection, 'cur')
        # cur.execute(qry1)



# calling only mehtod of class which has no argument.
Ora_Connection.new_conn()

# this will perform nothing
# temp = Ora_Connection

# creating an obj of class which has constructor.
temp = Ora_Connection()
print('***************-------------')
temp.new_conn1()
print('***************-------------')
temp.new_conn2()


temp.exe_select_qry()


