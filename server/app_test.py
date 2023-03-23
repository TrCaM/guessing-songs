import unittest
import server.app as app

class TestApp(unittest.TestCase):
  def test_example(self):
    self.assertEqual(app.home(), app.WELCOME_HOME_TEXT)