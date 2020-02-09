#program for guessgame in python
sec_no=6
guess_count=0
guess_limit=3
while guess_count<guess_limit:
      guess=int(input('Guess='))
      guess_count+=1 
      if guess==sec_no:
         print('you won!!!!!')
         break
      else:
           print('try again')  
      if guess_count==3:
         print('You failed')
         break
      
