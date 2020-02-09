#program for checking whether a no.is prime or not
no=int(input("Enter No:"))
if no > 1:
	for i in range(2, no//2):
		if (no % i) == 0:
			print(no, "is not a prime number")
			break
		else:
			print(no, "is a prime number")
else:
	print(no, "is not a valid case for prime no.")


