import web




class TestNode():


    def init(self):
        from pyspark import SparkConf, SparkContext
        conf = SparkConf()
        conf.setMaster("local")
        conf.setAppName("pyspark")
        web.sc = sc = SparkContext(conf = conf)

    def GET(self, path):
        if path == 'close':
            web.sc.stop()
            web.sc = None
            return 'Interpreter closed. Bye '
        if not web.sc:
            self.init()
            return self.example(web.sc)

    def example(self,sc):
        lines = sc.textFile("/var/log/uwsgi.log")
        return str(lines.count())

class TraitLink:

    def GET(self):
        return ''

class MatchSet:

    def GET(self):
        return ''

class NPProcess:

    def GET(self):
        return ''
