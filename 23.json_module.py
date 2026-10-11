#JSON (JavaScript Object Notation) is a lightweight data-interchange format. It is easy for humans to read and write. It is easy for machines to parse and generate. It is based on a subset of the JavaScript Programming Language Standard ECMA-262 3rd Edition - December 1999. JSON is a text format that is completely language independent but uses conventions that are familiar to programmers of the C-family of languages, including C, C++, C#, Java, JavaScript, Perl, Python, and many others. These properties make JSON an ideal data-interchange language.
#dump() function used to write json data into JSON file
import json
emp_dict={'empno':[1,2,3,4,5],
          'ename':['naresh','suresh','ramesh','kishore','rajesh']}
with open("docs/json/emp.json","w") as f:
    json.dump(emp_dict,f)
e=json.dumps(emp_dict)
print(e,type(e))

#load() function can use to read data from json file
import json
with open("docs/json/emp.json","r") as f:
    e=json.load(f)
    print(e,type(e))

#Binary file handling with wb mode
with open("docs/binary/file1","wb") as f:
    b=bytes(range(65,71))
    f.write(b)
    b1=b'ABCDE'
    f.write(b1)
    b2=bytearray("XYZ",'utf-8')
    f.write(b2)

#Binary file handling with rb mode
with open("docs/binary/file1","rb") as f:
    b=f.read()
    print(b,type(b))
    for x in b:
        print(x)

#pickle module with wb mode is used to serialize and deserialize python object structures. Any object in python can be pickled so that it can be saved on disk. Pickling is a way to convert a python object (list, dict, etc.) into a character stream. The idea is that this character stream contains all the information necessary to reconstruct the object in another python script.
import pickle
with open("docs/binary/file2","wb") as f:
    pickle.dump(65,f)
    pickle.dump(1.5,f)
    pickle.dump(1+2j,f)
    pickle.dump("PYTHON",f)
    pickle.dump([10,20,30,40],f)
    pickle.dump({1:10,2:20,3:30},f)

#pickle module with rb mode
import pickle
with open("docs/binary/file2","rb") as f:
    obj1=pickle.load(f)
    obj2=pickle.load(f)
    obj3=pickle.load(f)
    obj4=pickle.load(f)
    obj5=pickle.load(f)
    obj6=pickle.load(f)
    print(obj1,obj2,obj3,obj4,obj5,obj6)
    print(type(obj1),type(obj2),type(obj3),type(obj4),type(obj5),type(obj6))

#regular expression module with compile
import re
r1=r'nit'
print(r1,type(r1))
r2=re.compile('nit')
print(r2,type(r2))

#regular expression with search and match
import re
str1="python"
m=re.match(r'p',str1)
print(m)
m=re.match(r'a',str1)
print(m)
str2="Python"
p=re.compile('p',re.I)
m=p.match(str2)
print(m)
print(m.group(0))

import re
str1='''python is
object oriented programming langauge,
java is object oriented programming language'''
m=re.search(r'object',str1)
print(m)
print(m.group(0))
m=re.search(r'procedural',str1)
print(m)
if m!=None:
    print(m.group(0))

#regular expression with findall
import re
str1='''python is
object oriented programming langauge,
java is object oriented programming language'''

list1=re.findall(r'object',str1)
print(list1)
list2=re.findall(r'procedural',str1)
print(list2)
list3=re.findall(r'a',str1)
print(list3)

#regular expression with fullmatch
import re
str1="python"
m=re.fullmatch(r'python',str1)
print(m)
str2="ironpython"
m=re.fullmatch(r'python',str2)
print(m)
m=re.search(r'python',str2)
print(m)

#regular expression with search
import re
names=['naresh','raman','rajesh','kishore','jessy']
for name in names:
    m=re.search(r'h$',name)
    if m!=None:
        print(name)
for name in names:
    m=re.search(r's.$',name)
    if m!=None:
        print(name)

import re
str1='''python is scripting language
python is oopl
python is multipurpose programming language
java,python are object oriented programming languages'''
m1=re.search(r'^python',str1)
print(m1)
m1=re.findall(r'^python',str1,re.MULTILINE)


#datetime module use in python
import datetime
dt=datetime.datetime.today()
print(dt)
print(dt.strftime("%a"))
print(dt.strftime("%A"))
print(dt.strftime("%d"))
print(dt.strftime("%d %A"))
print(dt.strftime("%b"))
print(dt.strftime("%B"))
print(dt.strftime("%m"))
print(dt.strftime("%A %B %d"))
print(dt.strftime("%y"))
print(dt.strftime("%Y"))
print(dt.strftime("%A %B %d %Y"))
print(dt.strftime("%H"))
print(dt.strftime("%M"))
print(dt.strftime("%S"))
print(dt.strftime("%H:%M:%S %p"))
print(dt.strftime("%w"))
print(dt.strftime("%z"))
print(dt.strftime("%j"))
print(dt.strftime("%U"))
print(dt.strftime("%c"))
print(dt.strftime("%X"))
a=10
print(f'{a:d},{a:o},{a:x},{a:b}')
print("%d%o%x"%(a,a,a))

