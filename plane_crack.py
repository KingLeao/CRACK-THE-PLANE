#-*- coding:utf8 -*-
import pygame
# 导入pygame库
from pygame.locals import *
# 导入一些常用的函数和常量
from sys import exit
# 向sys模块借一个exit函数用来退出程序

pygame.init()
# 初始化pygame,为使用硬件做准备

screen = pygame.display.set_mode((450, 800), 0, 32)
# 创建了一个窗口
pygame.display.set_caption("Crack The Plane")
#设置窗口标题

background = pygame.image.load(r'C:\Users\LiJing\Desktop\planeBeating\back.jpg').convert()
plane = pygame.image.load(r'C:\Users\LiJing\Desktop\planeBeating\plane.png').convert_alpha()
# 加载并转换飞机及游戏背景图像
bullet = pygame.image.load(r'C:\Users\LiJing\Desktop\planeBeating\bullet.png').convert_alpha()
# 加载子弹图像
bullet_x=0
bullet_y=-1
# 初始化子弹位置
while True:
# 游戏主循环

    for event in pygame.event.get():
        if event.type == QUIT:
            # 接收到退出事件后退出程序
            exit()

    screen.blit(background, (0,0))
    # 将背景图画上去
    x, y = pygame.mouse.get_pos()
    # 获得鼠标位置
    if bullet_y<0:
        # 如果子弹位置超出了屏幕上端
		   #x,y = pygame.mouse.get_pos()
         bullet_x = x - bullet.get_width() / 2
         bullet_y = y - bullet.get_height() / 2
		   # 计算子弹的中心位置设为鼠标坐标
    else:
         bullet_y -= 5
        # 子弹的位置往上移
    screen.blit(bullet, (bullet_x,bullet_y))
    # 把子弹画到屏幕上

    x-= plane.get_width()/2
    y-= plane.get_height()/2
    screen.blit(plane,(x,y))
    # 把飞机画到屏幕上
    pygame.display.update()
    # 刷新一下画面



