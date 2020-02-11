#program for checking speeds of driving for licence related queries
speed=int(input("Enter the speed parameter :"))
demerit_pt=0
def drive(speed):
	if(speed < 70):
		return print("Ok")
	elif(speed > 70):
		speed1 = (speed-70)//5
		if speed1 <= 12:
	        	return print(f"Point: {speed1}")
		else:
			return print("License suspended")	
	

drive(speed)	

