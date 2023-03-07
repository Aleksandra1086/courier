# design a program to calculate the cost of sending parcel. ask the user to enter the price of the item

price_of_item = float(input('Please enter the price of the item you would like to purchase in two decimals: '))

# ask the user to enter the total distance of the delivery in kms

distance = int(input('Please enter the distance of the delivery in kms: '))

# ask the user to select each category Air or Freight:

air_or_freight = input('Are your sending the parcel by Air or Freight? Please state: Air or Freight: ')

if air_or_freight == 'air':
    print('Transport part of the delivery of your parcel by Air will cost: R {}*0.36.'.format(distance))
else:
    print('Transport part of the delivery of your parcel by Freight will cost: R {}*0.25.'.format(distance))

cost_of_transport=input('To accept the price please enter it here in the form of a number with two decimal points: ')

cost_transport_calc=float(cost_of_transport)

#Ask the user to select the category insurance

full_or_limited_ins=input('Please state if you would like full or limited insurance: ')

if full_or_limited_ins=='full':
    print('You chose full insurance. This will cost you R 50.00 in addition to your purchase and delivery cost.')
else:
    print('You chose limited insurance. This will cost you additional R 25.00 in addition to your purchase and delivery costs')

cost_of_insurance=input('To accept the price please enter it here in the form of a number with two decimal points: ')

insurance_cost_calc=float(cost_of_insurance)

#ask the user to select the purpose of sending the parcel
gift_or_no_gift=input('We need some additional information to calculate full cost of your delivery. Is your item a gift? Please state Yes or No:')

if gift_or_no_gift=='yes':
    print('There is an additional charge of R 15.00 for your gift item.')
else:
    print('There is no additional charge for sending your non-gift item.')

additional_cost=input('To accept the price please enter it here in the form of a number with two decimal points: ')

cost_add_calc=float(additional_cost)

#ask the user if they want the item to by sent by priority or standard delivery

priority_or_no=input('Would you like your parcel to be sent by priority or standard delivery? Please state:')

if priority_or_no=='priority':
    print('Charge for the priority delivery of your item is R 100.00.')
else:
    print('Charge for the standard delivery of your item is R 20.00.')

cost_of_delivery=input('To accept the price please enter it here in the form of a number with two decimal points: ')

delivery_cost_calc=float(cost_of_delivery)


#Calculate the total cost of the delivery. not sure how to make all the combinations and castings of types of data to make final calculation.

total_cost=(cost_transport_calc+insurance_cost_calc+cost_add_calc+delivery_cost_calc)

print('Your total cost for delivery of your item is: R' + str(total_cost))

print('Your total cost including purchase of your item with delivery and insurance is: R'+str(total_cost+price_of_item))
