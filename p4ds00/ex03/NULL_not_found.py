def NULL_not_found(obj: any) -> int:
    if obj is None:
        print("Nothing:", obj, "<class 'NoneType'>")
    elif isinstance(obj, float) and obj != obj:
        print("Cheese:", obj, "<class 'float'>")
    elif obj == 0:
        print("Zero:", obj, "<class 'int'>")
    elif isinstance(obj, str) and len(obj) == 0:
        print("Empty:", "<class 'str'>")
    elif isinstance(obj, bool) and not obj:
        print("Fake:", obj, "<class 'bool'>")
    else:
        print("Type not Found")
        return 1
    return 0