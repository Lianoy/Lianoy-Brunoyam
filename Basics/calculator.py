## создать функцию-калькулятор

def calc(num1,num2,op='+'):
   if op == '+':
       a = num1 + num2
   elif op == '-':
       a = num1 - num2
   elif op == '*':
       a = num1 * num2
   elif op == '/':
       a = num1 / num2
   return a

print (calc (4,5))
print (calc (4,5,'*'))