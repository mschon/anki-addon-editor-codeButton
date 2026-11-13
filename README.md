# codeButton for Anki note editor

## Overview

**codeButton** is an Anki addon that modifies the note editor toolbar to add a formatting button which wraps the currently-selected text in `<code></code>` HTML tags. This is useful for notes that include command line interface (CLI) commands, programming keywords, and so on. 

## Prerequisites

The following instructions assume that you already:

1. have [Anki](https://apps.ankiweb.net/) installed and 
2. have a basic understanding of how to [edit](https://docs.ankiweb.net/editing.html) and [format](https://docs.ankiweb.net/editing.html#editing-features) notes. 

## Installation

1. Clone this repository to your computer (`git clone https://github.com/mschon/anki-addon-editor-codeButton.git`).
2. In Anki, select **Tools**, then **Add-ons**. 
3. In the Add-ons menu, select **View Files**. 
4. This should open your add-ons directory, which may be called `addons21`. 
5. Copy the repository directory created in step 1 into the add-ons directory. 
6. The add-ons directory should now contain a directory called `anki-addon-editor-codeButton`, which contains a file called `__init__.py`. 
7. Restart Anki (i.e. exit and reopen).

## Using the feature

After reopening Anki, click the **Add** button to open the note editor. In the top toolbar, you should now see an additional button at the end labeled `<>`. 

Enter some text in any of the note fields, highlight a portion of that text, and click the `<>` button. The highlighted text should now appear in fixed-width font. If you view the HTML for the field, you should see the highlighted text is wrapped in `<code></code>` tags. 

## Troubleshooting

If the button doesn't appear, go to the main Anki window and select **Tools**, then **Add-ons**. Make sure that the **anki-addon-editor-codeButton** add-on is in the list and is enabled. 

## Uninstallation

To disable the add-on, go to the main Anki window and select **Tools**, then **Add-ons**. Select the **anki-addon-editor-codeButton** add-on and click **Toggle Enabled**. It should then appear as disabled in your add-ons list. You can also click **View Files** to open the add-ons directory and delete the `anki-addon-editor-codeButton` subdirectory from it. 

## Version History

Refer to [HISTORY.md](https://github.com/mschon/anki-addon-editor-codeButton/blob/main/HISTORY.md)

## Contributing to this project

Refer to [CONTRIBUTING.md](https://github.com/mschon/anki-addon-editor-codeButton/blob/main/CONTRIBUTING.md)

## Supporting this project

This add-on is available free of charge.

If you found this add-on useful, monetary gifts are appreciated via [PayPal](https://paypal.me/mattschonert). 

You are welcome to connect with me on [LinkedIn](https://www.linkedin.com/in/mattschonert/). 
