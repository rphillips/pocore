#!/usr/bin/env python
#
# rat.py :  run Apache RAT over PoCore
#
# ====================================================================
#   Copyright 2010 Greg Stein
#
#   Licensed under the Apache License, Version 2.0 (the "License");
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.
# ====================================================================
#

import sys
import os

# USAGE: rat.py PATH/TO/RAT.JAR
ratjar = sys.argv[1]

thisdir = os.path.dirname(sys.argv[0])

args = [
  '-jar', ratjar,
  '-c', 'Copyright 2010 Greg Stein',
  '--dir', '.',
  ]

for line in open(os.path.join(thisdir, 'rat-excludes')).readlines():
  line = line.strip()
  if (not line) or line.startswith('#'):
    continue
  args.append('--exclude')
  args.append(line)

os.chdir(os.path.join(thisdir, '../..'))
os.execlp('java', 'java', *args)
# NOTREACHED
