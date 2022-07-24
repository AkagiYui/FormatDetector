# FormatFinder

[![release](https://github.com/AkagiYui/FormatFinder/workflows/release/badge.svg)](https://github.com/AkagiYui/FormatFinder/actions?query=workflow%3Arelease)  [![pypi](https://img.shields.io/pypi/v/FormatFinder.svg)](https://pypi.org/project/formatfinder/) ![support-version](https://img.shields.io/pypi/pyversions/formatfinder)  [![license](https://img.shields.io/github/license/AkagiYui/FormatFinder)](https://github.com/AkagiYui/FormatFinder/blob/master/LICENSE)  [![commit](https://img.shields.io/github/last-commit/AkagiYui/FormatFinder)](https://github.com/AkagiYui/FormatFinder/commits/master)

A python library that can easily find out the real format of a binary file with a common format.

可以轻松找到一个常见格式的二进制文件的真实格式。

The result of the finder may be wrong, please be careful.

这个工具返回的结果可能是错误的，请谨慎使用。

If you find any bug or mistake, please report it in issues.

如果你发现了任何 bug 或者错误，请在 issues 中告诉我。

## Install 安装

```shell
pip install formatfinder
```

## Usage 使用

```python
from formatfinder import get_file_format

get_file_format('xxx.zip')  # ['zip', 'jar', 'apk', 'xapk']
get_file_format('fff.mp3')  # ['ogg'] # so the 'mp3' tag may be wrong
get_file_format('hhh')  # ['rar'] # now you find out the real format of the file with no extension name
```

## [Changelog 更新日志](https://github.com/AkagiYui/FormatFinder/blob/master/Changelog.md)

## Thanks 致谢

[python3通过文件头判断文件类型](https://blog.csdn.net/privateobject/article/details/78069500)
