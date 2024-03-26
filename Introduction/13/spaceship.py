import arcade


class SpaceshipGame(arcade.Window):
    def __init__(self):
        # Initialize the game window
        super().__init__(800, 600, "Spaceship Game")
        # Set the initial position of the spaceship
        self.spaceship_x, self.spaceship_y = 400, 300

    def on_draw(self):
        # Render the game screen
        arcade.start_render()
        # Draw the spaceship as a white circle
        arcade.draw_circle_filled(self.spaceship_x, self.spaceship_y, 20, arcade.color.WHITE)

    def on_key_press(self, key, modifiers):
        # Handle keyboard input (left and right arrow keys)
        if key == arcade.key.LEFT:
            self.spaceship_x -= 10
        elif key == arcade.key.RIGHT:
            self.spaceship_x += 10


if __name__ == "__main__":
    # Create an instance of the game and run it
    game = SpaceshipGame()
    arcade.run()
