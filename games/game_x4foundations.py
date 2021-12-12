from ..basic_game import BasicGame

class X4FoundationsGame(BasicGame):

    Name = "X4: Foundations Support Plugin"
    Author = "Katherine1"
    Version = "1.0.0"

    GameName = "X4: Foundations"
    GameShortName = "x4foundations"
    GameValidShortNames = ["x4"]
    GameNexusName = "x4foundations"
    GameNexusId = 2659
    GameSteamId = [392160]
    GameGogId = [1395669635, 1636239177, 1897444972, 1238357884, 1315103966, 1811185500]
    GameBinary = "X4.exe"
    GameDataPath = "extensions"
    GameSaveExtension = "gz" #can also be an uncompressed xml, but gz compressed is the default.
    GameDocumentsDirectory = "%DOCUMENTS%/Egosoft"
    GameSavesDirectory = "%GAME_DOCUMENTS%/X4/save"