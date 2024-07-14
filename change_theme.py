import os
import subprocess
import json

def getCurrentTheme():
    with open('currentTheme.json','r') as current:
    # current.cloyse()
        return json.load(current)

def setCurrentTheme(theme,id):
    with open('currentTheme.json','w') as saveFile:
        print(theme["name"])
        json.dump({"name":theme["name"],"id":id},saveFile,indent=4)
        setThemeToWaybar(theme["config"],theme["style"])

def loadThemesEntries():
   with open('themesEntries.json','r') as entries:
    return json.load(entries)

def nextTheme():
    current = getCurrentTheme()
    entries = loadThemesEntries()
    
    id = (current["id"] + 1) % len(entries)
    setCurrentTheme(entries[id],id)

def setThemeToWaybar(config, style):
    #subprocess.run(['pkill','waybar'])
    # waybar -c ~/.config/waybar/themes/theme_catputcini/config  -s ~/.config/waybar/themes/theme_catputcini/style.css
    config_path = os.path.expanduser(config)
    style_path = os.path.expanduser(style)

    subprocess.run(['waybar','-c',config_path,'-s',style_path])

def main():
    try:
        nextTheme()
    except Exception as e:
        print(f"Errore: {e}")
    return 0

if __name__ == '__main__':
    main()
