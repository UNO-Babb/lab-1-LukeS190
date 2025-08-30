#MadLib.py
#Name:Luke Sheardown
#Date:8-29-2025
#Assignment:Lab 1

def main():
  print("Madlib")
  #Ask user for words
noun1 = input("enter a noun: ")
noun2 = input("enter a noun: ")
adjective1 = input("enter an adjective: ")
verb1 = input("enter a verb: ")
verb2 = input("enter a verb: ")
adjective2 = input("enter an adjective: ")

  #Print the story with the user supplied words.
print("I love my dog " + noun1 + ".")
print("She loves to go on rides in the " + noun2 + ".")
print("She is just so " + adjective1 + "!")
print("I take her on long " + verb1 + ".")
print("When I first got her I didn't know she could " + verb2 + "!")
print("Sometimes when she plays outside she can get a little " + adjective2 + ".")


#Call the main function if this is the file being run.
if __name__ == '__main__':
    main()
