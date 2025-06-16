#!/usr/bin/env python3
"""
Teams-keep-awake (Windows, no external packages)
Sends a dummy Shift key-press once per minute, forever.
"""

import time
import ctypes

# --- Win32 constants ---
INPUT_KEYBOARD      = 1
KEYEVENTF_KEYUP     = 0x0002
VK_SHIFT            = 0x10

# --- Win32 structures we need ---
class KEYBDINPUT(ctypes.Structure):
    _fields_ = [("wVk",      ctypes.c_ushort),
                ("wScan",    ctypes.c_ushort),
                ("dwFlags",  ctypes.c_ulong),
                ("time",     ctypes.c_ulong),
                ("dwExtra",  ctypes.POINTER(ctypes.c_ulong))]

class _INPUT(ctypes.Union):
    _fields_ = [("ki", KEYBDINPUT)]

class INPUT(ctypes.Structure):
    _anonymous_ = ("u",)
    _fields_ = [("type", ctypes.c_ulong),
                ("u",    _INPUT)]

SendInput = ctypes.windll.user32.SendInput

def tap_key(vk_code: int) -> None:
    """Press + release a key with the given virtual-key code."""
    # key down
    down = INPUT(type=INPUT_KEYBOARD,
                 ki=KEYBDINPUT(wVk=vk_code, wScan=0,
                               dwFlags=0, time=0, dwExtra=None))
    # key up
    up   = INPUT(type=INPUT_KEYBOARD,
                 ki=KEYBDINPUT(wVk=vk_code, wScan=0,
                               dwFlags=KEYEVENTF_KEYUP, time=0, dwExtra=None))
    SendInput(1, ctypes.byref(down), ctypes.sizeof(INPUT))
    SendInput(1, ctypes.byref(up),   ctypes.sizeof(INPUT))

if __name__ == "__main__":
    try:
        while True:
            tap_key(VK_SHIFT)   #  tiny, invisible “nudge”
            time.sleep(60)      #  1 min; tweak if you like
    except KeyboardInterrupt:
        print("Stopped.")