#!/usr/bin/python
def readFile():
    print ("readFile")
    try:
        fileName = open("haha.txt",'r')
        data = fileName.read().split()
        data.sort(key=int)
        print(data)

    except IOError:
        print("Error: File do not exist")
        return

def main():
    readFile()
if __name__ == '__main__':
    main()
