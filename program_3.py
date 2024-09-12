#Programmer: Teresa Fischer
#Date: 9/12/2024
#Title: Program #3: Total Purchase

def calculate_total_purchase():
    # Get User Input
    item_1 = float(input('Enter the price of item 1:'))
    item_2 = float(input('Enter the price of item 2:'))
    item_3 = float(input('Enter the price of item 3:'))
    item_4 = float(input('Enter the price of item 4:'))
    item_5 = float(input('Enter the price of item 5:'))

    # Calculate subtotal
    subtotal = item_1 + item_2 + item_3 + item_4 + item_5
    # Calculate sales tax
    sales_tax = subtotal * .07
    # Calculate total
    total = subtotal + sales_tax
    # Print results
    print('Subtotal:', '$', subtotal)
    print('Sales tax:', '$', sales_tax)
    print('Total purchase:', '$', total)

calculate_total_purchase()