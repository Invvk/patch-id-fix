![](https://img.shields.io/badge/Python-3.8.5-green)

### Table of Contents
- [patch-id-fix](#patch-id-fix)
- [How to use](#how-to-use)
- [Licenses](#licenses)

# patch-id-fix
This simple python script that allows you to quickly rename patch files 0000-X.patch  in case the numbers are missed up.

# How to use
run the file and it will ask you to provide the directory that contains the missed up patches, then a starting id.<br>
Starting id is going to be used as the first id and then it will keep **increasing** each time it renames a file.

numbers such as `1.1` or `-1` is not allowed as a starting id. only Integers that is greater than 1.

# Licenses
This project uses [BSD 3-Clause "New" or "Revised" License](https://github.com/Invvk/patch-id-fix/blob/main/LICENSE).
