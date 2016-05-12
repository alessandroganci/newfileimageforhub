import unittest
from unittest.mock import patch

import mockredis
import hitcount

@patch('hitcount.r',mockredis.mock_strict_redis_client(host='0.0.0.0',port=6379,db=0))
class HitCountTest(unittest.TestCase):
	def testOneHit(self):
		hitcount.hit("user1")
		self.assertEqual(b'1',hitcount.getHit("user1"))

if __name__ == '__main__':
	unittest.main()

