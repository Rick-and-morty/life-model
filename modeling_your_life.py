
class Activities:

    def __init__(self):
        self.music = ["all the fun and enjoyment i get from being creative."]
        self.jogging = ["what i do to get think about my next coding challenge."]
        self.tv = ["the thing that makes me giggle at the end of a bad day."]
        self.stress = ["all the things going on in my head"]
        self.time = ["hours in the day"]
        self.the_struggle = ["all of the things that make us who we are"]


class My_old_band:

    def __init__(self):
        self.travis = "the ridculous drunk, but still my good friend"
        self.jon = "the guy who always had my back, even at the worst times"
        self.tyler = "me, haha no really sure what to say"

life = Activities()
shows = My_old_band()
if life.tv + life.music != life.time:
    print(life.stress)

else:
    print("take a break and clear your head")

print(life.the_struggle)
print("tyler, you never jog, don't lie to yourself, or joel hahahahah, you just think")

shows.travis = input("is travis sober? Y/n ")
if "n":
    print("looks like things are going to get interesting again!")
else:
    print("looks like we may have a show worth a damn for once!")


# the best i could do on today's assignment
# git hub is angering me
