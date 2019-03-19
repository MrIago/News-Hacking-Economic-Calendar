import functions, data

'''
# test the separator function
d = {}
d = functions.sep_items(d, data.headers_file, ':')
for k in d:
    print(k, d[k], sep=' -------> ')
'''

'''
# test the class
user = data.user()
functions.print_dict(user.headers, '\t<----->\t')
'''
