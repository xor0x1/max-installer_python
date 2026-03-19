# max-installer_python
GUI-инструмент для скачивания и установки MSI-пакета

# MSI Updater

Легковесная утилита на Python/tkinter для автоматического обновления или установки ПО.

## Возможности
- Скачивание MSI-файла по URL
- Прогресс-бар загрузки
- Установка в режиме per-user (MSIINSTALLPERUSER=1)
- Компилируется в standalone .exe

## Использование
1. Указать URL в переменной `MSI_URL`
2. Собрать: `pyinstaller --onefile --noconsole updater.py`
3. Распространить .exe пользователям

## ⚠️ Disclaimer
Это неофициальный инструмент, не связанный с разработчиками устанавливаемого ПО.
Используйте на свой страх и риск. Автор не несёт ответственности за возможные проблемы.


**Релиз:**
```
v1.0.1 — Исправлена ошибка загрузки на некоторых ПК
<urlopen error [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: self-signed certificate in certificate chain (_ssl.c:1010)>
