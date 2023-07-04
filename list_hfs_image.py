import argparse

from machfs import Volume, Folder

import common


def main():
    args = argparse.ArgumentParser()

    args.add_argument('hfs_image', help='Disk image', type=str)

    args = args.parse_args()
    hfs_image: str = args.hfs_image

    print(f'Checking if hfs image exists at {hfs_image} ...')
    if common.file_exists(hfs_image):
        common.ok()
    else:
        common.fail(f'{hfs_image} does not exist or is not a file')

    hfs: Volume = common.read_image(hfs_image)
    print(f'Listing folders on {hfs_image}')
    for p, obj in hfs.iter_paths():
        if type(obj) is Folder:
            obj: Folder
            image_hfs_folder = common.tuple_to_hfs_path(p)
            print(image_hfs_folder)
    common.ok()


if __name__ == '__main__':
    main()
