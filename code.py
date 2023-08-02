print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

pepps = 2
peppml= 3

cheese = 1
bill = 0

if size == "S" :
    bill = 15
   
    if add_pepperoni == "Y":
        bill = bill + pepps
       

elif size == "M" :
    bill = 20
    
    if add_pepperoni == "Y":
      bill = bill + peppml
      

elif size == "L" :
    bill = 25
    
    if add_pepperoni == "Y":
      bill = bill + peppml
      

if extra_cheese == "Y":
    bill = bill + cheese
    print(f"Your final bill is: ${bill}")   


else :
    print(f"Your final bill is: ${bill}")     
         
    

