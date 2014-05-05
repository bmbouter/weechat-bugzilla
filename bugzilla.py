# Copyright (c) 2013 by Wraithan <xwraithanx@gmail.com>

import re

import weechat


SCRIPT_NAME = 'bugzilla'
SCRIPT_AUTHOR = 'Wraithan <xwraithanx@gmail.com>'
SCRIPT_VERSION = '0.0.2'
SCRIPT_LICENSE = 'MIT'
SCRIPT_DESC = "Create bugzilla links from 'bz <number>'"
SCRIPT_COLOR = 'black'

settings = {}

if weechat.register(SCRIPT_NAME, SCRIPT_AUTHOR, SCRIPT_VERSION, SCRIPT_LICENSE, SCRIPT_DESC, '', ''):
    for option, default_value in settings.iteritems():
        if weechat.config_get_plugin(option) == '':
            weechat.config_set_plugin(option, default_value)

    weechat.hook_print('', '', 'bz', 1, 'hook_print_callback', '')


def hook_print_callback(data, buffer, date, tags, displayed, highlight, prefix, message):
    url = '{0}[https://bugzilla.redhat.com/show_bug.cgi?id={1}]'
    for number in re.findall(r'[bB][zZ] ?#?(\d+)', message):
        weechat.command(buffer, url.format(weechat.color(SCRIPT_COLOR), number))

    return weechat.WEECHAT_RC_OK
