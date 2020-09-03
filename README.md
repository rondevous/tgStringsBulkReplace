# Bulk Replacer
Rename strings of your Telegram langpack in bulk. All translation apps are supported. Unicode character-range is supported. You can replace latin and non-latin characters as well.

The words are replaced across all languages and scripts in the Unicode character set. That includes English, Russian, Hindi, Malayalam, Japanese, etc.

**Note:** This is still an early stage. There are plans to make it user-friendly in the coming months. But since, you may not have the patience to wait, you may use it in the terminal.

## Pros:
- Replaces the whole word (only exact matches)
- Works offline
- Finishes in under 2 secs

**Any replacements for the word "admin", will not replace the word "administrator".**<br>
Likewise, replacements for the word **"use" will not replace the word "house".**

## Cons:
- **Replacement pairs have to be made inside the code.**
- **Need to use the Terminal/Command Prompt**
- Need to install something (Python 3)
- Translator has to adjust with the code-y eyes.

### Tips:
In the "find":"replace" pairs
- "**members?**" will match both "**member**" and "**members**" <br>
- "**[Aa]dmin**" will match both "**Admin**" and "**admin**"


### Setup:
1. Download and Install **[Python 3](https://www.python.org/downloads)**
- Windows downloads:<br>
[Windows 64-bit](https://www.python.org/ftp/python/3.8.5/python-3.8.5-amd64.exe)<br>
[Windows 32-bit](https://www.python.org/ftp/python/3.8.5/python-3.8.5.exe)
- On Debian/Ubuntu:<br>
`apt install python3 python-is-python3`

2. Download **[replacer.py](https://github.com/rondevous/BulkReplacer/raw/master/replacer.py)**
_(right click the link > Save link as)_

### Preparation:
1. Export your language from [translations.telegram.org/**langname/appname**](https://translations.telegram.org)
2. Keep all files in the same folder:
```
replacer.py
android_lang.xml
```

### Running the replacer:
1. Open [replacer.py](https://github.com/rondevous/BulkReplacer/raw/master/replacer.py) in notepad/editor and edit the `find:replace` pairs at the TOP of the code:
```
replace_dictionary = {
  "groups":"baskets",
  "members":"onions",
  "Forever":"STFU",
}
```
Note that replacements are case-sensitive.<br>
After editing, it may look something like this:
```
replace_dictionary = {
  "subscribers":"सबस्ख्रायबर्झ",
  "subscriber":"सबस्ख्रयबर",
  "Group":"ग्रप",
  "group":"ग्रप",
  "channel":"चेनल",
  "channels":"चेनल्स",
}
```
2. Open folder in Command prompt / Terminal
On Windows, in the folder's address bar, type `cmd.exe` and press Enter
![open_folder_in_cmd](https://user-images.githubusercontent.com/67483423/91973117-4ed93d00-ed39-11ea-9eba-19f2a3cc3ece.png)

On Linux, launch the terminal:<br>
`cd path/to/folder`
If you enter `pwd`, the output should be `/complete/.../path/to/folder`


3. Run the replacer with this command (do not copy `$`)
```
$ python replacer.py --lang android_lang.xml
```
Tip: Pressing 'Tab' in the terminal will auto-complete the file name.

**Hint: If you get stuck**
```
$ python replacer.py --help
```

## More tools and support
Join us in the [Translation Platform Tools](https://t.me/TranslationTools) group

