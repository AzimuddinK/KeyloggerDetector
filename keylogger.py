import os
import subprocess
import psutil
import tkinter as tk
from tkinter import messagebox, scrolledtext


class KeyloggerDetector:
    def __init__(self, master):
        self.blacklist = []
        self.process_name = None
        self.timer = 1
        self.gui = master
        self.gui.geometry('600x400')
        self.gui.title("Keylogger Detector")
        self.create_widgets()

    def create_widgets(self):
        self.output_box = scrolledtext.ScrolledText(self.gui, height=20, width=60)
        self.output_box.pack(padx=10, pady=10)

        self.start_btn = tk.Button(self.gui, text="Start Detection", command=self.start_detection)
        self.start_btn.pack(pady=5)

        self.stop_btn = tk.Button(self.gui, text="Stop Detection", command=self.stop_detection)
        self.stop_btn.pack(pady=5)

        self.clear_btn = tk.Button(self.gui, text="Clear Output", command=self.clear_output)
        self.clear_btn.pack(pady=5)

    def start_detection(self):
        self.show_output()

    def stop_detection(self):
        self.timer = 0

    def clear_output(self):
        self.output_box.delete('1.0', tk.END)

    def show_output(self):
        if self.timer:
            self.check_for_keyloggers()
            self.gui.after(5000, self.show_output)

    def check_for_keyloggers(self):
        proc = subprocess.Popen('netstat -ano -p tcpv6 -p tcp | findStr /c:"587" /c:"465" /c:"2525"',
                                shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE)
        out, _ = proc.communicate()
        output = out.decode()

        if "ESTABLISHED" in output:
            self.output_box.insert(tk.END, "Potential keylogger detected!\n")

            self.process_name = self.get_process_name(output)
            self.output_box.insert(tk.END, f"Process Name: {self.process_name}\n")

            is_safe = messagebox.askyesno("Confirmation", "Do you trust this application?")
            if is_safe:
                self.output_box.insert(tk.END, "Application added to whitelist.\n")
            else:
                self.output_box.insert(tk.END, "Application added to blacklist and terminated.\n")
                self.blacklist.append(self.process_name)

        self.output_box.insert(tk.END, "\n")

    def get_process_name(self, output):
        lines = output.splitlines()
        for line in lines:
            if "ESTABLISHED" in line:
                process_id = line.split()[-1]
                process = psutil.Process(int(process_id))
                return process.name()


if __name__ == "__main__":
    root = tk.Tk()
    app = KeyloggerDetector(root)
    root.mainloop()
