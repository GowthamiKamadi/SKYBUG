# TASK 5 :- Password generator👾
#For this we have to import module called 'RANDOM' 
import random
#password includes alphabets, numbers, symbols, numbers
lower="abcdefghijklmnopqrstuvwxyz"
upper="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
symbols="()*@!#$^&;<>?[]{}"
numbers="1234567890"
#asking desired length of the user
length= int(input("length of the password: "))
#combining the data
all=lower+upper+symbols+numbers
#creating password
password="".join(random.sample(all,length))
print("generated password is:",password)
    



