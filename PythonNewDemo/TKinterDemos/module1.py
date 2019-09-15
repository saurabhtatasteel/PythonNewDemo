str = "this is string example....wow!!!"

suffix = "wow!!!"
print(str.endswith(suffix))
print(str.endswith(suffix,20))

suffix = "is"
print(str.endswith(suffix, 2, 4))
print(str.endswith(suffix, 2, 6))


#print(len(str))

str = "this is string example....wow!!!"
print (str.ljust(60, '0'))

str = "shubhra shalini is shubhra shalini z";
print ("Max character: " + max(str))

str = "this is a string example....wow!!!";
print ("Max character: " + max(str))


str1 = "this is string example....wow!!!";
print(str1.rjust(20, '0'))


print('India\nJapan\nUSA\nUK\nCanada\n'.splitlines()) 