# Theme dispatcher
A simple Theme Dispatcher for waybar which use json.

# installation
You need to have waybar installed.
git clone this repository and move all the scripts in ~/.config/waybar.
``` markdown
cd ~/.config/waybar #create waybar folder if doesn't exist.
mkdir themes #I recommend to create this folder for order purpose!
touch currentTheme.json
touch themeEntries.json
```

Import all your waybar themes in in ~/.config/waybar/themes (all in a directory you know well)
Now your waybar directory will be like:
``` markdown
.waybar
|-->themes
|   |-->theme1dir
|   .-->theme2dir
|
|-->change_theme.py
|-->themeDispatcher.sh
|-->currentTheme.json
|-->themeEntries.json
```

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
In currentTheme you need to specify:
``` markdown
{
    "id": 0,
    "name": "nametheme1",
    "config": "./themes/nametheme1/config",
    "style": "./themes/nametheme1/style.css"
}
```

# workflow and Flags
For now I recommand to use the bash script to interface the program
In future update i'll try to remove it if it's possible.

python script flags
**-l or --load** load the current theme in currentTheme.json
**-n or --next** change to the next theme using **id** in currentTheme.json as index of themeEntries.json.

bash script also use **-n** and **-l** and is useful for waiting waybar death and then change the theme.

# how to use
Complete the installation and write down all your themes in the correct way is explained.
Create a shortcut for your window manager,
For exemple Hyprland:
```markdown
#boot in your last waybar theme used
exec-once = ~/.config/waybar/themeDispatcher.sh -l

#shortcut to change theme (super + Y is an exemple you can choose your own binding)
bind = $mainMod, Y, exec, ~/.config/waybar/themeDispatcher.sh -n
```
