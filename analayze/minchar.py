import json
f = open('./C#-tgt-train.json')
# data=json.load(f)

import jsonlines

# start=1
# end=100
# now=start
# for line in f.readlines():
#     # print(line)
#     i=json.loads(line)
#     title=i['title']
#     title1=title.replace(" ","").strip()
#     topone=i['top_three_simple'][0]['title']
#     topone1=topone.replace(" ","").strip().lower()
#     if title==topone:
#         print('ok')
#     else:
#         print("___________________________")
#         print(title)
#         print(topone)
#         print("-----------------------------")
#     now+=1
#     if now==end:
#         break


# 有相同的标题的为止
ok=0
for line in f.readlines():
    # print(line)
    i=json.loads(line)
    title=i['title']
    title1=title.replace(" ","").strip()
    topone=i['top_three_simple'][0]['title']
    topone1=topone.replace(" ","").strip().lower()
    if title==topone:
        print('ok')
        ok=1
    else:
        print("___________________________")
        print(title)
        print(topone)
        print("-----------------------------")
    if ok==1:
        print("__________ok_________________")
        print(title)
        print(topone)
        print("------------ok-----------------")
        break