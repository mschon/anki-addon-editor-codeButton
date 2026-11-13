try:
    from aqt.gui_hooks import editor_did_init_buttons
except ImportError:
    editor_did_init_buttons = None


def on_code(editor):
    if editor.web is not None:
        editor.web.eval("wrap('<code>', '</code>');")


def add_button_modern(buttons, editor):
    buttons.append(
        editor.addButton(
            "",
            "code",
            on_code,
            tip="Use fixed-width type",
            label="&lt;&gt;",
        )
    )


def add_button_legacy(buttons, editor):
    editor._links["code"] = on_code
    return buttons + [editor._addButton("", "code", "Use fixed-width type", "&lt;&gt;")]


if editor_did_init_buttons is not None:
    editor_did_init_buttons.append(add_button_modern)
else:
    from anki.hooks import addHook

    addHook("setupEditorButtons", add_button_legacy)
