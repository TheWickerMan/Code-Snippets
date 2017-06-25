import argparse
from argparse import RawTextHelpFormatter

#Header on the help page
parser = argparse.ArgumentParser(description="----------Program-Help-Page----------", formatter_class=RawTextHelpFormatter)

#Inline Arguments
parser.add_argument("-x", help="Allows for a string to be added as an inline argument. \n")
parser.add_argument("-y", help="Allows for a integer to be added as an inline argument. \n", type=int)
parser.add_argument("-z", help="Allows for a boolean to be added as an inline argument.", action="store_true")

#Allocates the method to call the arguments to 'args'
args = parser.parse_args()

#Calls argument x and checks whether it is uses
if args.x == None:
  print("You forgot to use argument x")

#Prints the value of argument y
print(str(args.y))

#Checks whether z is present
if z == True:
  print("True")
else:
  print("False")
