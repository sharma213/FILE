# fh=open("python.txt","r")
# count=0
# lines=fh.readlines()
# for a in lines:
#     if (a.tolower().count("to") > 0) :
#           print(a)
# fh.close()





# f = open("demofile.txt",mode='w')
# data= f.write("manpreet-karishma")
# data=f.write("laxmi-aasama")
# data=f.write("ankit -harsh")
# data=f.write("rani-anshika")
# print(data)
# f.close()

# my_file2 = open("student2.txt", "w")
# my_file2.write("rani - anshika\n")
# my_file2.write("manpreet - karishma\n")
# my_file2.close()

# f=open('student2.txt',mode='r')
# data=f.read()
# print(data)

# f=open("student2.txt",mode="r")
# print(f.tell())
# data1=f.read(11)
# print(data1)


# f=open("student2.txt",mode="r")
# print(f.seek(11))
# data1=f.read(20)
# print(data1)


f=open('student2.txt',mode='r')
print(f.tell())
data1=f.read(6)
print(data1)
print(f.tell())
data2=f.read(3)
print(data2)
print(f.tell())