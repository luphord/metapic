import unittest

from metapic import parser


class Testmetapic(unittest.TestCase):

    def test_argument_parsing(self):
        args = parser.parse_args([])
        self.assertEqual(args.version, False)
        args = parser.parse_args(['--version'])
        self.assertEqual(args.version, True)
