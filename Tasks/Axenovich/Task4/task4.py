import FuncTask4 as Task4
import random
import numpy as np

print(Task4.check_str_v1())
print(Task4.check_str_v2())

print(Task4.check_str_v1('gergseAStgsrbv r gshbASd ibha bh abhASDa ASDefwkkbhfsdf$%^&* kbh awkekhb awkhb kbh askhsa kjb gaskjb rfwefwe$#R$gFekjb aEDWFEsdADSbbu akug%^&*khb  ab kbua ergkjhb aka sfkh&&(^*&^bl kbhbkbk kb'))
print(Task4.check_str_v2('gergseAStgsrbv r gshbASd ibha bh abhASDa ASDefwkkbhfsdf$%^&* kbh awkekhb awkhb kbh askhsa kjb gaskjb rfwefwe$#R$gFekjb aEDWFEsdADSbbu akug%^&*khb  ab kbua ergkjhb aka sfkh&&(^*&^bl kbhbkbk kb'))


print(Task4.is_prime(random.randint(0, 100)))
print(Task4.is_prime(random.randint(0, 10000000000000)))
print(Task4.is_prime(random.randint(0, 1000000000)))
print(Task4.is_prime(10))
print(Task4.is_prime(7))
print(Task4.is_prime(999999000001))


print(Task4.get_ranges([0, 1, 2, 3, 4, 7, 8, 10]))
print(Task4.get_ranges([4, 7, 10]))
print(Task4.get_ranges([2, 3, 8, 9]))
print(Task4.get_ranges(list(set(np.random.randint(0, 20, 10))))) #list(set()) - get format for solution and np.random get random list with number
print(Task4.get_ranges(list(set(np.random.randint(0, 20, 10)))))
print(Task4.get_ranges(list(set(np.random.randint(0, 20, 10)))))