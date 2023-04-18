from snirf import Snirf


def open_snirf(path: str | None = None) -> Snirf:
    if path:
        with Snirf(path, "r") as snirf:
            return snirf.copy()
    else:
        snirf = Snirf()
        return snirf
