from api import result

# For fun: tjek pythons "anti gravity" :D

# pip install matplotlib

from matplotlib import pyplot as plt
#--------------------------------------------------------------------------------------
# # vis indbyggede styles:
# # print(plt.style.available)
# # plt.style.use('fivethirtyeight')

# # eller brug extern comic style:
# # plt.xkcd()

# data_x = [25,26,27,28,29,30]
# data_y = [23444,65433,23444,76533,23444,26234]

# # Hjælp: https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.plot.html
# # Mere dokumentation: https://matplotlib.org/3.1.1/tutorials/introductory/customizing.html#a-sample-matplotlibrc-file
# plt.plot(data_x,data_y,color='b',linestyle='--',marker='.',label='kvinder')

# # data2_x = [25,26,27,28,29,30] bruges ikke da samme x-akse som data1...
# data2_y = [35684,39865,12548,32696,48755,15426]
# # marker vis prikker
# # color som kode eller hex value
# plt.plot(data_x, data2_y,color='#FF0000',marker='o',linewidth='3',label='mænd')

# plt.xlabel('x-akse')
# plt.ylabel('y-akse')
# plt.title('Mit diagram')

# plt.legend() # uden argument bruges 'label' fra .plot()

# # evt. hvis der er problemer med at diagram-vindue skæres forkert eller ting mangler:
# plt.tight_layout()

# # vis grid
# plt.grid(True)

# # save as picture
# plt.savefig('myDiagram.png')

# # vis diagram
# # plt.show()
#--------------------------------------------------------------------------------------

# DST.DK:
print(result.text) # result imported fra api

global x
global y
global year
year = []
x = []
y = []

myData = result.text.split(";")
myData = result.text.split("\r\n")

for index,field in enumerate(myData):
    if index < 20:
        # print(field.split(";"))
        xList = field.split(";")
        # print('xList', xList)
        # print('index: ',index)
        # TODO: Omdøb xList
        kommune = xList[0].replace('\ufeffKOMK','Kommune')
        xHeader = 'Kommune'
        if index != 0 and xList[0] != '':
            x.append(kommune)
            # print('new xList: ',xList[0])
            year.append(xList[1])
            y.append(float(xList[2].replace(',','.')))
            plt.barh(x, y,color='#0000FF')
            # pause = animation - se: https://www.youtube.com/watch?v=7RgoHTMbp4A&ab_channel=NeuralNine
            plt.pause(0.1)


print('x: ',x)
print('year: ', year)
print('y: ',y)

# plot = line
# plt.plot(x, y,color='#0000FF',linewidth='2',label='Gennemsnitsalder')

# bar = søjler
# PS begge kan aktiveres på samme tid
# plt.bar(x, y,color='#0000FF',label='Gennemsnitsalder')

#barh = liggende søjler
# plt.barh(x, y,color='#0000FF',label='Gennemsnitsalder')

plt.xlabel('x-akse', fontsize='small') #hvorfor virker fontsize ikke? tjek version af pyplot...
plt.xticks(rotation=90)

# behøver ikke ylabel ved barh type:
# plt.ylabel('y-akse')

plt.title('Mit diagram')

plt.legend()

plt.show()