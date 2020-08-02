""" DiscBotEmbedTemplate example by zenercurrent

To test the embed output in Discord, hook this to a discord bot.
DBET.fieldgen() is usually for testing purposes as it takes input from console.

Note: database.txt is empty when downloaded. Run example.py for dict to be saved in database.txt
"""

import DiscBotEmbedTemplate as DBET
import json

# Creates basic embed with parameters
embed = DBET.embedtemplate(
    title="title",
    descript="descript",
    url="https://github.com/zenercurrent/discord-embedtemplate",
    name="Name",
    icon="https://www.freepnglogos.com/uploads/discord-logo-png/concours-discord-cartes-voeux-fortnite-france-6.png",
    thumb="https://www.freepnglogos.com/uploads/discord-logo-png/concours-discord-cartes-voeux-fortnite-france-6.png",
    footer="footer"
)

# Adds three fields to the embed (with inline)
fname = ["field1", "field2", "field3"]
fvalue = ["value1", "value2", "value3"]
finline = [True, True, False]
embed = DBET.newfield(embed, fieldno=3, fname=fname, fvalue=fvalue, finline=finline)

# Storing embed to text file
"""
This example saves the embed into a dict() so when extracting embeds from database.txt,
it can be referred as key-value pairs. In this case, the example embed is saved as a value of key "test".
This allows a more organised and readable way to store embeds. 

To get the Embed object back from the dict form, use discord.Embed.from_dict(data)
To remove instances of dict, manually edit the text file and remove the whole line.
"""
path = "database.txt"
store = DBET.EDictFile(file=path, embed=embed)
store.add(prefix="{\"test\": ", suffix="}")

embeddict = dict()
datadump = store.get()
for r in datadump:
    embeddict.update(json.loads(r))
print("embeddict:", embeddict)

# select and get back the Embed object from the dict
extracted_embed = DBET.Embed.from_dict(embeddict["test"])
print("extract success:", extracted_embed.to_dict() == embed.to_dict())
