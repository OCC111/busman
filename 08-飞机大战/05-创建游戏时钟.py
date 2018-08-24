import pygame

pygame.init()

screen = pygame.display.set_mode((480,700))#创建游戏窗口

bg = pygame.image.load("./images/background.png")
hero = pygame.image.load("./images/hero1.png")

herorect = pygame.Rect(200,500,120,120)#创建一个rect类

clock = pygame.time.Clock()#创建游戏时钟

while True:
	clock.tick(60)#一秒刷新60次
	
	herorect.y-= 1#相当速度

	screen.blit(bg,(0,0))
	screen.blit(hero,herorect)

	if herorect.bottom <= 0:#控制飞机返航
		herorect.top = 700

	pygame.display.update()#更新
	
pygame.quit()
