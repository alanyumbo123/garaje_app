import tkinter as tk
from ui.app_tkinter import GarajeApp


def main():

    root = tk.Tk()

    app = GarajeApp(root)

    root.mainloop()


if __name__ == "__main__":
    main()
