# coding: utf-8

def t_table_print(table, has_caption=True, align_type="LEFT"):
    """t_table_print"""
    # max len of each field data
    field_max_len = {}
    for row in table:
        for index, item in enumerate(row):
            item_len = t_str_len(item)
            if index not in field_max_len:
                field_max_len[index] = item_len
                continue

            if field_max_len[index] < item_len:
                field_max_len[index] = item_len

    # format tpl of output
    content_tpl = "| "
    separation_tpl = "+-"
    separation_data = []
    for (index, fmlen) in field_max_len.items():
        content_tpl = content_tpl + "{} | "
        separation_tpl = separation_tpl + "{}-+-"
        separation_data.append(t_str_pad("", fmlen, "-", align_type))
    content_tpl = content_tpl.rstrip()
    separation_tpl = separation_tpl.rstrip("-")

    # output data
    print(separation_tpl.format(*separation_data))
    if has_caption:
        caption = table.pop(0)
        content = [t_str_pad(item, field_max_len[index], " ", align_type) for index, item in enumerate(caption)]
        print(content_tpl.format(*content))
        print(separation_tpl.format(*separation_data))
    for row in table:
        content = [t_str_pad(item, field_max_len[index], " ", align_type) for index, item in enumerate(row)]
        print(content_tpl.format(*content))
    print(separation_tpl.format(*separation_data))

def t_str_pad(istr, pad_len, pad_char, pad_type):
    """t_str_pad"""
    istr_len = t_str_len(istr)
    if (istr_len < pad_len):
        diff = pad_len - istr_len
        if pad_type == "RIGHT":
            istr = istr + pad_char * diff
        elif pad_type == "LEFT":
            istr = pad_char * diff + istr
        else: # CENTER
            ll = int(diff / 2)
            rl = diff - ll
            istr = pad_char * ll + istr + pad_char * rl

    return istr

def t_str_len(istr):
    """str_len"""
    # 一个汉字占2个字符，一个英文占1个字符
    return int((len(istr.encode("utf-8")) + len(istr)) / 2)


if __name__ == '__main__':
    istr = ['你好呀', 'abcd', 'ab哈哈cd']
    for s in istr:
        sl = t_str_len(s)
        # print(s + ': ' + str(sl))
        print('|' + t_str_pad(s, 12, ' ', 'CENTER') + '|')
        print('|' + t_str_pad(s, 12, ' ', 'RIGHT') + '|')
        print('|' + t_str_pad(s, 12, ' ', 'LEFT') + '|')
    print()

    table = [
        ["测试表头1", "测试表头2", "测试表头3", '测试表头4'],
        ["哈哈d", "dasfd12f", "哈哈哈哈", '123你好'],
        ["dalfja", "啦啦啦啦短发就是佛的", '大方nmm', '的沙发啊的'],
    ]
    t_table_print(table[0:])
    print()
    t_table_print(table[0:], has_caption=False)
    print()
    t_table_print(table[0:], has_caption=False, align_type="RIGHT")
    print()
    t_table_print(table[0:], has_caption=False, align_type="CENTER")
    print()
