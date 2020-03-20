from work.workm import work_on

class WorkCaller:
    def call_work(self):
        # Do important stuff that I want to test here

        # This call I don't care about in the test, but it needs to be called
        work_on()
