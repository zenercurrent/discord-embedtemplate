# discord-embedtemplate
discord bot embed builder that provides an easier way to create embeds
and has an additional feature to save them for usage later on. 

<hr>

### Dependencies
- discord

`pip install discord` or `pip install -r requirements.txt`

<hr>

### Examples
Creating a simple Embed that the bot can send to Discord.
```python
import DiscBotEmbedTemplate as DBET

embed = DBET.embedtemplate(
    title="title",
    descript="descript",
    url="https://github.com/zenercurrent/discord-embedtemplate",
    name="Name",
    icon="https://cdn.discordapp.com/attachments/720986344020508892/739479274922442792/unknown.png",
    thumb="https://cdn.discordapp.com/attachments/720986344020508892/739479274922442792/unknown.png",
    footer="footer"
)
```
<img src=https://cdn.discordapp.com/attachments/720986344020508892/739479274922442792/unknown.png width="300" alt="Example Embed">

More in-depth examples are provided and can be found in the examples folder. 

<hr>

### Usage
Saving an Embed object as a dict into a text file for easy accessibility.
Added bonus if saved as a json format for more organised extraction.
```python
store = DBET.EDictFile(file=path, embed=embed)
store.add(prefix="{\"test2\": ", suffix="}")
``` 

<img src=https://cdn.discordapp.com/attachments/720986344020508892/739482307001319434/unknown.png width="300" alt="database.txt">

Examples also show how to add and get these values.

<hr>