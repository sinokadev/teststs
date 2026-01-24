def _run_test(tests, func, eq=lambda a, b: a == b):    
    for case in tests:
        *args, expected = case
        try:
            result = func(*args)
        except Exception as error:
            return False, args, expected, result, error
        if not eq(result, expected):
            return False, args, expected, result, None

    return True, None, None, None, None

def teststs(tests, func, detail=False, eq=lambda a, b: a == b):
    ok, args, expected, result, error = _run_test(tests, func, eq)
    if not ok:
        if detail:
            print("Your code is shit")
            print("input:", args)
            print("expected:", expected)
            print("actual:", result)
            if error:
                print("error:", error)
        else:
            print("Your code is shit", args, result)
        return
    print("OK!")
