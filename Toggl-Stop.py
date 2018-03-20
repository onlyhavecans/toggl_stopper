#!/usr/bin/env python3

from TogglPy.TogglPy import Toggl
from pathlib import Path

CONFIG = '~/.togglapikey'

if __name__ == '__main__':
    config = Path(CONFIG).expanduser()
    api_key = config.read_text().strip()
    toggl = Toggl()
    toggl.setAPIKey(api_key)
    currentTimer = toggl.currentRunningTimeEntry()
    if currentTimer['data'] != None:
        toggl.stopTimeEntry(currentTimer['data']['id'])
