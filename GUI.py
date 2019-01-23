import os
import tkinter

from tkinter import Label, messagebox, Entry
from blockchain import get_all_blocks, create_new_block, mine, dir_path

class MainWindow:
    def __init__(self):
        self.root = tkinter.Tk()
        self.root.geometry("600x480")
        self.root.configure(background='#888A85')
        self.view()

    def view_file(self, file_name):
        file_name = os.path.join(dir_path, "{}.txt".format(file_name))
        file = open(file_name, "r")
        content = file.read()
        file.close()
        messagebox.showinfo("contents", content)

    def create_file(self, sender, receiver, amount, des):
        create_new_block(sender, receiver, amount, des)
        messagebox.showinfo("success", "Successful!")

    def mine_pressed(self):
        res_list = mine()
        if res_list[0]:
            messagebox.showinfo(
                "success", "All hashes are correct!\nBlockchain give you {} coins.".format(res_list[1]//5+1)
            )
        else:
            messagebox.showerror("danger", "There is a problem with hashes! Blocks are not a chain.")

    def view(self):

        file_list = get_all_blocks(dir_path)

        blocks = tkinter.StringVar()
        blocks.set("Available Blocks: {}".format("".join(x.split(".")[0]+", " for x in file_list)[:-2]))
        # blocks_title = Label(text="Available Blocks: {}".format(blocks.get()), background='#888A85')
        blocks_title = Label(textvariable=blocks, background='#888A85')
        blocks_title.config(font=("Accanthis ADF Std", 12))
        blocks_title.pack()
        blocks_title.place(x=20, y=40)

        file_entry_label = Label(text="Block Name : ", background='#888A85')
        file_entry_label.config(font=("Accanthis ADF Std", 12))
        file_entry_label.pack()
        file_entry_label.place(x=20, y=80)

        v = tkinter.StringVar(value="block")
        file_entry = Entry(textvariable=v)
        file_entry.pack()
        file_entry.place(x=120, y=80, height=25)

        file_entry_button = tkinter.Button(text="View",
                                           font=("Accanthis ADF Std", 12),
                                           command=lambda: self.view_file(file_entry.get())
                                           )
        file_entry_button.pack()
        file_entry_button.place(x=300, y=80, width=100)

        mine_button = tkinter.Button(text="Mine", font=("Accanthis ADF Std", 12), command=self.mine_pressed)
        mine_button.pack()
        mine_button.place(x=420, y=80, width=100)

        new_block_title = Label(text="Create new block:", background='#888A85')
        new_block_title.config(font=("Accanthis ADF Std", 12))
        new_block_title.pack()
        new_block_title.place(x=20, y=140)

        sender_entry_label = Label(text="Sender: ", background='#888A85')
        sender_entry_label.config(font=("Accanthis ADF Std", 12))
        sender_entry_label.pack()
        sender_entry_label.place(x=50, y=200)

        sender_entry = Entry()
        sender_entry.pack()
        sender_entry.place(x=200, y=200, height=25)

        receiver_entry_label = Label(text="Receiver: ", background='#888A85')
        receiver_entry_label.config(font=("Accanthis ADF Std", 12))
        receiver_entry_label.pack()
        receiver_entry_label.place(x=50, y=250)

        receiver_entry = Entry()
        receiver_entry.pack()
        receiver_entry.place(x=200, y=250, height=25)

        amount_entry_label = Label(text="Amount: ", background='#888A85')
        amount_entry_label.config(font=("Accanthis ADF Std", 12))
        amount_entry_label.pack()
        amount_entry_label.place(x=50, y=300)

        amount_entry = Entry()
        amount_entry.pack()
        amount_entry.place(x=200, y=300, height=25)

        description_entry_label = Label(text="Description: ", background='#888A85')
        description_entry_label.config(font=("Accanthis ADF Std", 12))
        description_entry_label.pack()
        description_entry_label.place(x=50, y=350)

        description_entry = Entry()
        description_entry.pack()
        description_entry.place(x=200, y=350, height=25)

        create_block_button = tkinter.Button(text="Create",
                                             font=("Accanthis ADF Std", 12),
                                             command=lambda: self.create_file(sender_entry.get(), receiver_entry.get(),
                                                                              amount_entry.get(),
                                                                              description_entry.get())
                                             )
        create_block_button.pack()
        create_block_button.place(x=450, y=350)

        def task():
            file_list = get_all_blocks(dir_path)
            blocks.set("Available Blocks: {}".format("".join(x.split(".")[0] + ", " for x in file_list)[:-2]))
            self.root.update_idletasks()
            self.root.after(2000, task)

        self.root.after(2000, task)
        self.root.mainloop()


g = MainWindow()