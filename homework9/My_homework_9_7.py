class UpperMethodsMeta(type):
    def __new__(mcs, name, bases, attrs):
        _new_attrs = {}
        for key, value in attrs.items():
            if key[0:2] != '__':
                _new_attrs[key.upper()] = value
            else:
                _new_attrs[key] = value

        return super(UpperMethodsMeta, mcs).__new__(mcs, name, bases, _new_attrs)

    def __call__(cls, *args, **kwargs):
        new_kwargs = {}
        for key, value in kwargs.items():
            new_kwargs[key.upper()] = value
        return super(UpperMethodsMeta, cls).__call__(*args, **new_kwargs)


class TmpClass(metaclass=UpperMethodsMeta):
    a = 7

    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)


if __name__ == '__main__':
    foo = TmpClass(r=1, t=89, p=5)
    print(foo.R, foo.T, foo.P, foo.A)
    g = '__method__'
