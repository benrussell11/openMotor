from PyQt5.QtCore import QObject
from PyQt5.QtWidgets import QFileDialog
from PyQt5.QtCore import pyqtSignal

class Converter(QObject):
    def __init__(self, manager, name, description, fileTypes):
        super().__init__()
        self.manager = manager
        self.name = name
        self.description = description
        self.fileTypes = fileTypes
        self.menu = None

    def getFileTypeString(self):
        return ";;".join([self.fileTypes[key] + " (*" + key + ")" for key in self.fileTypes.keys()])

    def showFileSelector(self):
        pass

    def exec(self):
        pass


class Exporter(Converter):
    def __init__(self, manager, name, description, fileTypes):
        super().__init__(manager, name, description, fileTypes)
        self.requirements = []

    def showFileSelector(self):
        """Open a dialog to pick the file to save to"""
        path = QFileDialog.getSaveFileName(None, 'Export ' + self.name, '', self.getFileTypeString())[0]
        if path == '' or path is None:
            return
        if path[-4:] != '.bsx':
            path += '.bsx'
        return path

    def exec(self):
        fileName = self.showFileSelector()

    def checkRequirements(self):
        for req in self.requirements:
            pass


class Importer(Converter):
    def __init__(self, manager, name, description, fileTypes):
        super().__init__(manager, name, description, fileTypes)

    def showFileSelector(self):
        """Open a dialog to pick the file to load"""
        if self.manager.unsavedCheck():
            path = QFileDialog.getOpenFileName(None, 'Import ' + self.name, '', self.getFileTypeString())[0]
            if path != '':
                return path
        return None

    def doConversion(self, path):
        pass

    def exec(self):
        path = self.showFileSelector()
        if path is not None:
            self.doConversion(path)