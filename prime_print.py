#program for printing prime no upto n
n=int(input("Enter the no. upto which you want to print prime nos:"))
if(n>1):
	for i in range(2,n):
		for y in range(2,i):
			if(i%y)==0:
				break
		else:		
			print(i)
else:
     print("not a valid case")	
		
	

