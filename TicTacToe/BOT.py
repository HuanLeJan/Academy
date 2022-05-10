import unittest
import Kolko_krzyzyk_JN as Kn
import random
from unittest import mock

rand_val = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,1,5,36,7,74,3]
random.shuffle(rand_val)
rand_player = [random.choice(['x','o'])]
val = rand_player + rand_val
print(val)

class TestGame(unittest.TestCase):
    @mock.patch('builtins.input', side_effect=val)
    def test1(self,input):
        Kn.main()


