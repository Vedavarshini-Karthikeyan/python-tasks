#To split
arn = "arn:aws:iam:123456:user/Veda"
print(arn.split("/"))
print(arn.split("/")[1])

#To switch the cases
name = "vedavarshini"
print(name.upper())
print(name.lower())

#To concat
str1 = "Veda"
str2 = "varshini"
res1 = str1 + str2
res2 = str1 + " " + str2
print(res1)
print(res2)

#To print the length
length = len(arn)
print(length)