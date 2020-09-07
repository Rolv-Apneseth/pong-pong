import pygame
import random

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
PURPLE = (147, 112, 219)


class Paddle():
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

        self.surface = pygame.Surface((self.width, self.height))
        self.surface.fill(WHITE)

        self.points = 0

    def draw(self, window):
        window.blit(self.surface, (self.x, self.y))

    def move(self, vel):
        self.x += vel


class Goal():
    def __init__(self, y, width, height):
        self.x = 0
        self.y = y
        self.width = width
        self.height = height

        self.surface = pygame.Surface((self.width, self.height))
        self.surface.fill(PURPLE)

    def draw(self, window):
        window.blit(self.surface, (self.x, self.y))


class Ball():
    # So ball waits before mobing in a direction
    COOLDOWN = 30  # 0.5 seconds at 60 fps

    def __init__(self, x, y, vel, radius):
        self.x = x
        self.y = y
        # Ball will therefore move in a random direction
        self.xvel = vel * random.choice([1, -1])
        self.yvel = vel * random.choice([1, -1])
        self.cooldown_counter = self.COOLDOWN
        self.radius = radius

    def reset_cooldown(self):
        """Cooldown so that ball does not start moving striaght away"""
        self.cooldown_counter = self.COOLDOWN

    def move(self):
        """Moves ball if cooldown is 0"""
        if self.cooldown_counter:
            self.cooldown_counter -= 1
        else:
            self.x += self.xvel
            self.y += self.yvel

    def draw(self, window):
        pygame.draw.circle(
            window, WHITE, (int(self.x), int(self.y)), self.radius)


def game_loop(window, WIDTH, HEIGHT):
    FPS = 60
    clock = pygame.time.Clock()

    win = False
    win_timer = 0
    who_won = None

    # So players can't spam balls
    ball_spawn_cooldown = 0

    BALL_RADIUS = 15
    BALL_VELOCITY = 3
    # Starting location for the ball, and place where it respawns
    DEFAULT_X = WIDTH // 2
    DEFAULT_Y = HEIGHT // 2

    PADDLE_VELOCITY = 5

    running = True

    # Goals, point scored if ball hits enemy goal object
    top_goal = Goal(round(HEIGHT * 0.1), WIDTH, round(HEIGHT * 0.02))
    bottom_goal = Goal(round(HEIGHT * 0.96), WIDTH, round(HEIGHT * 0.02))

    player1 = Paddle(round(WIDTH * 0.05), round(HEIGHT * 0.13),
                     round(WIDTH * 0.1), round(HEIGHT * 0.02))
    player2 = Paddle(round(WIDTH * 0.85), round(HEIGHT * 0.93),
                     round(WIDTH * 0.1), round(HEIGHT * 0.02))

    balls = []
    balls.append(Ball(DEFAULT_X, DEFAULT_Y, BALL_VELOCITY, BALL_RADIUS))

    score_label_font = pygame.font.SysFont("arial", 20)
    win_label_font = pygame.font.SysFont("arial", 40)

    def redraw_window(window):
        """Updates ui, executed once every frame."""

        # Background
        window.fill(BLACK)

        # Display Objects. Have to be redrawn because objects are moving every frame.
        top_goal.draw(window)
        bottom_goal.draw(window)

        player1.draw(window)
        player2.draw(window)

        for ball in balls:
            ball.draw(window)

        # Player Score Labels
        player1_score = score_label_font.render(
            f"Player 1 score: {player1.points}", 1, WHITE)
        window.blit(player1_score, (WIDTH // 10, HEIGHT // 15))

        player2_score = score_label_font.render(
            f"Player 2 score: {player2.points}", 1, WHITE)
        window.blit(player2_score, (WIDTH * 7 // 10, HEIGHT // 15))

        # Displays win label
        if win:
            win_label = win_label_font.render(f"{who_won} won the game!",
                                              1,
                                              (255, 255, 255)
                                              )

            window.blit(win_label,
                        (WIDTH // 2 - win_label.get_width() // 2, HEIGHT // 2)
                        )

        pygame.display.update()

    while running:
        clock.tick(FPS)

        redraw_window(window)

        # Checks if a player has won
        if player1.points >= 20:
            win = True
            who_won = "Player 1"
        if player2.points >= 20:
            win = True
            who_won = "Player 2"

        # Keeps a 1 second timer (at 60fps) when a player has won before ending the loop
        if win:
            win_timer += 1
            if win_timer >= 60:
                running = False
            else:
                continue

        ball_spawn_cooldown += 1

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # MOVEMENT
        keys = pygame.key.get_pressed()

        # player1, uses a and d keys
        if keys[pygame.K_a] and player1.x - PADDLE_VELOCITY > 0:  # left
            player1.move(-PADDLE_VELOCITY)
        if keys[pygame.K_d] and player1.x + PADDLE_VELOCITY + player1.width < WIDTH:  # right
            player1.move(PADDLE_VELOCITY)
        # player2, uses up and down arrow keys
        if keys[pygame.K_LEFT] and player2.x - PADDLE_VELOCITY > 0:  # left
            player2.move(-PADDLE_VELOCITY)
        if keys[pygame.K_RIGHT] and player2.x + PADDLE_VELOCITY + player2.width < WIDTH:  # right
            player2.move(PADDLE_VELOCITY)
        # Either player can press spacbar to create another ball
        if keys[pygame.K_SPACE]:
            if ball_spawn_cooldown >= 120:
                balls.append(Ball(DEFAULT_X, DEFAULT_Y,
                                  BALL_VELOCITY, BALL_RADIUS))
                ball_spawn_cooldown = 0

        # Ball movement and collisions
        for ball in balls:
            ball.move()
            # Contain in the x boundaries of the screen
            if ball.x < ball.radius or ball.x > WIDTH - ball.radius:
                ball.xvel *= -1
            # Collision with paddles, causes ball velocity to reverse
            if ball.y - ball.radius < player1.y + player1.height and player1.x < ball.x < player1.x + player1.width:
                ball.yvel *= -1
            if ball.y + ball.radius > player2.y and player2.x < ball.x < player2.x + player2.width:
                ball.yvel *= -1
            # Collision with goals, point added to respective player
            if ball.y + ball.radius > bottom_goal.y:
                player1.points += 1
                balls.remove(ball)
            # Two different if statements so that point can be awarded to the correct player
            if ball.y - ball.radius < top_goal.y + top_goal.height:
                # ball.xvel = random.choice([1, -1]) * BALL_VELOCITY
                # ball.yvel = random.choice([1, -1]) * BALL_VELOCITY
                player2.points += 1
                balls.remove(ball)
