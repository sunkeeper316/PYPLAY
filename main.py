import displaymap
from player import Player

def main() :
    print("開始執行")
    player = Player()
    player.start()

def saveFile(str):
    print("saveFile")
    
    with open("log.txt" , 'a') as t :
        t.write(str)
        # print("String Variable: {}".format(str), file=t)

# run start
print(__name__)

if __name__ == "__main__" :

    # a = .9
    # print(a)
    main()



