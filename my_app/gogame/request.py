import json
import requests






class GameSession:
    def __init__(self):
        self.data =  {"gameid":20,"moves":[],"color":1}



class Proxy:

    sess = GameSession()
    def GET(self,path):

        ds = json.dumps(Proxy.sess.data)
        response = requests.post('http://127.0.0.1/p/ai/go/19',data={'json':ds})
        Proxy.sess.data['moves'].append  ( json.loads(response.text)['pt'])
        response.close()
        return response.text


#p = Proxy()

#print p.GET(0)

#Proxy.sess.data['moves']=[json.loads(p.GET(0))['pt']]




#print p.GET(0)

#Proxy.sess.data['moves']=[json.loads(p.GET(0))['pt']]
#print Proxy.sess.data['moves']



