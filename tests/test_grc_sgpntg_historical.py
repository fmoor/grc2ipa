"""
SGPNTG = A Short Guide to the Pronunciation of New Testament Greek
"""

import pytest

import greek2ipa


def transcribe(grc: str) -> str:
    return greek2ipa.grc_sgpntg_historical(grc)


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
    """
    SGPNTG 4.1.1, pg 37

    Generally, the consonant γ is pronounced as IPA ɣ.
    """
    assert ipa == transcribe(grc)


@pytest.mark.parametrize(
    "grc,ipa",
    [
        ("γείνεσθαι", "ʝˈiːnɛs̠tʰɛː"),
        ("ἐγένετο", "ɛʝˈɛnɛto̞"),
        ("λόγοι", "lˈo̞ʝyː"),
    ],
)
def test_γ_before_front_vowels(grc: str, ipa: str):
    """
    SGPNTG 4.1.1, pg 37

    Before front vowels, namely ι, ει, υ, οι, η, ηι, ῃ, ε, or αι, γ is
    pronounced as IPA ʝ.
    """
    assert ipa == transcribe(grc)


@pytest.mark.parametrize(
    "grc,ipa",
    [
        ("σπόγγος", "s̠pˈo̞ŋɡo̞s̠"),
        ("φέγγος", "pʰˈɛŋɡo̞s̠"),
        ("ἀγγαρεύω", "aŋɡaɾˈɛβo̞"),
    ],
)
def test_γ_after_nasal_consonant(grc: str, ipa: str):
    """
    SGPNTG 4.1.1, pg 39

    After a nasal consonant, namely in the sequences (γ)γ or (ν)γ, γ is
    pronounced as the IPA ɡ.
    """
    assert ipa == transcribe(grc)


@pytest.mark.parametrize(
    "grc,ipa",
    [
        ("ἄγγελος", "ˈaɲɟɛlo̞s̠"),
        ("ἐγγύς", "ɛɲɟˈys̠"),
        ("ἐγγίζειν", "ɛɲɟˈiz̠in"),
    ],
)
def test_γ_after_nasal_consonant_and_before_front_vowels(grc: str, ipa: str):
    """
    SGPNTG 4.1.1, pg 40

    After a nasal consonant and before front vowels, namely in the sequences
    (γ)γ and (ν)γ followed by ι, ει, υ, οι, η, ηι, ῃ, ε, or αι then γ is
    pronounced as IPA ɟ.
    """
    assert ipa == transcribe(grc)


@pytest.mark.parametrize(
    "grc,ipa",
    [
        ("σάλπιγγα", "s̠ˈalpiŋɡa"),
        ("συγκαλεῖν", "s̠yŋkalˈiːn"),
        ("τυγχάνω", "tyŋkʰˈano̞ː"),
    ],
)
def test_γ_before_velar_consonants(grc: str, ipa: str):
    """
    SGPNTG 4.1.1, pg 41

    Before velar consonants, namely γ, κ, χ, ξ, the consonant γ is pronounced as ŋ.
    """
    assert ipa == transcribe(grc)


@pytest.mark.parametrize(
    "grc,ipa",
    [
        ("σάλπιγγι", "s̠ˈalpiɲɟi"),
        ("ἀνάγκη", "anˈaɲceː"),
        ("ἐλέγχειν", "ɛlˈɛɲcʰiːn"),
    ],
)
def test_γ_before_palatalized_velar_consonants(grc: str, ipa: str):
    """
    SGPNTG 4.1.1, pg 41

    Before palatalized velar consonants, namely in the sequence γ(γ), γ(κ), γ(χ)
    followed by ι, ει, υ, οι, η, ηι, ῃ, ε, or αι, then γ is pronounced as IPA ɲ.
    """
    assert ipa == transcribe(grc)


@pytest.mark.parametrize(
    "grc,ipa",
    [
        ("πρᾶγμα", "pɾˈaːŋma"),
        ("διωγμός", "dio̞ːŋmˈo̞s̠"),
        ("κήρυγμα", "cˈeːɾyŋma"),
    ],
)
def test_γ_before_bilabial_nasal(grc: str, ipa: str):
    """
    SGPNTG 4.1.1, pg 42

    Before the bilabial nasal, namely in the sequence γ(μ), the consonant γ
    is pronounced as IPA ŋ.
    """
    assert ipa == transcribe(grc)


@pytest.mark.parametrize(
    "grc,ipa",
    [
        ("βασιλεύς", "βas̠ilˈɛɸs̠"),
        ("λάβε", "lˈaβɛ"),
        ("βιβλίον", "βiβlˈio̞n"),
    ],
)
def test_β(grc: str, ipa: str):
    """
    SGPNTG 4.1.2, pg 43

    Generally, β is pronounced as IPA β.
    """
    assert ipa == transcribe(grc)


@pytest.mark.parametrize(
    "grc,ipa",
    [
        ("λαμβάνω", "lambˈano̞ː"),
        ("ἔμβολος", "ˈɛmbo̞lo̞s̠"),
        ("σύνβιος", "s̠ˈynbio̞s̠"),
    ],
)
def test_β_after_nasal_consonant(grc: str, ipa: str):
    """
    SGPNTG 4.1.2, pg 45

    After a nasal consonant, namely in the sequences (μ)β or (ν)β, β is
    pronounced as IPA b.
    """
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


@pytest.mark.parametrize(
    "grc,ipa",
    [
        ("κιβωτός", "ciβo̞ːtˈo̞s̠"),
        ("κεῖται", "cˈiːtɛː"),
        ("κοινωνία", "cyːno̞ːnˈia"),
        ("κηρύσσω", "ceːɾˈys̠o̞ː"),
        ("καί", "cˈɛː"),
    ],
)
def test_κ_before_front_vowels(grc: str, ipa: str):
    """
    SGPNTG 4.1.8, pg 59

    Before front vowels, namely ι, ει, υ, οι, η, ηι, ῃ, ε, or αι, κ is
    pronounced as IPA c.
    """
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


@pytest.mark.parametrize(
    "grc,ipa",
    [
        ("αὐτός", "aɸtˈo̞s̠"),
        ("εὐθέως", "ɛɸtʰˈɛo̞ːs̠"),
        ("ηὐχόμην", "eːɸkʰˈo̞meːn"),
    ],
)
def test_αυ_ευ_and_ηυ_before_voiceless_consonants(grc: str, ipa: str):
    """
    SGPNTG 4.2.1, pg 80

    Before voiceless consonants and in word-final position, this υ element is pronounced as IPA ɸ
    """
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
