# Theme dispatcher

# installation
You need to have waybar installed.
git clone this repository and move all the scripts in ~/.config/waybar.
``` markdown
cd ~/.config/waybar #create waybar folder if doesn't exist.
mkdir themes #I recommend to create this folder
touch currentTheme.json
touch themeEntries.json
```
# how to use
Import all your waybar themes in in ~/.config/waybar/themes (all in a directory you know well)
Write in themeEntries.json a list of themes:
``` markdown
[
    {
        "name": "nametheme1",
        "config": "./themes/nametheme1/config",
        "style": "./themes/default/style.css"
    },
    {
        "name":"nametheme2",
        "config":"./themes/nametheme2/config",
        "style":"./themes/nametheme2/style.css"
    }

]
```
In currentTheme:
