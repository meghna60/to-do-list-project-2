

def printt():
      for row in list:
       for item in row:
        print(f"{item}")
print("""TODO List Managment System

1: Add
2: View
3: Remove
4: Edit""")
w=input()
if w=='1':
  add=input("What do you want to add: ")
  due=input("When it is due: ")
  impo=input("Importance(1-4): ")
  row=[add,due,impo]
  list.append(row)
  printt()
elif w=='2':
  rem=input("What do you want to remove:")
  for row in list:
    if rem in row:
      list.remove(rem)
elif w=='3':
  printt()
elif w=='4':
  print("\033[31m","Your TODO list is:","\033[0m")
  printt()
  print("\033[31m","Which task do you want to edit:","\033[0m")
  edit=input("What do you want to edit")
  for row in list:
    if edit in row:
      list[row]=input("What do you want to replace it with?")
    else:
      print("That task does not exists.")