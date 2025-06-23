import turtle as t
import random

# Game Settings
WIDTH, HEIGHT = 500, 500
FOOD_SIZE = 10
DELAY = 100  # milliseconds
SCORE = 0

# Direction offsets
OFFSETS = {
    "up": (0, 20),
    "down": (0, -20),
    "left": (-20, 0),
    "right": (20, 0)
}

# Snake and food state
snake = []
snake_dir = "up"
food_position = (0, 0)

# --- Functions ---

def reset():
    """Reset the game state."""
    global snake, snake_dir, food_position, SCORE
    SCORE = 0
    snake.clear()
    snake.extend([[0, 0], [0, 20], [0, 40], [0, 60], [0, 80]])
    snake_dir = "up"
    food_position = get_random_food_position()
    food.goto(food_position)
    move_snake()

def move_snake():
    """Move the snake forward and handle all game logic."""
    global SCORE

    new_head = snake[-1].copy()
    new_head[0] += OFFSETS[snake_dir][0]
    new_head[1] += OFFSETS[snake_dir][1]

    # Collision with self
    if new_head in snake[:-1]:
        print(f"Game Over! Score: {SCORE}")
        reset()
        return

    snake.append(new_head)

    # Eat food or move normally
    if not food_collision():
        snake.pop(0)

    # Boundary wrap
    if new_head[0] > WIDTH // 2:
        new_head[0] -= WIDTH
    elif new_head[0] < -WIDTH // 2:
        new_head[0] += WIDTH
    elif new_head[1] > HEIGHT // 2:
        new_head[1] -= HEIGHT
    elif new_head[1] < -HEIGHT // 2:
        new_head[1] += HEIGHT

    # Draw snake
    pen.clearstamps()
    for segment in snake:
        pen.goto(segment[0], segment[1])
        pen.stamp()

    screen.update()
    screen.title(f"🐍 Snake Game | Score: {SCORE}")
    t.ontimer(move_snake, DELAY)

def food_collision():
    """Check and handle food collision."""
    global food_position, SCORE
    if get_distance(snake[-1], food_position) < 20:
        SCORE += 10
        food_position = get_random_food_position()
        food.goto(food_position)
        return True
    return False

def get_random_food_position():
    """Return a random, grid-aligned food position."""
    x = random.randint(-WIDTH // 2 + 20, WIDTH // 2 - 20)
    y = random.randint(-HEIGHT // 2 + 20, HEIGHT // 2 - 20)
    x -= x % 20
    y -= y % 20
    return (x, y)

def get_distance(pos1, pos2):
    """Euclidean distance between two positions."""
    return ((pos2[0] - pos1[0])**2 + (pos2[1] - pos1[1])**2) ** 0.5

# Direction controls
def go_up():
    global snake_dir
    if snake_dir != "down":
        snake_dir = "up"

def go_down():
    global snake_dir
    if snake_dir != "up":
        snake_dir = "down"

def go_left():
    global snake_dir
    if snake_dir != "right":
        snake_dir = "left"

def go_right():
    global snake_dir
    if snake_dir != "left":
        snake_dir = "right"

# --- Turtle Setup ---

# Screen
screen = t.Screen()
screen.setup(WIDTH, HEIGHT)
screen.bgcolor("lightgrey")
screen.tracer(0)
screen.title("Snake Game")

# Snake Pen
pen = t.Turtle("square")
pen.penup()
pen.speed(0)

# Food
food = t.Turtle()
food.shape("circle")
food.color("red")
food.shapesize(FOOD_SIZE / 20)
food.penup()
food.speed(0)
screen.listen()
screen.onkey(go_up, "Up")
screen.onkey(go_down, "Down")
screen.onkey(go_left, "Left")
screen.onkey(go_right, "Right")
reset()
t.done()
#vamsi