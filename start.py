class Player(object):
    """Player in the game."""
    def blast(self,enemy):
        print("Player is striking in the enemy.")
        enemy.die()

class Alien(object):
    """Bad person in the game."""
    def die(self):
        print("I was a good alien, but you decided to kill me ....")
        print("Remember me ....")

hero = Player()
invader = Alien()
hero.blast(invader)
input("Push 'Enter' if you want to close this programme.")
