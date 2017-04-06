LESS Buildes for Sublime Text
=============
Explicação

Usage
============
Install it using [Sublime Package Control](http://wbond.net/sublime_packages/package_control).
If TortoiseSVN is not installed at `C:\\Program Files\\TortoiseGIT\\bin\\TortoiseGitProc.exe`, specify the correct path
by setting property "tortoisegit_path" in your TortoiseSVN.sublime-settings file. 

The default key bindings are 
- [ctrl+alt+v then c] : commit changes to local repo
- [ctrl+alt+v then p] : push changes to remote repo
- [ctrl+alt+b] : open git bash from the current working directory

You can also call TortoiseGIT commands when right-clicking folders or files in the side bar.


IMPORTANT
==============

Do NOT edit the default TortoiseGIT settings. Your changes will be lost
when Sublime-TortoiseSVN is updated. ALWAYS edit the user Sublime-TortoiseSVN settings
by selecting "Preferences->Package Settings->TortoiseGIT->Settings - User".
Note that individual settings you include in your user settings will **completely**
replace the corresponding default setting, so you must provide that setting in its entirety.

Settings
==============

If your TortoiseProc.exe path is not the default, please modify the path by selecting 
"Preferences->Package Settings->TortoiseSVN->Settings - User" in the menu.

The default setting is:
    {
        // Auto close update dialog when no errors, conflicts and merges
        "autoCloseUpdateDialog": false,
        "tortoisegit_path": "C:\\Program Files\\TortoiseSVN\\bin\\TortoiseProc.exe",
		"gitbash_path": "C:\\Program Files (x86)\\Git\\bin\\sh.exe"
    }
