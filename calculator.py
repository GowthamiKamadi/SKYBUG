A = int(input("Enter A value:  "))
B = int(input("Enter B value:  "))
print("WELCOME TO SKYBUG CALCULATOR....😄")
operation = input('select one operation to perform(\n 1.ADDITION(+)\n 2.Subtraction(-)\n 3.Division(/)\n 4.Multiplication(*)\n 5.Power(**)\n 6.Floor division(//)👾:  ')
if (operation == '1' ):
    print ('The Answer is: ',A+B)
elif (operation == '2' ):
    print ('The Answer is: ',A-B)
elif (operation == '3' ):
    print ('The Answer is: ',A/B)          
elif (operation == '4' ):
    print ('The Answer is: ',A*B)
elif (operation == '5' ):
    print ('The Answer is: ',A**B)    
elif (operation == '6' ):
    print ('The Answer is: ',A**B)    
else:
    print('invalid choice🙄')
print('Thank you😊')  
  