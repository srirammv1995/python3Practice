userList = {

}


def createAUser():
  user = {

  }
  user["name"] = str(input("enter your name: "))
  user["age"] = str(input("enter your age: "))
  user["school"] = str(input("enter your school name: "))
  if user.get("name") not in userList:
    userList[user.get("name")] = user
    print(userList)
  else:
    print("user already exists")
    
def viewUser():
  name = input("enter the user name to view the details: ")
  if name not in userList:    
    print("user dosen't exist")
  else:    
    print(userList[name])
    
def viewAllUsers():
   for eachUser in userList.keys():
     print("Username: "+userList[eachUser].get("name"))
     print("age: "+userList[eachUser].get("age"))
     print("school: "+userList[eachUser].get("school"))
     print("------------------------------------------")
     
def deleteAUser():
  name = input("enter the user name to view the details: ")
  if name not in userList:
    print("user dosen't exist")
  else:
    del userList[name]
    
def router():
  print("""
  1.create a user 
  2.view user
  3.view all users
  4.delete user
  5.exit program
  """)
  number=int(input("enter your option: "))
  if number==1:
    createAUser()
  elif number==2:
    viewUser()
  elif number==3:
    viewAllUsers()
  elif number==4:
    deleteAUser()
  elif number==5:
    print("exiting")
    exit()
  else:
    print("please enter valid input")
  router()

    
router() 
print("program shutting down....")