from fastapi import APIRouter

router = APIRouter()
diaries: list[dict[str, str]] = []

@router.post("/Diary")
def membuat_diary(tanggal: str, judul: str, isi: str):
    if not tanggal or not judul or not isi:
        return "Diary gagal ditambahkan."
    
    diary_entry = {
        "Tanggal": tanggal,
        "Judul": judul,
        "Isi": isi,
    }
    diaries.append(diary_entry)
    return "Diary berhasil ditambahkan."

@router.get("/Diary")
def membaca_diary():
    if not diaries:
        return "Tidak ada diary yang tersedia."
    
    return diaries

@router.delete("/Diary")
def menghapus_diary(urutan: int):
    if type(urutan) != int or urutan < 1 or urutan > len(diaries):
        return "Urutan diary tidak valid."
    
    del diaries[urutan - 1]
    return "Diary telah dihapuskan."

@router.put("/Diary")
def membenarkan_diary(urutan: int, pilihan: str, mengganti: str):
    if type(urutan) != int or urutan < 1 or urutan > len(diaries):
        return "Urutan diary tidak valid."
    if pilihan not in ["Tanggal", "Judul", "Isi"]:
        return "Pilihan tidak valid."
    
    diary_dict = diaries[urutan - 1]

    if pilihan == "Tanggal":
        diary_dict["Tanggal"] = mengganti
    elif pilihan == "Judul":
        diary_dict["Judul"] = mengganti
    elif pilihan == "Isi":
        diary_dict["Isi"] = mengganti
    else:
        return "Pilihan tidak valid"

    diaries[urutan - 1] = diary_dict
    return "Diary berhasil di ubah"

# compatibility aliases
Router = router
MembuatDiary = membuat_diary
MembacaDiary = membaca_diary
MenghapusDiary = menghapus_diary
MembenarkanDiary = membenarkan_diary
