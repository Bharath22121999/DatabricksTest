#!/usr/bin/env python3
"""
keep_available_teams.py  (Windows, no extra packages)

Keeps Microsoft Teams status at “Available” by jig-jogging the mouse
every 4 minutes.  Stop with Ctrl-C or closing the console window.
"""

import time
import ctypes
from ctypes import wintypes

# --- Win32 API setup ---------------------------------------------------------
user32 = ctypes.WinDLL("user32", use_last_error=True)

class POINT(ctypes.Structure):
    _fields_ = [("x", wintypes.LONG),
                ("y", wintypes.LONG)]

GetCursorPos = user32.GetCursorPos
GetCursorPos.argtypes = [ctypes.POINTER(POINT)]
GetCursorPos.restype  = wintypes.BOOL

SetCursorPos = user32.SetCursorPos
SetCursorPos.argtypes = [wintypes.INT, wintypes.INT]
SetCursorPos.restype  = wintypes.BOOL
# -----------------------------------------------------------------------------


def jiggle():
    """Move mouse +1px and back to reset system idle timer."""
    pt = POINT()
    if GetCursorPos(ctypes.byref(pt)):            # current position
        SetCursorPos(pt.x, pt.y + 1)              # down
        SetCursorPos(pt.x, pt.y)                  # back

if __name__ == "__main__":
    print("Running…  Press Ctrl-C to exit.")
    try:
        while True:
            jiggle()
            time.sleep(240)  # 4 minutes  (under Teams’ 5-min idle threshold)
    except KeyboardInterrupt:
        print("\nStopped.")