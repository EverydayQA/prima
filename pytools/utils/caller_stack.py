import psutil
import datetime
from pprint import pprint


class CallerStack(object):

    def __init__(self):
        self.now = datetime.datetime.now()
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
        return datetime.datetime.fromtimestamp(timestamp).strftime("%Y-%m-%dT%H:%M:%S.%f")[:-3]

    def create_datetime(self, timestamp):
        if not timestamp:
            return None
        if not isinstance(timestamp, float):
            return None

        return datetime.datetime.fromtimestamp(timestamp)

    def ps_parent(self, ppid):
        if not ppid:
            print('not ppid')
            return
        me = psutil.Process(ppid)
        if not me:
            print('not me')
            return
        dp = me.as_dict(attrs=self.keys())
        if self.skip_log_process(dp) is False:
            create_time = self.create_time_iso(dp.get('create_time', None))
            dp['create_time'] = create_time

            self.d[me.pid] = dp

        return self.ps_parent(me.ppid())

    def psme(self):
        print('\n*** psme')
        me = psutil.Process()
        dp = me.as_dict(attrs=self.keys())
        if self.skip_log_process(dp) is False:
            create_time = self.create_time_iso(dp.get('create_time', None))
            dp['create_time'] = create_time

            self.d[me.pid] = dp
        self.ps_parent(me.ppid())

    def skip_log_process(self, dp):
        username = dp.get('username', None)
        if username == 'root':
            return True
        dt_create = self.create_datetime(dp.get('create_time', None))
        if not dt_create:
            return False
        delta = self.now - dt_create
        if delta.seconds > 6 * 3600:
            return True
        return False

    def keys_rm(self):
        """
        attrs that do not need for this app
        """
        return ['cpu_percent',
                'cpu_times',
                'cpu_num',
                'cpu_affinity',
                'connections',

                'gids',
                'ionice',
                'io_counters',
                'memory_percent',
                'memory_maps',
                'memory_full_info',
                'memory_info',
                'nice',
                'num_fds',
                'num_threads',
                'num_ctx_switches',
                'open_files',
                'status',
                'threads',
                'terminal',
                'uids',
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
