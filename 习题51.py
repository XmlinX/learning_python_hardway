'''把用户输入的不规范的英文名字，变为首字母大写，其他小写的规范名字。输入：['adam', 'LISA', 'barT']，输出：['Adam', 'Lisa', 'Bart']'''


def to_stanrd(s):
    new_list = []
    for i in s:
        new = i.title()
        new_list.append(new)
        # print(new_list)
    # print(new_list)
    return new_list


if __name__ == "__main__":
    my_list = ['adam', 'LISA', 'barT']
    a = map(to_stanrd, my_list)
    print(list(a))