results_file = "results.txt"

# Aranacak kelime
search_word = "Nötr"

word_count = 0

with open(results_file, "r", encoding="utf-8") as file: # Dosyayı okuma modunda aç
    # Satırları oku
    for line in file:
        # Satırdaki kelimeleri ayır
        for word in line.split():
            # Aranan kelimeyi bulunduğu zaman sayacı arttır
            if word == search_word:
                word_count += 1

# Sonucu yazdır
print(f"'{search_word}' kelimesi {word_count} kez geçiyor.")
