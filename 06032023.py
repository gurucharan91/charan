print("*******Demo for lists*****")
print("""Lists are ordered sequences of values
When we say that lists are ordered, it means that the items have a defined order, and that order will not change.
If you add new items to a list,the new items will be placed at the end of the list""")
print("create a new list")
l=[1,2.3,4+3j,"python"]
print(f"the list contains {l} and its type is {type(l)}")
print("create a empty list")
l1=[]
print(f"the list contains{l1}")
print("*****Accessing Elements from the list********")
shoping_list=["pen","pencil","Eraser","sharpner"]
print(f"""the zeroth element in the list is {shoping_list[0]}
the First element in the list is {shoping_list[1]}
the Second element in the list is {shoping_list[2]}
the third element in the list is {shoping_list[3]}
the length of the list is {len(shoping_list)}""")
print("######## LIST SLICING#################")
months=["January","February","March","April","May","June","July","August","September","October","November","Decemeber"]
print(f"""the first quarter list of months is {months[0:3]}
the Second quarter list of months is {months[3:6]}
the Third quarter list of months is {months[6:9]}
the Fourth quarter list of months is {months[9:12]}""")
print("*****Breakfast Menu**********")
breakfast_menu=["Ragi Malt","idly with vegetable chutney","Hotwater"]
print(f"SDMM'S BREAKFAST MENU IS {breakfast_menu}")
print("add biscuit to above menu")
breakfast_menu.append('biscuit')
print(f"SDMM'S BREAKFAST MENU after addition is {breakfast_menu}")
print("now SDMM wants to have juice instead of biscuit")
breakfast_menu.remove('biscuit')
breakfast_menu.append('Juice')
print(f"After the change now the breakfast menu is {breakfast_menu}")
print("now insert vegetable salad instead of idly with vegetable chutney")
breakfast_menu.insert(1,'vegetable salad')
print(f"SDMM'S BREAKFAST MENU after addition is {breakfast_menu}")
breakfast_menu.pop(0)
r=breakfast_menu.pop(0)
print("the value which is removed from list using pop is {r}")
print(f"SDMM'S BREAKFAST MENU after removing RAGI MALT is {breakfast_menu}")
check ="biscuit" in breakfast_menu
print(f"is biscuit there in the menu?\t{check}")
print("Add 2 more items milk and bread to above menu")
l1=["Milk","Bread","Milk"]
breakfast_menu.extend(l1)
print(f" after Adding 2 more items milk and bread to above menu{breakfast_menu}")

print("what is the index of Milk in above list")
i=breakfast_menu.index("Milk")
print(f"the index is {i}")
print("index always return first occurance")


