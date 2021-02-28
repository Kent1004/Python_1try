'''
Создать вручную список, содержащий цены на товары (10–20 товаров), например:
[57.8, 46.51, 97, ...]

Вывести на экран эти цены через запятую в одну строку, цена должна отображаться в виде <r> руб <kk> коп
(например «5 руб 04 коп»).
Подумать, как из цены получить рубли и копейки, как добавить нули, если, например, получилось 7 копеек или 0 копеек (
должно быть 07 коп или 00 коп).
Вывести цены, отсортированные по возрастанию, новый список не создавать (доказать, что объект списка после сортировки
остался тот же).
Создать новый список, содержащий те же цены, но отсортированные по убыванию.
Вывести цены пяти самых дорогих товаров. Сможете ли вывести цены этих товаров по возрастанию, написав минимум кода?

'''

list = [57.8, 46.51, 97 , 33.34 , 15, 42.7 , 125, 64.22, 21.3, 23]
result = ''
print ('list_ID: ',id(list))
for i in range(len(list)):
    list[i] = float(f'{list[i]:0.2f}')
    priceInStr = str(list[i])
    #list[i] = f" {list[i].split('.')[0]} руб {list[i].split('.')[1] } коп"
    result += f" {priceInStr.split('.')[0]} руб {priceInStr.split('.')[1] } коп, "

print(list,id(list))
print ('А: ',result , '\nlist_A_ID: ',id(list))
list.sort()
print ('В: ', list, '\nlist_B_ID: ' , id(list))
new_List = sorted(list,reverse=True)
print('C: ', new_List, '\nnew_List_C_ID: ' , id(new_List))
print('D: ', new_List[5::-1], '\nnew_List_C_ID: ' , id(new_List))