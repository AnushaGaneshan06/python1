import buil_in_module as m # define the variable all

from buil_in_module import * # import all

from  buil_in_module import calculate # specific

from  buil_in_module import calculate , a, area_of_square# specific function and variable

print(m.a)

print(a)

print(area_of_square(3))

print(m.area_of_square(4))


calculate(3, 4)