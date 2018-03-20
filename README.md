#TOGGL-STOP

This makes a mac program that stops whatever you are currently doing in toggl.

This program run silently and will do nothing if you do not have a timer running.
If you are missing the `~/.togglapikey` file then it currently errors silently. _I should change this_

## Usage

1. Createthe file `~/.togglapikey` and place _only_ [your api key](https://toggl.com/app/profile) in it.
1. `make` to create the app
1. copy `dist/Toggl-Stop.app` wherever you keep your apps.


## Why?
Well I have a few commands and scripts I'd like to hotkey, stopping Toggl is my top one and an app is the easiest thing to call out to. I may also make some simple apps for starting common Toggl things I monitor.
