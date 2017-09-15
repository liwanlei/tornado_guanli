# -*- coding: utf-8 -*-
# @Date    : 2017-09-15 13:04:17
# @Author  : lileilei 
import xlrd,xlwt
from xlutils.copy import copy
def datacel(filepath):
	file=xlrd.open_workbook(filepath)
	me=file.sheets()[0]
	nrows=me.nrows
	porject_id_list=[]
	casename_list=[]
	case_qianzhi_list=[]
	case_buzhou_list=[]
	case_yuqi_list=[]
	for i in range(1,nrows):
		porject_id_list.append(me.cell(i,0).value)
		casename_list.append(me.cell(i,2).value)
		case_qianzhi_list.append(me.cell(i,3).value)
		case_buzhou_list.append(me.cell(i,4).value)
		case_yuqi_list.append(me.cell(i,1).value)
	return porject_id_list,casename_list,case_qianzhi_list,case_buzhou_list,case_yuqi_list
