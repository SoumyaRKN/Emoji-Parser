# Emoji-Parser
This program will parse the emoji in a message and show it's parsed text.

# Setup
1. Create a virtual environment.
```
python3 -m venv .venv
```

2. Activate the virtual environment.
```
source .venv/bin/activate
```

3. Install required packages.
```
pip3 install -r requirments.txt
```

3. Install required packages.
```
pip3 install -r requirments.txt
```

# Usage
1. Parsing a message
```
python3 main.py -p "Python is 👍"


# Output
-------------------------
Parsing: Python is 👍

Parsed Message: Python is :thumbs_up:
```

2. Converting a message
```
python3 main.py -c "Python is :thumbsup:"

# Output
-------------------------
Converting: Python is :thumbsup:

Converted Message: Python is 👍
```