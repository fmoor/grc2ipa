import pathlib

import xpfcorpus

grc_sgpntg_historical = xpfcorpus.Transcriber(
    'grc_sgpntg_historical',
    rules_file=pathlib.Path(__file__).parent / "grc_sgpntg_historical.rules",
)
