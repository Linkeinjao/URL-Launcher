import tkinter as tk
import webbrowser
import json

class WebLauncherApp:
    def __init__(self, master):
        self.master = master
        master.title("Web Launcher")

        self.label_url = tk.Label(master, text="URL:")
        self.label_url.grid(row=0, column=0, sticky=tk.W)

        self.entry_url = tk.Entry(master)
        self.entry_url.grid(row=0, column=1)

        self.label_name = tk.Label(master, text="Name:")
        self.label_name.grid(row=1, column=0, sticky=tk.W)

        self.entry_name = tk.Entry(master)
        self.entry_name.grid(row=1, column=1)

        self.save_button = tk.Button(master, text="Save", command=self.save_url)
        self.save_button.grid(row=2, columnspan=2, sticky=tk.W+tk.E)

        self.launch_button = tk.Button(master, text="Launch", command=self.launch_url)
        self.launch_button.grid(row=3, columnspan=2, sticky=tk.W+tk.E)

    def save_url(self):
        url = self.entry_url.get()
        name = self.entry_name.get()

        # Load existing data or initialize an empty list
        try:
            with open('urls.json', 'r') as f:
                data = json.load(f)
        except FileNotFoundError:
            data = []

        # Add new URL and name to the data list
        data.append({"name": name, "url": url})

        # Save updated data to the JSON file
        with open('urls.json', 'w') as f:
            json.dump(data, f, indent=4)

        print(f"Saved '{name}' at '{url}'")

    def launch_url(self):
        # Open the JSON file and load URLs
        try:
            with open('urls.json', 'r') as f:
                data = json.load(f)
        except FileNotFoundError:
            print("No URLs saved yet.")
            return

        # Open each URL in the default web browser
        for entry in data:
            webbrowser.open(entry["url"])
            print(f"Launching '{entry['name']}' at '{entry['url']}'")

def main():
    root = tk.Tk()
    app = WebLauncherApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
