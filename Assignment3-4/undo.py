from copy import deepcopy

def undo(backup):
    return backup.pop()[:]

