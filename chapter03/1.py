
##import os
##
##
##print(os.getcwd())
##os.chdir("C:\\Users\\35191\\Desktop\\chapter03")
##print(os.getcwd())
##
##data = open("sketch.txt")
##print(data.readline(), end='')
##print(data.readline(), end='')
##data.seek(0)
##for each_line in data:
##    print(each_line, end='')
##data.close()


data = open("sketch.txt")
for each_line in data:
    (role, line_spoken) = each_line.split(':')
    print(role, end='')
    print(' said: ', end='')
    print(line_spoken, end='')

data.close()
