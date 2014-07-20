import wx

class aaron(wx.Frame):

    def __init__(self,parent,id):
        wx.Frame.__init__(self,parent,id,'frame window', size=(300,200))
        panel=wx.Panel(self)

        box =wx.SingleChoiceDialog(None,'What is the air speed velocity of a unladen swallow?','Title',['100mph','200mph','what kind of swallow?'])
        if box.ShowModal()==wx.ID_OK:
            answer=box.GetStringSelection()


if __name__=='__main__':
    app=wx.PySimpleApp()
    frame=aaron(parent=None,id=-1)
    frame.Show()
    app.MainLoop()
