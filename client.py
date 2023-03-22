import qbittorrentapi
import time
from statistics import mean
from abc import abstractmethod

class Client():

    name = ''
    client = 'qbittorrent'
    host = ''
    port = 8085
    username = None
    password = None

    def __init__(self, name, client, host, port, username, password):
        self.name = name
        self.client = client
        self.host = host
        self.port = port
        self.username = username
        self.password = password
        self.init()

    @abstractmethod
    def init(self):
        pass

    def __str__(self):
        return 'client:%s, host:%s, port:%s, username:%s, password:%s' % (self.client, self.host, self.port, self.username, self.password)

    @abstractmethod
    def get_speed(self):
        pass

class ClientQBittorrent(Client):
    client : qbittorrentapi.Client
    max_sample = 5
    speeds_up = []
    speeds_dl = []

    def init(self):
        try:
            self.client = qbittorrentapi.Client(self.host, self.port, self.username, self.password)
            self.client.auth_log_in()
        except qbittorrentapi.LoginFailed as e:
            print(e)

    def get_speed(self):
        # retry
        for i in range(3):
            try:
                if i > 0: #reinit
                    self.init()
                return self.fetch_data()
            except Exception as e:
                print(e)
            time.sleep(i)

    def fetch_data(self):
        info = self.client.transfer.info
        if len(self.speeds_up) >= self.max_sample:
            self.speeds_up.pop(0)
        if len(self.speeds_dl) >= self.max_sample:
            self.speeds_dl.pop(0)

        self.speeds_up.append(info['up_info_speed'])
        self.speeds_dl.append(info['dl_info_speed'])
        return mean(self.speeds_dl), mean(self.speeds_up)

