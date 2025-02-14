class Venicle:
    speed = True
    moving = True
    def __init__(self, speed_from_user, moving_from_user):
        self.speed = speed_from_user
        self.moving = moving_from_user
    def show_speed(self):
        print(self.speed)
    def show_moving(self):
        print(self.moving)

car = Venicle(20,True)
car.show_speed()
car.show_moving()