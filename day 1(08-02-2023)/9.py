time=int(input("enter the number of time slots:"))
entry=[int(input("enter the number of guests entring at time slot{}:".format(i+1)))for i in range(time)]
exit=[int(input("enter the number of gustes exiting at time slot{}:".format(i+1)))for i in range(time)]

count=0
gustes=[]
for i in range(len(entry)):
    count=count+entry[i]-exit[i]
    gustes.append(count)

print("the maximum number of gustes present at any time:",max(gustes))
