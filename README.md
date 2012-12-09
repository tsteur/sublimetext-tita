### Tita - Titanium Mobile / Alloy Framework - Sublime Text 2 Plugin

Only tested on MacOSX so far.

### Features
 * Run iPhone Simulator / Android Emulator
 * Compile MobileWeb (you need to run via Titanium Studio)
 * Clean Build Directories
 * Snippets
 * Auto-Completion

### Installation
Download and extract to Sublime Text 2 Packages folder:
 * Mac OS X: `~/Library/Application\ Support/Sublime\ Text\ 2/Packages/`

You need Titanium CLI + Alloy:
 * https://github.com/appcelerator/titanium
 * https://github.com/appcelerator/alloy

### Usage
 * Using context menu
 * Using the Command Palette (`Command+Shift+P` on OSX). Just search for `Titanium`
 * `super+alt+i` Run iPhone Simulator
 * `super+alt+a` Run Android Emulator
 * `super+alt+m` Run MobileWeb
 * `super+alt+g` Generate something
 * `super+alt+c` Clean Build Directories
 * To use snippets just start typing "alloy"

### TODO
 * Set Android SDK Environment Variable
 * Run Mobile Web
 * Run on device
 * Add Titanium-Code-Processor
 * Trigger Clean Build when changing tiapp.xml

### How to update sublime-completions
Auto-Completion file is generated using this PHP snippet: https://gist.github.com/4244185

### Licence
Copyright (c) 2012 Thomas Steur

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.