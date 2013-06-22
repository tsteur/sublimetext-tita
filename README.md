### Tita - Titanium Mobile / Alloy Framework - Sublime Text 2 Plugin

Only tested on MacOSX so far.

### Features
 * Run iPhone / iPad Simulator
 * Run Android Emulator / Android Device
 * Compile + Build MobileWeb (you need to run at least once via Titanium Studio)
 * Clean Build Directories
 * Snippets
 * Auto-completion
 * TSS Syntax highlighting and Auto-completions (Credits goes to AoDev https://github.com/AoDev/ti-alloy-in-sublime-text-2 Thx!)
 * Triggers Clean Build when changing tiapp.xml
 * Analyze code using Titanium-Code-Processor

### Installation

The easiest way to install this package is with [Package Control](http://wbond.net/sublime_packages/package_control). A more complex method is to download and extract the ZIP package to Sublime Text 2 Packages folder:
`~/Library/Application\ Support/Sublime\ Text\ 2/Packages/`

You need Titanium CLI + Alloy:
 * https://github.com/appcelerator/titanium
 * https://github.com/appcelerator/alloy

### Settings
 * Android SDK Path
 * Log Level

### Usage
 * Using context menu
 * Using the Command Palette (`Command+Shift+P` on OSX). Just search for `Titanium`
 * `super+alt+i` Run iPhone Simulator
 * `super+alt+p` Run iPad Simulator
 * `super+alt+d` Run Android Device
 * `super+alt+a` Run Android Emulator
 * `super+alt+m` Run MobileWeb
 * `super+alt+g` Generate something
 * `super+alt+c` Clean Build Directories
 * `super+alt+l` Analyze (Titanium Code Processor)
 * To use snippets just start typing "alloy"

### Troubleshooting
* Not able to run on Android? Execute `titanium setup` once and enter correct Android SDK Path
* Getting an error like `[Decode error - output not utf-8]`? Adjust encoding in Tita User-Settings.

### TODO
 * Run on iOS device

### How to update sublime-completions
Auto-Completion file is generated using this PHP snippet: https://gist.github.com/4244185

### Support
Please direct any feedback to:
* https://github.com/tsteur/sublimetext-tita
* https://twitter.com/tsteur

### Licence
Copyright (c) 2012 Thomas Steur

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
