# GigaAM vs Whisper: Russian ASR benchmark

This repository preserves a small, auditable comparison of **GigaAM v3 RNNT** and **Whisper large-v3** on the same 200 short Russian utterances from the Golos Crowd test split.

| Model | Word errors | Reference words | WER |
| --- | ---: | ---: | ---: |
| GigaAM v3 RNNT | 15 | 1,001 | **1.50%** |
| Whisper large-v3 | 128 | 1,001 | **12.79%** |

These numbers describe this fixed sample and normalization only. They are not a general accuracy claim for either model or for the Transkriba service.

## Verify the result

Python 3 is the only requirement:

```bash
python3 verify.py
```

Expected output:

```text
gigaam rnnt: 15/1001 words, WER 1.50%
whisper large-v3: 128/1001 words, WER 12.79%
```

The script recalculates edit distance from the archived references and hypotheses in `results.json`. It does not download models or rerun inference. See [METHODS.md](METHODS.md) for the sample, normalization, engines, and limits.

To verify the published files themselves:

```bash
sha256sum -c CHECKSUMS.sha256
```

On macOS, use `shasum -a 256 -c CHECKSUMS.sha256`.

## Files

- `results.json` contains the 200-item audio manifest, both archived reports, aggregate counts, provenance, and limitations.
- `verify.py` recalculates corpus WER without third-party packages.
- `example-000000.wav` is the unmodified first audio clip in the fixed sample.
- `license.pdf` is the original Golos data licence.
- `NOTICE.md` records attribution, changes, and file-level licensing.

The full Russian report, including an audio example and practical interpretation, is at [GigaAM и Whisper: замер на 200 записях Golos](https://transkriba.ru/stati/gigaam-protiv-whisper).

## What was measured

- Dataset: the first 200 rows of an archived local manifest from the Golos Crowd test split.
- Audio duration: 823.85 seconds, about 13.7 minutes.
- Device: CPU for both archived runs.
- GigaAM: [`ai-sage/GigaAM-v3`](https://huggingface.co/ai-sage/GigaAM-v3), branch or revision name `rnnt`.
- Whisper: [`faster-whisper`](https://github.com/SYSTRAN/faster-whisper), model name `large-v3`.
- Metric: corpus word error rate, `(substitutions + insertions + deletions) / reference words`.

The archived run recorded mutable model names rather than immutable weight hashes. Exact inference reproduction is therefore not guaranteed. This repository makes the inputs, outputs, aggregate arithmetic, and known limits inspectable.

## Main limitations

- The first 200 short Crowd clips are not a random sample of interviews, meetings, lectures, or customer recordings.
- WER ignores punctuation, speaker assignment, formatting, and editing time.
- Possible overlap between the evaluation audio and model training data was not ruled out.
- Runtime values are archived CPU observations, not a controlled speed benchmark.
- Only one audio file is redistributed here. The manifest stores SHA-256 hashes for all 200 files, but the other 199 recordings are not included.

## Source and licences

Golos was created by Alexander Denisenko, Angelina Kovalenko, Fedor Minkin, and Nikolay Karpov. This benchmark used the `bond005/sberdevices_golos_10h_crowd` Hugging Face mirror of the [SberDevices Golos corpus](https://github.com/sberdevices/golos).

`results.json` and `example-000000.wav` are distributed under the Golos **Public license with attribution and conditions reserved**, reproduced in `license.pdf`. The dataset licence is not a Creative Commons licence. The verifier and original documentation in this repository are licensed separately under MIT; see `LICENSE-CODE`. Read [NOTICE.md](NOTICE.md) before redistributing the data-derived files.

The material is provided as is, without warranties. The original authors and mirror maintainer do not endorse this benchmark or Transkriba.

## Citation

Use the metadata in [CITATION.cff](CITATION.cff). A DOI will be added to the citation metadata when the release is archived in a DOI-granting repository.

## Кратко по-русски

Это открытый архив сравнения GigaAM v3 RNNT и Whisper large-v3 на одинаковых 200 коротких русских записях Golos Crowd. Скрипт `verify.py` заново считает WER по сохранённым эталонам и гипотезам: 1,50% для GigaAM и 12,79% для Whisper. Он проверяет арифметику, но не запускает модели заново. Методика и ограничения описаны в [METHODS.md](METHODS.md), подробный разбор — [на сайте Транскрибы](https://transkriba.ru/stati/gigaam-protiv-whisper).
