# codeButton for Anki note editor

## Overview

**codeButton** is an Anki 2.1 addon that modifies the note editor toolbar to add a formatting button which wraps the currently-selected text in `<code></code>` HTML tags. This is useful for notes that include command line interface (CLI) commands, programming keywords, and so on. 

## Prerequisites

The following instructions assume that you already:

1. have [Anki](https://apps.ankiweb.net/) 2.1 installed and 
2. have a basic understanding of how to [edit](https://docs.ankiweb.net/editing.html) and [format](https://docs.ankiweb.net/editing.html#editing-features) notes. 

## Installation

1. Clone this repository to your computer. 
2. In Anki, select **Tools**, then **Add-ons**. 
3. In the Add-ons menu, select **View Files**. 
4. This should open your Add-ons directory, which may be called `addons21`. 
5. Copy the repository directory created in step 1 into the Add-ons directory. 
6. If done correctly, the Add-ons directory should contain a directory called `codeButton`, which contains a file called `__init__.py`. 
7. Restart Anki (i.e. exit and reopen).

## Using the feature

After reopening Anki, click the **Add** button to open the note editor. In the top toolbar, you should now see an additional button at the end labeled `<>`. 

Enter some text in any of the note fields, highlight a portion of that text, and click the `<>` button. The highlighted text should now appear in fixed-width font. If you view the HTML for the field, you should see the highlighted text is wrapped in `<code></code>` tags. 

## Troubleshooting

If the button doesn't appear, go to the main Anki window and select **Tools**, then **Add-ons**. Make sure that the **codeButton** addon is in the list and is enabled. 

## Uninstallation

To disable, go to the main Anki window and select **Tools**, then **Add-ons**. Disable the **codeButton** addon. You can also click **View Files** to open the Add-ons directory and delete the `codeButton` subdirectory from it.

## Version History

Refer to HISTORY.md

## Contributing to this project

Refer to CONTRIBUTING.md

## Supporting this project

This addon is available free of charge.

If you found this addon useful, monetary gifts are appreciated via [PayPal](https://paypal.me/mattschonert). 

You are welcome to connect with me on [LinkedIn](https://www.linkedin.com/in/mattschonert/). 
