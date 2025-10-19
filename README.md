# Disclaimer
Everything except the script code is mine. I used ChatGPT to write the script, given my logic flow and other involved tools

# TierListMaker
Every esport ends up with a community. Smash Ultimate, though a special esport in the grand scheme of things, has a large fanbase. And sometimes, local groups of players who attend the same events will form, and they want to engage in social trends. One of these is the "Group Tier List", which is popular on twitter. This is used to rank groups of people in varying subject matter, but the typical trend is that you rank a lot of important people within a given "region." The website "tiermaker.com" provides the platform to generate such a tier list, but the work of creating an icon for every single person while keeping them all neat is VERY tiresome.

My goal was to fix this issue by coming up with a script that would automate the generation of these icons. You'd still need something to draw from, so I geared this program to read off of a .xlsx file. That way, the user can generate a list of icons depicting a group of players with the least amount of effort possible.

## Room for growth
As smash ultimate has a wide variety of characters and color palettes for those characters, this program has the potential for a lot of expression. I did not write in the room for that level of customization, and as such this output of this program is rather minimal, despite being fully functional.

## Miscellaneous info for use
Before running, install proper dependencies (via pip): pandas, pillow, openpyxl
