# Write a program using a for loop that diplays the even numbers from the number_list
# create an odd/even numbers list in an array

number_list = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25]
odd_list = []
even_list = []
#n = (number_list % 2)
for i in number_list:
	n = i % 2
	if n == 0:
		even_list.append(i)
	else:	
		odd_list.append(i)

print(odd_list)
print(even_list)