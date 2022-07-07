# f=open("people2.txt",mode="r+")
# f.write('priyanka - shimla/nneela-delhi/nsashi-jaipur/n sarika-delhi/n deepti-shimla')
# data=f.readlines()
# print(len(data))
# f.close()

f=open('people1-exercise.txt',mode='r' )
c=0
for line in f:
    if line !="\n":
        c+=1
print(c)
f.close()