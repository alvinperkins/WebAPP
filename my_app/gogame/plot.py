
import web
import web.webapi
import cStringIO
import re

import matplotlib as mp
mp.use("Agg")
import matplotlib.pyplot as plt

def gen_image(plt, gameid, step_num):
    # create a 8" x 8" board
	fig = plt.figure(figsize=[8,8])
	fig.patch.set_facecolor((1,1,.8))

	ax = fig.add_subplot(111)

	# draw the grid
	for x in range(19):
	    ax.plot([x, x], [0,18], 'k')
	for y in range(19):
	    ax.plot([0, 18], [y,y], 'k')

	# scale the axis area to fill the whole figure
	ax.set_position([0,0,1,1])

	# get rid of axes and everything (the figure background will show through)
	ax.set_axis_off()

	# scale the plot area conveniently (the board is in 0,0..18,18)
	ax.set_xlim(-1,19)
	ax.set_ylim(-1,19)


	with open("/var/www/html/static/sgf/%s.sgf"%gameid) as f:
	    ss = f.read()

	moves = re.findall("[W|B]\[..\]",ss)[:step_num]
	Bmoves= [(ord(i[2])-ord('a'),ord(i[3])-ord('a')) for  i in moves if i[0] == 'B']
	Wmoves= [(ord(i[2])-ord('a'),ord(i[3])-ord('a')) for  i in moves if i[0] == 'W']

	for x,y in Wmoves:
	    ax.plot(x,y,'o',markersize=25, markeredgecolor=(0,0,0), markerfacecolor='w', markeredgewidth=2)
	for  x,y in Bmoves:
	    ax.plot(x,y,'o',markersize=25, markeredgecolor=(.5,.5,.5), markerfacecolor='k', markeredgewidth=2)

	output = cStringIO.StringIO()
	fig.savefig(output)
	fig.savefig('test.png')

class main:
    def GET(self, path):
#        web.header("Content-Type", "images/png")
        r = web.webapi.input()
        gen_image(plt,r.gameid,int(r.step))
        return open("test.png",'rb').read()
