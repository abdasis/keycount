import keyboard

def count_keystrokes():
    keystrokes = 0

    def on_key_press(event):
        nonlocal keystrokes
        keystrokes += 1

    keyboard.on_press(on_key_press)

    input("Program sedang berjalan. Tekan 'Enter' untuk berhenti.")

    keyboard.unhook_all()

    print("Jumlah keystrokes:", keystrokes)

count_keystrokes()
