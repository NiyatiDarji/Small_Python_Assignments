
# Check validity of 10 digit phone number ignoring any punctuation
print("Check validity of 10 digit phone number ignoring any punctuation")
input_no = input("Enter the phone number:")
valid_no_list = "0123456789"
invalid_no_list = "abcdefghijklmnopqrstuvwxyz"
phone_no = []
for ch in input_no:
    if ch in valid_no_list and ch.lower() not in invalid_no_list:
        phone_no.append(ch)
    if ch in invalid_no_list:
        phone_no = []
        break
if len(phone_no)== 10:
    print("Valid phone number ignoring punctuations is:",''.join(phone_no))
else:
    print("Invalid phone number:it is not a 10 digit number or there are alphabets in the number")

