"""Recalculate archived corpus WER without a model, GPU or third-party packages.
Download results.json beside this file, then run: python3 verify.py
Source, attribution, modifications and dataset licence are in results.json/license.pdf.
This script verifies arithmetic, not model provenance or inference reproducibility.
"""
import json
from pathlib import Path

def distance(reference, hypothesis):
    previous = list(range(len(hypothesis) + 1))
    for i, word in enumerate(reference, 1):
        current = [i]
        for j, other in enumerate(hypothesis, 1):
            current.append(min(current[-1] + 1, previous[j] + 1, previous[j-1] + (word != other)))
        previous = current
    return previous[-1]

if __name__ == '__main__':
    data = json.loads(Path(__file__).with_name('results.json').read_text(encoding='utf-8'))
    ids = None
    for report in data['reports']:
        references = {row['id']: row['ref'] for row in report['utterances']}
        assert ids is None or ids == references, 'Models must share IDs and references'
        ids = references
        errors = sum(distance(row['ref'].split(), row['hyp'].split()) for row in report['utterances'])
        words = sum(len(row['ref'].split()) for row in report['utterances'])
        assert errors == report['aggregate']['errors'] and words == report['aggregate']['ref_words']
        print(f"{report['engine']} {report['revision']}: {errors}/{words} words, WER {100*errors/words:.2f}%")
