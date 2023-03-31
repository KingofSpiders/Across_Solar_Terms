import tkinter as tk
import cv2
import os
import sys
from PIL import Image, ImageTk

def opengame():
    os.system("start "+os.getcwd()+"\\Game\\game.exe")
    root.destroy()
    sys.exit()
# 打开视频文件
cap = cv2.VideoCapture("Background.mp4")

# 获取视频帧率
fps = int(cap.get(cv2.CAP_PROP_FPS))

# 创建主窗口
root = tk.Tk()

# 设置窗口标题
root.title("游戏启动器")

# 设置窗口大小
root.geometry("1280x760")

root.resizable(False, False)

# 定义一个函数，用于更新背景图像
def update_background():
    global cap, background_label
    ret, frame = cap.read()
    if ret:
        # 将OpenCV图像转换为PIL图像
        img = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        img = Image.fromarray(img)
        img = img.resize((1280, 760))
        img_tk = ImageTk.PhotoImage(img)
        # 更新背景标签的图像
        background_label.config(image=img_tk)
        background_label.image = img_tk
    # 每隔1/fps秒更新一次背景图像
    root.after(int(1000/fps), update_background)

# 添加背景标签控件
background_label = tk.Label(root)
background_label.pack(fill=tk.BOTH, expand=False)

# 添加按钮控件
button = tk.Button(root, text="开始游戏", font=("楷体", 30), bg="green", fg="white", command=opengame)

button.place(relx=0.5, rely=0.55, anchor=tk.CENTER)

# 开始更新背景图像
update_background()

# 运行主循环
root.mainloop()

# 释放视频文件
cap.release()