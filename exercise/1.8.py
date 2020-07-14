def eps(x, y):
    return True if - 0.001 <= x-y**3 <= 0.001 else False


def cbrt(x, y=2.1):
    if eps(x, y):
        return y
    else:
        return cbrt(x, (x/y**2+2*y)/3)


if __name__ == "__main__":
    print(cbrt(8))
