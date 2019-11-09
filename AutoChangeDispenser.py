# Write a software for an automatic change dispenser
print("\n Write a software for an automatic change dispenser")
due_amount = int(input("Please enter the amount of change that is due between 0 to 99:"))
no_of_quarters = due_amount//25               #quarter = 25 cents
remaining_amount = due_amount%25
no_of_dimes = remaining_amount//10            #demis = 10 cents
remaining_amount_1 =  remaining_amount%10
no_of_nickels = remaining_amount_1//5         #nickels = 5 cents
remaining_amount_2 = remaining_amount_1%5
no_of_pennies = remaining_amount_2//1         #pennies = 1 cents
print("There are",no_of_quarters,"quarters",no_of_dimes,"dimes",no_of_nickels,"nickels and ",no_of_pennies,"pennies in the change")
