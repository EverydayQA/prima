#!/usr/bin/python
from gevent import sleep
import gevent


class MyWorker(object):

    def nap(self, n):
        for _ in range(n):
            print("sleep")
            sleep(5)
        return n * 5

    def gevent_nap(self, n):
        for _ in range(n):
            print("sleep")
            gevent.sleep(5)
        return n * 5

    def jogging(self, n):
        for i in range(n):
            print("jogging")
        return n * 3

    def working(self, n):
        """
        working n hours
        """
        # nap n minutes
        a = self.nap(n)
        # jogging n minutes
        b = self.jogging(n)
        return a + b


def main():
    worker = MyWorker()
    worker.run()


if __name__ == '__main__':
    main()
