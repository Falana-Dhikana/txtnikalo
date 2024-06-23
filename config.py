#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) ACE 

import os

class Config(object):
    # get a token from @BotFather
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "5947183588:AAHeZa8qM5UWUl3eINvoe0rWKUWzG_g3Bl8")
    API_ID = int(os.environ.get("API_ID", "14852801"))
    API_HASH = os.environ.get("API_HASH", "d4cee9b844c63eb5b1bcc8e3426beb40")
    AUTH_USERS = os.environ.get("AUTH_USERS", "1832139347")
