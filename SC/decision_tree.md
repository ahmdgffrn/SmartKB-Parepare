# 📑 Decision Tree – SmartKB  

## 1. Tujuan  
Dokumen ini berisi implementasi awal **rule-based decision tree** untuk sistem konsultasi **SmartKB**. Aturan dibuat berdasarkan variabel: umur, status pernikahan, jumlah anak, riwayat kesehatan, dan preferensi pengguna.  

---

## 2. Variabel Input  
- **Umur** (tahun)  
- **Status Pernikahan** (Menikah / Belum)  
- **Jumlah Anak** (0, 1, 2, >2)  
- **Riwayat Kesehatan** (Normal, Hipertensi, Diabetes, Jantung, dll)  
- **Preferensi** (Jangka Pendek / Jangka Panjang / Non-Hormonal)  

---

## 3. Aturan Rule-Based  

| Kondisi                              | Rekomendasi KB                   |
|--------------------------------------|-----------------------------------|
| Belum menikah                        | Edukasi (tanpa KB)                |
| Umur < 20 & menikah                  | Kondom / Pil KB                   |
| Umur 20–35 & anak ≤ 2                | Pil KB / Suntik                   |
| Umur 20–35 & anak > 2                | IUD / Implan                      |
| Umur > 35                            | IUD / Implan                      |
| Riwayat hipertensi/diabetes/jantung  | IUD (non-hormonal)                |
| Preferensi jangka pendek             | Kondom / Pil KB                   |
| Preferensi jangka panjang            | IUD / Implan                      |
| Preferensi non-hormonal              | IUD                               |

---

## 4. Pseudocode  

```text
FUNCTION rekomendasi_kb(umur, menikah, anak, riwayat, preferensi):

    IF menikah == False:
        RETURN "Edukasi (belum perlu KB)"

    IF umur < 20:
        RETURN "Kondom / Pil KB"

    IF umur >= 20 AND umur <= 35:
        IF anak <= 2:
            RETURN "Pil KB / Suntik"
        ELSE:
            RETURN "IUD / Implan"

    IF umur > 35:
        RETURN "IUD / Implan"

    IF riwayat IN ["hipertensi", "diabetes", "jantung"]:
        RETURN "IUD (non-hormonal)"

    IF preferensi == "jangka pendek":
        RETURN "Kondom / Pil KB"

    IF preferensi == "jangka panjang":
        RETURN "IUD / Implan"

    IF preferensi == "non-hormonal":
        RETURN "IUD"

END FUNCTION
