# -*- coding: utf-8 -*-
import wx
import methods


class mainWindow(wx.Frame):
    def __init__(self, parent, title):
        wx.Frame.__init__(self, parent, title="RC Car Controler", size=(700,500))

        menuBar = wx.MenuBar(0)

        fileMenu = wx.Menu()
        btn_sair = wx.MenuItem(fileMenu, wx.ID_ANY, "&Sair") #Botao
        fileMenu.AppendItem(btn_sair)
        menuBar.Append(fileMenu, "&Ficheiro")

        fileAbout = wx.Menu()
        btn_sobre = wx.MenuItem(fileAbout, wx.ID_ANY, "S&obre") #Botao
        fileAbout.AppendItem(btn_sobre)
        btn_website = wx.MenuItem(fileAbout, wx.ID_ANY, "&Pagina oficial") #Botao
        fileAbout.AppendItem(btn_website)
        menuBar.Append(fileAbout, "&Sobre")


        '''
        wxglade_tmp_menu = wx.Menu()
        wxglade_tmp_menu.Append(author, _("S&obre"), "", wx.ITEM_NORMAL)
        wxglade_tmp_menu.Append(webpage, _("&Webpage"), "", wx.ITEM_NORMAL)
        self.menubar.Append(wxglade_tmp_menu, _("&Sobre"))
        self.SetMenuBar(self.menubar) '''




        self.SetMenuBar(menuBar)

        self.Show(True)


    ##Metodos das accoes dos botoes



# MAIN
if __name__ == "__main__":
    app = wx.App(False)
    frame = mainWindow(None, "RC Car Controller")
    app.MainLoop()










































############################## GARBAGE ##############################################


'''class MainWindow(wx.Frame):
    def __init__( self, parent, title ):
        wx.Frame.__init__ ( self, parent, title="RC Car Controller", size = wx.Size(700,500) )

        self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )

        menuBar = wx.MenuBar( 0 )
        fileMenu = wx.Menu()
        btnMenu_Sair = wx.MenuItem( self.fileMenu, wx.ID_ANY, "&Sair", wx.EmptyString, wx.ITEM_NORMAL )
        fileMenu.AppendItem( self.btnMenu_Sair )

        menuBar.Append( self.fileMenu, "&Ficheiro" )

        sobreMenu = wx.Menu()
        btnMenu_Sobre = wx.MenuItem( self.sobreMenu, wx.ID_ANY, "S&obre", wx.EmptyString, wx.ITEM_NORMAL )
        sobreMenu.AppendItem( self.btnMenu_Sobre )

        btnMenu_Ajuda = wx.MenuItem( self.sobreMenu, wx.ID_ANY, "F&AQ (Online)", wx.EmptyString, wx.ITEM_NORMAL )
        sobreMenu.AppendItem( self.btnMenu_Ajuda )

        menuBar.Append( self.sobreMenu, "&Sobre" )



        self.SetMenuBar( self.menuBar )
        self.Centre( wx.BOTH )
        ############################



        #adiciona metodos aos botões
        self.Bind(wx.EVT_MENU, self.btnSair_onClick, btnMenu_Sair)
        #self.Bind(wx.EVT_MENU, self.btnSobre_onClick, btnSobre)


        self.Show(True)




    #------------- EVENTOS DE CLICKS NOS BOTOES, ETC ------------------------
    #Termina a aplicação
    def btnSair_onClick(self, event):
        self.Close()

    def btnSobre_onClick(self, event):
        dialog = wx.MessageDialog( self, "Programa para controlar o RC Car\n \nDesenvolvido por: Miguel Rosa");
        dialog.ShowModal() #mostra a caixa dialogo
        dialog.Destroy() #apos terminar, destroi



#Mostra no ecra
if __name__ == "__main__":
    app = wx.App(False)
    frame = MainWindow(None, "RC Car Controller")
    app.MainLoop()
'''