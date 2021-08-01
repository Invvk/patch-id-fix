# Auto Patch id by Invvk (https://github.com/Invvk)
#
# BSD 3-Clause License
#
# Copyright (c) 2021, Invvk
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
#
# 1. Redistributions of source code must retain the above copyright notice, this
#   list of conditions and the following disclaimer.
#
# 2. Redistributions in binary form must reproduce the above copyright notice,
#   this list of conditions and the following disclaimer in the documentation
#   and/or other materials provided with the distribution.
#
# 3. Neither the name of the copyright holder nor the names of its
#   contributors may be used to endorse or promote products derived from
#   this software without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
# DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE
# FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
# DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
# SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
# CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY,
# OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
# OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

# Python version 3.8.5

import os

basedir = input('current base directory that contains the patch files: ')
try:
    print('biggest patch id (example: 0100-X.patch which means 100 is the biggest or current number):')
    currentPoint = int(input('if you want to reset, type 1: '))
except ValueError:
    print('Error: patch id can\'t be float (example 1.1 is not acceptable), only integers.')
    quit()

if (currentPoint < 1):
    print('Error: patch id can\'t be less than 1')
    quit()

def format_id(startingPoint):
    if startingPoint > 999:
        return str(startingPoint)
    elif startingPoint > 99:
        return "0" + str(startingPoint)
    elif startingPoint > 9:
        return "00" + str(startingPoint)
    return "000" + str(startingPoint)


for file in os.listdir(basedir):
    if file.endswith('.patch') and file.startswith('0') and file.__contains__('-'):
        newName = format_id(currentPoint) + file.replace(file.split('-')[0], '')
        os.rename(f"{basedir}/{file}", f'{basedir}/{newName}')
        print(f'renamed {file} to {newName}')
        currentPoint += 1
