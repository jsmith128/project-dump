from random import shuffle
print('tourneyMaker.py 0.0.2')
print('Aug 2 2020, 21:00')

manualmode = 0 # Set this to 1 if you would like to change the values below, 
               # along with skipping the querying when you start the program

mm_participants = ['redacted1', 'redacted2', 'redacted3', 'redacted4'] # Participants (only effective if manualmode = 1)
                                                                # example:
                                                                # mm_participants = ['player1', 'player2']
mm_referees = ['redacted_ref'] # Participants (again, only effective if manualmode = 1)
                       # example above still applies



if manualmode == 1:
    participants = mm_participants
    referees = mm_referees
else:
    participants = []
    referees = []
    ########## Get participants
    answer = ''
    print('Type the names of the participants:') # Get participants
    while not answer == 'done': # keep looping until user types 'done'
        print('The current participants are: ')
        print(participants,'\nType "done" when done\n')

        answer = input('>>> ')
        if not answer == 'done':
            participants.append(answer)

    ########## Get referee(s)
    answer = '' # reset answer's value, to not skip this loop after the last
    print('Type the name(s) of the referee(s):')
    while not answer == 'done': # keep looping until user types 'done'
        print('The current referee(s) are: ')
        print(referees,'\nType "done" when done\n')

        answer = input('>>> ')
        if not answer == 'done':
            referees.append(answer)

print(participants)
players_num = len(participants)
shuffle(participants) # Shuffle participating players, to randomize the selection later

if len(participants)%2 == 0: # check if number of participants is even. If so, split
    print('The number of participants is even! (' + str(players_num) + ') \nSplitting...\n')
    players_half1 = participants[:players_num//2]
    players_half2 = participants[players_num//2:]
else: # if odd, quit
    print('\n\nSorry, the number of players is uneven (' + str(players_num) + '). Exiting...')
    exit()


########## Print stuff
print('\nThe tournament will consist of the following:') # print participant lineup
for i in range(len(players_half1)): # use players_half1 rather than participants/2, for reasons
    print(str(i+1)+'.', players_half1[i], 'vs.', players_half2[i] )

print('\nReferee(s):')
for ref in referees: # print referee(s)
    print(ref)
print('\n')