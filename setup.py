import pathlib

from setuptools import find_packages, setup

long_description = pathlib.Path('README.md').read_text(encoding='utf-8')  # 读取README.md文件内容
setup(
    name='formatfinder',  # 包名
    version='0.1.0',  # 版本号
    author='AkagiYui',  # 作者
    author_email='akagiyui@yeah.net',  # 作者邮箱
    description='A library that can easily find out the format of a binary file.',  # 描述
    long_description=long_description,  # 将 README.md 内容作为长描述
    long_description_content_type='text/markdown',
    url='https://github.com/AkagiYui/FormatFinder',  # 项目地址

    packages=find_packages('src'),  # 在此目录中寻找软件包
    package_dir={'': 'src'},
    classifiers=[  # PyPI分类
        'Development Status :: 4 - Beta',  # 开发进度
        'Programming Language :: Python :: 3.9',  # 编程语言，可以支持多种
        'Intended Audience :: Developers',  # 目标用户，可以有多个
        'License :: OSI Approved :: MIT License',  # 开源许可证
        'Operating System :: OS Independent'  # 支持系统，这里是不受限于操作系统的
    ],
    python_requires='>=3.7',  # Python版本限制
)
