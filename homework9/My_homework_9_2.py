import time


class Clock:
    def __init__(self, _start_time, _time_style):
        self._start_time = _start_time
        self._time_style = _time_style

    def now(self):
        return self._time_style.format(
            '{0:.5f} sec'.format(time.time()-self._start_time)
        )


class Timer:
    def __init__(self, _time_style):
        self._time_style = _time_style

    def __enter__(self):
        return Clock(time.time(), self._time_style)

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass


if __name__ == '__main__':
    with Timer("Time: {}") as timer:
        print(timer)
        print('do_some_logic()')
        time.sleep(1)
        print(timer.now())
        print('do_some_logic2()')
        time.sleep(1)
        print(timer.now())

    with Timer("Time: {}") as timer:
        print(timer)
        print('do_some_logic()')
        print(timer.now())
        print('do_some_logic2()')
        print(timer.now())
