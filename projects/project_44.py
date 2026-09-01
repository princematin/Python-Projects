def decorator_builder(validator):
    def decorator(func):
        def wrapper(*args, **kwargs):
            result = validator(*args, **kwargs)
            if result:
                return func(*args, **kwargs)
            else:
                return "error"
        return wrapper
    return decorator