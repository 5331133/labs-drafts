def chk_command(cmd, namesp, arg):
    """---command type processing---"""
    if cmd == 'add':
        add_func(namesp, arg)
    elif cmd == 'create':
        create_func(namesp, arg)
    elif cmd == 'get':
        get_func(namesp, arg)


def add_func(namesp, arg):
    """---'add' command processing---"""
    if namesp == 'global':
        dic['global']['vars'].append(arg)
    else:
        dic[namesp]['vars'].append(arg)


def create_func(namesp, arg):
    """---'create' command processing---"""
    if arg == 'global':
        dic.update({namesp: {'parent': None, 'vars': []}})
    else:
        dic.update({namesp: {'parent': arg, 'vars': []}})

def get_func(namesp, arg):
    """---'get' command processing---"""
    if namesp == 'global' and arg not in dic[namesp]['vars']:
        print("None")
    elif arg in dic[namesp]['vars']:
        print(arg, namesp)
    else:
        namesp = dic[namesp]['parent'] or 'global'
        get_func(namesp, arg)

test1 = [['create', 'foo', 'global'], ['create', 'bar', 'foo'], ['create', 'barz', 'bar'],
        ['create', 'bary', 'barz'], ['add', 'bar', 'b'], ['create', 'zoo', 'bar'], ['create', 'zoo2', 'zoo'],
        ['create', 'zoo3', 'zoo2'], ['add', 'bary', 'b'], ['create', 'doo', 'zoo'],
        ['get', 'foo', 'a']]  # ---testing list 'get', 'zoo', 'a'
test2 = [['add', 'global', 'a'], ['create', 'foo', 'global'], ['add', 'foo', 'b'],
        ['get', 'foo', 'a'], ['get', 'foo', 'c'], ['create', 'bar', 'foo'], ['add', 'bar', 'a'],
        ['get', 'bar', 'a'], ['get', 'bar', 'b']]  # ---testing list

dic = {'global': {'parent': None, 'vars': []}}

for i in test2:  # ---test
    cmd, namesp, arg = i  # ---test
    chk_command(cmd, namesp, arg)  # ---test
print(dic)



# for i in range (int(input())): #---number of inputs---
#    cmd, namesp, arg = input().split()
#    chk_command(cmd, namesp, arg)



#9
#add global a
#create foo global
#add foo b
#get foo a
#get foo c
#create bar foo
#add bar a
#get bar a
#get bar b

#Correct output:
#global
#None
#bar
#foo