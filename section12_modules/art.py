from pyfiglet import figlet_format
from termcolor import colored

def print_art(message, color): 
  # Check for actual colors.
  valid_colors = ["grey", "red", "green", "yellow", "blue", "magenta", "cyan", "white"]

  if color not in valid_colors:
    color = "magenta"

  art = figlet_format(message)
  colored_art = colored(art, color=color)
  print(colored_art)

message = input("What message do you want to print? ")
color = input("And in what color? ")
print_art(message, color)