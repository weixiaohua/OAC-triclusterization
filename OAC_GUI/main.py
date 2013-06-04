from Tkinter import *
import tkFileDialog
from tricl_visual import App, Rect
from OAC_prime import Context
from parse_input import parse_input

def ImpFile(ev):
    fn = tkFileDialog.Open(root, filetypes = [('*.txt files', '.txt')]).show()
    if fn == '':
        return
    textbox.delete('1.0', 'end') 
    global input_context
    input_context = parse_input(open(fn, 'rt'))
    textbox.insert('1.0', 'Context imported successfully.')

def Quit(ev):
    global root
    root.destroy()
    
def StartCalc(ev): 
    min_density = 0.7
    textbox.delete('1.0', 'end') 
    textbox.insert('1.0', 'In process')
    context = Context(input_context)
    Triclusters = context.triclusters(min_density)
    textbox.delete('1.0', 'end') 
    textbox.insert('1.0', Triclusters.values())
    
def Visualize(ev):
    def onObjectClick(event):                  
      print 'Got object click', event.x, event.y,
      print event.widget.find_closest(event.x, event.y)
    canv = Canvas(root, width=300, height=300)
    obj1Id = canv.create_line(0, 30, 100, 30, width=5, tags="obj1Tag")
    obj2Id = canv.create_text(50, 70, text='Click', tags='obj2Tag')
    
    canv.tag_bind(obj1Id, '<ButtonPress-1>', onObjectClick)       
    canv.tag_bind('obj2Tag', '<ButtonPress-1>', onObjectClick)   
    print 'obj1Id: ', obj1Id
    print 'obj2Id: ', obj2Id
    canv.pack()
          
def SaveFile(ev):
    fn = tkFileDialog.SaveAs(root, filetypes = [('*.txt files', '.txt')]).show()
    if fn == '':
        return
    if not fn.endswith(".txt"):
        fn+=".txt"
    open(fn, 'wt').write(textbox.get('1.0', 'end'))

def InitializeWindow(root):
    root.title('Triclusterization')
    
    panelFrame = Frame(root, height = 60, bg = 'gray')

    impBtn = Button(panelFrame, text = 'Import')
    loadBtn = Button(panelFrame, text = 'Start')
    visBtn = Button(panelFrame, text = 'Visualize')
    saveBtn = Button(panelFrame, text = 'Save')
    quitBtn = Button(panelFrame, text = 'Quit')
    impBtn.bind("<Button-1>", ImpFile)
    loadBtn.bind("<Button-1>", StartCalc)
    visBtn.bind("<Button-1>", Visualize)
    saveBtn.bind("<Button-1>", SaveFile)
    quitBtn.bind("<Button-1>", Quit)
    impBtn.grid(row = 0, column = 0 )
    loadBtn.grid(row = 0, column = 1)
    visBtn.grid(row = 0, column = 2)
    saveBtn.grid(row = 0, column = 3)
    quitBtn.grid(row = 0, column = 4)

    panelFrame.pack(side = 'top', fill = 'x')
    canv = Canvas(root, bg = 'black')
    canv.pack(fill = 'both', expand = 1)
    global textbox
    textbox = Text(root, font='Arial 14', wrap='word', width = 60, height = 4)
    textbox.pack(side = 'bottom', fill = 'both', expand = 1)     
    scrollbar = Scrollbar(root)
    scrollbar.pack(side=RIGHT, fill=Y)
    textbox.pack(side=LEFT, fill=Y)
    scrollbar.config(command=textbox.yview)
    textbox.config(yscrollcommand=scrollbar.set)
             
root = Tk()
InitializeWindow(root)
root.mainloop()