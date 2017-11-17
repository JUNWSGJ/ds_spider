# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy import Field
from scrapy import Item


class AdaguDsSpiderItem(Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass


class DsLeague(Item):
    id = Field()
    name = Field()
    name_short = Field()
    url = Field()


class DsTeam(Item):
    id = Field()
    name = Field()
    name_short = Field()
    name_en = Field()
    url = Field()


class DsMatch(Item):
    id = Field()
    league_id = Field()
    start_time = Field()
    home_id = Field()
    away_id = Field()
    home_score = Field()
    away_score = Field()
    url = Field()


class DsMatchEventList(Item):
    match_id = Field()
    datas = Field()


class DsMatchEvent(Item):
    id = Field()
    match_id = Field()
    type = Field()
    home_away = Field()
    team_name = Field()
    timestamp = Field()
    v = Field()
    info = Field()


class DsMatchEventTextList(Item):
    match_id = Field()
    datas = Field()


class DsMatchEventText(Item):
    match_id = Field()
    txt = Field()


class DsMatchEventJiaoqiu(Item):
    id = Field()
    match_id = Field()
    home_away = Field()
    team_name = Field()
    time_stamp = Field()
    v = Field()
    info = Field()


class DsMatchEventJiaoqiuList(Item):
    match_id = Field()
    datas = Field()


class DsMatchEventShezheng(Item):
    id = Field()
    match_id = Field()
    home_away = Field()
    team_name = Field()
    time_stamp = Field()
    v = Field()
    info = Field()


class DsMatchEventShezhengList(Item):
    match_id = Field()
    datas = Field()


class DsMatchEventShepian(Item):
    id = Field()
    match_id = Field()
    home_away = Field()
    team_name = Field()
    time_stamp = Field()
    v = Field()
    info = Field()


class DsMatchEventShepianList(Item):
    match_id = Field()
    datas = Field()


class DsMatchEventWeixian(Item):
    id = Field()
    match_id = Field()
    home_away = Field()
    team_name = Field()
    time_stamp = Field()
    v = Field()
    info = Field()


class DsMatchEventWeixianList(Item):
    match_id = Field()
    datas = Field()


class DsMatchEventJingong(Item):
    id = Field()
    match_id = Field()
    home_away = Field()
    team_name = Field()
    time_stamp = Field()
    v = Field()
    info = Field()


class DsMatchEventJingongList(Item):
    match_id = Field()
    datas = Field()


class DsMatchEventJinqiu(Item):
    id = Field()
    match_id = Field()
    home_away = Field()
    team_name = Field()
    time_stamp = Field()
    v = Field()
    info = Field()


class DsMatchEventJinqiuList(Item):
    match_id = Field()
    datas = Field()
