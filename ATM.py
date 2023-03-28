import time
print("Welcome to Lendi ECE Bank")
time.sleep(3)
print("Insert ATM Card")
time.sleep(4)
print("Welcome to Kiran")
time.sleep(2)
PIN_Number=int(input("Enter PIN Number: "))
if (PIN_Number==1234):
    cash=int(input("Enter Cash in terms: "))
    if(cash==500 or cash==1000 or cash==5000 or cash==10000):
        print("Cash Withdraw is Success")
        time.sleep(2)
        print("Collect ATM Card and Cash")
    else:
        print("Entered Valid Cash only")
else:
    print("Wrong Pin Number")
