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
from model.DsMatchEventJiaoqiu import DsMatchEventJiaoqiu
from model.DsMatchEventShezheng import DsMatchEventShezheng
from model.DsMatchEventShepian import DsMatchEventShepian
from model.DsMatchEventWeixian import DsMatchEventWeixian
from model.DsMatchEventJingong import DsMatchEventJingong
from model.DsMatchEventJinqiu import DsMatchEventJinqiu


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
        elif item_type == 'DsMatchEventJiaoqiuList':
            self.saveDsMatchEventJiaoqiuList(item)
        elif item_type == 'DsMatchEventJinqiuList':
            self.saveDsMatchEventJinqiu(item)
        elif item_type == 'DsMatchEventJingongList':
            self.saveDsMatchEventJingong(item)
        elif item_type == 'DsMatchEventWeixianList':
            self.saveDsMatchEventWeixian(item)
        elif item_type == 'DsMatchEventShepianList':
            self.saveDsMatchEventShepianList(item)
        elif item_type == 'DsMatchEventShezhengList':
            self.saveDsMatchEventShezhengList(item)
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
        match = session.query(DsMatch).filter(DsMatch.id == item['id']).delete()
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

    def saveDsMatchEventJiaoqiuList(self, item):
        print 'A'
        print item
        list = item['datas']
        match_id = item['match_id']
        session = loadSession()
        session.query(DsMatchEventJiaoqiu).filter(DsMatchEventJiaoqiu.match_id == match_id).delete()
        for i in list:
            jiaoqiu = DsMatchEventJiaoqiu()
            jiaoqiu.match_id = i['match_id']
            jiaoqiu.home_away = i['home_away']
            jiaoqiu.team_name = i['team_name']
            jiaoqiu.time_stamp = i['time_stamp']
            jiaoqiu.v = i['v']
            jiaoqiu.info = i['info']
            session.add(jiaoqiu)
        session.commit()

    def saveDsMatchEventShezhengList(self, item):
        list = item['datas']
        match_id = item['match_id']
        session = loadSession()
        session.query(DsMatchEventShezheng).filter(DsMatchEventShezheng.match_id == match_id).delete()
        for i in list:
            shezheng = DsMatchEventShezheng()
            shezheng.match_id = i['match_id']
            shezheng.home_away = i['home_away']
            shezheng.team_name = i['team_name']
            shezheng.time_stamp = i['time_stamp']
            shezheng.v = i['v']
            shezheng.info = i['info']
            session.add(shezheng)
        session.commit()

    def saveDsMatchEventShepianList(self, item):
        list = item['datas']
        match_id = item['match_id']
        session = loadSession()
        session.query(DsMatchEventShepian).filter(DsMatchEventShepian.match_id == match_id).delete()
        for i in list:
            shepian = DsMatchEventShepian()
            shepian.match_id = i['match_id']
            shepian.home_away = i['home_away']
            shepian.team_name = i['team_name']
            shepian.time_stamp = i['time_stamp']
            shepian.v = i['v']
            shepian.info = i['info']
            session.add(shepian)
        session.commit()

    def saveDsMatchEventWeixian(self, item):
        list = item['datas']
        match_id = item['match_id']
        session = loadSession()
        session.query(DsMatchEventWeixian).filter(DsMatchEventWeixian.match_id == match_id).delete()
        for i in list:
            weixian = DsMatchEventWeixian()
            weixian.match_id = i['match_id']
            weixian.home_away = i['home_away']
            weixian.team_name = i['team_name']
            weixian.time_stamp = i['time_stamp']
            weixian.v = i['v']
            weixian.info = i['info']
            session.add(weixian)
        session.commit()

    def saveDsMatchEventJingong(self, item):
        list = item['datas']
        match_id = item['match_id']
        session = loadSession()
        session.query(DsMatchEventJingong).filter(DsMatchEventJingong.match_id == match_id).delete()
        for i in list:
            jingong = DsMatchEventJingong()
            jingong.match_id = i['match_id']
            jingong.home_away = i['home_away']
            jingong.team_name = i['team_name']
            jingong.time_stamp = i['time_stamp']
            jingong.v = i['v']
            jingong.info = i['info']
            session.add(jingong)
        session.commit()

    def saveDsMatchEventJinqiu(self, item):
        list = item['datas']
        match_id = item['match_id']
        session = loadSession()
        session.query(DsMatchEventJinqiu).filter(DsMatchEventJinqiu.match_id == match_id).delete()
        for i in list:
            jinqiu = DsMatchEventJinqiu()
            jinqiu.match_id = i['match_id']
            jinqiu.home_away = i['home_away']
            jinqiu.team_name = i['team_name']
            jinqiu.time_stamp = i['time_stamp']
            jinqiu.info = i['info']
            jinqiu.v = i['v']
            session.add(jinqiu)
        session.commit()
