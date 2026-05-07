from fastapi import APIRouter
Router = APIRouter()

Diaries = []

@Router.post ("/Diary")
def MembuatDiary (Tanggal:str,Judul:str,Isi:str):
    Diary = {
        "Tanggalnya":Tanggal,
        "Judulnya":Judul,
        "Isi":Isi
        }
    Diaries.append(Diary)
    return "Diary berhasil ditambahkan."

@Router.get("/Diary")
def MembacaDiary ():
    return Diaries

@Router.delete ("/Diary")
def MenghapusDiary (Urutan:int):
    del Diaries[Urutan-1]
    return"Diary telah dihapuskan." 

@Router.put ("/Diary")
def MembenarkanDiary (Urutan:int,Pilihan:str,Mengganti:str):
    diary_dict = Diaries[Urutan-1]

    if Pilihan=="Tanggal":
        diary_dict["Tanggalnya"]=Mengganti
    elif Pilihan=="Judul":
        diary_dict["Judulnya"]=Mengganti
    elif Pilihan=="Isi":
        diary_dict["Isi"]=Mengganti
    else:
        return "Pilihan tidak valid"

    Diaries[Urutan-1] = diary_dict
    return"Diary berhasil di ubah"
