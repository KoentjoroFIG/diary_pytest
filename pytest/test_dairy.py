import pytest
from Backend.api import Dairy


class TestDairy:
    def test_membuat_dairy(self):
        hasil = Dairy.MembuatDiary ("7 may 2026", "judul", "halo")

        assert hasil == "Diary berhasil ditambahkan."

    def test_membaca_diary(self):
        expected = [{'Tanggal': '7 may 2026', 'Judul': 'judul', 'Isi': 'halo'}]
        assert Dairy.MembacaDiary() == expected

    def test_membenarkan_diary(self):

        assert Dairy.MembenarkanDiary(0, "Isi", "assalamualaikum") == "Diary berhasil di ubah"

    def test_menghapus_diary(self): 

        assert Dairy.MenghapusDiary(0) == "Diary telah dihapuskan."

    def test_membenarkan_diary(self):
        expected= [{'Tanggalnya': '7 may 2026', 'Judulnya': 'judul', 'Isi': 'halo'}]

        assert Dairy.MembenarkanDiary (0,"Tanggal", "12 may 2026") == "Diary berhasil di ubah"

    

    
        






