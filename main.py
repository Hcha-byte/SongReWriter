import argparse
import os

import lyricsgenius

# TRANSFORMATION_RULES = {
#     "scientific": {
#         r"\bsun\b": "solar radiation source",
#         r"\bwind\b": "atmospheric displacement",
#         r"\brain\b": "precipitation event",
#         r"\bstars\b": "celestial fusion reactors",
#         r"\bheartbeat\b": "cardiac cycle frequency"
#     },
#     "bureaucratic": {
#         r"\bI love you\b": "In accordance with previously established emotional parameters, I hereby declare a sustained affective attachment, contingent upon future developments.",
#         r"\bwe need to talk\b": "A formal discourse regarding the status of our association is required.",
#         r"\bleave me alone\b": "Cease and desist all unsolicited interactions immediately."
#     },
#     "engineering": {
#         r"\bheart\b": "emotional processing unit",
#         r"\btears\b": "emotional overflow event",
#         r"\bmemory\b": "data retention unit",
#         r"\bthinking\b": "parallel processing operation",
#         r"\blosing you\b": "critical data loss detected"
#     },
#     "military": {
#         r"\bfight\b": "engagement operation",
#         r"\blove\b": "strategic alliance",
#         r"\bretreat\b": "tactical withdrawal",
#         r"\bvictory\b": "mission success",
#         r"\bdefeat\b": "operational failure"
#     },
#     "medical": {
#         r"\bhappy\b": "elevated serotonin levels detected",
#         r"\bsad\b": "neurotransmitter depletion observed",
#         r"\bheartbeat\b": "cardiac rhythmic pulsation",
#         r"\bcrying\b": "lacrimal gland hyperactivity",
#         r"\bnervous\b": "increased sympathetic nervous system activation"
#     }
# }

genius = lyricsgenius.Genius("ArhWQHRhrvvM9i1P4YzpnDeTaucektN2wncx06117nWM-jd9AbsVdh96R88VRhB8")

from together import Together

# Initialize the client
client = Together()

def transform_to_technical_prose(lyrics, mode):
	api_key = os.getenv("TOGETHER_API_KEY")
	# Create the prompt for the AI model
	prompt = f"Rewrite this in {mode} technical prose:\n\n{lyrics}"

	try:
		# Use the `together` client to make the API request
		response = client.chat.completions.create(
			model="meta-llama/Llama-3.3-70B-Instruct-Turbo",  # Use the correct model
			messages=[{"role": "user", "content": prompt}],
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
