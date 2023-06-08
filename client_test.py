import unittest
from client3 import getDataPoint, getRatio

class ClientTest(unittest.TestCase):
  def test_getDataPoint_calculatePrice(self):
    quotes = [
      {'top_ask': {'price': 121.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]
    """ ------------ Add the assertion below ------------ """
    result0 = getDataPoint(quotes[0])
    result1 = getDataPoint(quotes[1])
    self.assertEqual(("ABC", 120.48, 121.2, 120.84), result0)
    self.assertEqual(("DEF", 117.87, 121.68, 119.775), result1)

  def test_getDataPoint_calculatePriceBidGreaterThanAsk(self):
    quotes = [
      {'top_ask': {'price': 119.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]
    result0 = getDataPoint(quotes[0])
    result1 = getDataPoint(quotes[1])
    self.assertEqual(("ABC", 120.48, 119.2, 119.84), result0)
    self.assertEqual(("DEF", 117.87, 121.68, 119.775), result1)


  """ ------------ Add more unit tests ------------ """
  def test_getRatio_zero(self):
    result = getRatio(15, 0)
    self.assertEqual(result, None)

  def test_getRatio_classic(self):
    result = getRatio(15, 2)
    self.assertEqual(result, 7.5)


if __name__ == '__main__':
    unittest.main()
