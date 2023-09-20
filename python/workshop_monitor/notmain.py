from requests import get
import pickle
from time import time
from datetime import datetime
from os import listdir, getcwd, path

def request_data(url:str, params:dict):
    r = get(url= url, params= params)

    data = r.json()['response']['publishedfiledetails'][0]

    if (data['result'] != 1):
        print(data['result'])
        print(data['message'])
    else:
        return data

def getcurrent(data):
    #print([key for key in data])
    cur = {}
    cur['subs'] = data['subscriptions']
    cur['favs'] = data['favorited']
    cur['views'] = data['views']

    cur['lt_subs'] = data['lifetime_subscriptions'] #lifetime subs
    cur['lt_favs'] = data['lifetime_favorited']

    cur['vote_data'] = data['vote_data']
    cur['comments'] = data['num_comments_public']
    cur['reports'] = data['num_reports']

    cur['time_created'] = data['time_created']
    cur['time_updated'] = data['time_updated']

    cur['time'] = round(time())

    return cur

def printkv(data):
    for key in data:
        if (key == 'file_description' or key == 'reactions' or key == 'tags'): continue
        print(key, data[key])



def printdata(new, old):
    dtime = new['time'] - old['time']
    print()
    print(f"from {datetime.fromtimestamp(old['time'])}")
    print(f"to {datetime.fromtimestamp(new['time'])}")
    print(f"{dtime/60:.1f} minutes later")
    print()
    print(f"Unique  Visitors:    {new['views']}\t({(new['views'] - old['views']):+})")
    print(f"Current Subscribers: {new['subs']}\t({(new['subs'] - old['subs']):+})")
    print(f"Current Favorites:   {new['favs']}\t({(new['favs'] - old['favs']):+})")
    print()
    print(f"All Time Subs:  {new['lt_subs']}\t({(new['lt_subs'] - old['lt_subs']):+})")
    print(f"All Time Faves: {new['lt_favs']}\t({(new['lt_favs'] - old['lt_favs']):+})")
    print()
    print('\tVotes:')
    print(f"Up:    {new['vote_data']['votes_up']}\t({(new['vote_data']['votes_up'] - old['vote_data']['votes_up']):+})")
    print(f"Down:  {new['vote_data']['votes_down']}\t({(new['vote_data']['votes_down'] - old['vote_data']['votes_down']):+})")
    print(f"  % {round(100 * new['vote_data']['score'])}")
    print()
    print(f"Comments: {new['comments']}\t({(new['comments'] - old['comments']):+})")
    print(f"Reports: {new['reports']}\t({(new['reports'] - old['reports']):+})")
    print()

def printrates(new, old):
    dtime = new['time'] - old['time']
    dtime /= 60 # turn it into minutes. 3600 for hours
    delta = {}
    delta['time'] = new['time'] - old['time']
    delta['views'] = new['views'] - old['views']
    delta['subs'] = new['subs'] - old['subs']
    delta['favs'] = new['favs'] - old['favs']
    delta['lt_subs'] = new['lt_subs'] - old['lt_subs']
    delta['lt_favs'] = new['lt_favs'] - old['lt_favs']
    delta['comments'] = new['comments'] - old['comments']
    delta['votes_up'] = new['vote_data']['votes_up'] - old['vote_data']['votes_up']
    delta['votes_down'] = new['vote_data']['votes_down'] - old['vote_data']['votes_down']
    delta['score'] = new['vote_data']['score'] - old['vote_data']['score']

    print('\tRATES:')
    print(f"time:       {dtime/dtime:.1f}/m")
    print(f"views:      {delta['views']/dtime:.1f}/m")
    print(f"subs:       {delta['subs']/dtime:.1f}/m")
    print(f"favs:       {delta['favs']/dtime:.1f}/m")
    print(f"total subs: {delta['lt_subs']/dtime:.1f}/m")
    print(f"total favs: {delta['lt_favs']/dtime:.1f}/m")
    print(f"comments:   {delta['comments']/dtime:.1f}/m")
    print(f"upvotes:    {delta['votes_up']/dtime:.1f}/m")
    print(f"downvotes:  {delta['votes_down']/dtime:.1f}/m")
    print(f"score:      {delta['score']/dtime:.1f}/m")
    print()

def savedata(data):
    direc = getcwd()
    with open(path.join(getcwd(), 'data', str(round(time()))+'.pkl'), 'wb') as f:
        pickle.dump(data, f)

def loaddata():
    
    direc = path.join(getcwd(), 'data')

    files = listdir(direc)

    if (len(files) == 0): return False

    # remove last 4 chars of each file
    files = [f[:-4] for f in files]

    # find newest version
    filepath = max(files)+'.pkl'

    with open(direc+'/'+filepath, 'rb') as f:
        return pickle.load(f)