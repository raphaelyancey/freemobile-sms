#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright (c) 2017 Raphael Yancey <raphael@badfile.net>

# Permission is hereby granted, free of charge, to any person obtaining a
# copy of this software and associated documentation files (the "Software"),
# to deal in the Software without restriction, including without limitation
# the rights to use, copy, modify, merge, publish, distribute, sublicense,
# and/or sell copies of the Software, and to permit persons to whom the
# Software is furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
# FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
# DEALINGS IN THE SOFTWARE.

#
# This program use the Free Mobile API to send a SMS.
# It is not affiliated with Free or Free Mobile.
#
# To the non-french curious : Free Mobile is a french GSM operator that developed an API to send a SMS to yourself.
# <https://mobile.free.fr>
#

from __future__ import (absolute_import, division,
                        print_function, unicode_literals)
from builtins import *

from sys import argv, exit
import argparse
import http.client

parser = argparse.ArgumentParser(description='Send a SMS with the Free Mobile SMS API.')

required = parser.add_argument_group('required arguments')
required.add_argument('-u', '--user', nargs=1, required=True, help="The Free Mobile user ID (as used to log on the website)", metavar="user ID")
required.add_argument('-k', '--key', nargs=1, required=True, help="The Free Mobile API key", metavar="API key")
required.add_argument('-m', '--message', nargs=1, required=True, help="The message to send as a SMS", metavar="message")

args = vars(parser.parse_args())

conn = http.client.HTTPSConnection("smsapi.free-mobile.fr")
url = "/sendmsg?user=" + args['user'][0] + "&pass=" + args['key'][0] + "&msg=" + args['message'][0]
conn.request("GET", url)
res = conn.getresponse()

if res.status == 200:
    print("SMS has been sent.")
    exit(0)
elif res.status == 400:
    print("Error: Missing parameter.")
    exit(1)
elif res.status == 402:
    print("Error: Throttling.")
    exit(1)
elif res.status == 403:
    print("Error: Wrong credentials or service not enabled by the user.")
    exit(1)
elif res.status == 500:
    print("Error: Internal server error, try again later.")
    exit(1)
else:
    print("Error: Unknown error.")
    exit(1)