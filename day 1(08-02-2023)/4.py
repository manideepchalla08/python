def is_palindrome(x):
    if x<0:
        return False
    return str(x)==str(x)[::-1]
x=int(input("entre an integer:"))
result = is_palindrome(x)
if result:
    print("the integer is a palidrome")
else:
     print("the integer is not a palindrome")
