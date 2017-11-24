# -*- coding: UTF-8 -*-
import sys
import os
reload(sys)
sys.setdefaultencoding('gbk')

class TABFILE:
    def __init__(self, filename, dest_file=None):
        self.filename = filename
        if not dest_file:
            self.dest_file = filename
        else:
            self.dest_file = dest_file
        self.filehandle = None
        self.content = [] # content包含包含头部在内的所有信息,一维,只作为中间变量使用
        self.initflag = False
        self.column = 0 # 列长
        self.row = 0    # 行长
        self.data = []  # 包含去除头部的信息,二维
        self.head = []  # 头部列表

    def Init(self):
        try:
            self.filehandle = open(self.filename, 'r')
            self.initflag = self._load_file()
        except:
            pass
        else:
            self.initflag = True
        return self.initflag

    def UnInit(self):
        if self.initflag:
            self.filehandle.close()

    def _load_file(self):
        if self.filehandle:
            flag = False
            self.content = self.filehandle.readlines()
            self.row = len(self.content) - 1
            self.head = self.content[0].rstrip('\n').split('\t')
            self.column = len(self.head)
            for line in self.content:
                # 这里需要去掉末尾的换行
                if flag == False:
                    flag = True
                    continue
                self.data.append(line.rstrip('\n').split('\t'))
            return True
        else:
            return False

    def GetValue(self, row, column):
        if 0 <= row < self.row and 0 <= column < self.column:
            return self.data[row][column]
        else:
            return None

    def SetValue(self, row, column, value):
        if 0 <= row < self.row and 0 <= column < self.column:
            self.data[row][column] = value
        else:
            return False

    def GetColIndexByName(self, name):
        for index, ColName in enumerate(self.head):
            if ColName == name:
                return index
        return -1

    def GetColNameByIndex(self, index):
        if 0 <= index < self.column:
            return self.head[index]
        else:
            return None

    def AddOneEmptyRowBehind(self):
        row = []
        for index in range(self.column):
            row.append("")
        self.data.append(row)
        self.row += 1
        return True

    def InsertOneEmptyRowByIndex(self, index):
        if not (0 <= index < self.column):
            return False
        row = []
        for index in range(self.column):
            row.append("")
        self.data.insert(index, row)
        self.row += 1
        return True

    def AddOneRowBehind(self, row):
        if (not isinstance(row, list)) or len(row) != self.column:
            return False
        self.data.append(row)
        self.row += 1
        return True

    def InsertOneRowByIndex(self, index, row):
        if not (0 <= index < self.column):
            return False
        if not isinstance(row, list) or len(row) != self.column:
            return False
        self.data.insert(index, row)
        self.row += 1
        return True

    def AddOneEmptyColBehind(self, colName):
        if (not isinstance(colName, str)) or len(colName) == 0:
            return False
        self.head.append(colName)
        for index, row in enumerate(self.data):
            self.data[index].append("")
        self.column += 1
        return True

    def InsertOneEmptyColByIndex(self, index, colName):
        if (not isinstance(colName, str)) or (len(colName) == 0) or not (0 <= index < self.column):
            return False
        self.head.insert(index, colName)
        for n, row in enumerate(self.data):
            self.data[n].insert(index, "")
        self.column += 1
        return True

    def InsertOneColByIndexWithContent(self, index, colName, content):
        if (not isinstance(colName, str)) or (len(colName) == 0) or not (0 <= index < self.column):
            return False
        self.head.insert(index, colName)
        for n, row in enumerate(self.data):
            self.data[n].insert(index, content)
        self.column += 1
        return True

    def DeleteRowByIndex(self, index):
        del self.data[index]
        self.row -= 1

    #只删除一个,要删除多个请循环删除
    def DeleteOneRowByContent(self, col, content):
        for index, data in enumerate(self.data):
            if data[col] == content:
                self.DeleteRowByIndex(index)
                return True
        return False

    def SaveToFile(self):
        filewrite = open(self.dest_file, 'w')
        if not filewrite:
            return False
        sep_char = '\t'
        filewrite.write(sep_char.join(self.head) + '\n')
        for line in self.data:
            filewrite.write(sep_char.join(line) + '\n')
        filewrite.close()
        return True
