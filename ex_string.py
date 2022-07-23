# s1 = "abcdefgh"
# s2="0123456"

# print("Happy :-) "+ "day")

# print("Happy :-) "*2)
# print("Happy :-)"[4])
# print(s1)
# print(s1[3])
# print(s1[1:5])
# print(s2[:3])
# print(s1+s2)
# print(s2[3:])
# print((s1+" ")*3)
# print(len(s1))
# print(s2[-5])
# print(s2[1::2])
# s3=s1*2
# print(s3)
# print(len(s3))

#fruits = ["apple", "banana", "cherry"]
#print(fruits[-1])

st=input("Enter string with 8 chr:")
print(st+"")
print((st+" ")*3)
print(st+st)
print("String length: ",len(st))
print("The 8 characters:",st+"")
print("st[0]={0}".format(st[0]))
print(f"st[1]={st[1]}")
pos=len(st) - 5
print(f"st[{pos}]={st[-5]}")
print("st[3:end]:",st[3:])
print("st[1:8]:",st[1:8])
print("skip in 2 number from the start:",st[::2])
print("skip in 2 number from st[3]:",st[3::2])

print("from end to start:", st[::-1])