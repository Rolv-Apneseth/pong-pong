import pygame

import pong_pong


def main_menu(window, WIDTH, HEIGHT):
    title_font = pygame.font.SysFont("arial", 40)

    run = True
    while run:
        # Background
        window.fill(pong_pong.BLACK)

        # Labels
        title_label = title_font.render("Welcome to Pong Pong!", 1, pong_pong.WHITE)
        title_middle = WIDTH // 2 - title_label.get_width() // 2
        window.blit(title_label, (title_middle, HEIGHT // 20))

        click_label = title_font.render(
            "To begin the game, simply left click.", 1, pong_pong.WHITE
        )
        click_middle = WIDTH // 2 - click_label.get_width() // 2
        window.blit(click_label, (click_middle, HEIGHT * 8 // 10))

        controls_label1 = title_font.render(
            "Player 1 moves with A and D", 1, pong_pong.WHITE
        )
        control1_middle = WIDTH // 2 - controls_label1.get_width() // 2
        window.blit(controls_label1, (control1_middle, HEIGHT * 2 // 10))

        controls_label2 = title_font.render(
            "Player 2 moves with left and right", 1, pong_pong.WHITE
        )
        control2_middle = WIDTH // 2 - controls_label2.get_width() // 2
        window.blit(controls_label2, (control2_middle, HEIGHT * 3 // 10))

        controls_label3 = title_font.render(
            "Either can spawn a new ball with spacebar", 1, pong_pong.WHITE
        )
        control3_middle = WIDTH // 2 - controls_label3.get_width() // 2
        window.blit(controls_label3, (control3_middle, HEIGHT * 4 // 10))

        win_label = title_font.render(
            "A player wins when they reach 20 points", 1, pong_pong.WHITE
        )
        win_middle = WIDTH // 2 - win_label.get_width() // 2
        window.blit(win_label, (win_middle, HEIGHT * 6 // 10))

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                pong_pong.game_loop(window, WIDTH, HEIGHT)


def main():
    pygame.font.init()

    WIDTH, HEIGHT = 750, 750
    WIN = pygame.display.set_mode((WIDTH, HEIGHT))

    pygame.display.set_caption("Pong Pong")

    main_menu(WIN, WIDTH, HEIGHT)

    pygame.quit()


if __name__ == "__main__":
    main()
