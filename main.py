import argparse
from app.functions import get_lyrics, transform_to_technical_prose


# noinspection PyUnboundLocalVariable
def main():
	parser = argparse.ArgumentParser(description="Convert song lyrics into technical prose.")
	parser.add_argument("--title", "-t", type=str, help="Song title for automatic generation")
	parser.add_argument("--artist", "-a", type=str, help="Artist name for automatic generation")
	parser.add_argument("--input", "-i", type=str, help="Manually enter song lyrics")
	parser.add_argument("--mode", "-m", type=str,
						choices=["scientific", "bureaucratic", "engineering", "military", "medical"],
						default="scientific", help="Select transformation mode")
	parser.add_argument("--help", "-h", action="help", help=f'''
	SongReWriter

	Convert song lyrics into technical prose
	
	Usage: python main.py [-h] [-t TITLE] [-a ARTIST] [-i INPUT] [-m MODE]
	
	optional arguments:
	  -h, --help            show this help message and exit
	  -t TITLE, --title TITLE
	                        Song title for automatic generation
	  -a ARTIST, --artist ARTIST
	                        Artist name for automatic generation
	  -i INPUT, --input INPUT
	                        Manually enter song lyrics
	  -m MODE, --mode MODE  
	                        Select transformation mode [default: scientific] from the following: scientific, bureaucratic, engineering, military, medical
	                        
	Examples:
	  python main.py --title "Song Title" --artist "Artist Name"
	  python main.py --input "Here comes the sun (Doo-d-doo-doo)\nHere comes the sun\nAnd I say, \"It's alright\""
	  
	----------------------------------------------------------------------------
	
	Version: 1.1.0
	
	Created by Hcha-byte
	
	MIT License © 2025
	''')
# Also used in README.md

	args = parser.parse_args()

	if args.input:
		lyrics = args.input
	elif args.title and args.artist:
		lyrics = get_lyrics(args.title, args.artist)
	elif args.help:
		parser.print_help()
	else:
		print("Please provide either a song title and artist or manual lyrics input.")
		return

	transformed_lyrics = transform_to_technical_prose(lyrics, args.mode)
	print("\nTechnical Prose Version:\n")
	print(transformed_lyrics)


if __name__ == "__main__":
	main()
