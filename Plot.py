# from api import result
# from gui2 import result
# For fun: tjek pythons "anti gravity" :D

# pip install matplotlib

from matplotlib import pyplot as plt
import os

# global x
# global y
x = []
y = []

def plot_results(results):
    print("TEST")
    print(results)
    # for r in results:
    #     print(r)

    # global year
    # year = []


    # myData = results.split("\n")[0] #.replace("\ufeff","")
    # print('myData:',myData)
    # for heading in myData:
    #     x.append(heading)
    
    myData = results.split("\n")
    # print('myData',myData)
    newData = myData[1:]
    # print('myData',newData)
    print("newData", newData)
    print("newData len", len(newData))
    for dat in newData:
        # print(dat)
        if len(dat) > 0:
            dat2 = dat.split(";")
            # print('dat2',dat2[1]," ",dat2[2])
            my_x = str(dat2[2])
            my_y = str(dat2[3])
            # print('my_y',my_y)
            print('my_x',my_x)
            # global x
            # global test
            # test += ","&my_x
            x.append(my_x)
            # # y.append(my_y)
            # print('x',x)
            # y.append('test y')
            # x.append('test x')
            # print("TEST 2")
        # print(test)
        print("lenght:",len(x))
        print('x',x)
        # return x

    # print("????")
    # for item in x:
    #     print('x',item)
    # for a in y:
    #     print('y',a)

    # nd = newData.replace("\\r","")
    # nd = newData.split(";")
    # print("nd",nd)

# for index,field in enumerate(myData):
#     if index < 20:
#         # print(field.split(";"))
#         xList = field.split(";")
#         # print('xList', xList)
#         # print('index: ',index)
#         # TODO: Omdøb xList
#         kommune = xList[0].replace('\ufeffKOMK','Kommune')
#         xHeader = 'Kommune'
#         if index != 0 and xList[0] != '':
#             x.append(kommune)
#             # print('new xList: ',xList[0])
#             year.append(xList[1])
#             y.append(float(xList[2].replace(',','.')))
#             plt.barh(x, y,color='#0000FF')
#             # print(f"{os.path.join(os.getcwd())}\\img{index}.png")
#             # [f"{i:03}" for i in range(121)]
#             save_img_path = f"img{index:03}.png"
#             plt.savefig(save_img_path)
#             # pause = animation - se: https://www.youtube.com/watch?v=7RgoHTMbp4A&ab_channel=NeuralNine
#             plt.pause(0.1)


# print('x: ',x)
# print('year: ', year)
# print('y: ',y)

# plot = line
# plt.plot(x, y,color='#0000FF',linewidth='2',label='Gennemsnitsalder')

# bar = søjler
# PS begge kan aktiveres på samme tid
# plt.bar(x, y,color='#0000FF',label='Gennemsnitsalder')

#barh = liggende søjler
# plt.barh(x, y,color='#0000FF',label='Gennemsnitsalder')



# plt.xlabel('x-akse', fontsize='small') #hvorfor virker fontsize ikke? tjek version af pyplot...
# plt.xticks(rotation=90)

# # behøver ikke ylabel ved barh type:
# # plt.ylabel('y-akse')

# plt.title('Mit diagram')

# #No artists with labels found to put in legend.
# #Note that artists whose label start with an underscore are ignored when legend() is called with no argument.
# plt.legend()

# plt.show()