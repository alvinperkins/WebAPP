
import web
import web.webapi
import re
import os

from config.settings import SessionDB, render

base_path = "/var/www/html/source/"


#----------- part----------------------
class CodePad:
    """editable code pad with syntax highlight
    List a directory if path refer to a directory.
    A search box in which you can search classname (analysis code first)"""

    def breadc(this,path):
        a=""
        b,c = "/o/code",""
        for t in path:
            b=b+"/"+t
            c="/"+t
            a+="<a href=%s> %s</a>"%(b,c)
        return a
    def listdir(this, path):
        p = base_path + path
        
        a =        [f for f in   os.listdir(p) if os.path.isdir(p+"/"+f)]
        b = [f for f in   os.listdir(p) if not os.path.isdir(p+"/"+f)]
        uList = [path+"/"+i for i in a] +[path+"/"+i for i in b] 
        uList = ["<a href=%s>%s</a>"%("/o/code/"+i,i) for i in uList]
        return "<br>".join(uList)
            
    def GET(this,path):


        session = web.webapi.config._session
        SessionDB.insert('visit', link = path, session_id = session.session_id )
        if path.startswith("index"):
            pass
        web.webapi.header("Content-type","text/html")
        arg = web.webapi.input()
        if not arg:
            try:
                with open(base_path +path) as f:
                    text = f.read()
            except:
                    return this.listdir(path) 
        else:
            i,j = int(arg["i"]),int(arg.j)
            k=0; lines = []
            with open(base_path +path) as f:
                for line in f:
                    k+=1
                    if k >=i and k <=j:
                      lines.append(line)
                    if k>j:
                        break

            text = "".join(lines)
        return  render.codemirror(path, this.breadc(path.split("/")), text)


