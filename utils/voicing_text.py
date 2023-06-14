import tempfile
import gtts
import threading
import time
import ctypes
import os
import sounddevice as sd
import soundfile as sf


class Voicing:
    def __init__(self):
        self.temp_file = None

    def speak_text(self, txt_any):
        tts = gtts.gTTS(text=txt_any, lang="en")
        _, self.temp_file = tempfile.mkstemp(suffix=".mp3")
        tts.save(self.temp_file)

        thread = threading.Thread(target=self.play_audio)
        thread.start()

    def play_audio(self):
        data, samplerate = sf.read(self.temp_file)
        sd.play(data, samplerate)
        sd.wait()

        time.sleep(1)

        try:
            if self.temp_file is not None:
                os.unlink(self.temp_file)
        except OSError:
            # Если удаление файла не удалось, попробуйте использовать функцию ctypes.windll.kernel32.DeleteFileW
            ctypes.windll.kernel32.DeleteFileW(self.temp_file)

        self.temp_file = None
