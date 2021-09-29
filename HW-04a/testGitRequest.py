# -*- coding: utf-8 -*-
"""
Created on Tue Sep 28 19:10:31 2021

@author: nicholas mirarchi
"""

import unittest

from gitRequest import repository_info

# This code implements the unit test functionality
# https://docs.python.org/3/library/unittest.html has a nice description of the framework

class testGit(unittest.TestCase):
    def test_repository_info(self):
        self.assertEqual(repository_info('nmirarchi12'), True)
        self.assertEqual(repository_info('john567'), True)
    def test_repository_info2(self):
        self.assertEqual(repository_info('!'), False, "Error... Account not found of no repos exist")
       
if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()