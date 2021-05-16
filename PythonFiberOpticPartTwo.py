# Eric Hayden 03/25/2021
# Introdusing the software, telling the customer the pricing
print("Hello welcome to Fiber Optic Inc.")
print("The pricing of our fiber optic cabling starts at $0.87/ft but is discounted if bought in bulk. the bulk pricing is 101ft to 250ft is $0.80 per foot, 251ft to 500ft is $0.70, and more than 500 feet is $0.50 per foot.")
# Geting the name of the customers company
print("Please enter your company name bellow to get started")
CustomerName=input("Please enter company name here:\n")
# Obtaining the customers order
print("Now please enter the length of cable required per ft")
feet=int(input("Please enter length required here: "))
# Calculating the price
print("Calculating please wait...")
if feet <101:
    price=0.87
elif feet <251:
    price=0.80
elif feet <501:
    price=0.70
elif feet >=501:
    price=0.50
total=feet*price
# Outputing the total cost
print('Your total comes out to', total)
# Goodbye message to the custiomer
print('Thank you for your patronage', CustomerName)