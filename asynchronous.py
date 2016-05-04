import threading

class NotYetDoneException(Exception):
    def __init__(self, message):
        self.message = message

class asynchronous:
    def __init__(self, fn):
        self.fn = fn
        self.t = None
        self.res = None

    def start(self, *args, **kwargs):
        def f(*args, **kwargs):
            self.res = self.fn(*args, **kwargs)
        self.t = threading.Thread(target=f, args=args, kwargs=kwargs)
        self.t.start()
        return self

    def is_done(self):
        return not self.t.is_alive()

    def get_result(self):
        if self.is_done(): return self.res
        raise NotYetDoneException('the call has not yet completed its task')
