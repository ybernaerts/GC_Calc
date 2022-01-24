import pytest
from gccalc import calc_gc_content
def test_mid_gc():
    seq = 'GCGCGCGCGCATATATATAT'
    exp = 50.0
    obs = calc_gc_content(seq)
    assert obs==exp

def test_high_gc():
    seq = 'GCGCGCGCGCGCGCGCGCGC'
    exp = 100.0
    obs = calc_gc_content(seq)
    assert obs==exp
    
def test_low_gc():
    seq = 'ATATATATATATATATATAT'
    exp = 0.0
    obs = calc_gc_content(seq)
    assert obs==exp
    
def test_empty_seq():
    seq = ""
    exp = 0.0
    obs = calc_gc_content(seq)
    assert obs==exp

@pytest.mark.skip(reason="Cleaning not yet implemented")
def test_invalid_characters():
    seq = "GCGCGCGCGCATATATATATXXXXX"
    exp = 50.0
    obs = calc_gc_content(seq)
    assert obs==exp