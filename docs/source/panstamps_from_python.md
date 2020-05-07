## Using Panstamps within Python

To use panstamps within your own scripts please read the full
documentation. But for those of you that can't wait, this snippet should
give you the basics:

``` python
from panstamps.downloader import downloader
from panstamps.image import image
fitsPaths, jpegPaths, colorPath = downloader(
    log=log,
    settings=False,
    downloadDirectory=False,
    fits=False,
    jpeg=True,
    arcsecSize=600,
    filterSet='gri',
    color=True,
    singleFilters=True,
    ra="70.60271",
    dec="-21.72433",
    imageType="stack",  # warp | stack
    mjdStart=False,
    mjdEnd=False,
    window=False
).get()

for j in jpegPaths:

    myimage = image(
        log=log,
        settings=False,
        imagePath=j
        arcsecSize=120,
        crosshairs=True,
        transient=False,
        scale=True,
        invert=False,
        greyscale=False
    ).get() 
```
