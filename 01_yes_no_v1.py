show_instructions = ""
while show_instructions.lower() != "xxx" :



   # Ask the user if they have played before
   show_instructions = input("Have you played this game before? ").lower()


   # If they say yes, output 'program continues'
   # If they say no, 'display instructions'
   # If the answer is invalid, 'print an error'
   if show_instructions == "yes":
      print("program continues")


   elif show_instructions =="y":
      print("program continues")


   elif show_instructions =="no":
      print("displays instructions")


   elif show_instructions == "n":
      print("displays instructions")




   else:
      print("Please answer yes / no")


      print("You chose {}".format(show_instructions))

