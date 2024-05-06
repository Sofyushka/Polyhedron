import math
import unittest
from unittest.mock import patch, mock_open

from shadow.polyedr import Polyedr


class TestPolyedr(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        fake_file_content = """200.0	45.0	45.0	30.0
8	4	16
-0.5	-0.5	0.5
-0.5	0.5	0.5
0.5	0.5	0.5
0.5	-0.5	0.5
-0.5	-0.5	-0.5
-0.5	0.5	-0.5
0.5	0.5	-0.5
0.5	-0.5	-0.5
4	5    6    2    1
4	3    2    6    7
4	3    7    8    4
4	1    4    8    5"""
        fake_file_path = 'data/holey_box.geom'
        with patch('shadow.polyedr.open'.format(__name__),
                   new=mock_open(read_data=fake_file_content)) as _file:
            self.polyedr = Polyedr(fake_file_path)
            _file.assert_called_once_with(fake_file_path)

    def test_num_vertexes(self):
        self.assertEqual(len(self.polyedr.vertexes), 8)

    def test_num_facets(self):
        self.assertEqual(len(self.polyedr.facets), 4)

    def test_num_edges(self):
        self.assertEqual(len(self.polyedr.edges), 16)


class TestSonya1(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        fake_file_content = """20  0   0   90
6   5   9
2 -2 2
2 -2 -2
-2 -2 2
-2 -2 -2
2 2 2
-2 2 2
3   1   2   5
3   3   4   6
4   1   2   4   3
4   1   3   6   5
4   5   2   4   6"""
        fake_file_path = 'data/soney_box.geom'
        with patch('shadow.polyedr.open'.format(__name__),
                   new=mock_open(read_data=fake_file_content)) as _file:
            self.polyedr = Polyedr(fake_file_path)
            _file.assert_called_once_with(fake_file_path)

    def test_area(self):
        self.assertAlmostEqual(
            40 + 16 * math.sqrt(2),
            self.polyedr.area
        )


class TestSonya2(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        fake_file_content = """69  0 0 180
5   5   8
2 0 -2
-2 0 -2
-2 0 2
2 0 2
2 4 -2
4 1 2 3 4
3 1 2 5
3 2 3 5
3 3 4 5
3 4 1 5"""
        fake_file_path = 'data/soney_box.geom'
        with patch('shadow.polyedr.open'.format(__name__),
                   new=mock_open(read_data=fake_file_content)) as _file:
            self.polyedr = Polyedr(fake_file_path)
            _file.assert_called_once_with(fake_file_path)

    def test_area(self):
        self.assertAlmostEqual(
            32 + 16 * math.sqrt(2),
            self.polyedr.area
        )
