#!/usr/bin/env python3
# vim: set fileencoding=utf-8 :
''' Unittests for hello_world '''

# The MIT License (MIT)
#
# Copyright (c) 2021 Georg Lutz
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.


# Standard library imports
import unittest
import io
import sys

from scx_hello_world import hello_world

class TestHelloWorld(unittest.TestCase):
    def test_hello_world(self):
        out = io.StringIO()
        captured_output = io.StringIO()
        sys.stdout = captured_output
        hello_world.hello_world()
        sys.stdout = sys.__stdout__
        captured_output.seek(0)
        # Check that at least something is output
        self.assertGreaterEqual(len(captured_output.getvalue().strip()), 100)

if __name__ == "__main__":
    unittest.main()