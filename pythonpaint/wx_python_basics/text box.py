import wx

class aaron(wx.Frame):

    def __init__(self,parent,id):
        wx.Frame.__init__(self,parent,id,'frame window',size=(300,200))
        panel=wx.Panel(self)

        box=wx.TextEntryDialog(None, "What is your name?","Title","default text")
        if box.ShowModal ()==wx.ID_OK:
            answer=box.GetValue()


if __name__=='__main__':
    app=wx.PySimpleApp()
    frame=aaron (parent =None, id=-1)
    frame.Show()
    app.MainLoop()
