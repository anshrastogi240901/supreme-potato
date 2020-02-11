#program to make a func fizzbuzz
no=int(input("Enter any number :"))
def fizz_buzz(no):
	if(no % 3)==0 or (no % 5)==0:
		if(no % 3)==0:
			r="Fizz"
		if(no % 5)==0:
			r="Buzz"
		if(no % 3)==0 and (no % 5)==0:		
			r="FizzBuzz"
		return r	
	else:
		return no
		
		
print(fizz_buzz(no))		
