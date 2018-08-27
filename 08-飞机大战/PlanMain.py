import pygame
import time
from MySprite import *
class PlaneGame(object):
	def __init__(self):
		self.screen = pygame.display.set_mode(SCREEN_RECT.size)
		self.clock = pygame.time.Clock()
		self.__create_sprites()
		self.a = True

		pygame.time.set_timer(CREATE_ENEMY_EVENT,1000)#敌机定时事件
		pygame.time.set_timer(FIRE_BULLET,200)#子弹定时事件
		


	def start_game(self):
		while True:
			self.__event_handler()
			if self.a :	
				# 1. 设置刷新帧率
				self.clock.tick(60)
				# 2. 事件监听
				self.__event_handler()
				# 3. 碰撞检测
				self.__check_collide()
				# 4. 更新精灵组
				self.__update_sprites()
				# 5. 更新屏幕显示
				pygame.display.update()

	def __create_sprites(self):#创建精灵组和精灵组
		bg1 = BackGroundSprite()
		bg2 = BackGroundSprite(True)
		self.bg_group = pygame.sprite.Group(bg1,bg2)
		self.enemy_group = pygame.sprite.Group()#创建敌机精灵组

		self.hero = HeroSprite()
		self.hero_group = pygame.sprite.Group(self.hero)

		self.down = Hero_down()
		self.down_group = pygame.sprite.Group(self.down)
    	        
	def __event_handler(self):
		"""事件监听"""
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				PlaneGame.__game_over()
			elif event.type == CREATE_ENEMY_EVENT:
				# print("事件被触发了")
				enemy = EnemySprite()
				self.enemy_group.add(enemy)#通过add方法添加
			elif event.type == FIRE_BULLET:
				self.hero.fire()
		keys_pressed = pygame.key.get_pressed()
		if keys_pressed[pygame.K_RIGHT]:
			self.hero.speed = 5
		elif keys_pressed[pygame.K_LEFT]:
			self.hero.speed = -5
		else:
			self.hero.speed = 0
		if keys_pressed[pygame.K_SPACE]:
			#print("该发射子弹了")
			if self.a :
				self.a = False
			else:
				self.a = True


	def __check_collide(self):
		"""碰撞检测"""
		pygame.sprite.groupcollide(self.hero.bullet_group, self.enemy_group, True, True)
		
	    # 2. 敌机撞毁英雄
		enemies = pygame.sprite.spritecollide(self.hero, self.enemy_group, True)
		

		if len(enemies) > 0:

	        # 让英雄牺牲
			self.hero.down_group
			time.sleep(0.5)
			self.hero.kill()
		
	        # 结束游戏
			PlaneGame.__game_over()
	def __update_sprites(self):
		"""更新精灵组"""
		self.bg_group.update()
		self.bg_group.draw(self.screen)
		

		self.enemy_group.update()
		self.enemy_group.draw(self.screen)

		self.hero_group.update()
		self.hero_group.draw(self.screen)

		self.hero.bullet_group.update()
		self.hero.bullet_group.draw(self.screen)

		self.down.down_group.update()
		self.down.down_group.draw(self.screen)

	
	@staticmethod
	def __game_over():
	   """游戏结束"""

	   print("游戏结束")
	   pygame.quit()
	   exit()	

if __name__ == '__main__':
    # 创建游戏对象
    game = PlaneGame()

    # 开始游戏
    game.start_game()
