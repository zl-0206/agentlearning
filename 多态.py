class Animal:
    def speak(self):
        pass#抽象方法

class Dog(Animal):
    def speak(self):
        print('WWW')
class Cat(Animal):
    def speak(self):
        print('MMM')

def makenoise(animal:Animal):
    animal.speak()

dog=Dog()
cat=Cat()
#makenoise(dog)
#makenoise(cat)



class ac:
    def cool(self):
        pass
    def hot(self):
        pass
    def swing(self):
        pass

class media(ac):
    def cool(self):
        print("media cool")
    def hot(self):
        print("media hot")
    def swing(self):
        print("media swing")

class hier(ac):
    def cool(self):
        print("hier cool")
    def hot(self):
        print("hier hot")
    def swing(self):
        print("hier swing")

def workcool(i:ac):
    i.cool()
def workhot(h:ac):
    h.hot()

me=media()
hi=hier()

workcool(me)
workcool(hi)
workhot(me)
workhot(hi)