import os
import subprocess
import json
import argparse

def getCurrentTheme():
    with open('currentTheme.json','r') as current:
        return json.load(current)

def setCurrentTheme(theme,id):
    with open('currentTheme.json','w') as saveFile:
        print(theme["name"])
        json.dump({"name":theme["name"],"id":id, "config":theme["config"], "style":theme["style"]},saveFile,indent=4)
        saveFile.flush()
        setThemeToWaybar(theme["config"],theme["style"])
        
def loadThemesEntries():
   with open('themesEntries.json','r') as entries:
    return json.load(entries)

def nextTheme():
    current = getCurrentTheme()
    entries = loadThemesEntries()
    
    id = (current["id"] + 1) % len(entries)
    setCurrentTheme(entries[id],id)

def currentTheme():
    current = getCurrentTheme()
    entries = loadThemesEntries()
    id = current["id"]
    
    setCurrentTheme(entries[id],id) 

def setThemeToWaybar(config, style):
    #subprocess.run(['pkill','waybar'])
    config_path = os.path.expanduser(config)
    style_path = os.path.expanduser(style)

    subprocess.run(['waybar','-c',config_path,'-s',style_path])

def main():

    parser = argparse.ArgumentParser(description="load actual theme or next theme")
    parser.add_argument('-n','--next',help="next theme", action='store_true')
    parser.add_argument('-l','--load',help="load current theme", action='store_true')
    args = parser.parse_args()
    if(args.next):
            
        try:
            nextTheme()
        except Exception as e:
            print(f"Errore: {e}")
        exit()

    if(args.load):
        try:
            currentTheme()
        except Exception as e:
            print(f'errore {e}')
        exit()
    parser.print_help()
    return 0

if __name__ == '__main__':
    main()
