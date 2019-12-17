import unittest

from security.zap import Zap


class TestScan(unittest.TestCase):
    zap = Zap()
    zap.start_zap()
    zap.check_zap_connection()
    print("Zap initialized")

    @staticmethod
    def test_a():
        zap = Zap()
        zap.run_spider("https://the-internet.herokuapp.com/forgot_password")
        zap.stop_zap()


if __name__ == '__main__':
    unittest.main(warnings = 'ignore')
