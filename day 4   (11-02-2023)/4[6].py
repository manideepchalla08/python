def delchar(s,c):

    if(len(c)==1):
        for i in range(len(s)):
            if(c is not s[i]):
               print(s[i])
            else:
                 continue
a=input("enter a pharese")
b=input("enter the letter to be deleted")
delchar(a,b)
