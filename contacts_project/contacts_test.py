import ast

a = 4

print(type(a))

test = open("masterlist_test","r")
test_str = test.read()
test_list = ast.literal_eval(test_str)
test_list.append([['First Name', 'Harrison'], ['Last Name', 'Yao'], ['Email', 'harrisonyaochip@gmail.com'], ['Phone Number', '6473811882']])
test.close()

test1 = open("masterlist_test", "w")
test1.write(str(test_list))

print(test_list)
print(type(test_list))
print(type(test_str))
test.close()

