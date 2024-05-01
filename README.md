
# PyWordDetector

A simple Python script to detect words and words containing words from a file or from plaintext using a list.

## Installation

#### Install Python

Make sure Python 3 is installed. If it isn't, install it from [python.org](https://www.python.org/).
## Running

Clone the project

```bash
  git clone https://github.com/FlpCastilho/PyWordDetector.git
```

Go to the project directory

```bash
  cd PyWordDetector
```

Run the script

```bash
  python PyWordDetector
```
## FAQ

#### Does this differentiate between lower and uppercase words?

No, the script converts everything to lowercase to avoid false negatives.

#### Does this identify only whole words?

By design the script will mark a positive if a word from the target text contains part of a word from the ```keywords.txt``` list, for example: if you put the word "pull" in your keywords the word "pulling" in the target text will be marked as a positive.

#### How do I set my keywords?

To set your keywords simply modify the ```keywords.txt``` document with the keywords you want to detect, remember to separate each keyword with a comma ```just, like, this```

## License

PyWordDetector is licensed under the [Unlicense License](https://unlicense.org/).
