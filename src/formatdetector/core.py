import os
from io import BufferedReader
from pathlib import Path, PurePath
from typing import Optional, Union

from formatdetector.dicts import format_list


def _bytes_to_hex(bytes_: bytes) -> str:
    length = len(bytes_)
    hex_str = ''
    for i in range(length):
        t = '%x' % bytes_[i]
        if len(t) % 2:
            hex_str += '0'
        hex_str += t
    return hex_str.upper()


def get_file_header(file: Union[str, bytes, BufferedReader]) -> str:
    if isinstance(file, str):
        if not Path(file).is_file():
            raise TypeError(f'{file} is not a file or not exist')
        with open(file, 'rb') as f:
            bins = f.read(20)
    elif isinstance(file, bytes):
        bins = file[:20]
    elif isinstance(file, BufferedReader):
        bins = file.read(20)
    else:
        raise TypeError('file must be str, bytes or BufferedReader')
    if not bins:
        raise TypeError('file is empty')
    return _bytes_to_hex(bins).lower()


def get_file_format(file: Union[str, bytes, BufferedReader] = None, header: str = None, max_diff: int = 35) \
        -> Optional[list[str]]:
    """

    :param file: file path or bytes or BufferedReader
    :param header: directly check format with this header (ignore file name)
    :param max_diff: max diff between file header and format in name
    :return: format the file may be
    """
    if not file and not header:
        raise TypeError('file or header must be given')
    bins = header or get_file_header(file)
    for _ in range(max_diff + 1):
        for hex_code in format_list.keys():
            if bins.startswith(hex_code) or hex_code.startswith(bins):
                return format_list[hex_code]
        bins = bins[:-1]
    return None


if __name__ == '__main__':
    # Traversing test 遍历测试
    from formatdetector.dicts import text_file_suffix
    check_paths = ['D:/']
    appeared = set()
    for check_path in check_paths:
        for parent_path, _, file_list in os.walk(check_path):
            if '$RECYCLE.BIN' in parent_path:
                continue  # ignore recycle bin 忽略回收站
            if not file_list:
                continue  # 空文件夹
            for file_name in file_list:
                format_in_name = PurePath(file_name).suffix[1:].lower()  # format in file name 文件名中的扩展名
                if not format_in_name:
                    continue  # no format in file name 没有扩展名
                if format_in_name in text_file_suffix:
                    continue  # text file 文件名中的扩展名是文本文件
                abspath = str(Path(parent_path, file_name))  # absolute path 文件的绝对路径
                try:
                    file_header = get_file_header(abspath)  # file header 文件头
                    format_in_file = get_file_format(header=file_header)  # format in file 文件中的格式
                except Exception:
                    continue
                if not format_in_file:
                    format_in_file = ['unknown']
                if format_in_name in format_in_file:
                    continue  # format match 格式匹配
                couple = (tuple(format_in_file), format_in_name)
                if couple in appeared:
                    continue  # already appeared 已经出现过
                if format_in_file == ['unknown']:
                    continue  # unknown format 忽略未知格式，仅在校对模式使用，在新增模式请注释
                print(f'{format_in_name:>10} {str(format_in_file):>50} {file_header:>40}  {file_name}  {parent_path}')
                appeared.add(couple)
