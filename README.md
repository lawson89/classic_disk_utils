# classic_disk_utils

Some disk utilities for classic mac os disk images based on machfs python
library

## Usage

1. Must have python 3 (tested on 3.10 but should run on 3.6+)
2. Create virtualenv
3. pip install -r requirements.txt

### List folders on disk image
```shell
python list_hfs_image.py /path/to/some.dsk
```


### Extract folder from disk image
```shell
python extract_hfs_folder.py /path/to/some.dsk Some:Folder:On:Image /local/folder/to/extract/to
```

### Help on any command use -h flag
```shell
python list_hfs_image.py -h
```

* I use this mainly for pulling folders of source code out of my minivmac disk
  image, so I can develop in ThinkC but check in via github 



