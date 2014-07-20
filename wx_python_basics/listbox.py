import wx

class aaron(wx.Frame):

    def __init__(self,parent,id):
        wx.Frame.__init__(self,parent,id,'window frame', size=(300,200))
        panel=wx.Panel(self)

        mylist=['gum','chocolate','beer','bannana','strawberry']
        unit=wx.ListBox(panel,-1,(20,20),(80,60),mylist,wx.LB_SINGLE)
        unit.SetSelection(3)

if __name__=='__main__':
    app=wx.PySimpleApp()
    frame=aaron(parent=None,id=-1)
    frame.Show()
    app.MainLoop()
