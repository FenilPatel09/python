f=open("A.txt","r")
games=[]
for i in f:
    part=i.strip().split()
    t1,s1,t2,s2=part[1],int(part[2]),part[3],int(part[4])
    games.append([t1,s1,t2,s2])
c=0
total=0
for i in games:
    total+=i[1]+i[3]
    c+=2
print("avg points : ",total/c)