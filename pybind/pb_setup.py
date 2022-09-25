import pybind11
from distutils.core import setup, Extension

ext_modules = [
    Extension(
        'cppExtension', # название нашей либы
        ['calculate.cpp', 'main.cpp'], # файлики которые компилируем
        include_dirs=[pybind11.get_include()],  # не забываем добавить инклюды pybind11
        language='c++',
        extra_compile_args=['-std=c++11'],  # используем с++11
    ),
]

setup(
    name='cppExtension',
    version='0.0.1',
    author='Nover',
    author_email='onverx@gmail.com',
    description='pybind11 extension that calculates matrix for Poisson PDE',
    ext_modules=ext_modules,
    requires=['pybind11']  # не забываем указать зависимость от pybind11
)