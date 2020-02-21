

for dialog in client.get_dialogs(limit=10):
    print(utils.get_display_name(dialog.entity), dialog.draft.message)
