#!/bin/bash

# Define the default folder
default_folder="/home/kym/Pictures"

# Prompt the user for the file path
read -p "Enter the image filename in /Pictures: " filename

# create the full path by appending the filename to the folder
image_path="$default_folder/$filename"

# Check if the file exists
if [ -f "$image_path" ]; then
    # Use gsettings to set the GNOME desktop background
    gsettings set org.gnome.desktop.background picture-uri "file://$image_path"

    # Set the background scaling mode to 'scaled' for no cropping
    gsettings set org.gnome.desktop.background picture-options 'scaled'

    echo "Desktop background updated!"
else
    echo "File not found: $image_path"
fi
