# -- coding: utf-8 --
'''
@author:rushi
@version:1.0.0
@time:2022/1/26 17:08
python setup.py build_ext --inplace
'''
from distutils.core import setup
from Cython.Build import cythonize
setup(ext_modules=cythonize(
    [
        'src/aioquant/*.py',
        'src/aioquant/platform/*.py',
        #'src/aioquant/utils/*.py',
        'src/datas/*.py',
        'src/markets/*.py',
        'src/strategy/*.py'
    ]
))