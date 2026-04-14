import tkinter as tk
from tokenize import group

def init_label_frame(frm: tk.Frame):
    labels = []
    # 生成3x3的Label
    for i in range(0,3):
        for j in range(0,3):
            label = tk.Label(frm, text=f"label{i}_{j}")
            labels.append(label)
            label.grid(row=i, column=j)
    return labels

def init_button_frame(frm: tk.Frame):
    buttons = []
    for i in range(0,3):
        for j in range(0,3):
            button = tk.Button(frm, text=f"button{i}_{j}")
            buttons.append(button)
            button.grid(row=i, column=j)
    return buttons

def init_entry_frame(frm: tk.Frame):
    entries = []
    for i in range(0,3):
        entry = tk.Entry(frm, width=30)
        entries.append(entry)
        entry.pack(pady=5)
    return entries

def init_text_frame(frm: tk.Frame):
    text = tk.Text(frm, width=40, height=10)
    text.pack(padx=5, pady=5)
    return text

def init_check_box_frame(frm: tk.Frame):
    check_buttons = []
    for i in range(0,4):
        for j in range(0,3):
            check_button = tk.Checkbutton(frm, text=f"checkbutton{i}_{j}")
            check_buttons.append(check_button)
            check_button.grid(row=i, column=j)
    return check_buttons

def init_radio_box_frame(frm: tk.Frame, bind_var):
    radio_buttons = []
    for i in range(0,4):
        for j in range(0,3):
            radio_button = tk.Radiobutton(frm, text=f"radiobutton{i}_{j}", variable=bind_var, value=f"{i}_{j}")
            radio_buttons.append(radio_button)
            radio_button.grid(row=i, column=j)
    return radio_buttons

def init_list_box_frame(frm: tk.Frame):
    list_box = tk.Listbox(frm, width=40, height=8)
    list_box.pack()
    for item in ['apple', 'banana', 'origin', 'watermelon', 'pear']:
        list_box.insert(tk.END, item)
    return list_box

def init_spin_box_frame(frm: tk.Frame):
    spin_boxes = []
    for i in range(0, 3):
        spin_box = tk.Spinbox(frm, from_=0, to=100, increment=1)
        spin_boxes.append(spin_box)
        spin_box.pack(pady=5)
    return spin_boxes

# 主窗口
root = tk.Tk()
root.grid()     # 使用grid布局
root.title('tk基础组件展示')

label_frame = tk.Frame(root)
button_frame = tk.Frame(root)
entry_frame = tk.Frame(root)
text_frame = tk.Frame(root)
check_button_frame = tk.Frame(root)
radio_button_frame = tk.Frame(root)
list_box_frame = tk.Frame(root)
spin_box_frame = tk.Frame(root)

# 初始化labels frame
labels_ret: list = init_label_frame(label_frame)
label_frame.grid(row=0, column=0, padx=30, pady=30)

# button frame
buttons_ret: list = init_button_frame(button_frame)
button_frame.grid(row=0, column=1, padx=30, pady=30)

entries_ret: list = init_entry_frame(entry_frame)
entry_frame.grid(row=0, column=2, padx=30, pady=30)

text_ret: tk.Text = init_text_frame(text_frame)
text_frame.grid(row=1, column=0, padx=30, pady=30)

check_box_ret: list = init_check_box_frame(check_button_frame)
check_button_frame.grid(row=1, column=1, padx=30, pady=30)

var = tk.StringVar(value="0_0")
radio_box_ref: list = init_radio_box_frame(radio_button_frame, var)
radio_button_frame.grid(row=1, column=2, padx=30, pady=30)

list_box_ref = init_list_box_frame(list_box_frame)
list_box_frame.grid(row=2, column=0, padx=30, pady=30)


spin_box_ref = init_spin_box_frame(spin_box_frame)
spin_box_frame.grid(row=2, column=1, padx=30, pady=30)



# label Frame
label_frame = tk.LabelFrame(root, text="个人信息", padx=30, pady=30)
label_frame.grid(row=2, column=2, padx=30, pady=30)
## label frame内部组件
label1 = tk.Label(label_frame, text="姓名: ")
label1.grid(row=1, column=0, sticky="w")
entry2 = tk.Entry(label_frame)
entry2.grid(row=1, column=1, padx=5)

label2 = tk.Label(label_frame, text="身份证: ")
label2.grid(row=2, column=0, sticky="w")
entry3 = tk.Entry(label_frame)
entry3.grid(row=2, column=1, padx=5)

label3 = tk.Label(label_frame, text="签名: ")
label3.grid(row=3, column=0, sticky="w")
text4 = tk.Text(label_frame, height=10, width=20)
text4.grid(row=3, column=1, padx=5)

submit_button = tk.Button(label_frame, text="提交")
submit_button.grid(row=4, column=0, columnspan=2, padx=5, pady=20)

root.mainloop()

