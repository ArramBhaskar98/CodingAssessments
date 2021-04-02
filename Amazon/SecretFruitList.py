# Acoording to Test Cases if secretFruitList is 0 and customerPurchasedList has non unique then Expected Output must be False
# Acoording to Test Cases if secretFruitList is 0 and customerPurchasedList has unique then Expected Output must be True

import re
import numpy as np
from itertools import chain

def secretFruitListAm(secretFruitList, customerPurchasedList):

	sequential_list = list(chain.from_iterable(secretFruitList))

	if len(secretFruitList) >= 2:
		# print('SecretFruitList in Function: ', secretFruitList)
		# print('CustomerPurchasedList in Function: ', customerPurchasedList)
		res = ''
	
		cuslst = ' '.join(customerPurchasedList)
		for code in secretFruitList:
			c = ' '.join(code)
			c = ' '+ c
			if 'anything' in c:
				c = c.replace('anything', '\w+')
				res = res + c + '[\w\s]*'
			else:
				res = res + c
				# print('Result: ', res)


		# print(res)
		if '\w+' in res:			
			r = re.compile(res)
			result = r.findall(cuslst)
			# print('Compiled Result: ',result)
		else:
			lst = list(map(str, res.split(' ')))
			lst = lst[1:]
			if all(item in customerPurchasedList for item in lst) and len(sequential_list) < len(customerPurchasedList):
				result = 1
			else:
				result = None

		if result:
			return True
		else:
			return False
	else:
		secretFruitList = secretFruitList[0]

	# print('SecretFruitList in Function: ', secretFruitList)
	# print('CustomerPurchasedList in Function: ', customerPurchasedList)

	if 'anything' in secretFruitList and len(secretFruitList) == len(customerPurchasedList):
		return True
	elif not secretFruitList and len(np.unique(customerPurchasedList)) == 1:
		return True
	else:
		return False

if __name__ == '__main__':

	# secretFruitList = []
	# numOfSubLists = int(input('Enter the Number of SubList you need: '))
	# numOfFruits = int(input('Enter the Number of Fruits you need in SubList: '))

	# for items in range(numOfSubLists):
	# 	lst = []
	# 	for fruits in range(numOfFruits):
	# 		lst.append(input('Enter the Fruit Name: '))
	# 	secretFruitList.append(lst)

	# customerPurchasedList = []
	# numOfPurchasedList = int(input('Enter the Number of Purchased Fruits: '))
	# for items in range(numOfPurchasedList):
	# 	customerPurchasedList.append(input('Enter the Purchased Fruits: '))

	# print('SecretFruitList: ', secretFruitList)
	# print('Customer Purchased Fruits: ', customerPurchasedList)

	tests = [dict(secretFruitList =  [['orange', 'mango'], ['watermelon', 'mango']],
				  customerPurchasedList = ['orange', 'mango', 'strawberry', 'watermelon', 'mango'],
				  result = True),
			 dict(secretFruitList =  [['watermelon','anything', 'mango']],
				  customerPurchasedList = ['watermelon', 'orange', 'mango'],
				  result = True),
			 dict(secretFruitList =  [['watermelon','anything', 'mango']],
				  customerPurchasedList = ['watermelon','apple' ,'orange', 'mango'],
				  result = False),
			 dict(secretFruitList=[['anything', 'apple'], ['banana', 'anything', 'banana']], 
			 	  customerPurchasedList=['orange', 'grapes', 'apple', 'orange', 'orange', 'banana', 'apple', 'banana', 'banana'],
			 	  result = True),
			 dict(secretFruitList=[[]], 
			 	  customerPurchasedList=['orange', 'grapes', 'apple', 'orange', 'orange', 'banana', 'apple', 'banana', 'banana'],
			 	  result = False),
			 dict(secretFruitList=[[]], 
			 	  customerPurchasedList=['orange', 'orange', 'orange'],
			 	  result = True),
			 dict(secretFruitList=[['apple', 'apple'], ['banana', 'anything', 'banana']], 
			 	  customerPurchasedList=['banana', 'orange', 'banana', 'apple', 'apple'],
			 	  result = False),
			 dict(secretFruitList=[['apple', 'apple'], ['banana', 'anything', 'banana']], 
			 	  customerPurchasedList=['apple', 'banana', 'apple', 'banana', 'orange', 'banana'],
			 	  result = False),
			 dict(secretFruitList=[['apple', 'apple'], ['banana', 'anything', 'banana']], 
			 	  customerPurchasedList=['orange', 'apple', 'apple', 'banana', 'orange', 'banana'],
			 	  result = True),
			 dict(secretFruitList=[['apple', 'apple'], ['apple', 'apple', 'banana']], 
			 	  customerPurchasedList=['apple', 'apple', 'apple', 'banana'],
			 	  result = False),
			 dict(secretFruitList=[['anything']], 
			 	  customerPurchasedList=['orange'],
			 	  result = True),
			 dict(secretFruitList=[['anything']], 
			 	  customerPurchasedList=['orange', 'apple'],
			 	  result = False)]
	i = 1
	for test in tests:
		assert secretFruitListAm(test['secretFruitList'], test['customerPurchasedList']) == test['result']
		# print(result)
		print(i," :----------------------------------------------------")
		i = i+1