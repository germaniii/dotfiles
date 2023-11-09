#!/bin/bash

# Set the low battery level threshold
low_battery_level=15

# Check if the notify-send command is available
if ! command -v notify-send &> /dev/null; then
    echo "Error: notify-send command not found. Please install it." >&2
    exit 1
fi

# Get the battery level from the first battery found (you can adjust this if needed)
battery_info=$(acpi -b | head -n 1)
battery_level=$(echo "$battery_info" | grep -oP '\d+(?=%)' | tr -d '\n')

# Check if the battery level is not empty and is below the threshold
if [ -n "$battery_level" ] && [ "$battery_level" -le "$low_battery_level" ]
then
    # Display a notification
    notify-send "Battery Low" "Battery level is ${battery_level}%!"
fi

