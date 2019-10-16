import csv
import matplotlib.pyplot as plt

def get_data(filename, y_name, x_name):
    km = []
    price = []
    with open(filename,mode='r') as csvfile:
        spamreader = csv.DictReader(csvfile)
        for row in spamreader:
            km.append(float(row[x_name]))
            price.append(float(row[y_name]))
        csvfile.close()
    return(km, price)

def cost_function(km, price, weight, bias):
    size = len(km)
    total_error = 0.0
    for i in range(size):
        total_error += (price[i] - (weight * km[i] + bias))**2
    return(total_error / size)

def update_weights(km, price, weight, bias, learning_rate):
    weight_deriv = 0
    bias_deriv = 0
    size = len(km)

    for i in range(size):
        weight_deriv += km[i] * ((weight * km[i] + bias) - price[i])
        bias_deriv += ((weight * km[i] + bias) - price[i])
    
    weight -= (weight_deriv / size) * learning_rate
    bias -= (bias_deriv / size) * learning_rate

    return weight, bias

def train(km, price, weight, bias, learning_rate, iters):
    cost_history = []
    for _ in range(iters):
        weight,bias = update_weights(km,price,weight,bias,learning_rate)
        cost = cost_function(km, price, weight, bias)
        cost_history.append(cost)
    return( weight, bias, cost_history)


km, price = get_data("data.csv","price","km")

x_min, x_max = min(km), max(km)

km = [x/10000 for x in km]
price = [x/1000 for x in price]


weight, bias, cost_history = train(km, price, 0, 0, 0.0001, 1000000)


km = [x*10000 for x in km]
price = [x*1000 for x in price]

bias = bias * 1000
weight = weight/10

min_x, max_x = min(km), max(km)
min_y = min_x * weight + bias
max_y = max_x * weight + bias

with open('theta.csv','w', newline='') as thetafile:
    spamwriter = csv.writer(thetafile, delimiter=',')
    spamwriter.writerow(['theta0','theta1'])
    spamwriter.writerow([str(bias),str(weight)])
    thetafile.close()

plt.scatter(km, price)
plt.plot([min_x,max_x],[min_y,max_y])
plt.xlabel('km')
plt.ylabel('price')
plt.show()