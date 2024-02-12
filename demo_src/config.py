# -*- coding: utf-8 -*-
"""Sample Configuration
"""

# For Maverick
site_prefix = "./"
template = "Galileo"
index_page_size = 10
archives_page_size = 30
fetch_remote_imgs = False
enable_jsdelivr = {
    "enabled": False,
    "repo": "AlanDecode/Maverick@gh-pages"
}
locale = "Asia/Shanghai"
category_by_folder = False

# For site
site_name = "jsq's blog"
site_logo = "${site_prefix}android-chrome-512x512.png"
site_build_date = "2024-2-08T12:00+08:00"
author = "jsq"
email = "deserverest2@gmail.com"
author_homepage = "github.com/Ji-Siqi"
description = "This is jsq's blog."
key_words = ["信息学", "JSQ", "OI", "blog", "C++"]
language = 'Chinese'
external_links = [
    {
        "name": "Maverick",
        "url": "https://github.com/AlanDecode/Maverick",
        "brief": "🏄‍ Go My Own Way."
    }
]
nav = [
    {
        "name": "Home",
        "url": "${site_prefix}",
        "target": "_self"
    },
    {
        "name": "Archives",
        "url": "${site_prefix}archives/",
        "target": "_self"
    },
    {
        "name": "About",
        "url": "${site_prefix}about/",
        "target": "_self"
    },
    {
        "name": "电子木鱼",
        "url": "${site_prefix}woodfish/",
        "target": "_self"
    }
]

social_links = [
    {
        "name": "GitHub",
        "url": "https://github.com/Ji-Siqi",
        "icon": "gi gi-github"
    }
]

valine = {
    "enable": True,
    "el": '#vcomments',
    "appId": "IKRAfuPq0zrz6Wfje8ahHAIP-gzGzoHsz",
    "appKey": "lFaCWkd4xCs0Ng5UWs1eHNwU",
    "visitor": True,
    "recordIP": True
}

head_addon = ''

footer_addon = ''

body_addon = ''
