import wx

class aaron(wx.Frame):

    def __init__(self,parent,id):
        wx.Frame.__init__(self,parent,id,'window frame',size=(300,200))
        panel=wx.Panel(self)

        accept = wx.TextEntryDialog(None,'What is your name?','Ttile','enter your name')
        if accept.ShowModal()==wx.ID_OK:
            apples=accept.GetValue()

        wx.StaticText(panel,-1, apples, (10,10))



if __name__=='__main__':
    app=wx.PySimpleApp()
    frame=aaron(parent=None,id=-1)
    frame.Show()
    app.MainLoop()
