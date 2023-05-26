# GUIを作成することができるPythonの標準モジュール
import tkinter as tk
from tkinter import ttk

# tkinterのオブジェクトを生成
root = tk.Tk()

# 画面のタイトルを設定
root.title('オリジナルデスクトップアプリケーション')

# 画面のサイズを設定
root.geometry('500x300')

# ウィジェットをグルーピングするためのコンテナを生成
main_frame = ttk.Frame(root, padding=10)
main_frame.grid()

# ボタンウィジェット作成し、メインフレームに配置
sample_button = tk.Button(main_frame, text='サンプルボタン')
sample_button.grid(row=0, column=0)

# プログラム実行中はtkinterオブジェクトを画面上に表示させ続けるためのメソッド
root.mainloop()
