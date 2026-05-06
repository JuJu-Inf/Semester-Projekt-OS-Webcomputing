#!/usr/bin/python3
print('Content-type: text/html \n')
class Print:
    def __init__(self):
        print('Hello World! \n')

N = 5
a = [Print() for i in range(N)] 
