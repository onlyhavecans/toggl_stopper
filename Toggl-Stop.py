#!/usr/bin/env python3

from pathlib import Path
from TogglPy.TogglPy import Toggl

CONFIG = '~/.togglapikey'

if __name__ == '__main__':
    config = Path(CONFIG).expanduser()
    api_key = config.read_text().strip()
    toggl = Toggl()
    toggl.setAPIKey(api_key)
    currentTimer = toggl.currentRunningTimeEntry()
    if currentTimer['data'] is not None:
        toggl.stopTimeEntry(currentTimer['data']['id'])
