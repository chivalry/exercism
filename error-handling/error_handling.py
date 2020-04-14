def handle_error_by_throwing_exception():
    raise Exception('error message')


def handle_error_by_returning_none(input_data: str):
    if not input_data.isdigit():
        return None
    return int(input_data)


def handle_error_by_returning_tuple(input_data):
    if input_data.isdigit():
        return True, int(input_data)
    return False, None


def filelike_objects_are_closed_on_exception(filelike_object):
    try:
        filelike_object.open()
        filelike_object.do_something()
        filelike_object.close()
    finally:
        filelike_object.close()
