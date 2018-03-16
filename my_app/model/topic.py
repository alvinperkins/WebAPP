import web
from config import settings
from data import topicData

class link:
    def __init__(this,url,title,text):
        this.url = url; this.title = title; this.text = text

class Content:
    "generate contents for rener"
            
    def __init__(this,o):
        this.captionUrl = o["captionU"]
        this.captionText = o["captionT"]
        
            
    def fill(this ,hls):
        this.headlines = [link(*h) for h in hls]
        

class Topic:
    def GET(this,top):
        web.header("Content-type","text/html")
        if "/" not in top:
            o = topicData.data[top]
        else:
            p,q = top.split("/")
            o = getattr(topicData,p)[q]
        content1 = Content(o); content1.fill(o["headlines"])

        return settings.render.topic(settings.render.newsCaptrue([content1]))   
    
    def get(this,*tops):
        res=[]
        for t in tops:
            o = topicData.data[t]
            content1 = Content(o); content1.fill(o["headlines"])
            res.append(content1)
        return res
    