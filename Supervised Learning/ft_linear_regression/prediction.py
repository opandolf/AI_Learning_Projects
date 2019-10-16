import csv

try:
   open("theta.csv", 'r')
except (FileNotFoundError, IOError):
    print("Initialisation des théta à 0")
    with open('theta.csv','w', newline='') as thetafile:
        spamwriter = csv.writer(thetafile, delimiter=',')
        spamwriter.writerow(['theta0','theta1'])
        spamwriter.writerow([str(0),str(0)])
        thetafile.close()

theta_list = []
with open('theta.csv', newline='') as thetafile:
    spamreader = csv.reader(thetafile, delimiter=',', quotechar='|')
    for row in spamreader:
        theta_list.append(row)
    thetafile.close()
theta = theta_list[1]
theta = [float(x) for x in theta]

km = int(input("km? "))
print(km * theta[1] + theta[0])