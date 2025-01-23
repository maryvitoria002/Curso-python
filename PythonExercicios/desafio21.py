from pygame import mixer
import time

mixer.init()

mixer.music.load(r'C:\Users\maryv\Downloads\musica.mp3')

mixer.music.play()

time.sleep(10**2)
