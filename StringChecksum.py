# Calculate string checksum: Formula = sum of the ord() values of each character, modulo 10
print("Calculate string checksum: Formula = sum of the ord() values of each character, modulo 10")
input_string = input("Enter the string you want checksum for:")
sum = 0
for ch in input_string:
    sum = sum + ord(ch)
checksum = sum%10
print("The checksum of string is: ",checksum)
