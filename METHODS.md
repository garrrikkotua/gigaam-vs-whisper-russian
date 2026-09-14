# Methods and limitations

## Question

For one fixed sample of short Russian Crowd recordings, what corpus word error rate do archived CPU outputs from GigaAM v3 RNNT and Whisper large-v3 produce under the same text normalization?

## Data selection

The source was the `test` split of the Hugging Face mirror `bond005/sberdevices_golos_10h_crowd`, derived from the SberDevices Golos corpus. The archived benchmark took rows 0 through 199 from a local manifest. It did not draw a random or stratified sample.

The fixed sample contains:

- 200 utterances;
- 823.8469375 seconds of audio, about 13.7 minutes;
- 1,001 reference words after normalization.

`results.json` contains all 200 IDs, normalized references, audio SHA-256 values, and the hypotheses from each engine. Only the unmodified audio for row 0 is included in this repository.

## Engines

Both archived reports record `cpu` as the device.

| Report | Recorded model or engine identifier |
| --- | --- |
| GigaAM | Hugging Face repository [`ai-sage/GigaAM-v3`](https://huggingface.co/ai-sage/GigaAM-v3), revision name `rnnt` |
| Whisper | [`faster-whisper`](https://github.com/SYSTRAN/faster-whisper), model name `large-v3` |

The reports record model branch or model names, not immutable model-weight commit hashes or a complete environment lockfile. They are sufficient to identify the intended engines, but insufficient to guarantee bit-for-bit inference reproduction.

## Text normalization

The same normalization was applied before scoring both reports:

1. convert text to lowercase;
2. replace `ё` with `е`;
3. express numbers as words;
4. remove punctuation;
5. compare whitespace-separated words.

The JSON stores the normalized reference and hypothesis strings used for scoring. The included verifier scores those stored strings directly; it does not repeat a normalization pipeline.

## Metric

The benchmark reports corpus WER:

```text
WER = (substitutions + insertions + deletions) / total reference words
```

This is one edit-distance total across the corpus divided by one reference-word total. It is not the unweighted mean of per-utterance WER values.

| Model | Substitutions | Insertions | Deletions | Errors | Reference words | WER |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| GigaAM v3 RNNT | 12 | 2 | 1 | 15 | 1,001 | 1.4985% |
| Whisper large-v3 | 102 | 7 | 19 | 128 | 1,001 | 12.7872% |

`verify.py` implements word-level Levenshtein distance and asserts that the recalculated error and reference-word counts match the archived aggregates.

## Runtime records

The archived JSON records 146.51 seconds for GigaAM and 1,692.26 seconds for Whisper over 823.85 seconds of audio. These observations were not collected as a controlled performance study. The environment, warm-up state, concurrency, and immutable software revisions were not preserved, so the values should not be used as a model-speed ranking.

## Interpretation limits

- The sample consists of short Crowd-domain phrases and does not represent every Russian accent, acoustic setting, speaking style, or recording length.
- The deterministic first-200 selection can differ from a random sample of the complete 9,994-item Crowd test split.
- Training-data overlap for either model was not investigated.
- WER does not measure punctuation, capitalization, speaker labels, paragraph structure, readability, or manual correction time.
- This compares archived model outputs. It does not measure the accuracy or latency of a hosted transcription product.
- No statistical uncertainty interval or significance test is reported.

## Provenance timeline

- Archived report commit: `a08d53e`
- Archived report commit time: 2026-08-31 23:32:09 +03:00
- Initial web publication: 2026-09-05
- Public repository packaging: 2026-09-14

## Upstream references

- [SberDevices Golos repository](https://github.com/sberdevices/golos)
- [Hugging Face mirror used for the archived manifest](https://huggingface.co/datasets/bond005/sberdevices_golos_10h_crowd)
- [Golos: Russian Dataset for Speech Research](https://arxiv.org/abs/2106.10161)
- [Russian benchmark report](https://transkriba.ru/stati/gigaam-protiv-whisper)
