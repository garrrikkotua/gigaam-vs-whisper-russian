---
pretty_name: "GigaAM v3 vs Whisper large-v3 — Golos Crowd 200"
language:
  - ru
license:
  - other
task_categories:
  - automatic-speech-recognition
tags:
  - asr
  - speech-recognition
  - word-error-rate
  - gigaam
  - whisper
  - russian
size_categories:
  - n<1K
---

# GigaAM v3 vs Whisper large-v3 — Golos Crowd 200

This dataset card describes an archived comparison of GigaAM v3 RNNT and Whisper large-v3 on the same first 200 utterances from a saved Golos Crowd test manifest.

| Model | Errors / reference words | Corpus WER |
| --- | ---: | ---: |
| GigaAM v3 RNNT | 15 / 1,001 | 1.50% |
| Whisper large-v3 | 128 / 1,001 | 12.79% |

The repository and canonical files are at <https://github.com/garrrikkotua/gigaam-vs-whisper-russian>. The full Russian explanation is at <https://transkriba.ru/stati/gigaam-protiv-whisper>.

## Dataset contents

- `results.json`: 200 audio IDs and hashes, normalized references, model hypotheses, aggregate error counts, provenance, and limitations.
- `verify.py`: dependency-free Python script that recalculates corpus WER from the archived text.
- `example-000000.wav`: the unmodified row-0 audio example.
- `license.pdf` and `NOTICE.md`: source licence, attribution, and changes.

The card does not publish the other 199 audio files. It preserves their hashes and the text needed to audit the reported WER.

## Source

The source is the test split of `bond005/sberdevices_golos_10h_crowd`, a Hugging Face mirror derived from the SberDevices Golos corpus. Golos was created by Alexander Denisenko, Angelina Kovalenko, Fedor Minkin, and Nikolay Karpov.

- Upstream: <https://github.com/sberdevices/golos>
- Mirror used: <https://huggingface.co/datasets/bond005/sberdevices_golos_10h_crowd>
- Paper: <https://arxiv.org/abs/2106.10161>

## Selection and scoring

The archived sample contains rows 0–199, 823.85 seconds of audio, and 1,001 normalized reference words. References were lowercased, `ё` was replaced with `е`, numbers were expressed as words, and punctuation was removed. Corpus WER is total word-level substitutions, insertions, and deletions divided by total reference words.

`verify.py` checks the saved hypotheses and aggregate arithmetic. It does not rerun either speech-recognition model.

## Limitations

- This deterministic, short-utterance sample is not representative of every Russian speech setting.
- The reports identify mutable model names rather than immutable weight commits, so exact inference reproduction is not guaranteed.
- Training-data overlap was not ruled out.
- WER omits punctuation, speaker assignment, formatting, and correction time.
- Archived runtime observations are not a controlled speed comparison.

## Licence

The data-derived files use the Golos **Public license with attribution and conditions reserved**, categorized as `other` by the source mirror. It is not a Creative Commons licence. Read `license.pdf` and `NOTICE.md` before reuse. Original verifier code and documentation use the separate MIT licence in `LICENSE-CODE`.

The material is provided as is, without warranties or endorsement by the Golos authors, SberDevices, or the source mirror maintainer.

## Citation

Use `CITATION.cff` from the GitHub repository. A DOI will be added after a canonical release is deposited with a DOI-granting archive.
