dic = {

    "Name":"Saima", "Age":15, "canVote":False
}
print (dic)
dic.update({"Age":20})
dicT = {"DOB":2004}
dic.update(dicT)
dic.pop("canVote")
dic.popitem()
del dic["Age"]
dic.clear()
# del dic
print (dic)
