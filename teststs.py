def _run_test(case, func, eq):
    *args, expected = case
    try:
        result = func(*args)
    except Exception as error:
        return False, args, expected, None, error
    if not eq(result, expected):
        return False, args, expected, result, None

    return True, None, None, None, None

def teststs(tests, func, detail=False, failed_stop=True, eq=lambda a, b: a == b):
    for case in tests:
        ok, args, expected, result, error = _run_test(case, func, eq)
        if not ok:
            if detail:
                print("Test failed")
                print("input:", args)
                print("expected:", expected)
                print("actual:", result)
                if error:
                    print("error:", error)
            else:
                print("Test failed:", args, result)
            if failed_stop:
                return
    print("OK!")
