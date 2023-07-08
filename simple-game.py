import arcade

WIDTH = 800
HEIGHT = 600

white = arcade.color.WHITE
blue = arcade.color.BLUE
green = arcade.color.GREEN

class GameWindow(arcade.Window):
    def __init__(self):
        super().__init__(WIDTH, HEIGHT, "Simple Game")
        self.player_x = WIDTH // 2
        self.player_y = HEIGHT // 2

    def setup(self):
        arcade.set_background_color(white)

    def on_draw(self):
        arcade.start_render()
        arcade.draw_rectangle_filled(self.player_x, 
        self.player_y, 50, 50, blue)
        arcade.draw_rectangle_filled(WIDTH // 2, 
        HEIGHT // 4, WIDTH, 10, green)

    def on_key_press(self, key, modifiers):
        if key == arcade.key.LEFT:
            self.player_x -= 10
        elif key == arcade.key.RIGHT:
            self.player_x += 10

def main():
    window = GameWindow()
    window.setup()
    arcade.run()

if __name__ == "__main__":
    main()

