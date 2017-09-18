# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

from model import loadSession
from model.DsLeague import DsLeague
from model.DsTeam import DsTeam
from model.DsMatchEvent import DsMatchEvent
from model.DsMatch import DsMatch


class AdaguDsSpiderPipeline(object):
    def process_item(self, item, spider):
        item_type = item.__class__.__name__
        if item_type == 'DsLeague':
            self.saveDsLeague(item)
        elif item_type == 'DsTeam':
            self.saveDsTeam(item)
        elif item_type == 'DsMatch':
            self.saveDsMatch(item)
        elif item_type == 'DsMatchEvent':
            self.saveDsMatchEvent(item)
        return item

    def saveDsLeague(self, item):
        session = loadSession()
        league = session.query(DsLeague).filter(DsLeague.id == item['id']).first()
        if league is None:
            league = DsLeague()
            league.id = item['id']
            league.name = item['name']
            league.url = item['url']
            session.add(league)
            session.commit()

    def saveDsTeam(self, item):
        session = loadSession()
        team = session.query(DsTeam).filter(DsTeam.id == item['id']).first()
        if team is None:
            team = DsTeam()
            team.id = item['id']
            team.name = item['name']
            team.url = item['url']
            session.add(team)
            session.commit()

    def saveDsMatch(self, item):
        session = loadSession()
        match = session.query(DsMatch).filter(DsMatch.id == item['id']).first()
        if match is None:
            match = DsMatch()
            match.id = item['id']
            match.start_time = item['start_time']
            match.league_id = item['league_id']
            match.home_id = item['home_id']
            match.away_id = item['away_id']
            match.home_goal = item['home_goal']
            match.away_goal = item['away_goal']
            match.url = item['url']
            session.add(match)
            session.commit()

    def saveDsMatchEvent(self, item):
        session = loadSession()
        event = session.query(DsMatchEvent).filter(DsMatchEvent.match_id == item['match_id'],
                                                   DsMatchEvent.type == item['type'],
                                                   DsMatchEvent.time_stamp == item['time_stamp'],
                                                   DsMatchEvent.team_name == item['team_name']).first()
        if event is None:
            event = DsMatchEvent()
            event.match_id = item['match_id']
            event.home_away = item['home_away']
            event.team_name = item['team_name']
            event.time_stamp = item['time_stamp']
            event.type = item['type']
            event.v = item['v']
            session.add(event)
            session.commit()
