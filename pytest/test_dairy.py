import pytest
from Backend.api import Dairy


class TestDairy:
    def test_membuat_dairy_berhasil(self):
        hasil = Dairy.MembuatDiary("7 may 2026", "judul", "halo")
        assert hasil == "Diary berhasil ditambahkan."

    def test_membuat_dairy_gagal(self):
        assert Dairy.MembuatDiary(None, "judul", "halo") == "Diary gagal ditambahkan."
        assert Dairy.MembuatDiary("7 may 2026", None, "halo") == "Diary gagal ditambahkan."
        assert Dairy.MembuatDiary("7 may 2026", "judul", None) == "Diary gagal ditambahkan."
        assert Dairy.MembuatDiary(None, None, None) == "Diary gagal ditambahkan."



    def test_membaca_diary_berhasil(self):
        expected = [{'Tanggal': '7 may 2026', 'Judul': 'judul', 'Isi': 'halo'}]
        assert Dairy.MembacaDiary() == expected

    def test_membaca_diary_gagal(self):
        Dairy.diaries.clear()
        assert Dairy.membaca_diary() == "Tidak ada diary yang tersedia."



    def test_membenarkan_diary_berhasil(self):
        Dairy.diaries.clear()
        Dairy.MembuatDiary("7 may 2026", "judul", "halo")
        assert Dairy.MembenarkanDiary(1, "Isi", "assalamualaikum") == "Diary berhasil di ubah"

    def test_membenarkan_diary_gagal(self):
        Dairy.diaries.clear()
        Dairy.MembuatDiary("7 may 2026", "judul", "halo")
        assert Dairy.MembenarkanDiary(1, "tanggal", "12 may 2026") == "Pilihan tidak valid."
        assert Dairy.MembenarkanDiary(1, "pilihan", "12 may 2026") == "Pilihan tidak valid."
        assert Dairy.MembenarkanDiary(None, None, None) == "Urutan diary tidak valid."
        assert Dairy.MembenarkanDiary(0, "Isi", "test") == "Urutan diary tidak valid."
        assert Dairy.MembenarkanDiary(99, "Isi", "test") == "Urutan diary tidak valid."



    

    def test_menghapus_diary(self):
        Dairy.diaries.clear()
        Dairy.MembuatDiary("7 may 2026", "judul", "halo")
        assert Dairy.MenghapusDiary(1) == "Diary telah dihapuskan."
