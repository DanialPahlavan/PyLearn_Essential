import arcade


class Spaceship(arcade.Sprite):
    def __init__(self, w, name):
        super().__init__(":resources:images/space_shooter/playerShip1_green.png")
        self.center_x = w // 2
        self.center_y = 100
        self.width = 45
        self.height = 45
        self.name = name
        self.speed = 2
        self.move_left = False
        self.move_right = False
