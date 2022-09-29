hp = 1000

def shoot(damage):
    global hp
    hp -= damage
    print("You dealt damage of {damage}"):
    return hp

def game_over(name):
    print("Game over " + name)

def fly_left():
    print("You moved left")

def fly_right():
    print("You moved right")

def fly_forward():
    print("You moved forward")

if __name__ == "__main__":
    health_points = "hp"

    shoot(450)
    fly_left()
    fly_right()
    fly_forward()
    game_over("Artyom")