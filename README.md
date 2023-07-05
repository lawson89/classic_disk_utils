# classic_disk_utils

Some disk utilities for classic mac os disk images based on machfs python
library which does all the heavy lifting

https://github.com/elliotnunn/machfs

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

Example from when I sync my C code over for check in
```shell
python extract_hfs_folder.py /home/rlawson/classic_mac/minivmac/disk3.dsk "Development:THINK C:Projects:Mac C Primer" /home/rlawson/code/mac_c_primer
Checking if hfs image exists at /home/rlawson/classic_mac/minivmac/disk3.dsk ...
✓ Ok
Extracting Development:THINK C:Projects:Mac C Primer -> /home/rlawson/code/mac_c_primer ...
✓ Ok

```

### Help on any command use -h flag
```shell
python list_hfs_image.py -h
```

* I use this mainly for pulling folders of source code out of my minivmac disk
  image, so I can develop in ThinkC but check in via github 



