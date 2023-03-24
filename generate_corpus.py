# Copyright (c) 2023 roket1428
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import math

# 7500th words frequency
NUM = 7694814

def normalize(path):
	words = []
	nums = []
	with open(path, "r") as in_f:
		for i, line in enumerate(in_f):
			if i == 7500:
				break
			tmp = line.split('\t')
			words.append(tmp[0])
			nums.append(math.floor(int(tmp[1])/NUM))

	return (words, nums)

def generate(words, nums):
	word_list = []
	for i, v in enumerate(words):
		word_list.append(v*nums[i])

	return word_list

def write(word_list):
	out = ""
	for w in word_list:
		out = f"{out}{w}"

	with open("corpus.txt", "w", encoding='utf-8') as out_f:
		out_f.write(out)

words, nums = normalize("count_1w.txt")
write(generate(words, nums))
