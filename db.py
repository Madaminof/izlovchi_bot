import os
import json

def get_message_id(kino_kodi):
    # Loyihaning asosiy katalogini aniqlash
    base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "channel_upload_bot"))
    json_path = os.path.join(base_dir, "kino_codes.json")

    print(f"JSON faylning yo'li: {json_path}")  # Tekshirish uchun yo'lni chiqarish

    try:
        # Faylni ochish va o'qish
        with open(json_path, "r", encoding="utf-8") as file:
            data = json.load(file)
            # Kino kodi bo'yicha message_id ni qaytarish
            return data.get(kino_kodi)
    except FileNotFoundError:
        print(f"Fayl topilmadi: {json_path}")
        return None
    except json.JSONDecodeError:
        print("JSON formatida xatolik mavjud.")
        return None
