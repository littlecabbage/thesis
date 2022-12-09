import os, json
import jieba as jb
#topk个中文词
topK = 25


def check_contain_chinese(check_str):
	for ch in check_str:
		if u'\u4e00' <= ch <= u'\u9fff':
			return True
		return False
l = list(filter(lambda x: os.path.isdir(x), os.listdir('./')))
f = []
for dir in l:
	f += [os.path.join(dir,x) for x in os.listdir(dir)]
l = list(filter(lambda x: x.endswith('.tex'), f))
txt = ''
for file in l:
	if os.path.isdir(file):
		continue
	txt += open(file,'r', encoding='utf-8').read()
words = jb.lcut(txt)
dt = {}
for word in words:
	if len(word) == 1 or not check_contain_chinese(word):
		continue
	dt[word] = dt.get(word,0)+1
dl = [(x, dt[x]) for x in dt]
dl.sort(key=lambda x:x[1], reverse=True)

for i in range(topK):
	print(dl[i])
