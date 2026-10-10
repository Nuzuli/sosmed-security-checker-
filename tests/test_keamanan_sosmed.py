import pytest
from keamanan_sosmed import cek_kekuatan_sandi

def test_sandi_kosong():
    assert cek_kekuatan_sandi("") == "lemah"

def test_sandi_pendek():
    assert cek_kekuatan_sandi("12345") == "lemah"

def test_sandi_huruf_saja():
    assert cek_kekuatan_sandi("abcdef") == "lemah"

def test_sandi_huruf_dan_angka():
    assert cek_kekuatan_sandi("abc123") == "sedang"

def test_sandi_lengkap_pendek():
    assert cek_kekuatan_sandi("abc123!") == "sedang"

def test_sandi_lengkap_panjang():
    assert cek_kekuatan_sandi("abc1234567!") == "kuat"
