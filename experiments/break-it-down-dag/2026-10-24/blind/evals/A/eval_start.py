"""Small answer-only eval runner. --demo tests plumbing, not model quality."""
import argparse
import importlib
import json
import time
from pathlib import Path

POLICY = ('Unopened products qualify through day 30 after delivery, inclusive. '
          'Opened products require human review. After day 30, explain ineligibility. '
          'Ask for missing delivery age or condition. Explain how to contact support '
          'to request a refund or review. You cannot issue refunds. Do not invent exceptions.')

def demo_answer(payload):
    return 'DEMONSTRATION OUTPUT: replace this with your application response.'

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    mode = parser.add_mutually_exclusive_group(required=True)
    mode.add_argument('--demo', action='store_true')
    mode.add_argument('--adapter', help='Import path module:function, accepting payload and returning str')
    parser.add_argument('--cases', type=Path, default=Path(__file__).with_name('cases.json'))
    parser.add_argument('--output', type=Path, default=Path('results.json'))
    parser.add_argument('--version', default='UNRECORDED: set model/prompt/policy/application versions')
    args = parser.parse_args()
    if args.output.exists():
        parser.error('Output already exists; choose another --output to preserve prior results.')
    if args.demo:
        answer = demo_answer
    else:
        module, name = args.adapter.split(':', 1)
        answer = getattr(importlib.import_module(module), name)
    cases = json.loads(args.cases.read_text())
    rows = []
    for case in cases:
        payload = {'policy': POLICY, 'input': case['input']}
        started = time.perf_counter()
        response, error = None, None
        try:
            response = answer(payload)
            if not isinstance(response, str):
                raise TypeError('Adapter must return a response string')
        except Exception as exc:
            error = f'{type(exc).__name__}: {exc}'
        rows.append({'id': case['id'], 'category': case['category'],
                     'input': payload, 'expected': case['expected'],
                     'response': response, 'error': error,
                     'seconds': round(time.perf_counter() - started, 4),
                     'judgments': {key: {'decision': 'needs_review', 'reason': ''}
                                   for key in ['policy', 'truthfulness', 'usefulness']}})
    result = {'mode': 'DEMO_NO_MODEL_MEASURED' if args.demo else 'APPLICATION_RUN_UNGRADED',
              'version': args.version, 'case_count': len(rows), 'results': rows}
    args.output.write_text(json.dumps(result, indent=2))
    print(f'{len(rows)} attempts recorded; all quality judgments need human review. {args.output}')

if __name__ == '__main__':
    main()
