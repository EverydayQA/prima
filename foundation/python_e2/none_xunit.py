#!/usr/bin//python
from widget import Widget

class TestWidget:
    def testSize(self):
        expectedSize = (40,40)
        widget = Widget()
        if widget.getSize() == expectedSize:
            print "test[Widget}: getSize workds perfect!"
        else:
            print "test:Widget] getSize does not work!"

if __name__ == '__main__':
    myTest = TestWidget()
    myTest.testSize()

