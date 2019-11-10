# Calculate the score of each word using sentinel loop
# exit the code when word is "quit"
# word score is the sum of the letter values
# value of any character is the ord() value minus 97

print("Calculate the score of each word using sentinel loop")
input_word = set(input("Enter the word. Enter 'quit' to exit the program:").lower())
alphabet_list = "abcdefghijklmnopqrstuvwxyz"

while input_word != "quit":
    score = 0
    for ch in input_word:
        if ch in alphabet_list:
            score = score + (ord(ch)-97)
        else:
            print("Invalid input. Please enter a string of alphabets")
            break
    if score!=0:
        print("The score of the word is:", score)
    input_word = input("Enter the word. Enter 'quit' to exit the program:").lower()
print("Program ended")