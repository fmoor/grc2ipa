import pathlib
import unicodedata

import xpfcorpus


_grc_sgpntg_historical = xpfcorpus.Transcriber(
    "grc_sgpntg_historical",
    rules_file=pathlib.Path(__file__).parent / "grc_sgpntg_historical.rules",
)


def grc_sgpntg_historical(grc: str) -> str:
    normalized = unicodedata.normalize("NFC", grc)
    return "".join(_grc_sgpntg_historical.transcribe(normalized))
