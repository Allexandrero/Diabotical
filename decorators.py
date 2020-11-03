import time


def sleep(timeout, retry=3):
    def the_real_decorator(function):
        def wrapper(*args, **kwargs):
            retries = 0
            while retries < retry:
                try:
                    value = function(*args, **kwargs)
                    if value is None:
                        return
                except:
                    time.sleep(timeout)  # Sleeping for {timeout} seconds
                    retries += 1

        return wrapper

    return the_real_decorator
