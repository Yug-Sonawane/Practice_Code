import random
computerint= random.choice([-1, 0, 1])
ReDict={-1:"rock", 0:"paper", 1:"scissor"}
computer= ReDict[computerint]

youstr= input("Choose your option:")
youDict={"rock":-1, "paper":0, "scissor":1}
you= youDict[youstr]

print(f"Game choose {computer}")
if computerint== you:
    print("Draw")

else:
    if computerint==-1 and you==0:
        print("You Win")
    elif computerint==-1 and you==1:
        print("You Loose")
    elif computerint==0 and you==-1:
        print("You Loose")
    elif computerint==0 and you==1:
        print("You Win")
    elif computerint==1 and you==-1:
        print("You Win")
    elif computerint==1 and you==0:
        print("You Loose")
    else:
        print("Something Went Worng")