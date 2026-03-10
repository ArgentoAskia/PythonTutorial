"""
在 Python 中，像 __name__ 这样以双下划线开头和结尾的变量（准确地说，通常是属性或方法）被统称为 "特殊属性" 或 "魔术方法/双下方法"。它们由 Python 解释器内部定义，用于实现各种语言特性、操作重载以及提供对象的内部接口。

可以使用dir()获取所有的内置属性
- __debug__: 	布尔值，如果 Python 未使用 -O 选项启动，则为 True。用于条件性地执行调试代码（常与 assert 配合）。
- __builtins__: 一个对**内置模块**（通常是 `builtins` 模块）的引用，或者是一个包含所有内置名称（如 `print`、`len`、`Exception` 等）的字典，在主模块（直接运行的脚本）中，`__builtins__` 通常就是 `builtins` 模块本身。在其他模块中，它可能是 `builtins` 模块的引用，或者是该模块的 `__dict__` 属性，具体取决于实现，但通常你可以直接通过它访问所有内置对象。
- __cached__: 字符串（路径）或 `None`， 当前模块被编译后生成的字节码文件（`.pyc` 文件）的**绝对路径**。
- __doc__: doc文档
- __file__: 字符串（文件路径）或 `None`, 当前模块的**文件路径**（绝对路径或相对路径，取决于加载方式）。
- __loader__:
- __name__: 当前模块的**名称**。 当模块被直接运行时，`__name__` 被设置为 `'__main__'`, 当模块被导入时，`__name__` 被设置为模块的完整导入名（如 `'os.path'`）。
- __package__: 模块所属包的名称。
- __spec__: __spec__ 是 Python 3.4 引入的一个模块级属性，它存储了一个 ModuleSpec（模块规范）对象，这个对象包含了关于如何加载、定位和执行一个模块的所有元数据。它是 Python 导入系统现代化（PEP 451）的核心部分，旨在替代旧版中分散的多个属性（如 __loader__、__file__ 等），提供一个统一且更强大的接口。
"""
print(dir())
print(f"__debug__ ==> {__debug__}")
print(f"__builtins__ ==> {__builtins__}")
# print(f'__cached__ ==> {__cached__}')
print(f'__doc__ ==> {__doc__}')
print(f'__file__ ==> {__file__}')
# print(f'__loader__ ==> {__loader__}')
print(f'__name__ ==> {__name__}')
print(f'__package__ ==> {__package__}')
# print(f'__spec__ ==> {__spec__}')
