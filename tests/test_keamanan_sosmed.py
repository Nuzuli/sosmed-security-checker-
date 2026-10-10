import pytest
from keamanan_sosmed import cek_kekuatan_sandi

def test_sandi_lemah():
    assert cek_kekuatan_sandi("123456") == "lemah"

def test_sandi_sedang():
    assert cek_kekuatan_sandi("Anak123!") == "sedang"

def test_sandi_kuat():
    assert cek_kekuatan_sandi("Kucing#99Bunga$") == "kuat"

def test_kosong():
    assert cek_kekuatan_sandi("") == "lemah"
