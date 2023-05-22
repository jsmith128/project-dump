from random import sample

with open('pwords.txt', 'r') as f:
    words = f.readlines()
    with open('out.txt', 'a+') as out:
        for i in range(100):
            ppp = sample(words, 3)
            out.write(''.join(ppp).replace('\n', ' ')+'\n')