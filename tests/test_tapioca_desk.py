# coding: utf-8

import unittest

from tapioca_desk import Desk


class TestTapiocaDesk(unittest.TestCase):

    def setUp(self):
        self.wrapper = Desk()


if __name__ == '__main__':
    unittest.main()
