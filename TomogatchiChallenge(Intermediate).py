import random
import time

class Tomogatchi():
    def __init__(self):
        self.good = False
        self.dead = False
        self.maxAge = random.randint(500,1000)
        self.age = 0
        self.happiness = (random.randint(45,55))
        self.hunger = 0
        self.poison = 0
        self.poopCount = 0
    
    def feed(self):
        self.hunger-=20
        print("Tomogatchi loves food!")
        
    def clean(self):
        print("You clean some poop.")
        self.poopCount-=1
    
    def eat(self):
        if(self.hunger>40):
            print('Tomogatchi is hungry.')
            if(self.poopCount>0):
                self.poopCount-=1
                self.poison+=40
                self.hunger-=10
                print("Tomogatchi ate some poop.")
            else:
                self.hunger+=10
        else:
            self.hunger+=4
    
    def play(self):
        print("Tomogatchi loves to play!")
        self.happiness+=random.randint(0,20)
        self.happiness = 100 if self.happiness>100 else self.happiness
    
    def deathCheck(self):
        death = False
        if(self.hunger>100):
            death = True
            print("Tomogatchi has starved to death.")
        elif(self.poison>100):
            death = True
            print("Tomogatchi ate too much poop and died.")
        elif(self.poopCount>8):
            death = True
            print("There is no room to poop. \n Tomogatchi's anus bursts and it dies.")
        elif(self.happiness<-20):
            death = True
            print("Tomogatchi is too sad. \n Tomogatchi commits suicide and dies.")
        elif(self.age>self.maxAge):
            death = True
            self.good = True
            print("Tomogatchi dies after a good long life at the age of ",self.age)
        elif(self.hunger<-100):
            death = True
            print("Tomogatchi gets diabetes, explodes, and dies.")
        if(death):
            print("Tomogatchi is dead.")
            if(self.good):
                print("You Win!")
            else:
                print("Game Over")
            self.dead = True
    
    def digest(self):
        self.eat()
        self.happiness-=random.randint(0,10)
        if(self.poison>0): self.poison-=1
        self.age+=1
        if(self.age % 15 == 0):
            self.poopCount+=1
            print("Tomogatchi takes a poop.")
        self.deathCheck()
        
    def __str__(self):
        ret = "\nTomogatchi\n"+"----------"+"Age: "
        ret+= str(self.age)+"\n"+"Hunger: "
        ret+= str(self.hunger)+"\n"+"Happiness: "
        ret+= str(self.happiness)+"\n"+"Poison Lvl: "
        ret+= str(self.poison)+"\n"+"Poop Count: "
        ret+= str(self.poopCount)+"\n"
        return ret

def main():
    tomo = Tomogatchi()
    lastTime = time.time()
    while(not tomo.dead):
        if(time.time()-lastTime>3):
            for i in range(int((time.time()-lastTime)/3)):
                 tomo.digest()
            lastTime = time.time()
        inp = "status"
        if(not tomo.dead):
             inp = input("What would you like to do? (feed, play, clean, status)")
        if(inp=="feed"):
            tomo.feed()
        elif(inp=="play"):
            tomo.play()
        elif(inp=="clean"):
            tomo.clean()
        elif(inp=="status"):
            print(tomo)

main()
