import bibtexparser

with open('./backup/reference.bib', encoding = 'utf-8') as bibtex_file:
    bib_database = bibtexparser.load(bibtex_file)
jieci = ["is", "for", "and", "using", "at", "with", "from", "in", "on", "based", "of","by", "the"]

def tran(title):
    warr = title.split()
    res = []
    for w in warr:
        if w not in jieci:
            w = w[0].title() +w[1:]
        res += [w]
    return " ".join(res)
def tranbt(title):
    warr = title.split()
    res = []
    for w in warr:
        if w not in jieci:
            w = w[0].title() +w[1:]
        res += [w]
    return " ".join(res)
def trana(author):
    warr = author.split()
    res = []
    for w in warr:
        i = -1
        target = 'a'
        idx = 0
        while idx < (len(w)):
            if w[idx] == '\'':
                i, target = idx+1, w[idx + 1]
                break
            idx += 1
        while idx < (len(w)):
            if w[idx] >= 'a' and w[idx] <= 'z':
                i, target = idx, w[idx]
                break
            idx += 1			
        if w not in jieci:
            w = w.upper()
        if i > 0:
            w = w[:i] + str(target) + w[i+1:]
        res += [w]
    return " ".join(res)
def check_contain_chinese(check_str):
	for ch in check_str:
		if u'\u4e00' <= ch <= u'\u9fff':
			return True
	return False
for i in range(len(bib_database.entries)):
    bib_database.entries[i]["title"] = tran(bib_database.entries[i]["title"])
    if "booktitle" in bib_database.entries[i]:
        bib_database.entries[i]["booktitle"] = tran(bib_database.entries[i]["booktitle"])
    if "journal" in bib_database.entries[i]:
        bib_database.entries[i]["journal"] = tran(bib_database.entries[i]["journal"])
    bib_database.entries[i]["author"] = trana(bib_database.entries[i]["author"])
    if "pages" not in bib_database.entries[i]:
        bib_database.entries[i]["pages"] = "1--12"
    if check_contain_chinese(bib_database.entries[i]["title"]):
	    bib_database.entries[i]["language"] = "zh"

with open('reference.bib', 'w', encoding = 'utf-8') as bibtex_file:
    bibtexparser.dump(bib_database, bibtex_file)