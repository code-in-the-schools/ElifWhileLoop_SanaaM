import random
r =random.randint(-100,100)

found = False 
while found == False:
  m = int(input("Guess a number  "))
  
  if m == r:
    found = True 
    print("You won!!!")
  elif m>r:
    print(str(m), "is more than it")
  elif m<r:
    print(str(m), "is less than it")
  else:
    print("THis is not a number, try again.") 

    import random
r =random.randint(1,26)

found = False 
while found == False:
  m = str(input("Guess a letter  "))
  
  if m == r:
    found = True 
    print("You won!!!")
  elif m == r:
    print(str(m), "is more thann it")
  elif m == r:
    print(str(m), "is less than it")
  else:
    print("THis is the letter r, try again.")