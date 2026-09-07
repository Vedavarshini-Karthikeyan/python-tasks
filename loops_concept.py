#for loop
aws_resources = ["ec2", "s3", "dynamodb", "r53", "lambda", "cloudfront"]
for i in aws_resources:
    print(i)

#while loo
count = 2
while count<7:
    print(count)
    count+=1

#loop manipulation: break
for a in aws_resources:
    if a == "dynamodb":
        break
    print(a)

#loop manipulation: continue
for b in aws_resources:
    if b == "lambda":
        continue
    print(b)