with open('/home/jon/Desktop/syfy', 'r') as f:
    movies = f.readlines()
    length = str(sum(1 for line in f))
movies_seen = []

print('"y" for yes, anything else (nothing) for no, "stop" to stop.\n')
c = 0
for movie in movies:
    c+=1
    seen = input(str(c)+'/'+length +' - '+movie.strip()+': ')
    if seen == 'y':
        print('Have seen '+ movie)
        movies_seen.append(movie.strip())
    elif seen == 'stop':
        print('Stopping...')
        break
    else:
        print('Have not seen '+ movie)

print(', '.join(movies_seen))