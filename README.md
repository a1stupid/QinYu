# QinYu

从HanLP借鉴学习，计划做一个简化版的语言处理工具包.

*Muti_task_leaning*
代码总共分为三个部分：**调用的模型变成组件部分，muti_task的模型实现部分，预测部分**

调用的模型变成组件部分：
代码核心是cls = getattr(importlib.import_module(module_name), class_name)，这里的module_name是multi_task_learning.py
这个模块，class_name是这个模块中的一个类MultiTaskLearning()，然后我们把实现了的类cls返回就可以。

muti_task的模型实现部分：
首先是初始化模型框架
然后是加载大模型
代码核心是obj.load(save_dir)，save_dir是加载预训练模型的地址，通过自己定义的load()函数来加载预训练模型。
