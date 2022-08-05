
a = int(input("Enter a number"))
f = open("star.txt", "w")
f.write("Hii john how are you?")
for i in range(a):
    f.write(" "*(a-i)+"* "*i+"\n")
for j in range(a):
     f. write(" "*j+"* "*(a-j)+"\n")
f.close()
f = open("star.txt", "r")
print(f.read())         


