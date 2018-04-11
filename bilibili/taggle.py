# -*- coding: utf-8 -*-
"""
@author: xulei
"""


from workflow import Workflow,web
import json
ICON_DEFAULT = 'icon.png'
import sys
reload(sys)
sys.setdefaultencoding('utf8')





def today():
    url = 'https://www.bilibili.com/index/rank/origin-3-0.json'
    r = web.get(url)
    r.raise_for_status()
    data = r.json()

    print(data)

    return data




def func(wf):

    news = wf.cached_data('today',today,max_age = 60)
    # print news
    for new in news['rank']['list']:
        subTitle = str('作者:%s,点击量:%s,评论数:%s'%(new['author'],new['play'],new['video_review']))
        video_url = str('https://www.bilibili.com/video/av%s'%new['aid'])
        wf.add_item(title=new['title'],
                    subtitle=subTitle,
                    arg=video_url,
                    valid=True,
                    icon=ICON_DEFAULT)
    wf.send_feedback()

if __name__ == '__main__':
    wf = Workflow()
    logger = wf.logger
    sys.exit(wf.run(func))
