""" Discord Bot Embed Template

Written by Isaac Goh (eyezacker/zenercurrent)
"""

from discord import Embed
import datetime
import json


def embedtemplate(title, descript, url="", name=None, icon=None, thumb=None, footer=None):
    embed = Embed(title=title, description=descript, url=url)
    if (name and icon and thumb) is not None:
        embed = metadata(embed, name, icon, thumb)
    if footer is not None:
        embed = setfooter(embed, footer)
    return embed


def metadata(embed, name, icon, thumb):
    embed.set_author(name=name, icon_url=icon)
    embed.set_thumbnail(url=thumb)
    return embed


# For testing purposes where the input is taken from Python Console
def fieldgen(embed, fieldno, finline_check=False):
    fname, fvalue = list(), list()
    if finline_check:
        finline = list()
    else:
        finline = [False] * fieldno

    for i in range(fieldno):
        fname.append(input(f'name {i + 1}? '))
        fvalue.append(input(f'value {i + 1}? '))
        if finline_check:
            finline.append(input(f'inline {i + 1}? '))

    return newfield(embed, fieldno, fname, fvalue, finline)


def newfield(embed, fieldno, fname, fvalue, finline=False):
    if not finline:
        finline = [False] * fieldno

    for i in range(fieldno):
        embed.add_field(name=fname[i], value=fvalue[i], inline=finline[i])
    return embed


def setfooter(embed, text):
    embed.set_footer(text=text)
    embed.timestamp = datetime.datetime.utcnow()
    return embed


# Storing Embed as Dict in text file:
class EDictFile:

    def __init__(self, file, embed=Embed()):
        self.file = file
        self.embed = embed
        self.edict = json.dumps(Embed.to_dict(embed))

    def get(self):
        dictFile = open(self.file)
        dictList = dictFile.readlines()
        dictFile.close()

        # remove '\n' at end
        for i in range(len(dictList)):
            dictList[i] = dictList[i][::-1].replace("\n", "", 1)[::-1]
        return dictList

    def add(self, prefix="", suffix=""):
        dictFile = open(self.file, "a")
        dictFile.write(prefix + str(self.edict) + suffix + "\n")
        dictFile.close()
        return
        # If edits are necessary, manually access the text file.
