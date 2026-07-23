"""
main.py
-------
Entry point for the BMI Smart Calculator desktop app.

Run with:
    python main.py

Developed by Aman Kumar
"""

import os
import sys
import tkinter as tk
from tkinter import messagebox

# Make sure `src` is importable regardless of the working directory
# the script is launched from.
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))


def _show_fatal_error(message: str) -> None:
    """Show a message box even if the app itself never got as far as building a window."""
    try:
        root = tk.Tk()
        root.withdraw()
        messagebox.showerror("Fatal Error", message)
    except Exception:
        # If even Tk itself can't start, fall back to the console so the
        # user still sees *something* instead of a silent exit.
        print(f"FATAL ERROR: {message}", file=sys.stderr)


def main():
    try:
        from src.gui import BMIApp
    except Exception as exc:
        _show_fatal_error(
            "The application failed to start because a required piece "
            f"could not be loaded:\n\n{exc}\n\n"
            "Make sure you're running this with Python 3.9+ and that "
            "tkinter is installed (on Linux: sudo apt install python3-tk), "
            "then run: pip install -r requirements.txt"
        )
        sys.exit(1)

    try:
        app = BMIApp()
        app.mainloop()
    except Exception as exc:  # top-level safety net so the app never crashes silently
        _show_fatal_error(f"The application encountered an error:\n{exc}")
        sys.exit(1)


if __name__ == "__main__":
    main()
