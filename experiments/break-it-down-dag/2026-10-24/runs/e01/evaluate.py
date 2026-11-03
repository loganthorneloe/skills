"""Small eval runner; use --self-test to verify runner without calling a model.
Real use: python3 evaluate.py --adapter my_app:answer --output results.jsonl
answer(*, message, context, policy) -> dict with decision and reply.
Only input/context/policy go to the app; expected decisions remain hidden.
"""
import argparse
import importlib
import json
from pathlib import Path
from time import perf_counter

POLICY = ('Fictional shop, policy v1: An unused item is eligible for return '
          'within 30 calendar days of delivery, including day 30. Used items '
          'and items delivered more than 30 days ago are ineligible. '
          'If delivery age or used status is missing, ask for it. '
          'For damaged items, escalate to a human regardless of age or use. '
          'Give advice only; do not claim to issue a refund. '
          'Return a dict with decision (eligible, ineligible, ask, escalate) '
          'and a customer-facing reply.')
CASES = [
    dict(id='day14', message='Can I return this?', context=dict(days=14, used=False, damaged=False), expected='eligible'),
    dict(id='day30', message='Can I return this?', context=dict(days=30, used=False, damaged=False), expected='eligible'),
    dict(id='day31', message='Can I return this?', context=dict(days=31, used=False, damaged=False), expected='ineligible'),
    dict(id='used', message='I used it once. Can I return it?', context=dict(days=14, used=True, damaged=False), expected='ineligible'),
    dict(id='unknown', message='Can I return this?', context=dict(used=False, damaged=False), expected='ask'),
    dict(id='damage', message='It arrived broken.', context=dict(days=40, used=True, damaged=True), expected='escalate'),
]

def evaluate(answer, output, repeats=3):
    rows = []
    for case in CASES:
        for trial in range(repeats):
            start = perf_counter()
            raw, error = None, None
            try:
                raw = answer(message=case['message'], context=case['context'].copy(), policy=POLICY)
                valid = (isinstance(raw, dict) and raw.get('decision') in {'eligible','ineligible','ask','escalate'}
                         and isinstance(raw.get('reply'), str) and bool(raw['reply'].strip()))
                matched = valid and raw['decision'] == case['expected']
                json.dumps(raw)  # fail clearly if the adapter returns an SDK object
            except Exception as exc:
                raw, error, valid, matched = repr(raw), repr(exc), False, False
            rows.append(dict(case_id=case['id'], trial=trial+1, expected=case['expected'],
                output=raw, error=error, schema_pass=valid, decision_pass=matched,
                latency_seconds=round(perf_counter()-start, 4), human_review='pending'))
    output.write_text('\n'.join(json.dumps(row) for row in rows)+'\n')
    print(f"Decision checks: {sum(row['decision_pass'] for row in rows)}/{len(rows)}")
    print('Replies still require human review; this is not an overall quality score.')
    return rows

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--adapter', help='Python module:function for your real application')
    parser.add_argument('--output', type=Path, default=Path('results.jsonl'))
    parser.add_argument('--self-test', action='store_true')
    args = parser.parse_args()
    if args.self_test:
        # Deliberately bad fixture: verify failures and denominator, not model quality.
        rows = evaluate(lambda **kwargs: dict(decision='eligible', reply='Fixture only.'), args.output)
        assert len(rows) == 18 and sum(r['decision_pass'] for r in rows) == 6
        assert all(r['human_review'] == 'pending' for r in rows)
        print('Runner self-test PASS (fixture; no model API called).')
    elif args.adapter:
        module, function = args.adapter.split(':', 1)
        evaluate(getattr(importlib.import_module(module), function), args.output)
    else:
        parser.error('Provide --adapter module:function or --self-test')
