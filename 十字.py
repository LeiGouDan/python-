import pygame
import win32gui
import win32con
import win32api

# 初始化 pygame
pygame.init()

# 获取屏幕的实际宽度和高度
screen_width = win32api.GetSystemMetrics(0)
screen_height = win32api.GetSystemMetrics(1)

# 创建无边框窗口，大小为实际屏幕大小
flags = pygame.NOFRAME
screen = pygame.display.set_mode((screen_width, screen_height), flags)

# 设置窗口标题
pygame.display.set_caption("无边框置顶全屏幕白色透明窗口带红色十字准星，鼠标穿透")

# 定义白色和红色
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# 获取窗口句柄
hwnd = pygame.display.get_wm_info()["window"]

# 将窗口置顶
win32gui.SetWindowPos(hwnd, win32con.HWND_TOPMOST, 0, 0, 0, 0,
                      win32con.SWP_NOMOVE | win32con.SWP_NOSIZE)

# 设置鼠标穿透
win32gui.SetWindowLong(hwnd, win32con.GWL_EXSTYLE,
                       win32gui.GetWindowLong(hwnd, win32con.GWL_EXSTYLE) | win32con.WS_EX_TRANSPARENT)

# 设置白色为透明色
win32gui.SetWindowLong(hwnd, win32con.GWL_EXSTYLE,
                       win32gui.GetWindowLong(hwnd, win32con.GWL_EXSTYLE) | win32con.WS_EX_LAYERED)
win32gui.SetLayeredWindowAttributes(hwnd, win32api.RGB(*WHITE), 0, win32con.LWA_COLORKEY)

# 主循环
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # 按下 ESC 键也可以退出窗口
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False

    # 填充屏幕背景色为白色
    screen.fill(WHITE)

    # 绘制红色十字准星，线条宽度为 1
    pygame.draw.line(screen, RED, (screen_width // 2, 0), (screen_width // 2, screen_height), 1)
    pygame.draw.line(screen, RED, (0, screen_height // 2), (screen_width, screen_height // 2), 1)

    # 更新屏幕显示
    pygame.display.flip()

# 退出 pygame
pygame.quit()