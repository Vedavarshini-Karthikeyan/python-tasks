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

#To remove the space in the test
text = "   Veda varshini "
stripped_text = text.strip()
print("Stripped text:",stripped_text)
print(text)

#To replace the word
text = "Python is awesome"
new_text = text.replace("awesome", "great")
print("Modified text:", new_text)

#Substring (To find the word in the text)
text = "Python is awesome"
substring = "is"
if substring in text:
    print(substring, "found in the text")