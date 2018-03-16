

import web
import web.webapi
import urllib.parse as parse


class api:

    #example: http://qemu/p/map/center=30.3,120.3
    my_key="AIzaSyAVGkcH1n7tBj9qnBlxnFSB0nhS07NXMO4"
    def GET(self, path):
        params = {"zoom":14,
                "size":"512x512",
                "key":api.my_key}
               # "center":"Berkeley,CA"}
        base = "https://maps.googleapis.com/maps/api/staticmap?"
        url = base + path + "&" + parse.urlencode(params) 
        tag = "<img src=%s></img>"% url

        web.webapi.header("Content-type","text/html")
        return tag

