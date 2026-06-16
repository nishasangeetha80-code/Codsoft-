Tasks=[]
while True:
  print("\n 1.Add Task")
  print('2.View Task')
  print("3.update Task")
  print("4.Delete Task")
  print('5.Exit')
  ch=int(input())
  if ch==1:
    Task= input(" Enter a task:")
    Tasks.append(Task)
  elif ch==2:
    print(Tasks)
  elif ch==3:
    n=int(input("Enter a numbers:")
    Tasks[n-1]=input("Enter a number:")
  elif ch==4:
    n=int(input("Enter a number:")
    Tasks.pop(n-1)
  elif ch==5:
    break
  else:
    print("Invalid choice")
  

