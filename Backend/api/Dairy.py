from fastapi import APIRouter

router = APIRouter()
diaries: list[dict[str, str]] = []

@router.post("/Diary")
def membuat_diary(tanggal: str, judul: str, isi: str):
    diary_entry = {
        "Tanggal": tanggal,
        "Judul": judul,
        "Isi": isi,
    }
    diaries.append(diary_entry)
    return "Diary berhasil ditambahkan."

@router.get("/Diary")
def membaca_diary():
    return diaries

@router.delete("/Diary")
def menghapus_diary(urutan: int):
    del diaries[urutan - 1]
    return "Diary telah dihapuskan."

@router.put("/Diary")
def membenarkan_diary(urutan: int, pilihan: str, mengganti: str):
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
