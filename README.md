# Welcome to punch-visualcode-plugin

Provide punchlang code assistance to visual code editor.

## Quick Start

1. Intall the extension
   
   ```bash
   cd $HOME/.vscode/extensions/
   git clone https://gitlab.thalesdigital.io/punch/parsers/punch-visualcode-plugin.git
   npm install
   npm run vscode:prepublish
   ```

2.  You may need to reopen your VSCode

3. Extension is activated when you first access a Punch file



## Prerequisites

- npm 

- nodejs

- Python = 3.6.8 ([Properly install Python using Pyenv](https://gitlab.thalesdigital.io/punch/product/punch/-/blob/8.0/documentation/docs/Common/Contribution_Guide/Developper/Setup/Setup_Python.md))



## Features

- Syntax Highlight

- Snippets for Punch operators

- Snippets for Java 

- Punch file formatter



## List Snippets Punch Operators

- cef

- cidrmatch

- csv

- findByKey

- grok2

- kv

- print

- raise

- tuple



## Extension Settings

This extension contributes the following settings :

- *Punch-formatter: Indentwidth* : number of spaces used for indentation (default = 1)

- *Punch-formatter: Python Path* : optional custom path to python executable (requires restarting vscode)

- *Punch-formatter: Formatter Path* : optional custom path to punch formatter (requires restarting vscode)



## License

All PunchPlatform software, documentation, resources are Copyright (c) Thales Services SAS, France 2015-2021. All rights reserved
