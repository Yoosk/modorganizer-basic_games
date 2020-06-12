# Mod Organizer 2 - Simple Games Plugin

Mod Organizer 2 meta-plugin to make creating game plugins easier and faster.

## Why?

In order to create a MO2 game plugin, one must implements the `IPluginGame` interface.
This interface was initially designed for Bethesda games such as the Elder Scrolls or 
Fallout series and thus contains a lot of things that are irrelevant for most games.

The goal of this meta-plugin is to allow creating game plugins for "basic" games by
providing a very simple `.ini` file or a very simple python class.

## How to install?

Download [the archive](https://github.com/Holt59/modorganizer-basic_games/archive/master.zip)
and extract it directly into your MO2 `plugins` folder.

**Important:** Extract the *folder* in your `plugins` folder, not the individual files. Your
`plugins` folder should look like this:

```
dlls/
plugins/
  data/
  modorganizer-basic_games-master/
    games/
      __init__.py
      ...
    __init__.py
    basic_game.py
    ...
  bsa_extractor.dll
  ...
ModOrganizer.exe
```

You can rename `modorganizer-basic_games-master` to whatever you want (e.g., `basic_games`).

**Note:** You can also clone this repository in your `plugins/` folder:
```
cd $MO2_PATH/plugins
git clone https://github.com/Holt59/modorganizer-basic_games basic_games
```

## Supported games

| Game | File | Extras |
|------|------|--------|
| The Witcher 3 | [`game_witcher3.py`](games/game_witcher3.py) | <ul><li>steam detection</li><li>save game preview</li></ul> |
| Stardew Valley | [`game_stardew_valley.py`](games/game_stardew_valley.py) | <ul><li>steam detection</li></ul> |

## How to add a new game?

You can create a plugin by providing a python class or a `.ini` file in the `games`
folder.

**Note:** If your game plugin does not load properly, you should set the log level
to debug and look at the `mo_interface.log` file.

### Using a `.ini` file

You simply need to createa your `game_XX.ini` file in the `games` folder with the following
content (see below for the full list of supported attributes):

```ini
[DEFAULT]
# Plugin details - this is the name of the plugin, not the name of the game!
Name=Witcher 3 Support Plugin
Author=Holt59
Version=1.0.0

# Game details:
GameName=The Witcher 3
GameShortName=witcher3
GameBinary=bin/x64/witcher3.exe
GameDataPath=mods
GameSaveExtension=sav
GameSteamId=292030
```

### Using a Python file

You need to create a class that inherits `BasicGame` and put it in a `game_XX.py` in `games`.
Below is an example for The Witcher 3 (see also [games/game_witcher3.py](games/game_witcher3.py)):

```python
from PyQt5.QtCore import QDir
from ..basic_game import BasicGame


class Witcher3Game(BasicGame):

    Name = "Witcher 3 Support Plugin"
    Author = "Holt59"
    Version = "1.0.0a"

    GameName = "The Witcher 3"
    GameShortName = "witcher3"
    GameBinary = "bin/x64/witcher3.exe"
    GameDataPath = "Mods"
    GameSaveExtension = "sav"
    GameSteamId = 292030

    def savesDirectory(self):
        return QDir(self.documentsDirectory().absoluteFilePath("gamesaves"))
```

`BasicGame` inherits `IPluginGame` so you can override methods if you need to.
Each attribute you provide corresponds to a method (e.g., `Version` corresponds
to the `version` method, see the table below). If you override the method, you do
not have to provide the attribute:

```python
from PyQt5.QtCore import QDir
from ..basic_game import BasicGame

import mobase


class Witcher3Game(BasicGame):

    Name = "Witcher 3 Support Plugin"
    Author = "Holt59"

    GameName = "The Witcher 3"
    GameShortName = "witcher3"
    GameBinary = "bin/x64/witcher3.exe"
    GameDataPath = "Mods"
    GameSaveExtension = "sav"
    GameSteamId = 292030

    def version(self):
        # Don't forget to import mobase!
        return mobase.VersionInfo(1, 0, 0, mobase.ReleaseType.final)

    def savesDirectory(self):
        return QDir(self.documentsDirectory().absoluteFilePath("gamesaves"))
```

### List of valid keys

If the column `Ini` is empty, it means it only accepts a basic string.

| Name | Description | `IPluginGame` method | Python | Ini |
|------|-------------|----------------------|--------|-----|
| Name | Name of the plugin | `name` | `str` | |
| Author | Author of the plugin | `author` | `str` | |
| Version | Version of the plugin | `version` | `str` or `mobase.VersionInfo` | |
| Description| Description (Optional) | `description` | `str` | `str` |
| GameName | Name of the game, as displayed by MO2 | `gameName` | `str` | |
| GameShortName | Short name of the game | `gameShortName` | `str` | |
| GameNexusName| Nexus name of the game (Optional, default to `GameShortName`) | `gameNexusName` | `str` | |
| GameValidShortNames | Other valid short names (Optional) | `validShortNames` | `List[str]` or comma-separated list of values | comma-separated list of values |
| GameNexusId | Nexus ID of the game (Optional) | `nexusGameID` | `str` or `int` | |
| GameBinary | Name of the game executable, relative to the game path | `binaryName` | `str` | |
| GameLauncher | Name of the game launcher, relative to the game path  (Optional) | `getLauncherName` | `str` | |
| GameDataPath | Name of the folder containing mods, relative to game folder| `dataDirectory` | | |
| GameSaveExtension | Save file extension (Optional) `savegameExtension` | `str` | |
| GameSteamId | Steam ID of the game (Optional) | `steamAPPId` | `str` | |

## Extra features

The meta-plugin provides some useful extra feature:

1. **Automatic Steam game detection:** If you provide a Steam ID for the game (via `GameSteamId` or by 
  overriding `steamAPPId()`), the game will be listed in the list of available games when creating a new
  MO2 instance (if the game is installed via Steam).
2. **Basic save game preview:** If you use the Python version, and if you can easily obtain a picture (file) 
  for any saves, you can provide basic save-game preview by using the `BasicGameSaveGameInfo`. 
  See [games/game_witcher3.py](games/game_witcher3.py) for  more details.
