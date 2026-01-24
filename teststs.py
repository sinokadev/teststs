def _run_test(tests, func, eq=lambda a, b: a == b):
    for case in tests:
        *args, expected = case
        result = func(*args)
        if not eq(result, expected):
            return False, args, expected, result
    return True, None, None, None

def teststs(tests, func, detail=False, eq=lambda a, b: a == b):
    ok, args, expected, result = _run_test(tests, func, eq)
    if not ok:
        if detail:
            print("Your code is shit")
            print("input:", args)
            print("expected:", expected)
            print("actual:", result)
        else:
            print("Your code is shit", args, result)
        return
    print("OK!")
