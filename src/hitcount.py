import redis
r =redis.StrictRedis(host='0.0.0.0',port=6379,db=0)

def hit(usr):
	r.incr(usr)

def getHit(usr):
	return(r.get(usr))
