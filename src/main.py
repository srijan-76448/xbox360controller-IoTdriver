from winsetup import Setup as WinSetup
from linuxsetup import Setup as LinuxSetup
import platform

if platform.system() == 'Windows':
    WinSetup()

else:
    LinuxSetup()

import os, json
import xbox360controller as xbox

mainDir = os.path.dirname(os.path.abspath(__file__))
settings_file_path = os.path.join(mainDir, "settings.json")
settings = dict(json.load(open(settings_file_path)))

dev_mood = settings['dev-mood']
