from matplotlib import pyplot as plt
import os
import shutil

x = []
y = []

def plot_results(results):
    
    myData = results.split("\n")

    newData = myData[1:]

    print("myData", myData)

    # Viser de to første headings i datasættet på grafen... skal det være mere dynamisk ved mange kolonner?
    headings = myData[1]
    headings = headings.split(";") #
    headings = headings[:2]
    print("headings", headings)
    plt.title(headings)

    print('headings:',headings)
    #slet gammel folder
    shutil.rmtree(f"{os.path.join(os.getcwd())}\\img") #TODO brug join i stedet for f string?
    os.mkdir(f"{os.path.join(os.getcwd())}\\img")

    for index,dat in enumerate(newData):

        if len(dat) > 0:
            dat2 = dat.split(";")
            # print("dat2:", dat2, len(dat2)-1)
            # print(f"{dat2[0]} {dat2[1]}")

            #TODO: Hardcoded: Henter 2 sidste kolonner, data og tid... overvej anden løsning, med valg i UI?
            my_x = str(dat2[len(dat2)-2])
            my_y = str(dat2[len(dat2)-1])
            try:
                my_x = my_x.replace("\r",'')
                my_y = my_y.replace("\r",'').replace(",",'.')
            except:
                pass

            if my_y == "..": #TODO <-- def. fra dst.dk for tomme celler
                pass

            else:
                x.append(my_x)
                y.append(float(my_y))


        #barh = liggende søjler
        plt.bar(x, y,color='#0000FF')

        print(f"{os.path.join(os.getcwd())}\\img\\img{index:03d}.png")
        save_img_path = f"{os.path.join(os.getcwd())}\\img\\img{index:03d}.png"

        plt.savefig(save_img_path)

        #TODO opret speed var:
        plt.pause(0.1)

    plt.show()


# if __name__ == '__main__':
#     print("main")
    