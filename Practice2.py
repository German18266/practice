try:
    n = input('Введите произвольную последовательность целых чисел (от 0 до 10) через пробел и нажмите Enter:')[:19]
    for i in n:
        if i == i:
            for s in "qwertyuiopasdfghjklzxcvbnm,./<>?;{}][+_)(*&^%$#@!йцукенгшщзхъэждлорпавыфячсмитьбюЙЦУКЕНГШЩЗХЪЭЖДЛОРПАВЫФЯЧСМИТЬБЮQWERTYUIOPLKJHGFDSAZXCVBNM":
                if s == i:
                    raise ValueError
    p = int(input('Введите любое целое число от 0 до 10 :'))

except ValueError:
    print(ValueError, "Вы ввели недопустимое значение------", n, '  Я в вас верю, у вас получится, попробуйте еще!!!')

################_____Переводим в несортированый список_____####################
n1 = n.split(' ')

n2 = [int(x) for x in n1]


######################---Складываем пополам и сортируем список____###########
def skladivaem_popolam(n2):
    if len(n2) < 2:
        return n2[:]

    else:
        n3 = len(n2) // 2
        levaya = skladivaem_popolam(n2[:n3])
        pravaya = skladivaem_popolam(n2[n3:])
        return sliyanie(levaya, pravaya)


def sliyanie(levaya, pravaya):
    n4 = []
    i = 0
    j = 0
    while i < len(levaya) and j < len(pravaya):
        if levaya[i] < pravaya[j]:
            n4.append(levaya[i])
            i += 1
        else:
            n4.append(pravaya[j])
            j += 1
    while i < len(levaya):
        n4.append(levaya[i])
        i += 1

    while j < len(pravaya):
        n4.append(pravaya[j])
        j += 1

    return n4


n4 = skladivaem_popolam(n2)
print(f'Последовательность отсортирована______{n4}')


###############----Поиск элемента введеного пользователем и определение его в отсортированом списке___#########
def poisk_element(n4, p, levaya, pravaya):
    if levaya > pravaya:
        print(f'в даной последовательности для введенного числа "{p}" нет места')
        return False
    seredina = (pravaya + levaya) // 2
    if n4[seredina] == p:
        return seredina
    elif p < n4[seredina]:
        return poisk_element(n4, p, levaya, seredina - 1)
    else:
        return poisk_element(n4, p, seredina + 1, pravaya)


print(f'В даной последовательности {n4}  введеное число "{p}" соответствует "{poisk_element(n4, p, 0, 10)}" позиции')
