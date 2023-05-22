a=int(input('Enter the first side length'))
b=int(input('Enter the second side length'))
c=int(input('Enter the third side length'))
if (c>a+b)or(a>b+c)or(b>a+c):
         print('no')
else:
        print('yes')