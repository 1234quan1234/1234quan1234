import pygame, sys
import cfg
def Loading_Bar(screen, cfg):
    screen.fill((29, 89, 98))
    font = pygame.font.Font(None, 36)
    text = font.render('Loading...', True, (255,255,255))
    text_rect = text.get_rect(center=(cfg.SCREENSIZE[0]//2, cfg.SCREENSIZE[1]//2-25))
    screen.blit(text, text_rect)

    # Draw the outer box
    outer_box = pygame.Rect(cfg.SCREENSIZE[0]//4, cfg.SCREENSIZE[1]//2 - 10, cfg.SCREENSIZE[0]//2, 20)
    pygame.draw.rect(screen, (255,255,255), outer_box, 2)

    for i in range(1, 101):  # 100 steps for the loading bar
        pygame.draw.line(screen, (255,255,255), (cfg.SCREENSIZE[0]//4, cfg.SCREENSIZE[1]//2), (cfg.SCREENSIZE[0]//4 + i*(cfg.SCREENSIZE[0]//2)//100, cfg.SCREENSIZE[1]//2), 20)
        pygame.display.update()
        pygame.time.wait(10)  # Wait for 10 milliseconds

    return True
