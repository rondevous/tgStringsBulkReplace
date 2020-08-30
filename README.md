# Bulk Replacer 
Rename strings of your Telegram langpack in bulk. All translation apps are supported. Unicode character-range is supported. You can replace latin and non-latin characters present in any language (English, Russian, Hindi, Malayalam, Chinese, etc).

### Setup:
1. Download and Install [Python 3](https://www.python.org/downloads)
2. Download [replacer.py](https://github.com/rondevous/tgStringsBulkReplace/raw/master/replacer.py)
_(right click the link > Save link as)_

### Preparations:
1. Export your language from [translations.telegram.org/**langname/appname**](https://translations.telegram.org)
2. Keep all files in the same folder:
```
replacer.py
language_file
```

## Run the replacer:
1. Open [replacer.py](https://github.com/rondevous/tgStringsBulkReplace/raw/master/replacer.py) in notepad/editor and edit the `"find":"replace"` pairs
2. [Open command prompt/terminal](https://github.com/rondevous/tgStringsBulkReplace#opening-command-prompt--terminal) and enter this command (do not copy `$`)
```
$ python replacer.py --file language.xml
```
Tip: Pressing 'Tab' in the terminal will auto-complete the file name.

**If you get stuck**
```
$ python replacer.py --help
```

### To open command prompt / Terminal
- In Windows, type `cmd.exe` in the folder's address bar. Or simply open the prompt and enter: `cd path\to\folder`
- In Linux terminal: `cd path/to/folder`

## More tools and support
Join us in the [Translation Platform Tools](https://t.me/TranslationTools) group

