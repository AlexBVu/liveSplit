from setuptools import setup

APP = ['livesplit.py']
OPTIONS = {
    'argv_emulation': False,          # must be False for rumps
    'plist': {
        'CFBundleName': 'livesplit',
        'CFBundleIdentifier': 'com.alexvu.livesplit',
        'LSUIElement': True,          # status-bar only, no Dock icon
    },
}

setup(
    app=APP,
    options={'py2app': OPTIONS},
)