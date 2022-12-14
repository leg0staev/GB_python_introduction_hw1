
m = int(input('введите количество долек шоколадки по ширине m='))
n = int(input('введите количество долек шоколадки по длине n='))
k = int(input('введите количество долек, кторое хотите отломить k='))


def PieceOfChokolate(int: m, n, k):
    if k > m*n:
        return "в нашей шоколадке нет столько долек :( "
    elif k % m == 0 or k % n == 0:
        return "отламывайте!"
    else:
        return "ровно отломить не выйдет.."


print(PieceOfChokolate(m, n, k))
