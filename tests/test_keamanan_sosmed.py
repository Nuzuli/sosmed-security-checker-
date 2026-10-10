import pytest
from keamanan_sosmed import cek_kekuatan_sandi

def test_sandi_lemah_kosong():
    assert cek_kekuatan_sandi("") == "lemah"

def test_sandi_lemah_pendek():
    assert cek_kekuatan_sandi("12345") == "lemah"

def test_sandi_lemah_huruf_saja():
    assert cek_kekuatan_sandi("abcdef") == "lemah"

def test_sandi_sedang():
    assert cek_kekuatan_sandi("abc123") == "sedang"

def test_sandi_kuat():
    assert cek_kekuatan_sandi("abc123!") == "kuat"

def test_sandi_kuat_panjang():
    assert cek_kekuatan_sandi("abcdefghij123!") == "kuat"
