import cx_Oracle

class Ora_Connection():
    def __init__(self):
        print('contructor called')

    def new_conn():
        print('new connection called')

    def file_conn(self, path):
        self.file_name = path
        print(self.file_name)

    def file_conn1(self):
        print('my test')


class new_class():
    def __init__(self):
        su_clas_cons = Ora_Connection()
        print('new calls cons called')


class new_two_class():
    def __init__(self):
        pass
    def new_method1():
        temp = Ora_Connection()

        # temp.new_conn()       # can't create obj like this, it is passing one value to : like this: new_conn(temp) so use below line
        Ora_Connection.new_conn()

        temp.file_conn('d drive')

        # Ora_Connection.file_conn1()       # can't create like this if you are passing value, so use below line.
        temp.file_conn1()


ntclass = new_two_class()
new_two_class.new_method1()

#
# nc = new_class()
#
# db_conn = Ora_Connection()
# Ora_Connection.__init__('test')
# print('---------------------------end')
#
# print('---------------------------start')
#
# Ora_Connection.new_conn()
# print('---------------------------end 1')
# db_conn.file_conn('d drive to new method')


#
# print()
# print('-----------------variables ----------')
#
# print(db_conn.__dict__)
#
# print('---------------------------')
# print(Ora_Connection.__dict__)
