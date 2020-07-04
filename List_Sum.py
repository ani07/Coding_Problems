# a = '1110010001111101110011110011000011011'
# b = ''
# d = ''
# c = []
# for y, i in enumerate(a):
#     if int(i) == 1:
#         b += i
#         if d != '':
#             c.append(d)
#             d = ''
#     elif int(i) == 0:
#         d += i
#         if b != '':
#             c.append(b)
#             b = ''
#     if y == len(a) - 1:
#         if b != '':
#             c.append(b)
#         else:
#             c.append(d)
# print(c)
#
# ONESANDOS = '1110010001'
# entry = ''
# result = []
#
# for e, i in enumerate(ONESANDOS):
#     entry += i
#     try:
#         if i != ONESANDOS[e + 1]:
#             result.append(entry)
#             entry = ''
#     except IndexError:
#         result.append(entry)
#
# print(result)


for i in range(2,50):
    f = open('project_euler'+str(i)+'.py','a')
    f.write('""" This solution is baswd on Problem statement from Project Euler Problem Number {}"""'.format(i))
    f.close()
