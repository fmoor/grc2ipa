"""
SGPNTG = A Short Guide to the Pronunciation of New Testament Greek
"""

import pytest

import greek2ipa


def transcribe(grc: str) -> str:
    return "".join(greek2ipa.grc_sgpntg_historical.transcribe(grc))


@pytest.mark.parametrize(
    "grc,ipa",
    [
        ("γ", "ɣ"),
        ("γάμος", "ɣˈamo̞s̠"),
        ("γράφω", "ɣɾˈapʰo̞ː"),
        ("λόγος", "lˈo̞ɣo̞s̠"),
    ],
)
def test_γ(grc: str, ipa: str):
    """SGPNTG 4.1.1, pg 37"""
    assert ipa == transcribe(grc)


@pytest.mark.parametrize(
    "grc,ipa",
    [
        ("γείνεσθαι", "ʝˈiːnɛs̠tʰɛː"),
        ("ἐγένετο", "ɛʝˈεnεto̞"),
        ("λόγοι", "lˈo̞ʝy"),
    ],
)
def test_γ_before_front_vowels(grc: str, ipa: str):
    """SGPNTG 4.1.1, pg 37"""
    assert ipa == transcribe(grc)


@pytest.mark.parametrize(
    "grc,ipa",
    [
        ("σπόγγος", "s̠pˈo̞ŋɡo̞s̠"),
        ("φέγγος", "pʰˈεŋɡo̞s̠"),
        ("ἀγγαρεύω", "aŋɡaɾˈεβo̞"),
    ],
)
def test_γ_after_nasal_consonant(grc: str, ipa: str):
    """SGPNTG 4.1.1, pg 39"""
    assert ipa == transcribe(grc)


@pytest.mark.parametrize(
    "grc,ipa",
    [
        ("ἄγγελος", "ˈaɲɟεlo̞s̠"),
        ("ἐγγύς", "εɲɟˈys̠"),
        ("ἐγγίζειν", "εɲɟˈiz̠in"),
    ],
)
def test_γ_after_nasal_consonant_and_before_front_vowels(grc: str, ipa: str):
    """SGPNTG 4.1.1, pg 40"""
    assert ipa == transcribe(grc)


@pytest.mark.parametrize(
    "grc,ipa",
    [
        ("σάλπιγγα", "s̠ˈalpiŋɡa"),
    ],
)
def test_γ_before_velar_consonants(grc: str, ipa: str):
    """SGPNTG 4.1.1, pg 41"""
    assert ipa == transcribe(grc)


# SGPNTG 4.1.5, pg 52
@pytest.mark.parametrize(
    "grc,ipa",
    [
        ("φ", "pʰ"),
    ],
)
def test_φ(grc: str, ipa: str):
    assert ipa == transcribe(grc)


# SGPNTG 4.1.11, pg 67
@pytest.mark.parametrize(
    "grc,ipa",
    [
        ("μ", "m"),
    ],
)
def test_μ(grc: str, ipa: str):
    assert ipa == transcribe(grc)


# SGPNTG 4.1.13, pg 71
@pytest.mark.parametrize(
    "grc,ipa",
    [
        ("λ", "l"),
    ],
)
def test_λ(grc: str, ipa: str):
    assert ipa == transcribe(grc)


# SGPNTG 4.1.14, pg 72
@pytest.mark.parametrize(
    "grc,ipa",
    [
        ("ρ", "ɾ"),
    ],
)
def test_ρ(grc: str, ipa: str):
    assert ipa == transcribe(grc)


# SGPNTG 4.1.15, pg 73
@pytest.mark.parametrize(
    "grc,ipa",
    [
        ("σ", "s̠"),
        ("ς", "s̠"),
    ],
)
def test_σ(grc: str, ipa: str):
    assert ipa == transcribe(grc)


# SGPNTG 4.3.5, pg 98
@pytest.mark.parametrize(
    "grc,ipa",
    [
        ("α", "a"),
    ],
)
def test_α(grc: str, ipa: str):
    assert ipa == transcribe(grc)


# SGPNTG 4.3.6, pg 99
@pytest.mark.parametrize(
    "grc,ipa",
    [
        ("ω", "o̞ː"),
    ],
)
def test_ω(grc: str, ipa: str):
    assert ipa == transcribe(grc)


# SGPNTG 4.3.6, pg 99
@pytest.mark.parametrize(
    "grc,ipa",
    [
        ("ο", "o̞"),
    ],
)
def test_ο(grc: str, ipa: str):
    assert ipa == transcribe(grc)
