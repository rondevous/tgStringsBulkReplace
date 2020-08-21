# Telegram Translation Strings Replacer
Rename strings in your Telegram langpack in one go. Unicode characters are supported.

## How to use
1. Download and Install [Python 3](https://www.python.org/downloads_
2. Download the [replacer.py](https://github.com/rondevous/tgStringsBulkReplace/raw/master/replacer.py) script.
    - When the page loads, `right click > save as` to download it.
3. Move the replacer.py and your language.XML to a new folder
4. Open replacer.py in an editor, and edit the dictionary (right at the top)
4. Open the folder in command prompt or terminal
5. Enter this: `python replacer.py --file language.xml`

### The script is in early stage of development
Currently, `replacer.py` only works with XML files.

Unicode is used to make replacements. That means you can find-replace non-latin characters present in russian, hindi, malayalam, etc

### Requirements
- Python3
