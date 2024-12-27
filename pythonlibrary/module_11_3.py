def introspection_info(obj):
    # тип
    obj_type = type(obj).__name__

    # атрибуты
    attributes = [attr for attr in dir(obj) if not callable(getattr(obj, attr)) and not attr.startswith("__")]

    # методы
    methods = [method for method in dir(obj) if callable(getattr(obj, method)) and not method.startswith("__")]

    # модуль
    obj_module = getattr(obj, '__module__', None)

    # документация
    docstring = getattr(obj, '__doc__', None)

    # имя класса
    class_name = getattr(obj, '__class__', None).__name__ if hasattr(obj, '__class__') else None

    info = {
        'type': obj_type,
        'attributes': attributes,
        'methods': methods,
        'module': obj_module,
        'docstring': docstring,
        'class_name': class_name
    }

    return info


number_info = introspection_info(42)
print(number_info)
