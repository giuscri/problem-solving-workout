import threading
import functools

class split_and_merge:
    def __init__(self, nthreads, recompose):
        self.nthreads = nthreads
        self.recompose = recompose
        # That's the threads' shared memory
        self.lst = []

    def __call__(self, f):

        def __f(l, lk):
            '''
            A wrapper around the wrapped function `f`.

            It will append to `self.lst` the returned value
            of `f` plus additional meta's about the thread
            that ran it.

            It will then notify the main thread that
            computation has finished.
            '''
            print('runner {}'.format(l))
            self.lst.append((threading.current_thread().name, f(l)))
            with lk: lk.notify()

        def _f(l):
            '''
            The function decorated: a set of threads
            will be created, then started.

            That's the main thread, that will wait for
            the whole threads set finish computation.

            It will then recompose the results.
            '''
            # Clean out the shared memory
            # from a previous call
            self.lst = []

            lk = threading.Condition()

            ts = []

            # Very dirty while loop, it would be better
            # to come out with something cleaner 
            i, thread_id = 0, 1
            while thread_id < self.nthreads and i < (len(l) - len(l)//self.nthreads) - 1:
                t = threading.Thread(target=__f, args=(l[i:i+len(l)//self.nthreads],lk), name=thread_id)
                ts.append(t)
                i += len(l)//self.nthreads
                thread_id += 1

            # Delegate to the last available thread
            # the remaining partition of the list
            t = threading.Thread(target=__f, args=(l[i:],lk), name=thread_id)
            ts.append(t)

            for t in ts:
                t.start()

            # Returns True, if all the threads in ts are dead
            completed = lambda ts=ts: \
                           functools.reduce(lambda x,y: x and y, \
                                               map(lambda t: not t.is_alive(), ts))

            # Acquire the lock and block if !completed
            with lk: lk.wait_for(completed)

            # Sort by thread-id ...
            self.lst.sort(key=lambda p: p[0])

            # ... and get a list of results only
            self.lst = list(map(lambda p: p[1], self.lst))

            return self.recompose(self.lst)

        return _f
