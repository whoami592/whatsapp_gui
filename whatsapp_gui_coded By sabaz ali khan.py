import tkinter as tk
from tkinter import ttk

class WhatsAppGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("WhatsApp Clone")
        self.root.geometry("800x600")
        self.root.configure(bg="#ECE5DD")

        # Main frame
        self.main_frame = tk.PanedWindow(self.root, orient=tk.HORIZONTAL, sashwidth=5)
        self.main_frame.pack(fill=tk.BOTH, expand=True)

        # Left panel (Contacts)
        self.contacts_frame = tk.Frame(self.main_frame, bg="#F7F7F7", width=250)
        self.main_frame.add(self.contacts_frame, minsize=200)

        # Contacts header
        tk.Label(self.contacts_frame, text="Chats", font=("Arial", 16, "bold"), bg="#F7F7F7").pack(pady=10)

        # Contacts list
        self.contacts_listbox = tk.Listbox(self.contacts_frame, font=("Arial", 12), bg="#F7F7F7", bd=0, highlightthickness=0)
        self.contacts_listbox.pack(fill=tk.BOTH, expand=True, padx=10, pady=5)
        sample_contacts = ["Alice", "Bob", "Charlie", "David"]
        for contact in sample_contacts:
            self.contacts_listbox.insert(tk.END, contact)

        # Right panel (Chat)
        self.chat_frame = tk.Frame(self.main_frame, bg="#ECE5DD")
        self.main_frame.add(self.chat_frame)

        # Chat header
        self.chat_header = tk.Frame(self.chat_frame, bg="#075E54")
        self.chat_header.pack(fill=tk.X)
        tk.Label(self.chat_header, text="Alice", font=("Arial", 14, "bold"), bg="#075E54", fg="white").pack(side=tk.LEFT, padx=10, pady=10)

        # Chat display
        self.chat_display = tk.Text(self.chat_frame, font=("Arial", 12), bg="#ECE5DD", bd=0, state='disabled', wrap=tk.WORD)
        self.chat_display.pack(fill=tk.BOTH, expand=True, padx=10, pady=5)

        # Message input frame
        self.input_frame = tk.Frame(self.chat_frame, bg="#ECE5DD")
        self.input_frame.pack(fill=tk.X, padx=10, pady=5)

        self.message_entry = tk.Entry(self.input_frame, font=("Arial", 12), bg="white", bd=0)
        self.message_entry.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=(0, 5))

        self.send_button = tk.Button(self.input_frame, text="Send", font=("Arial", 12), bg="#075E54", fg="white", command=self.send_message)
        self.send_button.pack(side=tk.RIGHT)

    def send_message(self):
        message = self.message_entry.get()
        if message:
            self.chat_display.configure(state='normal')
            self.chat_display.insert(tk.END, f"You: {message}\n")
            self.chat_display.configure(state='disabled')
            self.message_entry.delete(0, tk.END)
            self.chat_display.see(tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    app = WhatsAppGUI(root)
    root.mainloop()