import threading

class NotYetDoneException(Exception):
    def __init__(self, s):
        self.message = s

class asynchronous:
    def __init__(self, f):
        self.f = f

    def start(self, *args, **kwargs):
        def _f(*args, **kwargs):
            self.res = self.f(*args, **kwargs)
        self.t = threading.Thread(target=_f, args=args, kwargs=kwargs)
        self.t.start()
        return self

    def is_done(self):
        return not self.t.is_alive()

    def get_result(self):
        if not self.is_done():
            raise NotYetDoneException('the call has not yet completed its task')
        return self.res
