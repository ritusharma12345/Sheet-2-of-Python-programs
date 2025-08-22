n = int(input("Enter a number: "))
n_str = str(n)
rev_str = n_str[::-1]
if n_str == rev_str:
    print("{n} is a palindrome.")
else:
    print("{n} is not a palindrome.")





