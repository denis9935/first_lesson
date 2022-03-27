# with open('C:\\Users\\IT-Academy-Gomel\\Desktop\\test_text\\scratch.txt') as file_object:
#     lines =  file_object.readlines()
#     print(type(lines))
#     print(lines, '\n')

# pi_string = ''
# for line in lines:
#     pi_string += line.strip()
#
# print(pi_string)



file_path = 'C:\\Users\\IT-Academy-Gomel\\Desktop\\test_text\\scratch.txt'

# with open(file_path, 'r') as file_object:
#     lines = file_object.readlines()
#
# pi_string = ''
# for line in lines:
#     pi_string += line.strip()
#
# # print(pi_string[1:5])
# print(pi_string)
# birthday = '0506'
# if birthday in pi_string:
#     print('Есть')
# else:
#     print('нету')
# with open(file_path, 'w') as file_object:
#     file_object.write('I love python! ')
first_name = input('Ведите Имя:')
last_name = input('Ведите фамилию: ')

with open(file_path, 'w') as file_object:
    file_object.write(f'name: {first_name}\nsurname: {last_name}\n\n')

