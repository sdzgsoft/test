from gevent import monkey; monkey.patch_all()
import gevent
import urllib2
def f(url):
	print 'Get %s....'%url
	resp=urllib2.urlopen(url)
	data=resp.read()
	print ('%d bytes received from %s' %(len(data),url))
##添加注释
gevent.joinall([
	      gevent.spawn(f,'https://www.python.org/'),
	      gevent.spawn(f,'https://www.sina.com.cn/'),
	      gevent.spawn(f,'https://github.com/')])