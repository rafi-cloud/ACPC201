# Week 11 Lab - GUI Programming
# Rafi Miazi (K250249)

import time
import tkinter
import tkinter.messagebox
BG = "#b5fbfd"
ACCENT = '#1f3864'
TITLE_FONT = ('Segoe UI', 16, 'bold')
LABEL_FONT = ('Segoe UI', 11)
ENTRY_FONT = ('Segoe UI', 12)
RESULT_FONT = ('Segoe UI', 14, 'bold')


class AdditionGUI:
    def __init__(self):
        self.main_window = tkinter.Tk()
        self.main_window.title('Addition Calculator')
        self.main_window.geometry('420x300')      
        self.main_window.resizable(False, False)  
        self.main_window.config(bg=BG)


        self.title_frame = tkinter.Frame(self.main_window, bg=BG)
        self.first_frame = tkinter.Frame(self.main_window, bg=BG)
        self.second_frame = tkinter.Frame(self.main_window, bg=BG)
        self.third_frame = tkinter.Frame(self.main_window, bg=BG)
        self.fourth_frame = tkinter.Frame(self.main_window, bg=BG)


        self.title_label = tkinter.Label(self.title_frame, text='Addition Calculator',
                                         font=TITLE_FONT, fg=ACCENT, bg=BG)
        self.title_label.pack()

        # Row 1 - first number to be added
        self.label1 = tkinter.Label(self.first_frame, text='First number:',
                                    font=LABEL_FONT, bg=BG, width=14, anchor='w')
        self.entry1 = tkinter.Entry(self.first_frame, width=14, font=ENTRY_FONT,
                                    relief='solid', bd=1)
        self.label1.pack(side='left')
        self.entry1.pack(side='left', ipady=4)

        # Row 2 - second number to be added
        self.label2 = tkinter.Label(self.second_frame, text='Second number:',
                                    font=LABEL_FONT, bg=BG, width=14, anchor='w')
        self.entry2 = tkinter.Entry(self.second_frame, width=14, font=ENTRY_FONT,
                                    relief='solid', bd=1)
        self.label2.pack(side='left')
        self.entry2.pack(side='left', ipady=4)

        # Row 3 - showing result
        self.label3 = tkinter.Label(self.third_frame, text='Total:',
                                    font=LABEL_FONT, bg=BG, width=14, anchor='w')
        self.value = tkinter.StringVar()
        self.label4 = tkinter.Label(self.third_frame, textvariable=self.value,
                                    font=RESULT_FONT, fg=ACCENT, bg='white',
                                    relief='sunken', bd=1, width=12)
        self.label3.pack(side='left')
        self.label4.pack(side='left', ipady=6)

        # Row 4, the button with commands to run on click
        self.calc_button = tkinter.Button(self.fourth_frame, text='Add',
                                          font=LABEL_FONT, width=10,
                                          bg=ACCENT, fg='white',
                                          activebackground='#2f4f8f',
                                          activeforeground='white',
                                          relief='flat', cursor='hand2',
                                          command=self.add_numbers)
        self.quit_button = tkinter.Button(self.fourth_frame, text='Quit',
                                          font=LABEL_FONT, width=10,
                                          relief='flat', cursor='hand2',
                                          command=self.main_window.destroy)
        self.calc_button.pack(side='left', padx=6, ipady=3)
        self.quit_button.pack(side='left', padx=6, ipady=3)

        
        self.title_frame.pack(pady=(24, 18))
        self.first_frame.pack(padx=20, pady=8)
        self.second_frame.pack(padx=20, pady=8)
        self.third_frame.pack(padx=20, pady=(18, 8))
        self.fourth_frame.pack(pady=20)

        
        tkinter.mainloop()

    # the method for the actual addition operation
    def add_numbers(self):
        start = time.perf_counter()
        try:
            num1 = float(self.entry1.get())
            num2 = float(self.entry2.get())
            total = num1 + num2
            self.value.set(total)
            elapsed = time.perf_counter() - start
            print('Total:', total, '| Execution time:', round(elapsed, 6), 'seconds')
        except ValueError:
            tkinter.messagebox.showerror('Error', 'Please enter numbers only.')


if __name__ == '__main__':
    addition_gui = AdditionGUI()