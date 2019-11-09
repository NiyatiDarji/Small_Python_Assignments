# Determine the card brand from the credit card number
# Input : Credit cardc number Total digit = 16 dig-its, and the first digit serves to indicate the card brand.
# All Visa cards start with a 4; MasterCard cards always starts with a 5; and Discover cards start with a 6.
# If brand name not identified then output "Unknown Card"
print("Determine the card brand from the credit card number")
try:
    input_credit_card_no = int(input("Enter the 16 digit credit card number without spaces: ")) # int to only allow numbers in the string
    card_no = str(input_credit_card_no) # str conversion to fing the length of input number
    if len(card_no)!=16 :
        print("Invalid credit card number")
    else:
        deciding_digit = card_no[0] # get the first digit of the card number
        if deciding_digit == '4':
            print("Card is a Visa Card")
        elif deciding_digit == '5':
            print("Card is a Master Card")
        elif deciding_digit == '6':
            print("Card is a Discovery Card")
        else:
            print("Unknown Card")
except:
    print("Credit card number is invalid. Please enter a valid card number")