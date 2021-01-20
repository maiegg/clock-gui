import tkinter as tk
import time


class GUI(tk.Tk):
    def __init__(self):
       
        tk.Tk.__init__(self)

        
        mainLabel = tk.Label(self, font=('Helvetica', 50), bg='gray27', fg='#e64a2e')#ffcc66'
        # secondLabel = tk.Label(self, font=('Helvetica',35),bg='gray27', fg='#e64a2e')
        self.overrideredirect(1) #Remove border
        self.wm_attributes("-transparentcolor", "gray27")

        # secondLabel["text"] = 'hello world'

        def tick():
            s = time.strftime('%H:%M:%S')
            if s != mainLabel["text"]:
                mainLabel["text"] = s
            mainLabel.after(100, tick)
        tick()

        #mainButton = tk.Button(self, text = "Close Window", command = lambda: self.destroy())
        mainLabel.pack()
        # secondLabel.pack()

        #mainButton.pack()

        self.withdraw()
        self.update_idletasks() 

        x = (self.winfo_screenwidth() - self.winfo_reqwidth()) / 50
        y = (self.winfo_screenheight() - self.winfo_reqheight()) * 0.95
        self.geometry("+%d+%d" % (x, y))

# This seems to draw the window frame immediately, so only call deiconify()
# after setting correct window position
        self.deiconify()
        self.attributes("-topmost", True)

gui = GUI()
gui.mainloop()