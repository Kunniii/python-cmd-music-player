# import some packages
from sys        import argv
from os         import listdir, system
from random     import randint
from getopt     import getopt, error
from playsound  import playsound

# To-update :D
# Show playing list
# Show current play song


# Some default value
musicPath       = '.'
shuffle         = 0
alphabet        = 0
listOfSoundExt  = ('mp3', 'wav')
playedList      = []

def showPlaylist(musicList, current):
    global shuffle
    global alphabet
    system('clear')
    # Show play list
    print('\t+ ----------------------------------------------------------------- +')
    print('\t|                              Playlist                             |')
    print('\t+ ----------+-------+---------------------------------------------- +')
    print('\t|  Playing  |  No.  |  Name                                         |')
    print('\t+ ----------+-------+---------------------------------------------- +')
    # Show what song is playing
    for i in musicList:
        if musicList[i] == current:
            n = f"\t|  >>>>>>>  |  {i+1}" + " "*(5-len(f'{i+1}')) + f"|  {musicList[i]}"
        else:
            n = f"\t|           |  {i+1}" + " "*(5-len(f'{i+1}')) + f"|  {musicList[i]}"
        space = " "*(67-len(n))
        print(n, space, "|")
    # Show play mode
    print('\t+ ----------+-------+---------------------------------------------- +')
    isShuffle = ' Shuffle: ' + ('yes' if shuffle else 'no ')
    isAlpha   = 'Alphabet: ' + ('yes' if alphabet else 'no')
    mode = isShuffle + '        ' + isAlpha
    print('\t|', mode,' '*(64-len(mode)),'|')

    print('\t+','-'*65,'+')
    print('\t|',f' {"Now playing:   " + current}',' '*(62-len("Now playing:  " + current)),'|')
    print('\t+','-'*65,'+') 

def usage():
    print('Play music in command lines')
    print('-h       Help')
    print('-d       stirng    : Directory, where you want to load and play your music')
    print('-s       bool(1|0) : Shuffle your list')
    print('-a       bool(1|0) : Play in alphabet')

# If user not passing any argv, exit
if not argv[1:]:
    print('Need some arguments!')
    exit(1)

# try to get user opt
try:
    opt, val = getopt(argv[1:], "h:d:s:a:",('help', 'dir', 'shuff', 'alpha'))
    for o, v in opt:
        if o in ('-h', '--help'):
            usage()
            exit(0)
        elif o in ('-d', '--dir'):
            musicPath = v
            if "." in musicPath:
                musicPath=musicPath.replace('.','')
            if "\\" in musicPath:
                musicPath=musicPath.replace('\\', '')
            if "/" in musicPath:
                musicPath=musicPath.replace('/', '')
        elif o in ('-s', '--shuff'):
            shuffle = int(v)
        elif o in ('-a', '--alpha'):
            alphabet = int(v)
except error as e:
    print(e)
    usage()
    exit(1)

if alphabet and shuffle:
    print("These two values can not be True together!")
    print("Consider using alphabet")
    shuffle = 0

# Get music list or playlist
musicList = [i for i in listdir(musicPath) if i[-3:] in listOfSoundExt]

if alphabet:
    musicList = sorted(musicList)

musicList = {i:name for i, name in enumerate(musicList)}

# Play the list
if shuffle:
    while len(playedList) != len(musicList):
        index = randint(0, len(musicList)-1)
        while index in playedList:
            index = randint(0, len(musicList)-1)
        showPlaylist(musicList, musicList[index])
        playsound(f'{musicPath}/{musicList[index]}')
        playedList.append(index)
else:
    for i in musicList:
        print(f"Playing: {musicList[i][:-4]}")
        showPlaylist(musicList, musicList[i])
        playsound(f'{musicPath}/{musicList[i]}')

print("Played till the end of playlist!")




















