def countVovelStrings(n):
    return sum(range(1,n+1))
n=int(input("enter the length of the strings:"))
result=countVovelStrings(n)
print("the number of lexicographically sorted strings of length:",n,"consistint only of vowels is:",result)
