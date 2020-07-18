#!/usr/bin/python
from pprint import pprint
import psutil
import datetime


class PSTool(object):

    def __init__(self, **kwargs):
        self.kwargs = kwargs

    def find_processid_bynames(self, names):
        '''
        Get a list of all the PIDs of a all the running process whose name contains
        the given string processName
        '''

        lst = []

        # Iterate over the all the running process
        for proc in psutil.process_iter():
            try:
                pinfo = proc.as_dict(attrs=['pid', 'name', 'create_time'])
                # Check if process name contains the given name string.
                match = self.match_names(pinfo['name'], names)
                if match is True:
                    lst.append(pinfo)
            except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
                pass
        return lst

    def match_names(self, procname, names):
        if not names:
            return False
        if not procname:
            return False
        for item in names:
            if item.lower() not in procname.lower():
                return False
        return True

    def get_create_time(self, create_time):
        return datetime.datetime.fromtimestamp(create_time).strftime("%Y-%m-%d %H:%M:%S")

    def find_processid_byname(self, processName):
        '''
        Get a list of all the PIDs of a all the running process whose name contains
        the given string processName
        '''

        lst = []

        # Iterate over the all the running process
        for proc in psutil.process_iter():
            try:
                pinfo = proc.as_dict(attrs=['pid', 'ppid', 'exe', 'cmdline', 'status', 'cwd', 'username', 'uids', 'gids', 'open_files', 'name', 'create_time'])
                # pprint(pinfo)
                # Check if process name contains the given name string.
                # name
                if processName.lower() in pinfo['name'].lower():
                    lst.append(pinfo)
                    continue
                # exe
                exe = pinfo.get('exe', None)
                if exe and processName.lower() in exe.lower():
                    lst.append(pinfo)
                    continue

                # cmdline
                for item in pinfo['cmdline']:
                    if processName.lower() in item.lower():
                        lst.append(pinfo)
                        break

            except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
                pass
        return lst

    def is_process_running(self, processName):
        '''
        Check if there is any running process that contains the given name processName.
        '''
        # Iterate over the all the running process
        for proc in psutil.process_iter():
            try:
                # Check if process name contains the given name string.
                if processName.lower() in proc.name().lower():
                    return True
            except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
                pass
        return False


def main():
    pst = PSTool()
    items = pst.find_processid_byname('firefox')
    pprint(items)

    # items = pst.find_processid_bynames(['firefox'])
    # pprint(items)

    running = pst.is_process_running('firefox')
    print(running)


if __name__ == '__main__':
    main()
