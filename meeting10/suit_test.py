import unittest
import HtmlTestRunner

from homework9 import Test
from meeting9.new_test import Test2


class TestSuite(unittest.TestCase):

    def test_suite(self):
        smoke_test = unittest.TestSuite()
        smoke_test.addTests([
            unittest.defaultTestLoader.loadTestsFromTestCase(Test),
            unittest.defaultTestLoader.loadTestsFromTestCase(Test2),
        ])
# object html type
        runner = HtmlTestRunner.HTMLTestRunner(
            combine_reports=True,
            report_title='Test',
            report_name='Smoke Test Result'
        )

        runner.run(smoke_test)
