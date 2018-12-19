#!/usr/bin/env python3
import platform

def main():
    message()
def message():
    print('the python version = {}'.format(platform.python_version()))
if __name__=='__main__':main()