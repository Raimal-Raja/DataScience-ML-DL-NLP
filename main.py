## file handling and exception handling
try:
    file = open('example.txt', 'r')
    content = file.read()
    a=b
    print(content)
except FileNotFoundError:
    print('The file does not exists')
    
except Exception as e:
    print(e)
    
finally:
    if 'file' in locals() and not file.closed():
        file.close()
        print('file closed')