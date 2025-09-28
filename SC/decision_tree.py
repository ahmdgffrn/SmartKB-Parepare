def rekomendasi_kb(umur, menikah, anak, riwayat, preferensi):
    if not menikah:
        return "Edukasi (belum perlu KB)"
    if umur < 20:
        return "Kondom / Pil KB"
    if 20 <= umur <= 35:
        if anak <= 2:
            return "Pil KB / Suntik"
        else:
            return "IUD / Implan"
    if umur > 35:
        return "IUD / Implan"
    if riwayat in ["hipertensi", "diabetes", "jantung"]:
        return "IUD (non-hormonal)"
    if preferensi == "jangka pendek":
        return "Kondom / Pil KB"
    if preferensi == "jangka panjang":
        return "IUD / Implan"
    if preferensi == "non-hormonal":
        return "IUD"

print(rekomendasi_kb(22, True, 1, "normal", "jangka pendek"))
