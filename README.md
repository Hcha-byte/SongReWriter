# SongReWriter

## CLI Tool

### Important Note:

You will need to set the environment variable `GENIUS_API_KEY` to use the `--title` and `--artist` options. You will also need to set the environment variable `TOGETHER_API_KEY` to use the CLI.

### Overview

SongReWriter CLI is a command-line tool designed to convert song lyrics into various styles of technical prose, such as scientific, bureaucratic, engineering, military, and medical.

### Installation

#### Option 1 - With Python 3 installed

Ensure you have Python 3 installed. You can clone the repository and install the required dependencies using pip:

```bash
git clone https://github.com/Hcha-byte/SongReWriter.git
cd SongReWriter
pip install -r requirements.txt
```

#### Option 2 - Using a .exe file

You can download the .exe file from [here](https://github.com/Hcha-byte/SongReWriter/releases/latest) and run it directly from your command prompt.


### Usage

Run the following command to start the tool:

```bash
python3 main.py [options]
```
OR
```bash
main.exe [options]
```

### Options

- `--title, -t`: Specify the song title for automatic generation. This option requires the `--artist` option to be used as well.


- `--artist, -a`: Specify the artist name for automatic generation. This option requires the `--title` option to be used as well.


- `--input, -i`: Provide the song lyrics manually instead of fetching them automatically.


- `--mode, -m`: Select the transformation mode. Options are: `scientific`, `bureaucratic`, `engineering`, `military`, `medical`. Default is `scientific`.


- `--help, -h`: Display the help message.

Note:
Automatically generated song lyrics are fetched from Genius.com.

### Examples

Convert a song by providing the title and artist:

```bash
python3 main.py --title "Song Title" --artist "Artist Name"
```
OR
```bash
main.exe --title "Song Title" --artist "Artist Name"
```

Convert song lyrics provided manually:

```bash
python3 main.py --input "Here comes the sun (Doo-d-doo-doo)\nHere comes the sun\nAnd I say, \"It's alright\""
```
OR
```bash
main.exe --input "Here comes the sun (Doo-d-doo-doo)\nHere comes the sun\nAnd I say, \"It's alright\""
```

### Help

To view help information:

```bash
python3 main.py --help
```
OR
```bash
main.exe --help
```

```text
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
```
## GUI Tool

The GUI tool is located at `app/` and can be run with:

```bash
python3 -m flask run
```
OR
You can go to it [here](https://songrewriter-production.up.railway.app)

## Features

### GUI Tool
- Convert song lyrics into various styles of technical prose, such as scientific, bureaucratic, engineering, military, and medical. -> More modes to coming
- Automatically fetch song lyrics from Genius.com.
- View the original lyrics and the transformed lyrics side by side.
### CLI Tool
- Convert song lyrics into various styles of technical prose, such as scientific, bureaucratic, engineering, military, and medical.
- Automatically fetch song lyrics from Genius.com.
- Manually enter song lyrics.
- Better formatting of output
---
MIT License © 2025

Created by Hcha-byte

Version: 1.1.0