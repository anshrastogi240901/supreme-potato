#program to calculate the sum of multiples of 3 and 5 upto a limit
limit=int(input("Enter the limit :"))
def limit_sum(limit):
	s1=0
	for i in range(0,limit):
		if (i % 3 ==0) or (i % 5 ==0):
			s1=s1+i
	return s1
			
			
a=limit_sum(limit)		
print(a)
			
