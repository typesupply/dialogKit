from AppKit import *
from vanilla import Window as _Window
from vanilla import List as _List
from vanilla import PopUpButton as _PopUpButton
from vanilla import TextBox, EditText, Button, CheckBox, HorizontalLine, VerticalLine


__all__ = ['ModalDialog', 'Button', 'TextBox', 'EditText', 'PopUpButton', 'List', 'CheckBox', 'HorizontalLine', 'VerticalLine']


class ModalDialog(_Window):

    nsWindowLevel = NSModalPanelWindowLevel

    def __init__(self, posSize, title=None, okText="OK", cancelText="Cancel", okCallback=None, cancelCallback=None):
        if title is None:
            title = ''
        super(ModalDialog, self).__init__(posSize, title, minSize=None, maxSize=None,
                textured=False, autosaveName=None, closable=False)
        window = self.getNSWindow()
        self._window.standardWindowButton_(NSWindowCloseButton).setHidden_(True)       
        self._window.standardWindowButton_(NSWindowZoomButton).setHidden_(True)
        self._window.standardWindowButton_(NSWindowMiniaturizeButton).setHidden_(True)

        self._okCallback = okCallback
        self._cancelCallback = cancelCallback

        self._bottomLine = HorizontalLine((10, -50, -10, 1))
        self._okButton = Button((-85, -35, 70, 20), okText, callback=self._internalOKCallback)
        self._cancelButton = Button((-165, -35, 70, 20), cancelText, callback=self._internalCancelCallback)
        self.setDefaultButton(self._okButton)
        self._cancelButton.bind('.', ['command'])
        if len(posSize) == 2:
            self.center()

    def open(self):
        super(ModalDialog, self).open()
        NSApp().runModalForWindow_(self.getNSWindow())

    def close(self):
        super(ModalDialog, self).close()
        NSApp().stopModal()

    def _internalOKCallback(self, sender):
        self.close()
        if self._okCallback is not None:
            self._okCallback(self)

    def _internalCancelCallback(self, sender):
        self.close()
        if self._cancelCallback is not None:
            self._cancelCallback(self)


class List(_List):

    def __init__(self, posSize, items, callback=None):
        super(List, self).__init__(posSize, items=items, selectionCallback=callback)


class PopUpButton(_PopUpButton):

    def setSelection(self, value):
        super(PopUpButton, self).set(value)

    def getSelection(self):
        return super(PopUpButton, self).get()

