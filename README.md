# Bulk Replacer
Rename multiple strings of your Telegram langpack at once! All of telegram's apps on the [translation panel](https://translations.telegram.org) are supported.

You can replace words/phrases of any language script in the Unicode character set. That includes English, Russian, Hindi, Malayalam, Japanese, etc.

**Note:** This is still in an early stage. There are plans to make it user-friendly in the coming months. But you may not have the patience to wait, so you may use this in the terminal...

## Pros:
- Replaces the whole word in any language (only exact matches)
- **Works offline**
- Completes in few seconds
- **Replacements for the word "admin", will not affect the word "administrator".**
- Likewise, replacements for the word "use" will not affect the word "house".

## Cons:
- **Find-Replace pairs need to be made inside the code file.**
- Need to use the Terminal/Command Prompt
- **Need to install something (Python 3)**
- Translator has to adjust with the code-y eyes.

## How to use 'Bulk Replacer'

🔸 **Advice:** _Do not be afraid to open the file and look at the code._<br>
_Do not be afraid to run the code._

### Step 1: First, Install [Python 3](https://www.python.org/downloads)
Its a program that will process instructions of the Python programming language.

⬇️ [Python for Windows 64-bit](https://www.python.org/ftp/python/3.8.5/python-3.8.5-amd64.exe)<br>
⬇️ [Python for Windows 32-bit](https://www.python.org/ftp/python/3.8.5/python-3.8.5.exe)<br>
🐧 **Debian/Ubuntu/Linux Mint:** ` apt install python-is-python3 `<br>
🐧 **Fedora:** ` dnf install python3 `

### Step 2: Download the most recent copy of [replacer.py](https://cdn.jsdelivr.net/gh/rondevous/BulkReplacer/dev/replacer.py)
Also, make an export of your language. Put all the files in the same folder:

MyFolder<br>
|— [replacer.py](https://cdn.jsdelivr.net/gh/rondevous/BulkReplacer/replacer.py)<br>
|— android_lang.xml<br>
|— ios_language.strings<br>

**Note:** Unlike .xml files of Android and Android\_X, if you want to replace <ins>untranslated strings</ins> for <ins>iOS/ TDesktop/ MacOS</ins>, export the base language and then [split the untranslated strings](https://github.com/rondevous/lang_split) from it before using with the replacer.

### Step 3: Create your find-replace pairs
Open [replacer.py](https://cdn.jsdelivr.net/gh/rondevous/BulkReplacer/replacer.py) in notepad. Edit the find-replace pairs inside the `replace_dictionary` at the **top** of the code<br>
```
replace_dictionary = {
  "groups":"baskets",
  "members":"onions",
  "Forever":"STFU",
}
```

Here's what mine look like:<br>
![Edited Pairs](https://user-images.githubusercontent.com/67483423/92223855-ae148a00-eebe-11ea-9132-dc675d4fcc28.png)<br>
Check the syntax of the pairs:<br>

`"phrase to find":"phrase to replace",`<br>

Note the comma (`,`) at the end of each pair.


### Step 4: Open folder in Command prompt / Terminal
- **Windows**<br>
![Open folder in cmd](https://user-images.githubusercontent.com/67483423/91973117-4ed93d00-ed39-11ea-9eba-19f2a3cc3ece.png)<br>
On Windows, type `cmd.exe` in the folder's address bar and press Enter<br>

The command prompt will open to that folder

- **Linux**<br>
![Open folder in Terminal](https://user-images.githubusercontent.com/67483423/92240500-5b48cb80-eeda-11ea-81a1-88a6ab1ed97a.png)<br>
On Linux, some file managers have this option.

If not, open terminal, and **cd** to the folder where the files are placed.

`cd path/to/folder`

Tip: you can check the "current folder" with the `pwd` command. `ls` will show what files are present in it


### Step 5: Run the replacer
![Run-the-Replacer](https://user-images.githubusercontent.com/67483423/92239337-6dc20580-eed8-11ea-8ab2-3fa0ba676c27.gif)<br>
Type the command and press enter
```
python replacer.py --lang android_lang.xml
```
🔸 Tip: Press `Tab` to auto-complete the filename in cmd / terminal

🔸 Tip: If the same word is found with a different case (UPPERCASE, lowercase, or SomeOtherCASE), a file named `possibilities.log` will be made in the same folder.

That's all. 😁 <br>
Import your EDITED file on the [translations platform](https://translations.telegram.org)
---
**If you get an error**<br>
Check what you typed. Make sure you have typed the full filename.

**Please check for any grammar issues.**<br>
When importing any file on the translations platform, it will always give you a chance to see the strings that you are going to import. 

Use this opportunity to review the strings, change them if needed, and then import them 😊

## More tools and support
Join us in the [Translation Platform Tools](https://t.me/TranslationTools) group

