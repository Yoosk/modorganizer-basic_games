# -*- encoding: utf-8 -*-

from PyQt5.QtCore import QDir, QFileInfo, QStandardPaths

import mobase

from ..basic_game import BasicGame


class SsfeGame(BasicGame):
    Name = "Serious Sam Classic The First Encounter"
    Author = "Yoosk"
    Version = "1.0.0a"
    Description = "High-adrenaline single-play and 16-player co-operative arcade-action FPS"

    GameName= "Serious Sam Classic The First Encounter"
    GameShortName = "ssfe"
    GameBinary = "bin/SeriousSam.exe"
    GameDataPath = ""
    GameSaveExtension = "des"
    GameSteamId = "41050"

    def savesDirectory(self):
        return QDir(self.documentsDirectory().absoluteFilePath("SaveGame"))

    def executables(self):
        return [
            mobase.ExecutableInfo(
                "Serious Sam Classic The First Encounter", QFileInfo(self.gameDirectory(), "bin/serioussam.exe")
            ),
            mobase.ExecutableInfo(
                "Serious Editor", QFileInfo(self.gameDirectory(), "bin/SeriousEditor.exe")
            ),
            mobase.ExecutableInfo(
                "Serious Modeler", QFileInfo(self.gameDirectory(), "bin/SeriousModeler.exe")
            ),
            mobase.ExecutableInfo(
                "Dedicated Server", QFileInfo(self.gameDirectory(), "bin/DedicatedServer.exe")
            ),
        ]