# Pi Volume Control 🎚️

A lightweight Python script that lets you control your **laptop or PC's system volume** programmatically. No Raspberry Pi or GPIO needed — just pure Python and your computer's audio interface.

Perfect for:
- Custom keyboard volume shortcuts
- Automation scripts
- DIY software knobs
- Accessibility tools

---

## 🧠 Features

- 🔊 Increase and decrease system volume
- 🔇 Mute/unmute toggle
- 🖱️ Optional GUI or tray icon support (if extended)
- 🪟 Works on Windows (supports `pycaw` or `ctypes` methods)

---

## 🧰 Requirements

- Python 3.x
- Works best on **Windows**
- Required libraries:

```bash
pip install pycaw comtypes
