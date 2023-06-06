import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

import web_manager as wm


def handle_click_button():
    response = wm.access_to_yahoo()
    messagebox.showinfo('アクセス結果', response)


root = tk.Tk()
root.title('オリジナルデスクトップアプリケーション')
root.geometry('500x300')

# ウィジェットをグルーピングするためのコンテナを生成
main_frame = ttk.Frame(root, padding=10)
main_frame.grid()

# ボタンウィジェット作成し、メインフレームに配置
sample_button = tk.Button(main_frame, text='Yahoo! JAPANにアクセス', command=handle_click_button)
sample_button.grid(row=0, column=0)

# プログラム実行中はtkinterオブジェクトを画面上に表示させ続けるためのメソッド
root.mainloop()
