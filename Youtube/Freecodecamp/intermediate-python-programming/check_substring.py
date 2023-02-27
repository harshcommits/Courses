string = "TestBucket"
if "buc" in string:
    print("yes")
else:
    print("No")

print(string.startswith("T"))

#returns -1 if nothing found
print(string.find(('Bucket')))

print(string.count('e'))

print(string.replace('Bucket', 'Project'))

print("How are you doing".split(","))