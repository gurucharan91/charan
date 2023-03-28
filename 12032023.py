import mysql.connector

mydb = mysql.connector.connect(
  host="172.17.125.2",
  user="charan",
  password="1234"
)

mycursor = mydb.cursor()
mycursor.execute('create database amazon')
mycursor.execute('create table amazon.sales(item_name varchar(50), no_of_items int, price decimal(10, 2))')

grand_total_price = 0

while True:
    item_name = input('Enter the item name or type "done" to exit: ')
    if item_name.lower() == 'done':
        break
    
    no_of_items = int(input(f"Enter the number of {item_name} you want to buy: "))

    if item_name.lower() == 'pen':
        price = 2
    elif item_name.lower() == 'pencil':
        price = 4
    elif item_name.lower() == 'eraser':
        price = 1
    else:
        print("Invalid item name!")
        continue

    total_price = price * no_of_items
    grand_total_price += total_price

    data = (item_name, no_of_items, total_price)
    mycursor.execute('insert into amazon.sales values (%s, %s, %s)', data)
    mydb.commit()

    print(f"{no_of_items} {item_name} have been added to the cart. Total price: {total_price}")

print("You have successfully entered your items")

# Update grand total price in the sales table
mycursor.execute('alter table amazon.sales add grand_total_price decimal(10, 2)')
mycursor.execute('update amazon.sales set grand_total_price = %s', (grand_total_price,))
mydb.commit()

# Display the items in the sales table
mycursor.execute('select * from amazon.sales')
for i in mycursor:
    print(i)
