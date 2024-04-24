meme_dict = {
            "CRINGE": "Garip ya da utandırıcı bir şey",
            "LOL": "Komik bir şeye verilen cevap",
            "CREEPY": "ürkütücü"
            }
            
            
word = input("anlamadığın bir kelimeyi benimle paylaş!")

if word in meme_dict:
    print(word, "kelimesinin anlamı =" , meme_dict[word])
else:
    print("maalasef verdiğiniz kelime listemde yok!!!")
