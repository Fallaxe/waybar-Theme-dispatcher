#!/bin/bash
pkill waybar; 
while pgrep -x waybar > /dev/null; 
    do sleep 0.1; 
done; 
cd ~/.config/waybar/ && python ./change_theme.py