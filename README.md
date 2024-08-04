# Text Utilities

Several text conversion utilities based on LLM. Utilities including subtitles to text conversion, creating paragraphs,
shortening and translation.

## Installation

Note: some utilities use [ollama](https://ollama.com/). So you must install it before using translation or
shortening.

```bash
python -m venv venv # create virtual environment, if needed
source venv/bin/activate # activate virtual environment, if needed
python -m pip install -r requirements.txt
```

## Usage

Convert YouTube subtitles to plain text:

```bash
python main.py convert ~/downloads/f.txt # Where f.txt - YouTube subtitles file

```

Split dirty text to paragraphs:

```bash
python main.py paragraph /tmp/musk-interview.txt # Text file, created from subtitles or PDF

```

Shorten text:

```bash
python main.py shorten --factor 10 /tmp/musk-interview.txt # Shorten text, summarize every 10 paragraphs to one

```

Translate text

```bash
python main.py translate --language russian /tmp/musk-interview.txt # Translate text into Russian language

```

## License

Source code is primarily distributed under the terms of the MIT license. See LICENSE for details.
