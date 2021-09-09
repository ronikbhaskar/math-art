

# main for the project
# houses the GUI

# imports
from tree import Tree
import tkinter as tk
from tkinter import filedialog
from functools import partial
from math import log

# constants
TITLE_FONT = ("Courier New",30,"bold")
COMPONENT_FONT = ("Courier New",20, "italic")
SLIDER_FONT = ("Courier New",15)
BKG_COLOR = "#77dd77"

class EntryField(tk.Entry):

    def set_color(self):
        print(self.get())
        try:
            print(self.get())
            self.configure(background = self.get())
            #this part keeps the number readable
            if int(self.get()[1:],16) < 3355443:
                self.configure(foreground = "#FFFFFF") # white
            else:
                self.configure(foreground="#000000")  # black
        except:
            pass

    def __init__(self,root,*args,**kwargs):

        tk.Entry.__init__(self,root, width = 7, borderwidth = 2)
        self.grid(columnspan = 1, padx = 10, pady = 10)
        self["font"]=COMPONENT_FONT
        self.configure(background = BKG_COLOR)

class Text(tk.Label):

    def __init__(self,root,*args,**kwargs):

        tk.Label.__init__(self,root,borderwidth = 3,*args,**kwargs)
        self.grid(columnspan = 1, padx = 10, pady = 10)
        self["font"]=COMPONENT_FONT
        self.configure(background=BKG_COLOR)

class Slider(tk.Scale):

    def __init__(self,root,end,*args,**kwargs):

        tk.Scale.__init__(self,root,orient=tk.HORIZONTAL, *args, **kwargs)
        self.grid(columnspan=1, padx=10, pady=10)
        self["font"] = SLIDER_FONT
        self.configure(background=BKG_COLOR)
        self.end = end

    def set_end(self,end):
        self.end = end
        self.configure(to=end)

    def get_end(self):

        return

class Btn(tk.Button):

    def __init__(self,root,*args,**kwargs):

        tk.Button.__init__(self,root,*args,**kwargs)
        self.grid(columnspan=1,padx=20,pady=20)
        self["font"] = COMPONENT_FONT
        self.configure(background=BKG_COLOR)

class TreeGeneratorApp(tk.Tk):

    def create_left_labels(self):
        for i,t in enumerate(["Branches","Proportion","Angle","Layers","Thickness"]):
            lbl = Text(self.frame,text=t)
            lbl.grid(row = i+1, column = 0,sticky="w")
            self.left_labels.append(lbl)

    def create_right_labels(self):
        for i,t in enumerate(["Offset","Color (hex)","Secondary Color (hex)","Transition Layer","Background Color (hex)"]):
            lbl = Text(self.frame,text=t)
            lbl.grid(row = i+1, column = 2,sticky="w", columnspan = 2)
            self.left_labels.append(lbl)

    def update_branches(self):
        self.angle_input.set_end(360 // max(self.branch_input.get(),1))
        self.layer_input.set_end(log(100000,max(self.branch_input.get(),2)))

    def update_layers(self):
        self.transition_input.set_end(self.layer_input.get() + 1)

    def check_colors(self):
        l = None
        try: # checks all the color inputs to confirm validity
            l = tk.Label(self,fg=self.color_input.get())
            l.configure(fg = self.secondary_color_input.get())
            l.configure(fg = self.bkg_input.get())
            self.warnings.configure(text = "")
            del l
            return True
        except:
            self.warnings.configure(text = "Error: Invalid Color(s)")
            del l
            return False

    def generate(self):
        if not self.check_colors():
            return

        #branches, proportion, angle, thickness, color, bkg, color2, offset, layers, transition_branch
        self.tree = Tree(self.branch_input.get(),self.proportion_input.get(),self.angle_input.get(),
                      self.thickness_input.get(),self.color_input.get(),self.bkg_input.get(),
                      self.secondary_color_input.get(),self.offset_input.get(),self.layer_input.get(),
                      self.transition_input.get())

        self.tree.create()

    def save(self):
        try:
            self.tree.save(filedialog.asksaveasfilename())
            self.warnings.configure(text="Saved!")
        except:
            pass

    def __init__(self,*args,**kwargs):

        tk.Tk.__init__(self,*args,**kwargs)

        self.tree = None

        #self.geometry("600x400")
        self.title("Tree Generator")
        self.resizable(False,False)

        self.frame = tk.Frame(self,width=600,height=400)
        self.frame.rowconfigure(0, weight = 1)
        self.frame.columnconfigure(0, weight = 1)
        self.frame.grid(sticky="nesw")
        self.frame.configure(background = BKG_COLOR)

        self.header = Text(self.frame,text = "Tree Generator")
        self.header.grid(row = 0, column = 1, columnspan = 3)
        self.header["font"] = TITLE_FONT

        self.left_labels = []
        self.create_left_labels()
        self.right_labels = []
        self.create_right_labels()


        # left inputs
        self.branch_input = Slider(self.frame,10,from_=0,to=10, command = lambda x: self.update_branches())
        self.branch_input.grid(row = 1, column = 1)
        self.angle_input = Slider(self.frame,10,from_=0,to=360)
        self.angle_input.grid(row = 3, column = 1)
        self.layer_input = Slider(self.frame,10,from_=0,to=10, command = lambda x: self.update_layers())
        self.layer_input.grid(row = 4, column = 1)
        self.proportion_input = Slider(self.frame,10,from_=0,to=0.85, resolution = 0.01)
        self.proportion_input.grid(row = 2, column = 1)
        self.thickness_input = Slider(self.frame, 10, from_=0, to=1, resolution=0.01)
        self.thickness_input.grid(row=5, column=1)

        # right inputs
        self.color_input = EntryField(self.frame)
        self.color_input.grid(row = 2, column = 4)
        self.secondary_color_input = EntryField(self.frame)
        self.secondary_color_input.grid(row=3, column=4)
        self.bkg_input = EntryField(self.frame)
        self.bkg_input.grid(row=5, column=4)
        self.offset_input = Slider(self.frame, 10, from_=0, to=1, resolution=0.01)
        self.offset_input.grid(row=1, column=4)
        self.transition_input = Slider(self.frame, 10, from_=0, to=10)
        self.transition_input.grid(row=4, column=4)

        # bottom widgets
        self.generate_btn = Btn(self.frame, text = "Generate", command = lambda: self.generate())
        self.generate_btn.grid(row = 6, column = 2, columnspan = 2, sticky = "nsew")
        self.save_btn = Btn(self.frame,text = "Save", command = lambda: self.save())
        self.save_btn.grid(row = 6, column = 4, sticky = "nsew")
        self.warnings = Text(self.frame, fg = "#800000", text = "")
        self.warnings.grid(row = 6, column = 0, columnspan = 2, sticky = "nsew")

        self.frame.pack()

# main
def main():
    app = TreeGeneratorApp()
    app.mainloop()

if __name__ == '__main__':
    main()
