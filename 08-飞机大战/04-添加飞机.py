import pygame

pygame.init()
screen = pygame.display.set_mode((480,700))#创建游戏窗口
bg = pygame.image.load("./images/background.png")


hero = pygame.image.load("./images/hero1.png")
#screen.blit(hero,(200,500))

herorect = pygame.Rect(200,500,120,120)

while True:
	herorect.y-=10
	screen.blit(bg,(0,0))
	screen.blit(hero,herorect)
	pygame.display.update()#更新
	
pygame.quit()
 