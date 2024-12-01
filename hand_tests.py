from Function import salary, hello_who
hello_who('test')
salary(2,10)
if salary != 20:
    print('error in the salary')
else:
    print('good')
if hello_who('max')=='Hello, max':
    print('good')
else:
    print('bad')
if hello_who('Leo')=='Hello, Leo':
    print('good')
else:
    print('bad')
if salary('r',5):
    print('bad')
else:
    print('good')
if hello_who(23)=='Hello, 23':
    print('bad')
else:
    print('good')

