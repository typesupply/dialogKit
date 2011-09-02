from AppKit import NSModalPanelWindowLevel
from vanilla import Window as _Window
from vanilla import TextBox, EditText, Button, PopUpButton, List, CheckBox, HorizontalLine, VerticalLine


__all__ = ['ModalDialog', 'Button', 'TextBox', 'EditText', 'PopUpButton', 'List', 'CheckBox', 'HorizontalLine', 'VerticalLine']


class ModalDialog(_Window):

    nsWindowLevel = NSModalPanelWindowLevel

    def __init__(self, posSize, title=None, okText="OK", cancelText="Cancel", okCallback=None, cancelCallback=None):
        if title is None:
            title = ''
        super(ModalDialog, self).__init__(posSize, title, minSize=None, maxSize=None,
                textured=False, autosaveName=None, closable=False)
        self._okCallback = okCallback
        self._cancelCallback = cancelCallback
        #
        self._bottomLine = HorizontalLine((10, -50, -10, 1))
        self._okButton = Button((-85, -35, 70, 20), okText, callback=self._internalOKCallback)
        self._cancelButton = Button((-165, -35, 70, 20), cancelText, callback=self._internalCancelCallback)
        self.setDefaultButton(self._okButton)
        self._cancelButton.bind('.', ['command'])
        if len(posSize) == 2:
            self.center()

    def open(self):
        app = NSApp()
        self._modalSession = app.beginModalSessionForWindow_(self.getNSWindow())
        app.runModalSession_(self._modalSession)

    def close(self):
        app = NSApp()
        app.endModalSession_(self._modalSession)
        w = self.getNSWindow()
        w.orderOut_(None)
        w.autorelease()

    def _internalOKCallback(self, sender):
        self.close()
        if self._okCallback is not None:
            self._okCallback(self)

    def _internalCancelCallback(self, sender):
        self.close()
        if self._cancelCallback is not None:
            self._cancelCallback(self)

