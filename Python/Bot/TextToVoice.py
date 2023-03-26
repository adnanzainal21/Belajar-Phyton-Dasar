from gtts import gTTS

text = "Apa kabar semuaa..."
bahasa = "id"

filesaya = gTTS(text=text, lang=bahasa )

filesaya.save("apakabar.mp3")
print("filetersimpan")