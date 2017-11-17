# -*- coding: UTF-8 -*-

import sys

reload(sys)

sys.setdefaultencoding('utf-8')

import datetime
import json

from scrapy.spiders import Spider
from scrapy import Request
from adagu_ds_spider.items import DsLeague, DsMatch, DsTeam, DsMatchEvent, DsMatchEventList, DsMatchEventText, \
    DsMatchEventTextList


class dsSpider(Spider):
    name = 'ds'
    allowed_domains = ['dszuqiu.com']
    # start_urls = ['https://www.dszuqiu.com/race_xc/394590']

    # start_urls = ['https://www.dszuqiu.com/diary/20170701/p.5']

    # start_urls = ['https://www.dszuqiu.com/race_xc/342955']

    def __init__(self):
        self.init_start_urls()
        pass

    def init_start_urls(self):
        begin_date = datetime.datetime.strptime('2015-01-01', "%Y-%m-%d")
        end_date = datetime.datetime.strptime('2016-12-31', '%Y-%m-%d')

        while begin_date <= end_date:
            date_str = begin_date.strftime("%Y%m%d")
            url = 'https://www.dszuqiu.com/diary/' + date_str + '/p.1'
            begin_date += datetime.timedelta(days=1)
            self.start_urls.append(url)

    def start_request(self):
        for url in self.start_urls:
            yield Request(url, self.parse)

    def parse(self, response):
        if response.url.find('diary') >= 0:
            return self.parse_diary(response)
        elif response.url.find('race_xc') >= 0:
            return self.parse_event(response)
        elif response.url.find('/league/') >= 0:
            return self.parse_league(response)
        elif response.url.find('/team/') >= 0:
            return self.parse_team(response)

    def gen_league_url(self, league_id):
        return 'https://www.dszuqiu.com/league/' + str(league_id)

    def gen_team_url(self, team_id):
        return 'https://www.dszuqiu.com/team/' + str(team_id)

    def get_id_from_url(self, url):
        if url.find('league') > 0:
            return url.split('league')[1].replace('/', '')
        else:
            return url.split('team')[1].replace('/', '')

    def parse_diary(self, response):
        # print response.xpath('//div[@id="pager"]/text()').extract_first()
        tr_list = response.xpath('//div[@id="diary_info"]/table/tbody/tr')
        tr_list_len = len(tr_list)
        for tr in tr_list:
            # 1.联赛信息
            league_href = tr.xpath('./td[1]/a/@href').extract_first()
            league_href_splits = league_href.split('/')
            league_id = league_href_splits[len(league_href_splits) - 1]
            # league_name = tr.xpath('./td[1]/a/text()').extract_first()
            # dsLeague = DsLeague()
            # dsLeague['id'] = league_id
            # dsLeague['name'] = league_name
            # dsLeague['url'] = league_href
            # yield dsLeague
            league_url = self.gen_league_url(league_id)
            yield Request(league_url, self.parse)

            # 2.比赛时间
            start_time_txt = '20' + tr.xpath('./td[3]/text()').extract_first()
            start_time = datetime.datetime.strptime(start_time_txt, '%Y/%m/%d %H:%M')

            # 3.主队
            home_href = tr.xpath('./td[4]/a/@href').extract_first()
            home_href_splits = home_href.split('/')
            home_id = home_href_splits[len(home_href_splits) - 1]
            # home_name = tr.xpath('./td[4]/a/text()').extract_first().strip()
            # dsTeam = DsTeam()
            # dsTeam['id'] = home_id
            # dsTeam['name'] = home_name
            # dsTeam['url'] = home_href
            # yield dsTeam
            home_url = self.gen_team_url(home_id)
            yield Request(home_url, self.parse)

            # 4.比赛结果
            results = tr.xpath('./td[5]/text()').extract_first()
            home_score = results.split(':')[0].strip()
            away_score = results.split(':')[1].strip()

            # 5.客队
            away_href = tr.xpath('./td[6]/a/@href').extract_first()
            away_href_splits = away_href.split('/')
            away_id = away_href_splits[len(away_href_splits) - 1]
            # away_name = tr.xpath('./td[6]/a/text()').extract_first().strip()
            # dsTeam = DsTeam()
            # dsTeam['id'] = away_id
            # dsTeam['name'] = away_name
            # dsTeam['url'] = away_href
            # yield dsTeam
            away_url = self.gen_team_url(away_id)
            yield Request(away_url, self.parse)

            match_href = tr.xpath('./td[9]/div[@class="statusListWrapper"]/a/@href').extract_first()
            match_href_splits = match_href.split('/')
            match_id = match_href_splits[len(match_href_splits) - 1]
            dsMatch = DsMatch()
            dsMatch['id'] = match_id
            dsMatch['start_time'] = start_time
            dsMatch['league_id'] = league_id
            dsMatch['home_id'] = home_id
            dsMatch['away_id'] = away_id
            dsMatch['home_score'] = home_score
            dsMatch['away_score'] = away_score
            dsMatch['url'] = match_href
            yield dsMatch
            yield Request('https://www.dszuqiu.com' + match_href, self.parse)

        if tr_list_len > 0:
            current_url = response.url
            current_url_splits = current_url.split('p.')
            current_page = int(current_url_splits[1]) + 1
            next_page_url = current_url_splits[0] + 'p.' + str(current_page)
            yield Request(next_page_url, self.parse)

    def parse_team(self, response):
        team_name_text = response.xpath(
            '//main[@id="pjax-container"]//div[@class="teamInfo"]/h1/text()').extract_first()
        print team_name_text
        if team_name_text is not None:
            team_names = team_name_text.split('/')
            team_name = team_names[0].strip(' ')
            team_name_en = '' if len(team_names) < 2 else team_names[1].strip(' ')
            team = DsTeam()
            team['id'] = self.get_id_from_url(response.url)
            team['name'] = team_name
            team['name_short'] = None
            team['name_en'] = team_name_en
            team['url'] = response.url
            yield team

    def parse_league(self, response):
        league_name_text = response.xpath('//main[@id="pjax-container"]/div[1]//h1/text()').extract_first()
        if league_name_text is not None:
            league_names = league_name_text.split('：')[1].split('，')
            league_name = league_names[0] if len(league_names) > 0 else ''
            league_short_name = league_names[1] if len(league_names) > 1 else ''
            league = DsLeague()
            league['id'] = self.get_id_from_url(response.url)
            league['name'] = league_name
            league['name_short'] = league_short_name
            league['url'] = response.url
            yield league

    def parse_event(self, response):
        current_url = response.url
        match_id = current_url.split('race_xc/')[1]
        scripts = response.xpath('//script')
        events = []
        for script in scripts:
            script_txt = str(script.xpath('./text()').extract_first())
            if script_txt.find('$(\'#shezheng\').highcharts') != -1 \
                    or script_txt.find('$(\'#shepian\').highcharts') != -1 \
                    or script_txt.find('$(\'#danger\').highcharts') != -1 \
                    or script_txt.find('$(\'#attack\').highcharts') != -1:
                # print script_txt
                # 1. 射正球门
                shezheng_start = script_txt.find('shezheng_chart_options.series =')
                shezheng_end = script_txt.find('$(\'#shezheng\').css')
                shezheng_txt = script_txt[shezheng_start:shezheng_end].replace('shezheng_chart_options.series =',
                                                                               '').strip()
                shezheng_txt = shezheng_txt[:len(shezheng_txt) - 1].replace('\'', '"')
                # print shezheng_txt
                shezheng_json = json.loads(shezheng_txt)
                shezheng_json0 = shezheng_json[0]
                team_name0 = shezheng_json0['name']
                team_data0 = shezheng_json0['data']
                jiaoqiu = []
                shezheng = []
                jinqiu = []
                for d in team_data0:
                    if d['marker'].has_key('radius'):
                        event = DsMatchEvent()
                        event['match_id'] = match_id
                        event['home_away'] = 'h'
                        event['type'] = 'o'
                        event['team_name'] = team_name0
                        event['timestamp'] = d['x']
                        event['v'] = d['y']
                        event['info'] = d['info']
                        events.append(event)
                    elif d['marker'].has_key('symbol'):
                        symbol = d['marker']['symbol']
                        if symbol.find('icon_corner') >= 0:
                            event = DsMatchEvent()
                            event['match_id'] = match_id
                            event['home_away'] = 'h'
                            event['type'] = 'c'
                            event['team_name'] = team_name0
                            event['timestamp'] = d['x']
                            event['v'] = d['y']
                            event['info'] = d['info']
                            events.append(event)
                        elif symbol.find('icon_goal') >= 0:
                            event = DsMatchEvent()
                            event['match_id'] = match_id
                            event['home_away'] = 'h'
                            event['type'] = 'g'
                            event['team_name'] = team_name0
                            event['timestamp'] = d['x']
                            event['v'] = d['y']
                            event['info'] = d['info']
                            events.append(event)

                shezheng_json1 = shezheng_json[1]
                team_name1 = shezheng_json1['name']
                team_data1 = shezheng_json1['data']
                for d in team_data1:
                    if d['marker'].has_key('radius'):
                        event = DsMatchEvent()
                        event['match_id'] = match_id
                        event['home_away'] = 'a'
                        event['type'] = 'o'
                        event['team_name'] = team_name1
                        event['timestamp'] = d['x']
                        event['v'] = d['y']
                        event['info'] = d['info']
                        events.append(event)
                    elif d['marker'].has_key('symbol'):
                        symbol = d['marker']['symbol']
                        if symbol.find('icon_corner') >= 0:
                            event = DsMatchEvent()
                            event['match_id'] = match_id
                            event['home_away'] = 'a'
                            event['type'] = 'c'
                            event['team_name'] = team_name1
                            event['timestamp'] = d['x']
                            event['v'] = d['y']
                            event['info'] = d['info']
                            events.append(event)
                        elif symbol.find('icon_goal') >= 0:
                            event = DsMatchEvent()
                            event['match_id'] = match_id
                            event['home_away'] = 'a'
                            event['type'] = 'g'
                            event['team_name'] = team_name1
                            event['timestamp'] = d['x']
                            event['v'] = d['y']
                            event['info'] = d['info']
                            events.append(event)

                # jiaoqiu_list = DsMatchEventJiaoqiuList()
                # jiaoqiu_list['match_id'] = match_id
                # jiaoqiu_list['datas'] = jiaoqiu
                # yield jiaoqiu_list
                #
                # shezheng_list = DsMatchEventShezhengList()
                # shezheng_list['match_id'] = match_id
                # shezheng_list['datas'] = shezheng
                # yield shezheng_list
                #
                # jinqiu_list = DsMatchEventJinqiuList()
                # jinqiu_list['match_id'] = match_id
                # jinqiu_list['datas'] = jinqiu
                # yield jinqiu_list

                # 2. 射偏球门
                shepian_start = script_txt.find('draw_half_line( $(\'#shezheng\').highcharts() );')
                shepian_end = script_txt.find('$(\'#shepian\').css')
                shepian_txt = script_txt[shepian_start:shepian_end]
                shezheng_start = shepian_txt.find('shepian_chart_options.series =')
                shepian_txt = shepian_txt[shezheng_start:].replace('shepian_chart_options.series =', '').strip()
                shepian_txt = shepian_txt[:len(shepian_txt) - 1].replace('\'', '"')
                # print shepian_txt
                shepian_json = json.loads(shepian_txt)
                shepian_json0 = shepian_json[0]
                team_name0 = shepian_json0['name']
                team_data0 = shepian_json0['data']
                shepian = []
                for d in team_data0:
                    if d['marker'].has_key('radius'):
                        event = DsMatchEvent()
                        event['match_id'] = match_id
                        event['home_away'] = 'h'
                        event['type'] = 'f'
                        event['team_name'] = team_name0
                        event['timestamp'] = d['x']
                        event['v'] = d['y']
                        event['info'] = d['info']
                        events.append(event)

                shepian_json1 = shepian_json[1]
                team_name1 = shepian_json1['name']
                team_data1 = shepian_json1['data']
                for d in team_data1:
                    if d['marker'].has_key('radius'):
                        event = DsMatchEvent()
                        event['match_id'] = match_id
                        event['home_away'] = 'a'
                        event['type'] = 'f'
                        event['team_name'] = team_name1
                        event['timestamp'] = d['x']
                        event['v'] = d['y']
                        event['info'] = d['info']
                        events.append(event)

                # shepian_list = DsMatchEventShepianList()
                # shepian_list['match_id'] = match_id
                # shepian_list['datas'] = shepian
                # yield shepian_list

                # 3. 危险进攻
                danger_start = script_txt.find('draw_half_line( $(\'#shepian\').highcharts() );')
                danger_end = script_txt.find('$(\'#danger\').css')
                danger_txt = script_txt[danger_start:danger_end]
                danger_start = danger_txt.find('shepian_chart_options.series =')
                danger_txt = danger_txt[danger_start:].replace('shepian_chart_options.series =', '').strip()
                danger_txt = danger_txt[:len(danger_txt) - 1].replace('\'', '"')
                # print danger_txt
                danger_json = json.loads(danger_txt)
                danger_json0 = danger_json[0]
                team_name0 = danger_json0['name']
                team_data0 = danger_json0['data']
                weixian = []
                for d in team_data0:
                    if d['marker'].has_key('radius'):
                        event = DsMatchEvent()
                        event['match_id'] = match_id
                        event['home_away'] = 'h'
                        event['type'] = 'd'
                        event['team_name'] = team_name0
                        event['timestamp'] = d['x']
                        event['v'] = d['y']
                        event['info'] = d['info']
                        events.append(event)

                danger_json1 = danger_json[1]
                team_name1 = danger_json1['name']
                team_data1 = danger_json1['data']
                for d in team_data1:
                    if d['marker'].has_key('radius'):
                        event = DsMatchEvent()
                        event['match_id'] = match_id
                        event['home_away'] = 'a'
                        event['type'] = 'd'
                        event['team_name'] = team_name1
                        event['timestamp'] = d['x']
                        event['v'] = d['y']
                        event['info'] = d['info']
                        events.append(event)

                # weixian_list = DsMatchEventWeixianList()
                # weixian_list['match_id'] = match_id
                # weixian_list['datas'] = weixian
                # yield weixian_list

                # 4. 进攻
                jingong_start = script_txt.find('draw_half_line( $(\'#danger\').highcharts() );')
                jingong_end = script_txt.find('$(\'#attack\').css')
                jingong_txt = script_txt[jingong_start:jingong_end]
                jingong_start = jingong_txt.find('shepian_chart_options.series =')
                jingong_txt = jingong_txt[jingong_start:].replace('shepian_chart_options.series =', '').strip()
                jingong_txt = jingong_txt[:len(jingong_txt) - 1].replace('\'', '"')
                # print jingong_txt
                jingong_json = json.loads(jingong_txt)
                jingong_json0 = jingong_json[0]
                team_name0 = jingong_json0['name']
                team_data0 = jingong_json0['data']
                jingong = []
                for d in team_data0:
                    if d['marker'].has_key('radius'):
                        event = DsMatchEvent()
                        event['match_id'] = match_id
                        event['home_away'] = 'h'
                        event['type'] = 'a'
                        event['team_name'] = team_name0
                        event['timestamp'] = d['x']
                        event['v'] = d['y']
                        event['info'] = d['info']
                        events.append(event)

                jingong_json1 = jingong_json[1]
                team_name1 = jingong_json1['name']
                team_data1 = jingong_json1['data']
                for d in team_data1:
                    if d['marker'].has_key('radius'):
                        event = DsMatchEvent()
                        event['match_id'] = match_id
                        event['home_away'] = 'a'
                        event['type'] = 'a'
                        event['team_name'] = team_name1
                        event['timestamp'] = d['x']
                        event['v'] = d['y']
                        event['info'] = d['info']
                        events.append(event)
                        # jingong_list = DsMatchEventJingongList()
                        # jingong_list['match_id'] = match_id
                        # jingong_list['datas'] = jingong
                        # yield jingong_list

        if len(events) > 0:
            match_event_list = DsMatchEventList()
            match_event_list['match_id'] = match_id
            match_event_list['datas'] = events
            yield match_event_list

        race_events = response.xpath('//ul[@id="race_events"]/li')
        event_texts = []
        for li in race_events:
            text_content = li.xpath('./text()').extract()[1]
            text_content = text_content.replace('\n', '').replace('                                ',
                                                                  '') if text_content is not None else ''
            event_text = DsMatchEventText()
            event_text['match_id'] = match_id
            event_text['txt'] = text_content
            event_texts.append(event_text)
        if len(event_texts) > 0:
            event_text_list = DsMatchEventTextList()
            event_text_list['match_id'] = match_id
            event_text_list['datas'] = event_texts
            yield event_text_list
