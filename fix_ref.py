import os 

strs = ""
with open("./reference.bib","r") as fr:
    line = fr.readline()
    while line:
        line = str(line)
        print(line)

        if "=" in line and "title" in line:
            title = line.split("=")[-1]
            title = title[:-1]
            title = "{" + title + "}"
            strs = " title = " + title + ",\n"
        strs += line
        line = fr.readline()

with open("./reference","w") as fw:
    fw.write(strs)

            
