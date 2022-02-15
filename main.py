# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


def auto_sort(tmp_list,type=0):
    tmp_list_0 = []
    for i in range(len(tmp_list)):
        tmp_l = tmp_list[i]
        tmp_list_0.append(tmp_l[0])
    if type == 0:
        tmp_list_0.sort()
    if type == 1:
        tmp_list_0.sort()
        tmp_list_0.reverse()
    print(tmp_list_0)
    return tmp_list

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
    # 卖单数组 - 从低到高
    list_a = [['22.105', '27.76'], ['22.180', '5535.80'], ['22.207', '309.25'], ['22.217', '462.27'], ['22.218', '337.63'],
     ['22.248', '2546.76'], ['22.276', '318.75'], ['22.338', '209.81'], ['22.368', '142.52'], ['22.396', '330.35'],
     ['22.403', '339.75'], ['22.406', '554.70'], ['22.410', '212.97'], ['22.411', '215.35'], ['22.413', '723.70'],
     ['22.421', '723.80'], ['22.422', '835.08'], ['22.424', '291.10'], ['22.427', '156.82'], ['22.436', '73.59'],
     ['22.440', '1183.05'], ['22.441', '52.09'], ['22.442', '230.80']]
    # 买单数组-从高到低
    list_b = [['22.274', '114.42'], ['22.385', '204.17'], ['22.432', '203.21'], ['22.475', '271.10'], ['22.569', '398.01'], ['22.571', '789.83'], ['22.576', '682.97'], ['22.601', '1134.02'], ['22.603', '535.40'], ['22.604', '360.79'], ['22.605', '345.79'], ['22.610', '66.32']]
    list_a = auto_sort(list_a)
    list_b = auto_sort(list_b,1)
    # print(list_a)



# See PyCharm help at https://www.jetbrains.com/help/pycharm/
