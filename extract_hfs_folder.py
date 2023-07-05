import argparse

from machfs import Volume, Folder

import common


def main():
    args = argparse.ArgumentParser()

    args.add_argument('hfs_image', help='Disk image', type=str)
    args.add_argument('hfs_folder', help='HFS Folder on disk image', type=str)
    args.add_argument('local_folder', help='Destination folder to extract to, files/folders within will be overwritten',
                      type=str)

    args = args.parse_args()
    hfs_image: str = args.hfs_image
    hfs_folder: str = args.hfs_folder
    local_folder: str = args.local_folder

    print(f'Checking if hfs image exists at {hfs_image} ...')
    if common.file_exists(hfs_image):
        common.ok()
    else:
        common.fail(f'{hfs_image} does not exist or is not a file')

    hfs: Volume = common.read_image(hfs_image)
    found_hfs_folder: bool = False
    print(f'Extracting {hfs_folder} -> {local_folder} ...')
    for p, obj in hfs.iter_paths():
        if type(obj) is Folder:
            obj: Folder
            image_hfs_folder = common.tuple_to_hfs_path(p)
            if image_hfs_folder == hfs_folder:
                obj.write_folder(local_folder)
                common.ok()
                found_hfs_folder = True
                break
    if not found_hfs_folder:
        common.fail(f'Unable to find {hfs_folder} on {hfs_image}')


if __name__ == '__main__':
    main()
