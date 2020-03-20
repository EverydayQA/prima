#!/usr/bin/python
import os

index = 'src/haha.txt'


def get_dynamic_index(index):
    path = os.path.abspath(__file__)
    dirname = os.path.dirname(path)
    print dirname
    path = os.path.join(dirname, index)
    return path


def loadTopicNames():
    path = get_dynamic_index(index)
    print path
    with open(index, 'r') as file:
        data = file.readlines()
        topicNames = []
        for row in data:
            row = row.replace('\n', '')
            topicNames.append(row)
        return topicNames


def readFile():
    print ("readFile")
    try:
        fileName = open("./src/haha.txt", 'r')
        data = fileName.read().split()
        data.sort(key=int)
        print(data)

    except IOError:
        print("Error: File do not exist")
        return


def main():
    # readFile()
    print loadTopicNames()


if __name__ == '__main__':
    main()
