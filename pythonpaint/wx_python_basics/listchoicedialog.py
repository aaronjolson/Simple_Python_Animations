import wx
     

if __name__=='__main__':
    app=wx.PySimpleApp()

    names=['aaron','sarah','caleb','thomas']
    modal=wx.SingleChoiceDialog(None,'what is your name?','Title',names)
    if modal.ShowModal()==wx.ID_OK:
        print 'your name is %s\n' % modal.GetStringSelection()
    modal.Destroy()    

    
