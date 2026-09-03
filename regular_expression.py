import re

#To match the patterns (begining only not anywhere else)
text1 = "Python is easy to learn"
text2 = "I am learning Python"

pattern = r"Python"

match1 = re.match(pattern, text1)
match2 = re.match(pattern, text2)

print("Text 1:", match1.group() if match1 else "No match")
print("Text 2:", match2.group() if match2 else "No match")


#To search the patterns (anywhere)
text1 = "Python is easy to learn"
text2 = "I am learning Python"

pattern = r"Python"

search1 = re.search(pattern, text1)
search2 = re.search(pattern, text2)

print("Text 1:", search1.group() if search1 else "No match")
print("Text 2:", search2.group() if search2 else "No match")


#To replace the words
replace = "Python Language"
new_text1 = re.sub(pattern, replace, text1)
new_text2 = re.sub(pattern, replace, text2)
print(new_text1)
print(new_text2)


#To split and povide as list
fruits = "apple,banana,orange,grape"
vegetables = "Carrot Beans Cabbage"
pattern1 = r","
pattern2 = r" "
split_result1 = re.split(pattern1, fruits)
split_result2 = re.split(pattern2, vegetables)
print("Split result:", split_result1)
print("Split result:", split_result2)