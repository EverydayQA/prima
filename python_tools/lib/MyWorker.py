#!/usr/bin/python
#from gevent import sleep

class MyWorker(object):
    def run(self):
        for _ in range(10):
            print ("sleep")
            #sleep(1)
def main():
    worker = MyWorker()
    worker.run()
    

if __name__ == '__main__':
    main()

