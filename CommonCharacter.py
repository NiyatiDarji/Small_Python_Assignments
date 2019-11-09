# Program to demonstrate set() intersection operation on string
# Program to find if the corresponding elements of two list contains common characters
# e.g.: input: a=['hello','hi'], b= ['world','bye']
# output: yes,no because comparing hello and world gives o,l as same characters. Therefore 'yes'
# similarly comparing hi and bye has no same characters. Hence 'no'

a= ['hello','hi']
b = ['world','bye']
for i in range(0, len(a)):
    str_a = set("".join(a[i].split()))
    str_b = set("".join(b[i].split()))
    response = "NO"
    print(str_a.intersection(str_b))
    if len(str_a.intersection(str_b)) != 0:
        response = "YES"
    print(response)
