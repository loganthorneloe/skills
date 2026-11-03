def answer(payload):
    assert set(payload) == {'policy', 'input'}, 'Expected answers leaked to application'
    assert 'expected' not in payload['input']
    if payload['input']['days_since_delivery'] is None:
        return 123
    if payload['input']['days_since_delivery'] == 40:
        raise RuntimeError('Deliberate test failure')
    return 'Test fixture response; not a model answer.'
