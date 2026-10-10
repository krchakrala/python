#write operations using csv module into csv file
import csv
f=open("docs/csv/emp.csv","w",newline='')
csv_writer=csv.writer(f)
csv_writer.writerow(['empno','ename','salary'])
while True:
    empno=int(input("Enter EmployeeNo "))
    ename=input("Enter EmployeeName ")
    salary=float(input("Enter Salary "))
    csv_writer.writerow([empno,ename,salary])
    ans=input("Add another employee?")
    if ans=="no":
        break

f.close()


#read operations from csv module 
import csv
f=open("docs/csv/emp.csv","r",newline='')
csv_reader=csv.reader(f)
for e in csv_reader:
    print(e)
f.close()

#read operations for total salary using csv module 
import csv
f=open("docs/csv/emp.csv","r",newline='')
csv_reader=csv.reader(f)
total=0
emp_list=list(csv_reader)
print(emp_list)
for i in range(1,len(emp_list)):
    total=total+float(emp_list[i][2])
    print(f'{emp_list[i][0]}\t{emp_list[i][1]}\t{emp_list[i][2]}')
print(f'Total Salary {total}')
