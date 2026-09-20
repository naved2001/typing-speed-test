# ⌨️ Typing Speed Test

A Python command-line typing speed test that measures **Words Per Minute (WPM)** and typing accuracy.

The project allows users to generate random sentences using an API or enter their own sentence. It also includes an user input sentences so the application can continue working if the API is unavailable.

## Features

* 🎲 Random sentence generation using an API
* ✍️ Custom sentence input
* ⏱️ Custom time limit
* ⌨️ Real-time keyboard input
* 🔙 Backspace support
* 🔔 Beep when the time limit expires
* 📊 WPM calculation
* 🎯 Typing accuracy calculation
* ✅ Correct character count
* ❌ Wrong character count
* 🛡️ Input validation

## Technologies

* Python 3
* Requests
* REST API
* Command Line Interface

## Project Structure

```text
typing-speed-test/
│
├── typing_speed_test.py
├── sentence_api.py
├── requirements.txt
├── README.md
└── .gitignore
```

## Requirements

* Python 3.x
* Windows

The project uses `msvcrt` and `winsound`, which are Windows-specific Python modules.

## Installation

Clone the repository:

```bash
git clone https://github.com/naved2001/typing-speed-test
```

Open the project:

```bash
cd typing-speed-test
```

Install the dependency:

```bash
pip install -r requirements.txt
```

## Run

Start the application:

```bash
python typing_speed_test.py
```

## How It Works

When the application starts, you can choose:

```text
1. Generate Random Sentence
2. Enter Your Own Sentence
```

### Random Sentence

The program requests a sentence from the API.

If the API is unavailable, You can enter your own sentence.

### Custom Sentence

You can enter your own sentence and use it for the typing test.

### Time Limit

You choose how many seconds the typing test should run.

For example:

```text
Enter time limit (seconds): 30
```

When the time expires, the program stops the test and produces a beep sound.

## Results

After the test, the program displays:

```text
========================================
              RESULT
========================================
Words typed  : 8
Time taken   : 30.01 seconds
Typing speed : 15.99 WPM
Accuracy     : 94.5%
Correct chars: 70
Wrong chars  : 4
========================================
```

## WPM Calculation

The typing speed is calculated using:

```text
WPM = (Number of words / Time in seconds) × 60
```

## Accuracy

Accuracy is calculated by comparing the characters typed with the characters in the target sentence.

## Future Improvements

Possible future features:

* Graphical user interface
* Multiple difficulty levels
* High-score system
* Typing history
* Leaderboard
* More sentence categories
* Better character-level error tracking

## Author

**Naved**

A Python learning project focused on keyboard input, APIs, timing, string processing, and basic application structure.
