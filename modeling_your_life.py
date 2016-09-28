
class Activities:

    def __init__(self):
        self.music = ["all the fun and enjoyment i get from being creative."]
        self.jogging = ["what i do to get think about my next coding challenge."]
        self.tv = ["the thing that makes me giggle at the end of a bad day."]
        self.stress = ["all the things going on in my head"]
        self.time = ["hours in the day"]
        self.the_struggle = ["all of the things that make us who we are"]

life = Activities()

if life.tv + life.music != life.time:
    print(life.stress)

else:
    print("take a break and clear your head")


print(life.the_struggle)
print("tyler, you never jog, don't lie to yourself, or joel hahahahah, you just think")
# the best i could do on today's assignment
