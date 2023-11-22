#TODO Выполнить проверку диапозона чисел в границе промежутка


#mod 1
# data_left = int(input())
# data_right = int(input())
# while data_cycle := int(input()):
#     print("Entered:", data_cycle)
#     for data_cycle in range(data_left, data_right):
#         print("You cool baby")


#mod 2
# data_left = int(input())
# data_right = int(input())
# while data_cycle := int(input()):
#     if data_cycle >= data_left and data_cycle <= data_right:
#         data_cycle = True
#     elif data_left < data_cycle > data_right:
#         data_cycle = False


#mod 3
data_left = int(input())
data_right = int(input())
while True:
    data_input = int(input())
    if data_input == '':
        break
    elif data_left <= data_input <= data_right:
        data_input = True
        # print("Число входит в промежуток")
    else:
        data_input = False
        # print("Число за границами промежутка")
    


        





