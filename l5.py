#for loop
for i in range(0,10):
	print(i)	
for j in range(1,10):
	print("*"*j)
	
cost_items=[100,200,300,400]
total_sum =0
for item in range(0,4):
	print(f"total sum ={total_sum}+{cost_items[item]}")
	total_sum= total_sum+cost_items[item]
	print(f"after adding total_sum={total_sum}")
	print("****")
print(f"total amount to be paid : {total_sum}")
