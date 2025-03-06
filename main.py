import argparse
import json
import os

from app.functions import get_lyrics, transform_to_technical_prose

CONFIG_FILE = "config.json"

ASCII_ART = r'''
SongReWriter

  /$$$$$$                                /$$$$$$$            /$$      /$$           /$$   /$$                        
 /$$__  $$                              | $$__  $$          | $$  /$ | $$          |__/  | $$                        
| $$  \__/  /$$$$$$  /$$$$$$$   /$$$$$$ | $$  \ $$  /$$$$$$ | $$ /$$$| $$  /$$$$$$  /$$ /$$$$$$    /$$$$$$   /$$$$$$ 
|  $$$$$$  /$$__  $$| $$__  $$ /$$__  $$| $$$$$$$/ /$$__  $$| $$/$$ $$ $$ /$$__  $$| $$|_  $$_/   /$$__  $$ /$$__  $$
 \____  $$| $$  \ $$| $$  \ $$| $$  \ $$| $$__  $$| $$$$$$$$| $$$$_  $$$$| $$  \__/| $$  | $$    | $$$$$$$$| $$  \__/
 /$$  \ $$| $$  | $$| $$  | $$| $$  | $$| $$  \ $$| $$_____/| $$$/ \  $$$| $$      | $$  | $$ /$$| $$_____/| $$      
|  $$$$$$/|  $$$$$$/| $$  | $$|  $$$$$$$| $$  | $$|  $$$$$$$| $$/   \  $$| $$      | $$  |  $$$$/|  $$$$$$$| $$      
 \______/  \______/ |__/  |__/ \____  $$|__/  |__/ \_______/|__/     \__/|__/      |__/   \___/   \_______/|__/      
                               /$$  \ $$                                                                             
                              |  $$$$$$/                                                                             
                               \______/   
'''


def load_config():
	"""Loads configuration from the config file or creates default settings."""
	if os.path.exists(CONFIG_FILE):
		with open(CONFIG_FILE, "r") as file:
			return json.load(file)
	else:
		return {"first_run": True, "show_banner": True}

def save_config(config):
	"""Saves configuration settings to the config file."""
	with open(CONFIG_FILE, "w") as file:
		# noinspection PyTypeChecker
		json.dump(config, file, indent=4)

# noinspection PyUnboundLocalVariable
def main():
	parser = argparse.ArgumentParser(description="Convert song lyrics into technical prose.")
	parser.add_argument("--title", "-t", type=str, help="Song title for automatic generation")
	parser.add_argument("--artist", "-a", type=str, help="Artist name for automatic generation")
	parser.add_argument("--input", "-i", type=str, help="Manually enter song lyrics")
	parser.add_argument("--mode", "-m", type=str,
						choices=["scientific", "bureaucratic", "engineering", "military", "medical"],
						default="scientific", help="Select transformation mode")
	parser.add_argument("--no-banner", action="store_true", help="Disable ASCII art banner")
	parser.add_argument("--show-banner", action="store_true", help="Enable ASCII art banner")

	args = parser.parse_args()

	config = load_config()

	# Determine whether to show the banner
	if args.show_banner:
		config["show_banner"] = True
	elif args.no_banner:
		config["show_banner"] = False

	# Show banner if it's the first run OR if enabled
	if config["first_run"] or config["show_banner"]:
		print(ASCII_ART)

	# Mark first run as completed
	config["first_run"] = False
	save_config(config)


	if args.input:
		lyrics = args.input
	elif args.title and args.artist:
		lyrics = get_lyrics(args.title, args.artist)
	else:
		print("Please provide either a song title and artist or manual lyrics input.")
		return

	transformed_lyrics = transform_to_technical_prose(lyrics, args.mode)
	print("\nTechnical Prose Version:\n")
	print(transformed_lyrics)


if __name__ == "__main__":
	main()
