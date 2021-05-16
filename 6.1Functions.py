#Eric Hayden 04/24/2021
#greeting and gathering name
Name=input('Please enter your name here:')
print('Welcome '+Name+'. This program will gather your driven miles and calculate the total and give you the total miles you have driven in miles and kilometers.')
#gathering miles driven
try:
   miles=int(input('Please enter the total number of miles driven:'))
   kilometers=float(1.60934)
   #miles to kilometers function
   def conversion_function():
      return miles*kilometers
   print(f"Hello {Name}. Your total miles driven is {miles}. That is also {conversion_function()} kelometers.")
except:
   print(f"We are sorry {Name} but we where not able to convert the muber of miles you have driven to kelometers. Please try again.")