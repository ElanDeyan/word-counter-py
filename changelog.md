## **0.1.0**&emsp;<sub><sup>2024-03-30 (3eeb77ab7a98ee038085f72e3db768ed5d854061...6684e193d1c75489993888a54ee1a88460009dae)</sup></sub>

### Features

- adds lines, words commands to cli (778dc3fc715ba408fd458e013f1fb7afeb53b514)
- changes filename to path and prints as posix (02dab51befe9191127698c85ee3a7880d075ea1d)
- makes the xml output pretty printed (ed60c01834b2749b8ae38db486b378084c61adcb)
- transfers the logic from this directory (b90f50f7b8a146fed4a604816e1f4aa0de5c980b)
- moves the format option to a separated file (e5741d253cb649a94f75a433ecf8d05f1d25552b)
- supports the stdin content from cat command (1d60bf67bb4776839ea1b5af291b3e91be4076db)
- updates to handle TextIO also (607548e96e6ca52a9fe8688447630140ac39558a)
- adds support to read stdin and removes format option from the entry point (8ed743b01aff546d2e1d374f7585cf21afcadcd2)

##### &ensp;`chars`

- adds characters count command (ba82567fe2d2a7952bc2ffbaf12529c3b33d7526)
- adds chars command (db107d100416c82487681d6476f6266e2d5b34c0)
- adds output format and variadic arguments (ad3bc78e160a45e13228f1f7ee4781862098319a)

##### &ensp;`lines`

- adds the lines counter command (582918b142f0d49babfc9b6d11f448efddeda5fe)
- adds variadic arguments and output format (24f64e4a92bd2a351fb6ed3d56c29153aff992d6)

##### &ensp;`scan`

- adds a new command that shows all data of other commands (49f4cdf378dad954e8728e3509fdcdfe5f7e3681)

##### &ensp;`size`

- adds size of a file option (25792f906375d04b77908cc762813034610a7f2e)
- adds exaustively match again and adds helper function (1c6daa12d866e2e90dc7d6e88abf5939716ae0d2)
- adds variadic files arguments and refactors (70f7d4ae1f184744a21d2817a75c93a08582a11c)
- adds \-\-format option to the output format (03f0c5a9ebc1a49324e2649a91dbe3f1fe57eb47)
- adds prompt and case insensitive for unit option (5f3905b78b3ba5cc3e2ccc981c029bf6819d302a)
- add a new option to specify decimal precision (d27623893f89ec682e6dc3ee224beac730cf50e3)

##### &ensp;`words`

- adds word counter command (f39cc9113e29a63fec2ecc7ebce5ac184d69b90c)
- adds variadic number of files and output format (efe50761da4851ba72796d1dc840b5468ca30027)
- renames and prints filepath (15b120cf8f8f0283e1b820a1163310b0a76d78cc)

### Bug Fixes

- improves prompt message (d94f5c0ba69380059966bc71374311f02126daf6)
- fixes logic for conversion between bytes to other formats (9de6e28f6768cd70189e780ddb15828d2fd8b20d)

### ? ? ?

- Initial commit (3eeb77ab7a98ee038085f72e3db768ed5d854061)


### BREAKING CHANGES
-  now core functions handle only str data (b6fea3e82ce4e1e6db73d113aac9322a37d418c0)
-  filesize now backs to deal with path (8d0f6c3b47a0bd451dce62566a5bf80b2f48d376)
<br>


