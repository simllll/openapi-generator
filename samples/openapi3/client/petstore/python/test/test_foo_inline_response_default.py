"""
    OpenAPI Petstore

    This spec is mainly for testing Petstore server and contains fake endpoints, models. Please do not use this for any other purpose. Special characters: \" \\  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import petstore_api
from petstore_api.model.foo import Foo
globals()['Foo'] = Foo
from petstore_api.model.foo_inline_response_default import FooInlineResponseDefault


class TestFooInlineResponseDefault(unittest.TestCase):
    """FooInlineResponseDefault unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testFooInlineResponseDefault(self):
        """Test FooInlineResponseDefault"""
        # FIXME: construct object with mandatory attributes with example values
        # model = FooInlineResponseDefault()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
