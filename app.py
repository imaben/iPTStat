import rumps
import config

clients = []
config_ready = False

def pretty_print(speed):
    if speed < 1024:
        return '%.2fB/s' % speed
    speed /= 1024
    if speed < 1024:
        return '%.2fKB/s' % speed
    speed /= 1024
    if speed < 1024:
        return '%.2fMB/s' % speed

class App(rumps.App):

    display = []
    menu_items = {}

    def __init__(self):                                 
        super(App, self).__init__("iPTStat", icon='app.icns')
        if not config_ready:
            rumps.notification('未配置客户端', '', '请打开配置目录配置客户端')
            return

        for clt in clients:
            menu_item = rumps.MenuItem(clt.name)
            self.menu_items[clt.name] = menu_item
            self.menu.add(menu_item)

    def refresh_status(self):
        self.title = self.display.pop()

    def get_values(self):
        tdl = tup = 0
        for c in clients:
            dl, up = c.get_speed()
            tdl += dl
            tup += up
            self.menu_items[c.name].title = '%s:↓%s ↑%s' % (c.name, pretty_print(dl), pretty_print(up))
        tdl = pretty_print(tdl)
        tup = pretty_print(tup)
        return tdl, tup

    @rumps.timer(3) 
    def get_stats(self, sender):
        if not config_ready:
            return
        if len(self.display) == 0:
            dl, up = self.get_values()
            dl = '↓%s' % dl
            up = '↑%s' % up
            self.display.append(dl)
            self.display.append(up)

        self.refresh_status()

if __name__ == '__main__':
    config_ready, clients = config.init()
    myapp = App()
    myapp.run()
