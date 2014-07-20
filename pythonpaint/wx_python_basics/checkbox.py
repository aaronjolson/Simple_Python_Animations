import wx

class aaron(wx.Frame):

    def __init__(self,parent,id):
        wx.Frame.__init__(self,parent,id,'window frame', size=(300,200))
        panel=wx.Panel(self)

        wx.CheckBox(panel, -1,'apples',(20,20), (160,-1))
        wx.CheckBox(panel, -1,'pineapples',(20,40), (160,-1))
        wx.CheckBox(panel, -1,'kiwi',(20,60), (160,-1))
        
      

if __name__=='__main__':
    app=wx.PySimpleApp()
    frame=aaron(parent=None,id=-1)
    frame.Show()
    app.MainLoop()
