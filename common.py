import sys
from pathlib import Path

from machfs import Volume

CHECK_MARK = u'\N{check mark}'
CROSS_MARK = u'\N{cross mark}'

HFS_SEP = ':'


def tuple_to_hfs_path(path_tuple: ()) -> str:
    return HFS_SEP.join(path_tuple)


def file_exists(fpath: str):
    p: Path = Path(fpath)
    return p.is_file() and p.exists()


def ok():
    print(f'{CHECK_MARK} Ok')


def fail(message: str):
    print(f'{CROSS_MARK} {message}')
    sys.exit(-1)


def read_image(disk_image_path: str) -> Volume:
    v = Volume()
    with open(disk_image_path, 'rb') as f:
        flat = f.read()
        v.read(flat)
    return v
