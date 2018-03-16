
import web.db
import web.template
import web.utils


#import sae.const

#----------------------------------------------------------
def linkdb(dbname):
    return  web.db.database(dbn = 'mysql',
            user= "root",                   
            pw= "hello",                   
            host="localhost",
            port= 3307,
            db= dbname)
SessionDB = linkdb("session")
ContentDB = linkdb("content")

















#-------------------------------------------------------
render = web.template.render('view',cache = False)

config = web.utils.storage(email = 'user@example.com',
                     name = 'todolist')

web.template.Template.globals['render']= render
web.template.Template.globals['config']= config
