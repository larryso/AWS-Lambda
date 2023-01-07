

my_dict = {'colum1': ['v1','v2'], 'colum2':['v3, v4'], 'culum3': 'testString'}

print(my_dict)

for i in my_dict:
    print(my_dict[i])

print(my_dict["colum1"])

my_dict["colum4"] = "colum4_value"

print(my_dict)

my_dict.pop("colum4")
print(my_dict)
