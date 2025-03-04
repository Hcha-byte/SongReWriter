import argparse
import os

import lyricsgenius


genius = lyricsgenius.Genius(os.getenv("GENIUS_API_KEY"), timeout=15)

from together import Together

example = """[Chorus]
Here comes the sun (Doo-d-doo-doo)
Here comes the sun
And I say, "It's alright"

[Verse 1]
Little darling
It's been a long, cold, lonely winter
Little darling
It feels like years since it's been here
"""


# Initialize the client
client = Together()

def transform_to_technical_prose(lyrics, mode):
	api_key = os.getenv("TOGETHER_API_KEY")
	# Create the prompt for the AI model
	prompt = [{"role": "user", "content": f"Rewrite this in {str(mode)} technical prose while preserving verse format and putting an end-line at the end of each verse (exanple: {str(example)}):\n\n{str(lyrics)}"}]

	try:
		# Use the `together` client to make the API request
		response = client.chat.completions.create(
			model="meta-llama/Llama-3.3-70B-Instruct-Turbo",  # Use the correct model
			messages=[{"role": "user", "content": str(prompt)}],
		)

		# Extract and return the AI-generated content
		return response.choices[0].message.content

	except Exception as e:
		return f"Error: {str(e)}"




def get_lyrics(artist, song_title):
	song = genius.search_song(song_title, artist)
	if song:
		return song.lyrics
	else:
		return "Song not found"


def main():
	parser = argparse.ArgumentParser(description="Convert song lyrics into technical prose.")
	parser.add_argument("--title", "-t", type=str, help="Song title for automatic generation")
	parser.add_argument("--artist", "-a", type=str, help="Artist name for automatic generation")
	parser.add_argument("--input", "-i", type=str, help="Manually enter song lyrics")
	parser.add_argument("--mode", "-m", type=str,
						choices=["scientific", "bureaucratic", "engineering", "military", "medical"],
						default="scientific", help="Select transformation mode")

	args = parser.parse_args()

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
