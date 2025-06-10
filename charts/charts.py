import matplotlib.pyplot as plt 

def generate_pie_chart():
    labels=["A","B","C","D"]
    values=[15, 30, 45, 10]
    
    fig, ax = plt.subplots()
    ax.pie(values, labels=labels)
    ax.set_title("Pie Chart Example")
    #plt.show()
#generate_pie_chart()
    plt.savefig(".pie.png")
    plt.close()