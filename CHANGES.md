
## Release Notes

**v0.6.7 - June 7, 2024**

* **FIXED**: fixing broken downloader regex

**v0.6.6 - December 15, 2023**

* **FIXED**: broken init command (thanks to [@fforster](https://github.com/fforster) for reporting).

**v0.6.5 - February 23, 2023**

* **FIXED**: fixed bug in parsing FITS urls. This was resulting in empty FITS files getting downloaded. (thanks to [@fmannucci](https://github.com/fmannucci)
 for reporting the [issue](https://github.com/thespacedoctor/panstamps/issues/11).)

**v0.6.4 - January 19, 2023**

* **FIXED**: a change to the JPEG endpoint URLs broke regex looking for images. JPEG images should be downloadable again. (thanks to [@fforster](https://github.com/fforster)
 for reporting the [issue](https://github.com/thespacedoctor/panstamps/issues/9).)

**v0.6.3 - January 6, 2023**

* **refactor**: moving from plpsipp1v.stsci.edu to ps1images.stsci.edu as end point to collect panstars images (thanks to Rick White for the pull-request)

**v0.6.2 - May 11, 2022**

* **FIXED** doc fixes
* **UNFEATURE** Removing Python 2 support

**v0.6.1 - July 10, 2020**

* **ENHANCEMENT** Unit tests now added for command-line tools
* **FIXED** Command-line tools now correctly parse arguments
* **FIXED** Regex matching of warp image URLs updated to match filename changes made by STScI PanSTARRS image server

**v0.6.0 - May 7, 2020**

* Now compatible with Python 3.\*
