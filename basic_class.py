class company:
		def dept(self,depart):
			 print(f'your dept is {depart}')


class employee(company):
	  def em_name(self,name):
		   print(f'Employee name is {name}')



emp=employee()
emp.dept("Finance")
emp.em_name("Ansh") 
	 
