import pygame
from MySprite import *

pygame.init()

screen = pygame.display.set_mode((480,700))#创建游戏窗口

bg = pygame.image.load("./images/background.png")
hero = pygame.image.load("./images/hero1.png")

herorect = pygame.Rect(200,500,120,120)#创建一个rect类

clock = pygame.time.Clock()#创建游戏时钟

enemy = EnemySprite()#创建敌机精灵
enemy1 = EnemySprite()#创建敌机精灵
enemy1.rect.x = 50
enemy1.speed = 2
enemy_group = pygame.sprite.Group(enemy,enemy1)#把精灵加到精灵组


while True:
	clock.tick(60)#一秒刷新60次
	
	herorect.y-= 1#相当速度

	screen.blit(bg,(0,0))
	screen.blit(hero,herorect)

	if herorect.bottom <= 0:#控制飞机返航
		herorect.top = 700

	enemy_group.update()#更新
	enemy_group.draw(screen)#画到哪

	# 事件监听
	for event in pygame.event.get():

        # 判断用户是否点击了关闭按钮
		if event.type == pygame.QUIT:
			print("退出游戏...")
			pygame.quit()
            #直接退出系统
			exit()	

	pygame.display.update()#更新
	

