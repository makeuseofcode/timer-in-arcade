import arcade
import time

WIDTH = 800
HEIGHT = 600

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
        self.timer = Timer(10)

    def on_key_press(self, key, modifiers):
        if key == arcade.key.SPACE:
            self.timer.start()

    def on_draw(self):
        # Existing code
        if self.timer.is_running:
            elapsed_time = self.timer.get_elapsed_time()
            remaining_time = max(self.timer.duration - elapsed_time, 0)
            print(f"Countdown: {remaining_time:.1f} seconds")


class GameWindow(arcade.Window):
    def __init__(self):
        super().__init__(WIDTH, HEIGHT, "Simple Game")
        self.player_x = WIDTH // 2
        self.player_y = HEIGHT // 2
        self.timer = Timer(10)

    def setup(self):
        arcade.set_background_color(arcade.color.WHITE)

    def on_draw(self):
        arcade.start_render()
        arcade.draw_rectangle_filled(self.player_x, self.player_y, 50, 50, arcade.color.BLUE)
        arcade.draw_rectangle_filled(WIDTH // 2, HEIGHT // 4, WIDTH, 10, arcade.color.GREEN)
        if self.timer.is_running:
            elapsed_time = self.timer.get_elapsed_time()
            remaining_time = max(self.timer.duration - elapsed_time, 0)
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
