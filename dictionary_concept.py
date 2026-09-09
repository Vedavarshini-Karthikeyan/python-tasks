#dictionary
student_info = {
    "name" : "Veda",
    "age" : "15",
    "class" : "Tenth Standard"
}

print(student_info["class"])

#list of dictionaries
s3_info = [
    {
        "bucket-name": "bucket1",
        "arn" : "arn-12345"
    },
    {
        "bucket-name": "bucket2",
        "arn" : "arn-67890"
    }
]

print(s3_info[1]["bucket-name"])