#program to create a func shownum for labelling even's and odd's
limit=int(input("Enter the limit :"))
def ShowNum(limit):
	for i in range(0,limit):
		if (i % 2 ==0):
			print(f'{i} EVEN')
		elif (i % 2 !=0):
			print(f'{i} ODD')


ShowNum(limit)				
