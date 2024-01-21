def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.
    intervals = [[2,3],[2,2],[3,3],[1,3],[5,7],[2,2],[4,6]]
    intervals.sort(key=lambda x: x[0])
    print(intervals)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
