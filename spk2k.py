import tkinter as tk
from tkinter import ttk , font


def update_result(*args):
    try:
        frame_rate = float(frame_rate_entry.get())
        fps_text = fps_entry.get()
        seconds_text = seconds_entry.get()
        frames_text = frames_entry.get()

        if fps_text:
            fps = float(fps_text)
            total_seconds = fps / frame_rate
            seconds = int(total_seconds)
            frames = round((total_seconds - seconds) * frame_rate)
            result.set(f"{seconds} + {int(frames)} k")
        elif seconds_text or frames_text:
            seconds = int(seconds_text) if seconds_text else 0
            frames = int(frames_text) if frames_text else 0
            total_fps = seconds * frame_rate + frames
            result.set(f"{int(total_fps)} k")
    except ValueError:
        result.set("请输入有效的数值。")

# 创建主窗口
root = tk.Tk()
root.title("帧秒转换")

# 创建输入框和标签
frame_rate_label = ttk.Label(root, text="FPS:")
frame_rate_label.grid(column=0, row=0, padx=5, pady=5)
frame_rate_entry = ttk.Entry(root)
frame_rate_entry.grid(column=1, row=0, padx=5, pady=5)
frame_rate_entry.insert(0, "24")

fps_label = ttk.Label(root, text="帧数 (k):")
fps_label.grid(column=0, row=1, padx=5, pady=5)
fps_entry = ttk.Entry(root)
fps_entry.grid(column=1, row=1, padx=5, pady=5)

seconds_label = ttk.Label(root, text="秒数:")
seconds_label.grid(column=0, row=2, padx=5, pady=5)
seconds_entry = ttk.Entry(root)
seconds_entry.grid(column=1, row=2, padx=5, pady=5)

frames_label = ttk.Label(root, text="帧数:")
frames_label.grid(column=0, row=3, padx=5, pady=5)
frames_entry = ttk.Entry(root)
frames_entry.grid(column=1, row=3, padx=5, pady=5)

# 创建结果显示标签
result = tk.StringVar()
result_font = font.Font(size=30)  # 只设置字号
result_label = ttk.Label(root, textvariable=result, font=result_font)
result_label.grid(column=0, row=4, columnspan=4, padx=5, pady=5)

# 绑定事件
frame_rate_entry.bind("<KeyRelease>", update_result)
fps_entry.bind("<KeyRelease>", update_result)
seconds_entry.bind("<KeyRelease>", update_result)
frames_entry.bind("<KeyRelease>", update_result)

# 运行主循环
root.mainloop()
