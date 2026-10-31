# test ffi function call with the wrong number of arguments
try:
    import ffi
except ImportError:
    print("SKIP")
    raise SystemExit


def ffi_open(names):
    err = None
    for n in names:
        try:
            return ffi.open(n)
        except OSError as e:
            err = e
    raise err


libc = ffi_open(("libc.so", "libc.so.0", "libc.so.6", "libc.dylib"))
abs_ = libc.func("i", "abs", "i")

print(abs_(-1))
for args in ((), (1, 2)):
    try:
        abs_(*args)
    except TypeError:
        print("TypeError")

try:
    abs_(i=1)
except TypeError:
    print("TypeError")
