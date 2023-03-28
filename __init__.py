from anki.hooks import addHook

# wrap currently-selected text in code HTML tag
def onCode(editor):
    editor.web.eval("wrap('<code>', '</code>');")

# add button to editor toolbar
def addMyButton(buttons, editor):
    editor._links['code'] = onCode
    return buttons + [editor._addButton(
        "",  # icon path
        "code",  # link name
        "Use fixed-width type",  # tooltip
        "&lt;&gt;")]  # label

addHook("setupEditorButtons", addMyButton)
