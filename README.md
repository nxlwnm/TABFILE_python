# TABFILE_python
py file to read .tab file

起源是以前随便找的一个tab读写类，后来发现不仅反程序员，而且bug极多，后来花了点时间自己重写了一遍

功能:
get
set
add
insert
delete
常用的CURD都有，并且添加了一些自己比较常用的函数，源代码都在这

使用：
1，
tab = TABFILE.TABFILE( filepath )
tab.Init()

tab.SaveToFile()
没了，记得要Init一下就好了，不喜欢Init的自己写进构造函数
