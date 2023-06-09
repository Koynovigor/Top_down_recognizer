T = ["a", "b", "(", ")", "!", "+", "*"] # множество терминальных символов
G = [["A1", "!B!"], ["B1", "T"], ["B2", "T+B"], ["T1", "M"], ["T2", "M*T"], ["M1", "a"], ["M2", "b"], ["M3", "(B)"]]
l1 = []         # стек 1
l2 = str("A")   # стек 2
#w = str(input("input string: "))    # входная цепочка
#w = w.lower()   
w = "!a++b!"
n = len(w)      # длина входной цепочки
i = 0
s = "q"         # состояние алгоритма
                # q – состояние нормальной работы
                # b – состояние возврата
                # t  - заключительное состояние (нормальное завершение)

res = ""        # результат

def get_rule(alt):
    for g in G:
        if g[0] == alt: 
            return g[1]
    return None

for number in range(1000):
    if s == "q":
        if l2[0] in T:
            if l2[0] != w[i]: s = "b" # шаг 4
            else:
                # нач шаг 2
                l1.append(l2[0])
                l2 = l2[1:]
                i += 1
                # кон шаг 2
                if i == n:
                    if len(l2) == 0: s = "t" # шаг 3
                    else: s = "b" # шаг 3'
                else:
                    if len(l2) == 0: s = "b" # шаг 3'
        else:
            # нач шаг 1
            a = l2[0] + "1"
            l1.append(a)
            l2 = l2.replace(a[0], get_rule(a), 1)
            # кон шаг 1
        continue
    if s == "b":
        if l1[len(l1) - 1] in T:
            # нач шаг 5
            l2 = l1[len(l1) - 1] + l2
            l1 = l1[: len(l1) - 1]
            i -= 1
            # кон шаг 5
        else:
            a_l1 = l1[len(l1) - 1]
            a_l1_new = a_l1[0] + chr(ord(a_l1[1]) + 1)
            if get_rule(a_l1_new) != None:
                # нач шаг 6a
                l1 = l1[: len(l1) - 1]
                l1.append(a_l1_new)
                l2 = l2.replace(get_rule(a_l1), get_rule(a_l1_new), 1)
                s = "q"
                # кон шаг 6a
            else:
                if (a_l1_new == "A2") and (i == 0):
                    break # шаг 6б
                else:
                    # нач шаг 6в
                    l2 = l2.replace(get_rule(a_l1), a_l1[0], 1)
                    l1 = l1[: len(l1) - 1]
                    # кон шаг 6в
        continue
    if s == "t":
        for x in l1:
            get_idx = 0
            for g in G:
                if g[0] == x:
                    get_idx = G.index(g) + 49
                    break
            if get_idx != 0: res += " " + str(chr(get_idx))
        break
if res != "": print(res)
else: print("Error!")
