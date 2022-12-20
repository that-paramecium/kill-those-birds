from functions.py import *
from rpsTEST.py import *


while stillcalculating == True:
     resp = input('wanna play rock paper scissors?')
     if resp == 'y':
         rockPaperScissors()
     elif resp != 'n' and resp != 'y':
         raise InputError
     whichCalculate = input('What should I calculate (arithmetic, factoring, gcf, roots, squares ') 
     if whichCalculate == 'factoring':
          num1 = int(input('what first num ')) 
          num2 = int(input('what 2nd num '))
          num3 = int(input('what 3rd num '))
          quadraticFunction(num1,num2,num3)
          exitCheck()
     
     if whichCalculate == 'arithmetic':
        num1 = int(input('what first num '))
        num2 = int(input('what second num '))
        whichOp = input('which operation do you wanna use (add, subt,m mult, divide) ')
        if whichOp == 'add':
            print(num1+num2)
        if whichOp == 'subt':
               print(num1-num2)
        if whichOp == 'mult':
               print(num1*num2)
        if whichOp == 'divide':
           print(num1/num2)
        exitcheck()
     if whichCalculate == 'square':
        num1 = int(input('what base'))
        num2 = int(input('what are you squaring it by (i.e. if you want a cube, put 3) '))
        for i in range(num2-1):
            num1 = num1**2
        print(num1)
     if whichCalculate == 'root':
        num1 = int(input('what are you rooting '))
        num2 = int(input('whats the root (i.e. if you want a cube root put 3, if you want a 4th root, put 4)'))
        print(num1**(1/num2))
 
