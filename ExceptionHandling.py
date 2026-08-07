# Lesson: Exception Handling (try / except)

def divide(a,b):
    try :
        c=a/b
        print(c)
    except Exception as e:
        print(e)
divide(10,0)

def read_file(filename):
    try:
       with open(f'filename','r') as file:
        return file.readlines()
    except FileNotFoundError:
       print('File does not exist')

read_file('ed')