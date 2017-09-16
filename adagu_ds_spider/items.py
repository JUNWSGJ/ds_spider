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
    url = Field()

class DsMatch(Item):
    id = Field()
    league_id = Field()
    start_time = Field()
    home_id = Field()
    away_id = Field()
    home_goal = Field()
    away_goal = Field()
    url = Field()

class DsMatchEvent(Item):
    id = Field()
    match_id = Field()
    home_away = Field()
    team_name = Field()
    time_stamp = Field()
    type = Field()
    v = Field()
