while True:
  try:
    num = int(input("Please enter a number: "))
  except:
    print("That's not a number.")
  else:
    print("Else")
    break
  finally:
    print("And finally")

