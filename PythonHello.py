print("Hello welcome to Fiber Optic Inc.")
print("The pricing of our fiber optic cabling is $0.87/ft")
print("Please enter your company name bellow to get started")
CustomerName=input("Please enter company name here:\n")
print("Now please enter the length of cable required per ft")
feet=int(input("Please enter length required here: "))
print("Calculating please wait...")
price=0.87
total=feet*price
print('Your total comes out to', total)
print('Thank you for your patronage', CustomerName)