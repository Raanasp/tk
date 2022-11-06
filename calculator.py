from tkinter import *
cal = Tk()
cal.title("Calculator")
operator = ""
text_input = StringVar()
txtDisplay = Entry(cal, font=('arial', 20, 'bold'), textvariable=text_input, bd=30,
                   insertwidth=4, bg='powder blue', justify='right').grid(columnspan=4)
btn7 = Button(cal, padx=16, pady=16, bd=8, fg='black', font=('arial', 20, 'bold'),
              text='7').grid(row=1, column=0)
cal.mainloop()