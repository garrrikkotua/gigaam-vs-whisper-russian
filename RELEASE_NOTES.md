# GigaAM vs Whisper Russian ASR benchmark v1.0.0

This release freezes the public audit package for the 200-utterance Golos Crowd comparison.

- GigaAM v3 RNNT: 15 errors / 1,001 reference words, 1.50% corpus WER.
- Whisper large-v3: 128 errors / 1,001 reference words, 12.79% corpus WER.
- Includes archived hypotheses and references, a dependency-free verifier, one unmodified audio example, checksums, methods, attribution, and the original data licence.

The verifier reproduces the reported arithmetic. The archived run did not retain immutable model-weight hashes or a complete environment lockfile, so the release does not claim exact inference reproduction.
