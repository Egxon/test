def erase(cc):
    res = ""
    i = 0
    while i < len(cc):
        if cc[i] == " ":
            j = 1
            while i+j < len(cc) and cc[i+j] == " ":
                j += 1
            if j > 1:
                res += " "*(j)
                i += j-1
        else:
            res += cc[i]
        i += 1
    return res


import time

start_time = time.time()

with open('texteSAE.txt') as file:
    content = " ".join([c for c in file])


print("["+erase(content)+"]")




print("%s seconds" % (time.time() - start_time))