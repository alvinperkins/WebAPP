import web 
import os

class do:
    def GET(this):
        def a():
            ans = []
            for x,y,z in os.walk("./static/sparkx"):
                for i in z:
                    if i.endswith(".jpg") or i.endswith(".JPG"):
                        ans .append( os.path.join(x,i))
            return ans
        def b():
            ans = []
            for x,y,z in os.walk("./static/sparkx"):
                for i in z:
                    if 'sparkx/scala' in x:
                        ans .append( os.path.join(x,i))
            return ",\n".join(["'"+str(i)+"'" for i in ans])
                    

        def b():
            ans = []
            for x,y,z in os.walk("./static/sparkx"):
                for i in z:
                    if 'cata' in x or 'execution' in x:
                        ans .append('.'+os.path.join(x,i)[15:])
          
            return ",\n".join(["'"+str(i)+"'" for i in ans])
                    
        return str(b())