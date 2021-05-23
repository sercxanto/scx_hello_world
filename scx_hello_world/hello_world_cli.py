#!/usr/bin/env python3
# vim: set fileencoding=utf-8 :
""" hello_world_cli.py

    command line interface"""

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


# Standard library imports:
import argparse
import logging

# Own imports:
from scx_hello_world import hello_world


def get_args():
    '''Configures command line parser and returns parsed parameters'''
    parser = argparse.ArgumentParser(
        description="Hello world dummy/template project")
    parser.add_argument(
        "-d", "--debug", dest="debuglevel", action="store_const",
        const=logging.DEBUG, default=logging.INFO,
        help="Enables verbose/debug output")
    return parser.parse_args()


def main():
    '''Main'''
    args = get_args()
    logging.basicConfig(format="%(message)s", level=args.debuglevel)
    logging.debug("Main called")
    hello_world.hello_world()


if __name__ == "__main__":
    main()
