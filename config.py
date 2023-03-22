import os, json, pathlib
import client

config_path = os.path.join(pathlib.Path.home(), '.config', 'iPTStat')
config_file = os.path.join(config_path, 'config.json')

config_empty = '''{
  "sites": [
    {
        "name": "qb",
        "client": "qbittorrent",
        "host": "",
        "port": "8085",
        "username": "",
        "password": ""
    }
  ]
}
'''

def init_empty_config():
    if not os.path.exists(config_path):
        os.mkdir(config_path)
        with open(config_file, 'w') as fp:
            fp.write(config_empty)

def init():
    global interval
    if not os.path.exists(config_file):
        init_empty_config()
        return False, []

    clients = []
    with open(config_file) as fp:
        config = json.load(fp)
        if 'sites' not in config:
            raise Exception('config invalid')

        for site in config['sites']:
            if invalid_site(site):
                continue
            clazz = None
            if site['client'] == 'qbittorrent':
                clazz = client.ClientQBittorrent
            else:
                raise Exception('unsupport client %s' % site['client'])
            clt = clazz(site['name'], site['client'], site['host'], site['port'], site['username'], site['password'])
            clients.append(clt)

    return len(clients) > 0, clients

def invalid_site(site):
    return empty_str(site["name"]) or empty_str(site['client']) or empty_str(site['host']) or empty_str(site['port']) or empty_str(site['username']) or empty_str(site['password'])

def empty_str(str):
    return str is None or len(str) == 0
