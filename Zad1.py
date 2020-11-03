

def reverse_tab(tab):
    print(f'Reverse_tab - Start - {tab}')
    tab2 = ""

    for i in range(len(tab)):
        tab2 += tab[len(tab)-i-1]

    print(f'Reverse_tab - Stop - {tab2}')


if __name__ == '__main__':
    str = input("Enter string to revers! ")
    reverse_tab(str)

