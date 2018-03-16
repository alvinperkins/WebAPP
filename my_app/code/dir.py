from config.settings import render

from data import sparkdir,scaladir
import code
import random
import web

import time,os


class random_walk():




    r = random.Random()

    def GET(this):
        #a,b,c
        direc = sparkdir.deps + sparkdir.res
        #direc = sparkdir.scala+sparkdir.breeze
        #direc = sparkdir.net_work + sparkdir.res
        #direc = sparkdir.coreplus  #2016/3/24
        #direc = sparkdir.cat_sch + sparkdir.spark_str[21:47] #2016/4/5
        #direc = sparkdir.core[171:223]+sparkdir.spark_str[21:47]+sparkdir.core[281:353]#2016/4/8
        #direc = sparkdir.spark_sql[:21]+sparkdir.spark_sql[135:235]+sparkdir.spark_str[21:47]+sparkdir.net_work#2016/5/6
       # direc = sparkdir.deps[220:300]+scaladir.all[534:600]+sparkdir.appendix
        direc = sparkdir.core#2017/10/10

        #session based on time , used if no store available
        class Session:
            def __init__(this):
                this.cursor = int(time.time())/15

       
        session = web.webapi.config._session
        


        if 'cursor' not in session.__dict__:
                session.cursor = random_walk.r.randint(1,400)
        length = len(direc)
        session.cursor = (session.cursor+random_walk.r.randint(1,6))%length
        path = direc[session.cursor]
        
    
        raise web.webapi.seeother('/o/code/spark2/core/scala/spark/'+path[1:])

class search:

    def GET(self):
        web.webapi.header("Content-type","text/html")   
        kw = web.webapi.input().get('kw',"")
        result = [t for t in sparkdir.revert if kw in t[0]]
        return "<br>\n".join([self.tagMaker(t) for t in result])

    def tagMaker(self, t):
        return "<a href=/o/code/spark2/core/scala/%s>%s</a>" %(t[-1],t[0])











Bdir  = ['accessibility', 'android', 'app_mode', 'autocomplete', 'autofill', 'automation', 'background', 'bookmarks', 'browsing_data', 
         'captive_portal', 'chromeos', 'common', 'component_updater', 'content_settings', 'custom_handlers', 'devtools', 'diagnostics', 
         'download', 'extensions', 'external_protocol', 'favicon', 'feedback', 'first_run', 'geolocation', 'google', 'google_apis', 'gpu', 
         'hang_monitor', 'history', 'importer', 'infobars', 'lifetime', 'mac', 'managed_mode', 'media', 'media_galleries', 'metrics', 'metro_viewer',
         'nacl_host', 'net', 'notifications', 'omnibox', 'page_cycler', 'parsers', 'password_manager', 'performance_monitor', 'plugins', 'policy',
         'predictors', 'prefs', 'prerender', 'printing', 'profiles', 'profile_resetter', 'renderer_host', 'rlz', 'safe_browsing', 'search', 
         'search_engines', 'service', 'sessions', 'signin', 'speech', 'spellchecker', 'ssl', 'status_icons', 'storage_monitor', 'sync',
         'sync_file_system', 'tab_contents', 'task_manager', 
         'task_profiler', 'themes', 'thumbnails', 'translate', 'ui', 'usb', 'value_store', 'webdata', 'web_applications', 'web_resource']

class cppeditor:


    """  code pad similar to todo.code, some chromium cpp code"""
    def GET(this,path):
        if 0:
            choice = [d for d in Bdir if d[0] == path[0]]
            base = "./static/browser/"+choice[random_walk.r.randint(0,len(choice))]+"/"
            Lcc = os.listdir(base)
            #external call
            x=base+Lcc[random_walk.r.randint(0,100)%len(Lcc)]

            return code.cppeditor.GET(x)
        else:
            try:
                return code.cppeditor.GET("./static/browser/"+path)
            except:
                
                try:
                    l = os.listdir("./static/browser/"+path)
                    l = ["/browser/"+path+"/"+i for i in l]
                    l = [(i,i) for i in  l]
                    return settings.render.listdir(l)
                except:
                    try:
                        l = os.listdir("./static/sparkx/"+path)
                        l = [("/code/sparkx/"+path+"/"+i,path+"/"+i) for i in l]
                        return settings.render.listdir(l)
                    except:
                        flist = os.listdir("./static/"+path)
                        #return l[0]
                        l = [("/browser/"+path+"/"+i,path+"/"+i) for i in flist if '.' not in i]
                        l .extend([("\"/static/"+path+"/"+i+'"',path+"/"+i) for i in flist if '.'  in i])
                        return settings.render.listdir(l)
                
           












#-------------------------------------   sina   cloud  storage   -------------------------------------------------------------------
from third_party.sinastorage.bucket import SCSBucket
from third_party import sinastorage


sinastorage.setDefaultAppInfo("2kosi4vjeUQKyAwe5ODh","e3ecee8b1a204b6c96d39dbb3fa63250e5dbaff5")


def  fromSCS():
    s = SCSBucket()
    response = s['tong001/img/6631207403678731577.jpg']
    return response.read()

    CHUNK = 16 * 1024
    s = []
    while True:
        chunk = response.read(CHUNK)
        if not chunk: break
        s.append(chunk)
    return s

class IMG:
    
#    img = fromSCS()
    def GET(this):
        web.webapi.header("Content-type",'image/jpg')
 #       return this.img
