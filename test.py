import unittest
from dgaintel import get_prediction

class TestPrediction(unittest.TestCase):

	def test_pred(self):
		pred = get_prediction('teststr')
		self.assertTrue(pred)

	def test_pred_true(self):
		pred = get_prediction('wikipedia.com')
		self.assertTrue(pred < 0.5)

	def test_pred_false(self):
		pred = get_prediction('spgjjbdvddxorx.com')
		self.assertTrue(pred > 0.5)

if __name__ == '__main__':
	unittest.main()