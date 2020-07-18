import psutil
from pprint import pprint


class CallerStack(object):

    def __init__(self):
        self.d = {}
        self.psme()

    def psutil(self):
        me = psutil.Process()
        print(me)
        print(me.cmdline())
        print(me.ppid())
        parent = psutil.Process(me.ppid())
        print(parent)
        print(parent.cmdline())
        gp = psutil.Process(parent.ppid())
        print(gp.cmdline())

    def create_time_iso(self, timestamp):
        import datetime
        return datetime.datetime.fromtimestamp(timestamp).strftime("%Y-%m-%dT%H:%M:%S")

    def ps_parent(self, ppid):
        if not ppid:
            print('not ppid')
            return
        me = psutil.Process(ppid)
        if not me:
            print('not me')
            return
        dp = me.as_dict(attrs=self.keys())
        create_time = self.create_time_iso(dp.get('create_time', None))
        dp['create_time'] = create_time
        self.d[me.ppid()] = dp
        return self.ps_parent(me.ppid())

    def psme(self):
        print('\n*** psme')
        me = psutil.Process()
        dp = me.as_dict(attrs=self.keys())
        create_time = self.create_time_iso(dp.get('create_time', None))
        dp['create_time'] = create_time
        self.d[me.ppid()] = dp
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
    pprint(ca.d)


if __name__ == '__main__':
    main()
