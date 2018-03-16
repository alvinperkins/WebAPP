import web

def myloadhook():
    global session
    session = web.config._session

class count:
    def GET(self):

        session = web.config._session
        if 'count0' not in session:
                session.count0 = 0
        session.count0 += 1
        return str(session.cursor)

class reset:
    def GET(self):
        session = web.config._session
        session.kill()
        return ""