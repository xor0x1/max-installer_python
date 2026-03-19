import tkinter as tk
from tkinter import ttk, messagebox
import urllib.request
import subprocess
import tempfile
import os
import threading

# === НАСТРОЙКИ ===
MSI_URL = "Ссылка на приложение max.msi в нашем случае"
MSI_NAME = "MAX.msi"
# =================


class UpdaterApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Обновление Макс Мессенджера")
        self.root.geometry("400x150")
        self.root.resizable(False, False)

        # Центрирование окна
        self.root.eval('tk::PlaceWindow . center')

        # Статус
        self.status_label = tk.Label(root, text="Нажмите 'Обновить' для загрузки")
        self.status_label.pack(pady=10)

        # Прогресс-бар
        self.progress = ttk.Progressbar(root, length=350, mode='determinate')
        self.progress.pack(pady=10)

        # Кнопка
        self.update_btn = tk.Button(root, text="Обновить", command=self.start_update, width=20, height=2)
        self.update_btn.pack(pady=10)

    def start_update(self):
        self.update_btn.config(state='disabled')
        self.status_label.config(text="Скачивание...")
        threading.Thread(target=self.download_and_install, daemon=True).start()

    def download_and_install(self):
        try:
            # Путь в TEMP пользователя
            temp_dir = tempfile.gettempdir()
            msi_path = os.path.join(temp_dir, MSI_NAME)

            # Скачивание с прогрессом
            self.download_file(MSI_URL, msi_path)

            # Запуск установки
            self.root.after(0, lambda: self.status_label.config(text="Запуск установки..."))
            
            cmd = f'msiexec /i "{msi_path}" ALLUSERS=2 MSIINSTALLPERUSER=1 /quiet'
            subprocess.Popen(cmd, shell=True)

            self.root.after(0, lambda: messagebox.showinfo("Готово", "Установка запущена"))
            self.root.after(0, self.root.destroy)

        except Exception as e:
            self.root.after(0, lambda: messagebox.showerror("Ошибка", str(e)))
            self.root.after(0, lambda: self.update_btn.config(state='normal'))
            self.root.after(0, lambda: self.status_label.config(text="Ошибка загрузки"))

    def download_file(self, url, dest):
        req = urllib.request.urlopen(url)
        total_size = int(req.headers.get('Content-Length', 0))
        downloaded = 0
        block_size = 8192

        with open(dest, 'wb') as f:
            while True:
                chunk = req.read(block_size)
                if not chunk:
                    break
                f.write(chunk)
                downloaded += len(chunk)

                if total_size > 0:
                    percent = (downloaded / total_size) * 100
                    self.root.after(0, lambda p=percent: self.progress.config(value=p))


if __name__ == "__main__":
    root = tk.Tk()
    app = UpdaterApp(root)
    root.mainloop()
