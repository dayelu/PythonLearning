with open("../recycle/confirmed_users.txt") as py_object:
    content = py_object.read()          #python读文件存在严重的乱码问题
    print(content.rstrip())
