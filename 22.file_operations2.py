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


#writerows() for writing the csv file and converting each row into a list.
import csv
students = [[1, "Ravi", 90],[2, "Kiran", 85],[3, "Anil", 95]]
with open("docs/csv/students.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(
        ["Id", "Name", "Marks"]
    )
    writer.writerows(students)

#writerow() for writing the csv file and converting each row into a list.
import csv
with open("docs/csv/employee.csv","w",newline='') as f:
    csv_writer=csv.writer(f,delimiter=':')
    csv_writer.writerow(['pname','price'])
    csv_writer.writerow(['mouse',100])
    csv_writer.writerow(['keyboard',1200])

#reader() for reading the csv file and converting each row into a list.
import csv
with open("docs/csv/employee.csv","r",newline='') as f:
    csv_reader=csv.reader(f,delimiter=':')
    for row in csv_reader:
        print(row)

#readerows() for reading the csv file and converting each row into a list.
import csv
import os
filename = "docs/csv/emp.csv"
if os.path.exists(filename):
    with open(filename, "r", newline="") as file:
        reader = csv.reader(file)
        for row in reader:
            print(row)
else:
    print(
        "CSV file does not exist"
    )

#DictWriter() for writing the csv file and converting each row into a dictionary. The keys of the dictionary are taken from the first row of the csv file. 
import csv
with open("docs/csv/employee.csv","w",newline='') as f:
    csv_writer=csv.DictWriter(f,fieldnames=["rollno","name","course"])
    csv_writer.writeheader()
    while True:
        rollno=int(input("Enter Rollno "))
        name=input("Enter Name ")
        course=input("Enter Course ")
        csv_writer.writerow({'rollno':rollno,'name':name,'course':course})
        ans=input("Add another student?")
        if ans=="no":
            break
#DictReader() for reading the csv file and converting each row into a dictionary. The keys of the dictionary are taken from the first row of the csv file. 
import csv
with open("docs/csv/employee.csv","r",newline='') as f:
    dict_reader=csv.DictReader(f)
    for row in dict_reader:
        print(row['rollno'],row['name'],row['course'])


