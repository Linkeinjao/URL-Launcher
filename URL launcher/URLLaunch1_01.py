import tkinter as tk
import webbrowser
import json

class WebLauncherApp:
    def __init__(self, master):
        self.master = master
        master.title("Web Launcher")

        self.label_saved_urls = tk.Label(master, text="Saved URLs:")
        self.label_saved_urls.grid(row=0, column=0, sticky=tk.W)

        self.listbox_saved_urls = tk.Listbox(master, width=50)
        self.listbox_saved_urls.grid(row=0, column=1, columnspan=2, sticky=tk.W+tk.E)

        self.scrollbar_saved_urls = tk.Scrollbar(master, orient=tk.VERTICAL, command=self.listbox_saved_urls.yview)
        self.scrollbar_saved_urls.grid(row=0, column=3, sticky=tk.N+tk.S)
        self.listbox_saved_urls.config(yscrollcommand=self.scrollbar_saved_urls.set)

        self.label_url = tk.Label(master, text="URL:")
        self.label_url.grid(row=1, column=0, sticky=tk.W)

        self.entry_url = tk.Entry(master)
        self.entry_url.grid(row=1, column=1, columnspan=2, sticky=tk.W+tk.E)

        self.label_name = tk.Label(master, text="Name:")
        self.label_name.grid(row=2, column=0, sticky=tk.W)

        self.entry_name = tk.Entry(master)
        self.entry_name.grid(row=2, column=1, columnspan=2, sticky=tk.W+tk.E)

        self.save_button = tk.Button(master, text="Save", command=self.save_url)
        self.save_button.grid(row=3, column=0, sticky=tk.W+tk.E)

        self.launch_button = tk.Button(master, text="Launch", command=self.launch_url)
        self.launch_button.grid(row=3, column=1, columnspan=2, sticky=tk.W+tk.E)

        # Populate the listbox with saved URLs
        self.load_saved_urls()

    def load_saved_urls(self):
        try:
            with open('urls.json', 'r') as f:
                data = json.load(f)
                for entry in data:
                    self.listbox_saved_urls.insert(tk.END, entry["name"])
        except FileNotFoundError:
            pass

    def save_url(self):
        url = self.entry_url.get()
        name = self.entry_name.get()

        try:
            with open('urls.json', 'r') as f:
                data = json.load(f)
        except FileNotFoundError:
            data = []

        data.append({"name": name, "url": url})

        with open('urls.json', 'w') as f:
            json.dump(data, f, indent=4)

        self.listbox_saved_urls.insert(tk.END, name)

        print(f"Saved '{name}' at '{url}'")

    def launch_url(self):
        selected_index = self.listbox_saved_urls.curselection()
        if selected_index:
            try:
                with open('urls.json', 'r') as f:
                    data = json.load(f)
            except FileNotFoundError:
                print("No URLs saved yet.")
                return

            selected_name = self.listbox_saved_urls.get(selected_index)
            for entry in data:
                if entry["name"] == selected_name:
                    webbrowser.open(entry["url"])
                    print(f"Launching '{entry['name']}' at '{entry['url']}'")
                    break
        else:
            print("Please select a saved URL.")

def main():
    root = tk.Tk()
    app = WebLauncherApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
