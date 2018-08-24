import pygame

pygame.init()
screen = pygame.display.set_mode((480,700))#创建游戏窗口
bg = pygame.image.load("./images/background.png")
screen.blit(bg,(0,0))
pygame.display.update()#更新



while True:
	pass
pygame.quit()
