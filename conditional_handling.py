import sys
type = sys.argv[1]

if type == "t2.micro":
    print("This will cost 2rs per day")

elif type == "t2.small":
    print("This is cost 4rs per day")

elif type == "t2.medium":
    print("This is cost 8rs per day")

elif type == "t3.xlarge":
    print("This is cost 16rs per day")

else:
    print("Provide the valid instance")