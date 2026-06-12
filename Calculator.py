print("Simple Calculator")
a=int(input())
b=int(input())
op=input("Enter a operator(+,-,/,*):")
if op=="+":
  print("addition :",a+b)
elif op=="-":
  print(" Subtraction:",a-b)
elif op== "*":
  print(" Multiplication:",a*b)
elif op=="/":
  if b==0:
    print("Input proper number")
  else:
    print("Division:",a/b)
else:
  print("Invalid Operator")
