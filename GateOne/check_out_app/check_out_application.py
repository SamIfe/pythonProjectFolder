items_purchased = []
quantity_purchased = []
price_per_unit = []


print("""
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

        WELCOME TO SEMI-COLON AFRICA MULTI-PURPOSE STORE.

            ADDRESS : 312, HERBERT MACAULAY WAY, SABO YABA, LAGOS.
            PHONE NUMBER: +23490884456.
            EMAIL: store@semicolonafrica.com.

@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

""")
        
name = input("Enter customer's name: ")
control = 1
        
while control == 1:
	item = input("What items did the user purchase? ")
	items_purchased.append(item)

	pieces = int(input("How many pieces?: "))
	while pieces < 1:
		pieces = int(input("How many pieces?: "))
		quantity_purchased.append(pieces)

	unit_price = int(input("How much per unit?: "))
	while unit_price < 1:
		price_per_unit.append(unit_price)

	control = int(input("Enter 1 to add more items or any numeric value to stop: "))

discount = int(input("Any discount applied: "))
cashier_name = input("What is your name?: ")

print("\nSEMICOLON STORES")
print("MAIN BRANCH")
print("LOCATION : 312, HERBERT MACAULAY WAY, SABO YABA, LAGOS.")
print("TEL : 03293828343")
print("DATE : 27/10/2024 , 12 : 50 : 11 pm")
print(f"Cashier: {cashier_name}")
print(f"Customer Name: {name}")

print("=" * 120)
print(f"{'ITEM(s)':<20}{'QTY':<15}{'PRICE':<15}{'TOTAL':<20}")
print("-" * 120)

subtotal = 0
for index in range(len(items_purchased)):
	total = quantity_purchased[index] * price_per_unit[index]
	subtotal += total
print(f"{items_purchased[index]:<20}{quantity_purchased[index]:<15}{price_per_unit[index]:<15}{total:<20.2f}")

total_discount = subtotal - discount
print("-" * 120)

print(f"Sub Total: {subtotal:.2f}")
print(f"Discount at {discount}: {total_discount:.2f}")

vat = (subtotal / 100) * 7.50
print(f"VAT @ 7.50%: {vat:.2f}")
print("=" * 120)

bill_total = total_discount + vat
print(f"Bill Total: {bill_total:.2f}")
print("=" * 120)

print(f"HERE IS YOUR RECEIPT OF {bill_total:.2f}\nTHANK YOU FOR BEING A VALUED CUSTOMER OF SEMI-COLON AFRICA!!")
print("=" * 120)
