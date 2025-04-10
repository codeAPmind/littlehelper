
# -*- encoding=utf8 -*-
__author__ = "xiwen"

from airtest.core.api import *
# from airtest.core.api import *  # Make sure you import everything from Airtest

from airtest.core.win import Windows

from pywinauto import Application  # Import Application from pywinauto

import time

import math
from pynput.keyboard import Key, Controller

import subprocess

# subprocess.run(['runas', '/user:Administrator', 'F:\\UnityProjects\\crealityscan_pc2\\Build\\Windows\\unpack\\CrealityScan 4.exe'])

# 启动桌面应用，比如 Notepad
app = Application().start("F:\\UnityProjects\\crealityscan_pc2\\Build\\Windows\\unpack\\CrealityScan 4.exe")


# # Wait for 3 seconds
time.sleep(20)
# 1. 启动应用程序（注意处理路径空格）
app_path = r"F:\\UnityProjects\\crealityscan_pc2\\Build\Windows\\unpack\\CrealityScan 4.exe"
auto_setup(__file__, devices=["Windows:///"])


# 3. 显式绑定窗口句柄
# connect_device(f"Windows:///{handle}")
connect_device("Windows:///?title_re=.*CrealityScan.*")  # 自动完成窗口查找与绑定‌:ml-citation{ref="1,3" data="citationList"}



# # 假设我们在 Notepad 中执行键盘输入

print("touch being")
# Wait for the app to be ready
app.window(title="CrealityScan 4").wait('ready')


# # 使用 Airtest 进行自动化操作
# # 假设我们在 Notepad 中执行键盘输入

# print("touch new project ")
# if exists(Template(r"newscan.png", record_pos=(-0.149, -0.232), resolution=(1552, 903))):
#     touch(Template(r"newscan.png", record_pos=(-0.149, -0.232), resolution=(1552, 903)))
# else:
#     print("newscan.png not found!")


#########
### skip 掉
########
print("skip 掉 ")
# [3.973, 7.754, 6.908, 14.61, 4.5809999999999995, 6.645, 4.681, 11.396, 3.731, 4.2780000000000005, 
# 17.161, 4.229, 5.66, 10.573, 4.336, 4.043, 48.422, 4.695, 4.436, 5.325, 6.757, 3.503, 30.796, 3.45, 4.654, 4.099, 4.916, 5.965, 5.436, 5.518, 3.2969999999999997, 6.747, 6.017, 7.458, 10.296, 5.161]
time.sleep(3.973)
if exists(Template(r"tpl1744190450855.png", record_pos=(-0.256, 0.197), resolution=(1552, 903))):
    touch(Template(r"tpl1744190450855.png", record_pos=(-0.256, 0.197), resolution=(1552, 903)))
time.sleep(3.973)
if exists(Template(r"tpl1744190452473.png", record_pos=(-0.169, 0.17), resolution=(1552, 903))):
    touch(Template(r"tpl1744190452473.png", record_pos=(-0.169, 0.17), resolution=(1552, 903)))
time.sleep(3.973)
if exists(Template(r"tpl1744190454824.png", record_pos=(0.121, 0.229), resolution=(1552, 903))):
    touch(Template(r"tpl1744190454824.png", record_pos=(0.121, 0.229), resolution=(1552, 903)))
time.sleep(3.973)

print("检查是否连接扫描仪器 ")
# 使用 assert_exists 进行模板检查
try:
    # 检查是否连接扫描仪器
    assert_exists(Template(r"tpl1744191312770.png", record_pos=(-0.387, -0.189), resolution=(1552, 903)), "Please fill in the test point.")
    print("Template exists, continuing with the test.")
except AssertionError:
    # 如果模板不存在，捕获异常并处理
    print("Template not found! Performing recovery steps.")
    # 在这里可以执行任何你想做的操作，如截图或退出测试
    snapshot(filename="error_screenshot.png")
    # 你可以选择停止执行或继续执行
    raise  # Uncomment if you want to stop the test

#########
### 新建工程到扫描结束
########
print("### 新建工程到扫描结束 ")
touch(Template(r"tpl1744185964011.png", record_pos=(-0.112, -0.231), resolution=(1552, 903)))
time.sleep(3.973)
touch(Template(r"tpl1744185965984.png", record_pos=(0.035, 0.051), resolution=(1552, 903)))
time.sleep( 7.754)
touch(Template(r"tpl1744185971738.png", record_pos=(-0.337, 0.103), resolution=(1552, 903)))
time.sleep(6.908)
touch(Template(r"tpl1744185976646.png", record_pos=(-0.434, 0.23), resolution=(1552, 903)))
time.sleep( 19.61)
swipe(Template(r"tpl1744185989256.png", record_pos=(0.41, 0.241), resolution=(1552, 903)), vector=[0.009, 0.0133])
time.sleep( 0.5)
touch(Template(r"tpl1744185991837.png", record_pos=(-0.427, 0.222), resolution=(1552, 903)))
# time.sleep( 6.645)
# swipe(Template(r"tpl1744185996482.png", record_pos=(-0.358, 0.238), resolution=(1552, 903)), vector=[0.0039, 0.0066])
time.sleep(4.681)
touch(Template(r"tpl1744185999163.png", record_pos=(-0.358, 0.241), resolution=(1552, 903)))
time.sleep(  11.396)

#########
### 继续扫描 到 批量 点云融合
########
print("###继续扫描 到 批量 点云融合")
#起步阶段做检查是否可以继续
if exists(Template(r"tpl1744186008559.png", record_pos=(-0.469, -0.201), resolution=(1552, 903))):
    touch(Template(r"tpl1744186008559.png", record_pos=(-0.469, -0.201), resolution=(1552, 903)))
else:
    print("newscan.png not found!")
    snapshot(filename="error_screenshot.png")
    # 你可以选择停止执行或继续执行
    raise 

# touch(Template(r"tpl1744186008559.png", record_pos=(-0.469, -0.201), resolution=(1552, 903)))
time.sleep( 3.731)
touch(Template(r"tpl1744186010290.png", record_pos=(-0.341, 0.099), resolution=(1552, 903)))
time.sleep(4.278)
touch(Template(r"tpl1744186012568.png", record_pos=(-0.436, 0.232), resolution=(1552, 903)))
time.sleep(17.161)
swipe(Template(r"tpl1744186027729.png", record_pos=(0.414, 0.232), resolution=(1552, 903)), vector=[0.0097, 0.0244])
time.sleep( 0.5)
swipe(Template(r"tpl1744186029958.png", record_pos=(-0.431, 0.23), resolution=(1552, 903)), vector=[0.0013, 0.0044])
time.sleep(5.66)
touch(Template(r"tpl1744186033618.png", record_pos=(-0.362, 0.241), resolution=(1552, 903)))
time.sleep(10.573)
touch(Template(r"tpl1744186042191.png", record_pos=(-0.442, -0.127), resolution=(1552, 903)))
time.sleep(4.336)
touch(Template(r"tpl1744186044527.png", record_pos=(-0.405, -0.204), resolution=(1552, 903)))
time.sleep(4.69)
# ok 之后才是执行
touch(Template(r"tpl1744186046570.png", record_pos=(0.028, 0.051), resolution=(1552, 903)))
time.sleep(57.422)
#########
### 拼接
########
print("###拼接")
touch(Template(r"tpl1744186092992.png", record_pos=(-0.262, -0.24), resolution=(1552, 903)))
time.sleep(5.32)
touch(Template(r"tpl1744186095687.png", record_pos=(-0.457, -0.208), resolution=(1552, 903)))
time.sleep(4.69)
touch(Template(r"tpl1744186098123.png", record_pos=(-0.375, 0.249), resolution=(1552, 903)))
time.sleep(39.796)
touch(Template(r"tpl1744186101448.png", record_pos=(-0.43, 0.254), resolution=(1552, 903)))
time.sleep(4.654)
#########
### mesh 平滑，补洞
########
print("### mesh 平滑，补洞")
#起步阶段做检查是否可以继续
if exists(Template(r"tpl1744186106205.png",  record_pos=(-0.397, -0.207), resolution=(1552, 903))):
     touch(Template(r"tpl1744186106205.png", record_pos=(-0.397, -0.207), resolution=(1552, 903)))
else:
    print("newscan.png not found!")
    snapshot(filename="error_screenshot.png")
    # 你可以选择停止执行或继续执行
    raise 

# touch(Template(r"tpl1744186106205.png", record_pos=(-0.397, -0.207), resolution=(1552, 903)))
time.sleep(4.0)
touch(Template(r"tpl1744186107708.png", record_pos=(-0.33, 0.029), resolution=(1552, 903)))
time.sleep(25)
touch(Template(r"tpl1744186136504.png", record_pos=(-0.344, -0.206), resolution=(1552, 903)))
time.sleep(4.0)
touch(Template(r"tpl1744186137954.png", record_pos=(-0.343, -0.214), resolution=(1552, 903)))
time.sleep(5.0)
swipe(Template(r"tpl1744186140608.png", record_pos=(-0.36, -0.184), resolution=(1552, 903)), vector=[-0.0348, 0.0044])
time.sleep(5.0)
swipe(Template(r"tpl1744186142707.png", record_pos=(-0.363, -0.185), resolution=(1552, 903)), vector=[-0.0361, -0.0089])
time.sleep(5.0)
touch(Template(r"tpl1744186145623.png", record_pos=(-0.334, -0.058), resolution=(1552, 903)))
time.sleep(6.0)
touch(Template(r"tpl1744186149588.png", record_pos=(-0.39, -0.047), resolution=(1552, 903)))
time.sleep(5.5)
touch(Template(r"tpl1744186153024.png", record_pos=(-0.398, -0.019), resolution=(1552, 903)))
time.sleep(5.5)
swipe(Template(r"tpl1744186156542.png", record_pos=(-0.494, -0.158), resolution=(1552, 903)), vector=[0.0399, 0.0033])
time.sleep(3.5)
touch(Template(r"tpl1744186157839.png", record_pos=(-0.338, -0.126), resolution=(1552, 903)))
time.sleep(6.7)
touch(Template(r"tpl1744186162586.png", record_pos=(-0.386, -0.127), resolution=(1552, 903)))
time.sleep(6.5)
touch(Template(r"tpl1744186166603.png", record_pos=(-0.374, -0.095), resolution=(1552, 903)))
time.sleep(7.5)
touch(Template(r"tpl1744186172061.png", record_pos=(-0.341, -0.002), resolution=(1552, 903)))
time.sleep(10.3)
touch(Template(r"tpl1744186180357.png", record_pos=(-0.389, -0.005), resolution=(1552, 903)))
time.sleep(5.161)
touch(Template(r"tpl1744186183518.png", record_pos=(-0.475, -0.238), resolution=(1552, 903)))

# time.sleep(5.161)
#########
### 编辑操作
########
print("### 编辑操作")
time.sleep( 3.731)
### 进入编辑页面先检测是否顺利，否侧退出
if exists(Template(r"tpl1744250679955.png", record_pos=(0.479, -0.036), resolution=(1552, 903))):
     touch(Template(r"tpl1744250679955.png", record_pos=(0.479, -0.036), resolution=(1552, 903)))
else:
    print("edit.png not found!")
    snapshot(filename="error_screenshot.png")
    # 你可以选择停止执行或继续执行
    raise 
###
# touch(Template(r"tpl1744250679955.png", record_pos=(0.479, -0.036), resolution=(1552, 903)))
time.sleep( 3.731)
touch(Template(r"tpl1744252195233.png", record_pos=(0.479, 0.007), resolution=(1552, 903)))
time.sleep(1)
touch(Template(r"tpl1744250689001.png", record_pos=(0.445, -0.037), resolution=(1552, 903)))

keyboard = Controller()

# Press and hold the Shift key
keyboard.press(Key.shift)

# Simulate dragging or other actions while Shift is held
# 模拟拖动，从屏幕中心拖动到计算出的终点
# swipe((center_x, center_y), (end_x, end_y), duration=2)

# Release the Shift key
# keyboard.release(Key.shift)
# swipe(Template(r"tpl1744192925380.png", record_pos=(0.006, 0.098), resolution=(1552, 903)), vector=[-0.4034, -0.2625])
# 获取屏幕中心坐标（假设你已经知道这些值，或者用截图方式获取）
center_x, center_y = 960, 540  # 假设屏幕分辨率为 1920x1080

# 斜线的长度
line_length = 500

# 计算45度斜线的终点坐标
dx = line_length / math.sqrt(2)  # 计算 X 方向的变化量
dy = dx  # 由于是45度角，所以 Y 方向的变化量与 X 相等

# 计算终点坐标（向右下方画斜线）
end_x = center_x + dx
end_y = center_y + dy

# 使用 swipe 函数模拟从屏幕中心滑动到终点
swipe((center_x, center_y), (end_x, end_y), duration=2)
keyboard.release(Key.shift)
# 按住 Shift 键（模拟按下 Shift 键）
# keyevent("KEY_SHIFT", down=False)
time.sleep( 3.731)
if exists(Template(r"tpl1744250858971.png", record_pos=(0.479, 0.074), resolution=(1552, 903))):
     touch(Template(r"tpl1744250858971.png", record_pos=(0.479, 0.074), resolution=(1552, 903)))
else:
    print("newscan.png not found!")
    snapshot(filename="error_screenshot.png")
    # 你可以选择停止执行或继续执行
    raise 
time.sleep( 3.731)
if exists(Template(r"tpl1744250966794.png", record_pos=(0.479, 0.216), resolution=(1552, 903))):
     touch(Template(r"tpl1744250966794.png", record_pos=(0.479, 0.216), resolution=(1552, 903)))
else:
    print("newscan.png not found!")
    snapshot(filename="error_screenshot.png")
    # 你可以选择停止执行或继续执行
    raise 

# touch(Template(r"tpl1744193131475.png", record_pos=(0.479, 0.074), resolution=(1552, 903)))
# touch(Template(r"tpl1744193137524.png", record_pos=(0.479, 0.216), resolution=(1552, 903)))
#################################################################################
################################################################################

# 文件名列表
# filenames = [
#     "1744185964011 ",
# "1744185965984 ",
# "1744185971738 ",
# "1744185976646 ",
# "1744185989256 ",
# "1744185991837 ",
# "1744185996482 ",
# "1744185999163 ",
# "1744186008559 ",
# "1744186010290 ",
# "1744186012568 ",
# "1744186027729 ",
# "1744186029958 ",
# "1744186033618 ",
# "1744186042191 ",
# "1744186044527 ",
# "1744186046570 ",
# "1744186092992 ",
# "1744186095687 ",
# "1744186098123 ",
# "1744186101448 ",
# "1744186106205 ",
# "1744186107708 ",
# "1744186136504 ",
# "1744186137954 ",
# "1744186140608 ",
# "1744186142707 ",
# "1744186145623 ",
# "1744186149588 ",
# "1744186153024 ",
# "1744186156542 ",
# "1744186157839 ",
# "1744186162586 ",
# "1744186166603 ",
# "1744186172061 ",
# "1744186180357 ",
# "1744186183518 "

#     # "tpl1744185964011.png", "tpl1744185965984.png", "tpl1744185971738.png", "tpl1744185976646.png", "tpl1744185999256.png",
#     # "tpl1744185998137.png", "tpl1744185996942.png", "tpl1744185999642.png", "tpl1744186008559.png", "tpl1744186010290.png",
#     # "tpl1744186021568.png", "tpl1744186027729.png", "tpl1744186029955.png", "tpl1744186032618.png", "tpl1744186042191.png",
#     # "tpl1744186044527.png", "tpl1744186045670.png", "tpl1744186092929.png", "tpl1744186095687.png", "tpl1744186098123.png",
#     # "tpl1744186101448.png", "tpl1744186106205.png", "tpl1744186107708.png", "tpl1744186108504.png", "tpl1744186137945.png",
#     # "tpl1744186140608.png", "tpl1744186142707.png", "tpl1744186145223.png", "tpl1744186149585.png", "tpl1744186153244.png",
#     # "tpl1744186156428.png", "tpl1744186157389.png", "tpl1744186165286.png", "tpl1744186166603.png", "tpl1744186172061.png",
#     # "tpl1744186183518.png"
# ]

# # 去除"tpl"和".png"后缀，得到数字部分
# numbers = [int(f[0:-1]) for f in filenames]

# # 计算新数组：每个数字与前一个数字的差值，再除以1000
# differences = [((numbers[i] - numbers[i-1]) / 1000 ) + 2 for i in range(1, len(numbers))]

# print(differences)