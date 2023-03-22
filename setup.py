from setuptools import setup

APP = ['app.py']
DATA_FILES = ['app.icns']
OPTIONS = {
    'argv_emulation': True,
    'iconfile': 'app.icns',
    'plist': {
        'LSUIElement': True,
    },
    'packages': ['rumps', 'qbittorrentapi'],
}

setup(
    name = 'iPTStat',
    version = '0.0.1',
    app=APP,
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
)
