#!/bin/bash
pkill waybar;

while pgrep -x waybar > /dev/null; 
    do sleep 0.1; 
done;

while getopts ":ln" flag;
do
    case "${flag}" in
        l) cd ~/.config/waybar/ && python ./change_theme.py -l;;
        n) cd ~/.config/waybar/ && python ./change_theme.py -n;;
    esac
done