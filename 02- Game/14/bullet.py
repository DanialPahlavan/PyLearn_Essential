import arcade


class Bullet(arcade.Sprite):
    def __init__(self, x, y):
        super().__init__(":resources:images/space_shooter/laserRed01.png")
        self.position = x, y
        self.velocity = 0, 5
