
import sys
sys.path.append('../')

import unittest

from pymobi import util


class UtilTestCase(unittest.TestCase):
    def doVarint(self, fint):
        print('origin: 0x%x' % fint)
        vint = util.encodeVarint(fint)
        print('varint: 0x%x' % vint)
        ffint = util.decodeVarint(vint)
        print('fint: 0x%x' % ffint)
        self.assertEqual(ffint, fint)

    def testSomeValue(self):
        self.doVarint(0x11111)
        print('-' * 79)
        self.doVarint(0x2000)
        print('-' * 79)
        self.doVarint(0x4000)


def suite():
    return unittest.makeSuite(UtilTestCase, 'test')


if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    runner.run(suite())
