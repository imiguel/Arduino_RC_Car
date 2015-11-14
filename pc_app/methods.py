# -*- coding: utf-8 -*-
import webbrowser
import wx


def aboutDialogMessage(self):
    dialog = wx.MessageDialog(self, "Programa para controlar RC Car\n \n"
                                    "Desenvolvido por: Miguel Rosa\n \n \n \n"
                                    "Todos os direitos reservados\n \n"
                                    "Mértola 2016",
                                    "RC Car Controller - Sobre")
    dialog.ShowModal()#Mostra a caixa de dialogo
    dialog.Destroy() #destroi a caixa de dialogo


def openWebPageFromGitHub():
    linkToPage = "https://github.com/imiguel/Arduino_RC_Car/wiki"
    webbrowser.open_new(linkToPage)