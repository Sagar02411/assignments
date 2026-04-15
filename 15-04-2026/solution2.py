def safe_divide(a, b):
    try:
        result = a/b
        return result
    except Exception as e:
        print(f"error: {e}")
    except ZeroDivisionError:
        raise f"Can not devide by zero"
print(safe_divide(2,0))