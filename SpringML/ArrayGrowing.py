# The main aim of the program is to list the sequence of whole number in any array size.
# Input: 
# 4
# 2,2
# 2,3
# 3,3
# 3,4

# Output:
# [[1, 2], [3, 4]]
# [[1, 2, 3], [4, 5, 6]]
# [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]

n = int(input('Enter the Number of Jobs: '))
lst = []
for item in range(n):
	lst.append(list(map(int, input('Enter the row and column separated with , : ').split(','))))
print(lst)

for item in range(n):
	result = [[0 for i in range(lst[item][1])] for j in range(lst[item][0])]
	num=1
	for i in range(lst[item][0]):
		for j in range(lst[item][1]):
			result[i][j] = num
			num=num+1
	print(result)