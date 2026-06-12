print("Simple Calculator")
a=int(input("Enter first number:"))
b=int(input("Enter second number:"))
op=input("Enter an operator(+,-,/,*):")
if op=="+":
  print("addition:",a+b)
elif op=="-":
  print("Subtraction:",a-b)
elif op=="*":
  print("Multiplication:",a*b)
elif op=="/":
  if b==0:
    print("Second number should not be zero")
  else:
    print("Division:",a/b)
else:
  print("Invalid Operator")
