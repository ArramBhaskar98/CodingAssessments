import numpy as np

m = int(input('Enter the Number of rows: '))
n = int(input('Enter the number of columns: '))

res = np.zeros((m,n), int)
num = 1
left = 0
right = n-1
top = 0
bottom = m-1

while True:
	if left > right:
		break
	for r in range(right,left-1,-1):
		res[top][r] = num
		num=num+1
	top=top+1

	if top>bottom:
		break
	for t in range(top, bottom+1):
		res[t][left] = num
		num=num+1
	left=left+1

	if left>right:
		break
	for l in range(left, right+1):
		res[bottom][l] = num
		num=num+1
	bottom=bottom-1

	if top>bottom:
		break
	for b in range(bottom, top-1, -1):
		res[b][right] = num
		num=num+1
	right=right-1

print(res)
