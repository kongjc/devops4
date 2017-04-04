# coding=utf-8

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def getPages(request, obj_list, content):
    """分页器"""
    paginactor = Paginator(obj_list, 10)    # 实例化 Paginator, 将10个对象为1页
    page = request.GET.get("page", 1)       # 获取当前第几页(页码数),若没有该参数，默认为1
    before_index = 4        # 当前页往前几页
    after_index = 3         # 当前页往后几页

    try:
        page_obj = paginactor.page(page)        # 读取当前页的数据
        curr_page = request.GET.get("page", 1)  # 当前页

        start_index = page_obj.number - before_index

        if start_index < 0:
            start_index = 0

        show_page_range = page_obj.paginator.page_range[start_index: page_obj.number + after_index]
        print(show_page_range)

        content['show_page_range'] = show_page_range        # 最终给页面循环展示的 list
        content['page_obj'] = page_obj
        # content['curr_page'] = curr_page

    except PageNotAnInteger:
        # 异常处理，如果用户传递的page值不是整数，则把第一页的值返回给他
        page_obj = paginactor.page(1)

    except EmptyPage:
        # 如果用户传递的 page 值是一个空值，那么把最后一页的值返回给他
        page_obj = paginactor.page(paginactor.num_pages)
    # 返回当前页的数据

    return content