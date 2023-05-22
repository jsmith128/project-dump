from time import gmtime
from os import open

activity_list = ['running', 'computer', 'a'] #TODO: read from file
activity = ''
dur_hours = 0
dur_minutes = 0
dur_seconds = 0

def ask():
    global activity
    global dur_hours
    global dur_minutes
    global dur_seconds

    print(activity_list)
    activity = input('What activity? (enter an activity above, or enter a new one to create it)\n>>>').strip().lower()
    try:
        dur_hours = str(input('How many hours?\n>>>'))
        dur_minutes = str(input('How many minutes?\n>>>'))
        dur_seconds = str(input('How many seconds?\n>>>'))
    except:
        print('Sorry, there was an error')
        exit()

def saveInfo():
    


    year, month, mday, hour, minute, sec, wday, yday, idst = gmtime()
    year, month, mday, hour, minute, sec, wday, yday, idst = str(year), str(month), str(mday), str(hour), str(minute), str(sec), str(wday), str(yday), str(idst)
    #                                                                                                                                I'm aware that I can put all of these variables in a dictionary and loop through them and convert them to str. I'm just too lazy to do so and this works.
    print(month+'/'+mday+'/'+year + ',', hour+':'+minute+':'+sec + ';', activity, 'for', dur_hours, 'hours,', dur_minutes, 'minutes and', dur_seconds, 'seconds.')


ask()
saveInfo()


