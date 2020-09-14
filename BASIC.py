Python 3.7.1 (v3.7.1:260ec2c36a, Oct 20 2018, 14:57:15) [MSC v.1915 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> bus name="YBM"
SyntaxError: invalid syntax
>>> busname="YBM"
>>> bustype="voivo"
>>> price=782.5
>>> phnnumber=7894561233
>>> print("busname")
busname
>>> print(busname)
YBM
>>> print(bustype)
voivo
>>> print(price)
782.5
>>> print(phnnumber)
7894561233
>>> print("transport Name:",busname,)
transport Name: YBM
>>> print("transport Name:",busname,"volvo or not:",bustype,"fare:",price,"customer number:",phnnumber,))
SyntaxError: invalid syntax
>>>  print("transport Name:",busname,"volvo or not:",bustype,"fare:",price,"customer number:",phnnumber,)
SyntaxError: unexpected indent
>>> print("transport Name:",busname,"volvo or not:",bustype,"fare:",price,"customer number:",phnnumber,)
transport Name: YBM volvo or not: voivo fare: 782.5 customer number: 7894561233
>>> print("transport Name:",busname,"\nvolvo or not:",bustype,"\nfare:",price,"\ncustomer number:",phnnumber,)
transport Name: YBM 
volvo or not: voivo 
fare: 782.5 
customer number: 7894561233
>>> type(busname)
<class 'str'>
>>> type(bustype)
<class 'str'>
>>> type(price)
<class 'float'>
>>> type(phnnumber)
<class 'int'>
>>> print("transport %s\n")
transport %s

>>> print("transport %s\n")(busname)
transport %s

Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    print("transport %s\n")(busname)
TypeError: 'NoneType' object is not callable
>>> print("transport %s\nclassic %s\nfare %.2f\nnumber%d\n"%(busname,bustype,price,phnnumber))
transport YBM
classic voivo
fare 782.50
number7894561233

>>> bus=True
>>> print(bus)
True
>>> print("bushi:%s\n"%(bus))
bushi:True

>>> a
