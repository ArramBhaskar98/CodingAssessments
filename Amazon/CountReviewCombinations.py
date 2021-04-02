from itertools import combinations, chain
# chain.from_iterable() converts list of lists into flat list. 

def countReviewCombinations(num, lengths, minReviews, minLength, maxLength):

	selectedList = []
	for item in range(minLength, maxLength+1):
		if item in lengths:
			selectedList.append(item)
		else:
			continue
	print('Selected List Items: ', selectedList)

	comb_lst = []
	for i in range(minReviews, len(selectedList)+1):
		comb_lst.append(list(combinations(selectedList, i)))

	print('Final combinations List: ', comb_lst)

	final_com_lst = list(chain.from_iterable(comb_lst))
	print('After removing list of lists: ',final_com_lst)

	return len(final_com_lst)


if __name__ == '__main__':
	
	num = int(input('Enter the Number: '))
	lengths = []
	for i in range(num):
		lengths.append(int(input('Enter the Items in List: ')))
	minReviews = int(input('Enter the Min Review: '))
	minLength = int(input('Enter the Min Length: '))
	maxLength = int(input('Enter the Max Length: '))

	result = countReviewCombinations(num, lengths, minReviews, minLength, maxLength)
	print('Final Result: ', result)