
import web.webapi
from config import settings
from datetime import datetime

from model.topic import Topic 
db = settings.SessionDB
hdfs = db
views = settings.render


# hdfs as a store of product 2017/3/29
# produce plan  of axis


#XXX HISTORY
#2016/4/14 
#
#2016/4/16
# removed class link: Content: to topic module

def get_by_id(id):

    s = hdfs.select(tb,
                  where='id=$id',
                  vars = globals())
    if not s:
        return False
    return s[0]


class Index():
    def GET(this):
        web.webapi.header("Content-type","text/html")
        axice = hdfs.select(tb,
                          order = 'inbase_time asc ')
        
        return jsf.listaxis(axice)


class New():
    def POST(this):
        
        #URL query parameters (which appears after the ?) can be obtained using web.input()
        i = web.webapi.input()
        Title = i.get ('title',None)
        if not Title:
            return render.error('title expected')
        #hdfs.insert(tb,title,posttime = datetime.now())
        hdfs.insert(tb,title=Title,id=0)
        raise web.webapi.seeother('/todo')





#--------------------------------------------------------------------------------


class welcome:

    def GET(self):
        web.webapi.header("Content-type","text/html")
        newsbox = views.newsCaptrue( Topic().get("welcome"))
        return views.welcome(self.getquote(), newsbox).__str__()

    def getquote(self):
        db = settings.ContentDB
        import time
        result = db.select("quote",where="yday = %s" % time.gmtime().tm_yday)[0].sentence
        result.replace("\n", "<br>\n")
        return result


class Me:
    def GET(this):
        web.webapi.header("Content-type","text/html")

        return views.me()
 

class default:
    # static file app

    def GET(this,filename):
        if  this.check_path(filename, "seecode"):
            web.webapi.seeother('/v2/code/'+filename)
        else:
            with open('/var/www/html/'+filename) as F:
                return F.read()

    
    def check_path(this,filename, option):
        if option == "seecode":
            return filename.find("Context") > 0
        else :
            return False

