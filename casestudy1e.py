# code to determine if a number is a palindrome or not

# getting the input
num = input("Enter a number: ") 

#determining if palindrome or not
if num == num[::-1]: 
    print("Palindrome") 
else: 
    print("Not a Palindrome") 