# -*- coding: utf-8 -*-
# @Date    : 2017-08-23 13:06:40
# @Author  : lileilei 
class Pagination:
    def __init__(self, current_page, all_item):
        try:
            page = int(current_page)
        except:
            page = 1
        if page < 1:
            page = 1
        all_pager, c = divmod(all_item, 10)
        if int(c) > 0:
            all_pager += 1
        self.current_page = page
        self.all_pager = all_pager
    @property
    def start(self):
        return (self.current_page - 1) * 10
    @property
    def end(self):
        return self.current_page * 10
    def string_pager(self, base_url="/index/"):
        if self.current_page == 1:
            prev = '<li><a href="javascript:void(0);">上一页</a></li>'
        else:
            prev = '<li><a href="%s%s">上一页</a></li>' % (base_url, self.current_page - 1,)
        if self.current_page == self.all_pager:
            nex = '<li><a href="javascript:void(0);">下一页</a></li>'
        else:
            nex = '<li><a href="%s%s">下一页</a></li>' % (base_url, self.current_page + 1,)
        last = '<li><a href="%s%s">尾页</a></li>' % (base_url, self.all_pager,)
        str_page = "".join((prev,nex,last))
        return str_page