# iPTStat

**Mac OS在状态栏中实时监控BT/PT下载类软件的速度**

<img width="211" alt="image" src="https://user-images.githubusercontent.com/3390195/226912326-fb03c59b-8d45-45f1-8b39-c734a8027b13.png">


## 构建

```
git clone https://github.com/imaben/iPTStat.git
cd iPTStat
python setup.py py2app
```

## 配置

**目录**

```
$HOME/.config/iPTStat/config.json
```

**内容**

```
{
  "sites": [
    {
      "name": "qb",
      "client": "qbittorrent",
      "host": "your host",
      "port": "8085",
      "username": "admin",
      "password": "admin"
    }
  ]
}
```

可配置多个客户端，状态栏中的上/下行速度是多个客户端的总和。

## 客户端支持

- [x] qbittorrent
- [ ] transmission
- [ ] utorrent
