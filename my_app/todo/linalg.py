import web
import numpy as np

class solver:
    def GET(this):
        web.header("Content-type","text/html")
        return '<body><form action="/linalg" method=post><textarea  name="look" id="look"></textarea><input type="submit">   <hr> </form></body>'
    def POST(this):
        web.header("Content-type","text/html")
        s=""
        s=web.input().get("look")
        try:
            y = calulate(s)
        except:
            y = "None"
        return '<body><form action="/linalg" method=post><textarea  name="look" id="look"></textarea><input type="submit">   <hr> </form></body>'+y

def calulate(s):
    ls = [[int(x) for x in i.split(" ")] for i in s.split("\n")]
    y = np.linalg.det(np.array(ls))
    return str(y)
    