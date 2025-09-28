"""
Decision Tree Rule-Based for SmartKB
------------------------------------
Program sederhana untuk memberikan rekomendasi metode KB
berdasarkan umur, status pernikahan, jumlah anak, riwayat kesehatan, dan preferensi.

Author : [Mochammad Aprianto]
"""

def rekomendasi_kb(umur, menikah, anak, riwayat, preferensi):
    # Jika belum menikah
    if not menikah:
        return "Edukasi (belum perlu KB)"

    # Jika umur < 20
    if umur < 20:
        return "Kondom / Pil KB"

    # Jika umur 20–35
    if 20 <= umur <= 35:
        if anak <= 2:
            return "Pil KB / Suntik"
        else:
            return "IUD / Implan"

    # Jika umur > 35
    if umur > 35:
        return "IUD / Implan"

    # Jika ada riwayat penyakit tertentu
    if riwayat.lower() in ["hipertensi", "diabetes", "jantung"]:
        return "IUD (non-hormonal)"

    # Preferensi pengguna
    if preferensi.lower() == "jangka pendek":
        return "Kondom / Pil KB"
    if preferensi.lower() == "jangka panjang":
        return "IUD / Implan"
    if preferensi.lower() == "non-hormonal":
        return "IUD"

    # Default fallback
    return "Konsultasi langsung dengan petugas KB"


# --- Contoh Pengujian ---
if __name__ == "__main__":
    dataset = [
        (18, True, 0, "normal", "jangka pendek"),
        (22, True, 1, "normal", "jangka panjang"),
        (28, True, 3, "normal", "jangka panjang"),
        (30, True, 0, "hipertensi", "non-hormonal"),
        (40, True, 2, "diabetes", "jangka panjang"),
        (19, False, 0, "normal", "-")
    ]

    for data in dataset:
        umur, menikah, anak, riwayat, preferensi = data
        hasil = rekomendasi_kb(umur, menikah, anak, riwayat, preferensi)
        print(f"Input: {data} → Rekomendasi: {hasil}")
