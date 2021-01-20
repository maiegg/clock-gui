import tkinter as tk
import time as time

class GUI(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)

        mainLabel = tk.Label(self, font=('consolas', 15), bg='gray27', justify='left',fg='#00FF00')
        self.overrideredirect(1) #Remove border
        # self.wm_attributes("-transparentcolor", "gray27")

        def tick():
            s = time.strftime('%H:%M:%S')
            if s != mainLabel["text"]:
                mainLabel["text"] = s + ' ' + zh + ' ' + en + ' ' + tr
                mainLabel.after(100, tick)

        def fetch_new_word():
            from lxml import html as lxDotHtml
            from lxml import etree
            import html
            import requests
            import json

            # Send request to get the web page
            response = requests.get('https://www.chineseclass101.com/chinese-phrases/')

            # Check if the request succeeded (response code 200)
            if (response.status_code == 200):
                # Parse the html from the webpage
                pagehtml = lxDotHtml.fromstring(response.text)

                # search for news headlines
                zhword = pagehtml.xpath('//*[@id="wotd-widget"]/div[2]/div[1]/div[2]')
                zhword = str(etree.tostring(zhword[0]))
                zhword = zhword.split('>')[1].split(';</')[0]
                zhword = html.unescape(zhword)

                engword = pagehtml.xpath('//*[@id="wotd-widget"]/div[2]/div[2]/div[1]')
                engword = str(etree.tostring(engword[0]))
                engword = engword.split('>')[1].split('</')[0]
                engword = html.unescape(engword)

                trans = pagehtml.xpath('//*[@id="wotd-widget"]/div[2]/div[3]')
                trans = str(etree.tostring(trans[0]))
                trans = trans.split('>')[1].split('</')[0]
                trans = html.unescape(trans)

            return(zhword, engword, trans)



        date_last_fetched = '2019-07-10'

        if time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))[0:10] != date_last_fetched:
            print('fetching new word -',time.ctime())
            zh, en, tr = fetch_new_word()
            date_last_fetched = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))[0:10]

        tick()

        #mainButton = tk.Button(self, text = "Close Window", command = lambda: self.destroy())
        mainLabel.pack()

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
