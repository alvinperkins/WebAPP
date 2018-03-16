import web
import web.webapi
import web.session
import web.application


import sys, os
os.chdir("/home/app/v2/2")


#import pandas

from config.url import urls
from config import settings
web.webapi.config.debug=False



class hello:
    def GET(self, name):
        if not name:
            name = 'World'
        return 'Hello, ' + name + '!'



app = web.application.application(urls, globals(),autoreload=False)
application = app.wsgifunc()


#--------------------------------------------------------------
#web.session.__dict__['pv'] = pandas.DataFrame()

store = web.session.DBStore(settings.SessionDB, 'sessions')
web.webapi.config._session = web.session.Session(app, store, initializer={'access_token': 'true'})




