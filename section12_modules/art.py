import pyfiglet
from termcolor import colored

message = print(input("What message do you want to print? "))
color = print(input("And in what color? "))

# Check for actual colors.
valid_colors = ["grey", "red", "green", "yellow", "blue", "magenta", "cyan", "white"]

if color not in valid_colors:
  color = "magenta"

art = pyfiglet.figlet_format(message)
colored_art = colored(art, color=color)

print(colored_art)