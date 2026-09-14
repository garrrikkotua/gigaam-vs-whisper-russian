# Attribution, changes, and licences

## Golos material

The source dataset is Golos, created by the SberDevices Team:

- Alexander Denisenko
- Angelina Kovalenko
- Fedor Minkin
- Nikolay Karpov

Upstream project: <https://github.com/sberdevices/golos>

Dataset mirror used for this archived benchmark: <https://huggingface.co/datasets/bond005/sberdevices_golos_10h_crowd>, maintained by `bond005`.

Original licence: **Public license with attribution and conditions reserved**. The complete English licence supplied by the upstream project is reproduced byte-for-byte as `license.pdf`. The source URL is <https://github.com/sberdevices/golos/blob/master/license/en_us.pdf>.

The upstream material is provided as is, without warranties. Nothing in this repository implies endorsement by the Golos authors, SberDevices, or the Hugging Face mirror maintainer.

## Data-derived files and changes

The following files are distributed under the Golos data licence in `license.pdf`:

- `example-000000.wav`: unmodified audio from row 0 of the fixed test sample.
- `results.json`: adapted benchmark material containing normalized Golos reference transcriptions and a manifest derived from the source data, plus machine-generated ASR hypotheses and benchmark metadata.

Changes represented in `results.json`:

- selected the first 200 rows of an archived local Golos Crowd test manifest;
- normalized reference text to lowercase;
- replaced `ё` with `е`;
- expressed numbers as words;
- removed punctuation;
- recorded audio SHA-256 values;
- added hypotheses produced by GigaAM v3 RNNT and Whisper large-v3;
- added error counts, provenance, and explicit limitations.

No additional legal or technical restrictions are imposed on those data-derived files.

## Original code and documentation

`verify.py`, `README.md`, `METHODS.md`, the GitHub Actions workflow, `CITATION.cff`, and other original repository-maintenance text are Copyright (c) 2026 Igor Kotua and licensed under MIT as stated in `LICENSE-CODE`.

`CHECKSUMS.sha256` is factual metadata and may be reused without restriction to the extent permitted by law.
