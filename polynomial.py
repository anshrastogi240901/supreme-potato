#program to find the value of function f(x) withy a given degree for some x
#basic form of a equation here is a0x^n+a1x^n-1+....+a^nx0
deg=int(input("Enter the degree of polynomial:"))
x=int(input("Enter the value for which you want to find out the value of f(x) :"))
coef = []  
for i in range(0, deg+1): 
	ele = int(input(f'Enter the coeficient a{i}: '))
	coef.append(ele) 


powsum=[1,1,1,1,1,1,1]
add=0#for addding the values of f(x)
temp=deg
for j in range(0, deg+1):
	for y in range(0, temp):
		powsum[j]=powsum[j]*x
	temp=temp-1


for i in range(0, deg+1):
	add+=(coef[i]*powsum[i])
print("Value of f(",x,"): ",add)	
	
	    
