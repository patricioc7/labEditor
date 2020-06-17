import pymongo
from bson.objectid import ObjectId
from pprint import pprint

newLab = "fb_leadads"

myclient = pymongo.MongoClient("DB SRV")
mydb = myclient["DATABASE NAME"]

websites = mydb["Website"]
companies = mydb["Company"]

ids = ["52d593d1e4b065ff0956935d",
       "52d978c2e4b00fc01a69db04", "5615227ce4b09dde941b4b01"]

for item in ids:
    website = websites.find_one({"_id": ObjectId(item)})
    companyId = website["companyId"]

    company = companies.find_one({"_id": ObjectId(companyId)})
    pprint("procesando:" + company["name"])

    query = {"_id": ObjectId(companyId)}

    if "labs" in company:
        if newLab not in company["labs"]:
            print("tiene labs")
            newvalues = {"$set": {"labs":  company["labs"] + "," + newLab}}
            companies.update_one(query, newvalues)
    else:
        print("no tiene labs")
        newvalues = {"$set": {"labs": newLab}}
        companies.update_one(query, newvalues)

    print(company["labs"])
    print("----------0----------")
