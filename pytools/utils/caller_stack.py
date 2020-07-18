import sys
from pprint import pprint
import traceback


class CallerStack(object):

    def __init__(self):
        self.d = {}
        self.psme()
        pprint(self.d)

    def os_trackback(self):
        # items = sys.last_traceback()
        # pprint(items)
        # items = sys.call_tracing()
        # pprint(items)
        pprint(sys.exc_info())
        pprint(traceback.extract_stack())
        pprint(traceback.format_exc())
        pprint(traceback.StackSummary())

    def psutil(self):
        import psutil
        me = psutil.Process()
        print(me)
        print(me.cmdline())
        print(me.ppid())
        parent = psutil.Process(me.ppid())
        print(parent)
        print(parent.cmdline())
        gp = psutil.Process(parent.ppid())
        print(gp.cmdline())

    def ps_parent(self, ppid):
        import psutil
        if not ppid:
            print('not ppid')
            return
        me = psutil.Process(ppid)
        if not me:
            print('not me')
            return
        self.d[me.ppid()] = me.as_dict(attrs=self.keys())
        return self.ps_parent(me.ppid())

    def psme(self):
        print('\n*** psme')
        import psutil
        me = psutil.Process()
        # pprint(me.as_dict().keys())
        self.d[me.ppid()] = me.as_dict(attrs=self.keys())
        self.ps_parent(me.ppid())

    def keys_rm(self):
        """
        attrs that do not need for this app
        """
        return ['memory_percent',
                'memory_maps',
                'memory_full_info',
                'memory_info',
                'cpu_percent',
                'cpu_times',
                'cpu_num',
                'cpu_affinity',
                'ionice',
                'num_ctx_switches',
                'threads',
                'io_counters',
                'connections',
                'environ']

    def keys(self):
        """
        all attrs for current version
        """
        items = set(self.keys_all()) - set(self.keys_rm())
        return list(items)

    def keys_all(self):
        return ['uids', 'cpu_affinity', 'open_files', 'memory_full_info', 'cwd', 'environ', 'pid', 'ppid', 'num_threads', 'cpu_num', 'connections', 'terminal', 'num_fds', 'ionice', 'threads', 'cpu_percent', 'memory_maps', 'create_time', 'name', 'gids', 'memory_percent', 'num_ctx_switches', 'exe', 'cpu_times', 'cmdline', 'username', 'status', 'memory_info', 'nice', 'io_counters']


def main():
    ca = CallerStack()
    ca.psutil()
    ca.psme()


if __name__ == '__main__':
    main()
