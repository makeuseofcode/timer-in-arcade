import arcade
import time

WIDTH = 800
HEIGHT = 600

white = arcade.color.WHITE
blue = arcade.color.BLUE
green = arcade.color.GREEN


class Timer:
    def __init__(self, duration):
        self.duration = duration
        self.start_time = 0
        self.is_running = False

    def start(self):
        self.start_time = time.time()
        self.is_running = True

    def stop(self):
        self.is_running = False

    def get_elapsed_time(self):
        if self.is_running:
            return time.time() - self.start_time
        return 0

    def is_expired(self):
        return self.get_elapsed_time() >= self.duration

class GameWindow(arcade.Window):
    def __init__(self):
        super().__init__(WIDTH, HEIGHT, "Simple Game")
        self.player_x = WIDTH // 2
        self.player_y = HEIGHT // 2
        self.timer = Timer(5)

    def setup(self):
        arcade.set_background_color(white)

    def on_draw(self):
        arcade.start_render()
        arcade.draw_rectangle_filled(self.player_x, 
        self.player_y, 50, 50, blue)
        arcade.draw_rectangle_filled(WIDTH // 2, 
        HEIGHT // 4, WIDTH, 10, green)
        if self.timer.is_running:
            elapsed_time = self.timer.get_elapsed_time()
            r_time = self.timer.duration - elapsed_time
            remaining_time = max(r_time, 0)
            print(f"Countdown: {remaining_time:.1f} seconds")

    def on_key_press(self, key, modifiers):
        if key == arcade.key.LEFT:
            self.player_x -= 10
        elif key == arcade.key.RIGHT:
            self.player_x += 10
        elif key == arcade.key.SPACE:
            self.timer.start()

def main():
    window = GameWindow()
    window.setup()
    arcade.run()

if __name__ == "__main__":
    main()

