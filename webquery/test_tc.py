import jaydebeapi
from objects import Employee
import json

conn = jaydebeapi.connect('com.intersys.jdbc.CacheDriver',
                           ['jdbc:Cache://10.88.23.56:1972/bmc-test', 'hmstest', '1234qwer'],
                           'C:\hmsgw\webquery\drivers\CacheDB.jar',)
curs = conn.cursor()

curs.execute("select top 20 * from SQLUser.PA_PatMas")
# results = curs.fetchall()

arr_objects = []

for data_row in curs.fetchall():

    print(data_row[0], data_row[1], data_row[2], data_row[3], data_row[4])
    # print(data_row[0][0],data_row[0][1],data_row[0][2],data_row[0][3],data_row[0][4])
    # emp = Employee(results[0][0],results[0][1],results[0][2],results[0][3],results[0][4])
    # emp = Employee(data_row[0], data_row[1], data_row[2], data_row[3], data_row[4])
    arr_objects.append(Employee(data_row[0], data_row[1], data_row[2], data_row[3], data_row[4]))

    for x in arr_objects:
        print(x)

    #print (vertex.label for vertex in arr_objects)
    #print(arr_objects.__str__)
    # "This would create second object of Employee class"
    # emp1.displayEmployee()
    # print ("Total Employee %d") % Employee.empCount
    # data=json.dumps(emp.__dict__)
    # print(data);
    #print(*arr_objects, sep='\n')
