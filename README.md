# Telegram Translation Strings Replacer
Rename strings of your Telegram langpack in one go. Only supports XML files. Unicode character-range is supported.

## How to use
1. Download and Install [Python 3](https://www.python.org/downloads)
2. Download the [replacer.py](https://github.com/rondevous/tgStringsBulkReplace/raw/master/replacer.py) script.
    - When the page loads, `right click > save as` to download it.
3. Copy the script (replacer.py) and your language.XML file to an empty folder
4. Edit the script's dictionary with your replacements
5. Now open the folder in terminal or command prompt 
    - In Windows: type `cmd.exe` in the folder's address bar. (or using the prompt: `cd path\to\folder`)
    - In Linux/bash terminal: `cd path/to/folder`
6. Finally, run the script: `python replacer.py --file language.xml`

- If you get stuck: `python replacer.py --help`

### The script is in early stage of development
Currently, `replacer.py` only works with XML files.
Unicode is used to make replacements. That means you can find-replace non-latin characters present in russian, hindi, malayalam, etc

### Requirements
- Python3

### Further help
Join us in the [Translation Platform Tools](https://t.me/TranslationTools) group