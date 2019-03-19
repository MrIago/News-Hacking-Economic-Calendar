def sep_items(dct, file, separator):
    f = open(file)
    text = f.readlines()

    '''
    a = "".join(text)
    print("Num de linhas: ", a.count("\n"))
    '''

    for i in text:
        content = i.split(separator)
        dct[content[0]] = content[1].strip()
    return dct

def print_dict(dct, sep='\t'):
    for k in dct:
        print(k, dct[k], sep=sep)

def print_list(lst, sep='\t'):
    for i in lst:
        print(i, sep=sep)
