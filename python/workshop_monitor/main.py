from notmain import *

key = 'STEAMAPI_KEY_HERE'
appid = 'DESIRED_APPID'
pubid = 'WORKSHOP_ITEM_ID'

params = {
    'key': key,
    'publishedfileids[0]':pubid,
    'includetags': 1,
    'includeadditionalpreviews':0,
    'includechildren':0,
    'includekvtags':1,
    'includevotes':1,
    'short_description':0,
    'includeforsaledata':1,
    'includemetadata':1,
    'return_playtime_stats':0,
    'appid':appid,
    'strip_description_bbcode':1,
    'includereactions':1,
}

url = 'https://api.steampowered.com/IPublishedFileService/GetDetails/v1/'


data = request_data(url= url, params= params)


curr = getcurrent(data)
last = loaddata()

printdata(curr, last)
printrates(curr, last)

savedata(curr)