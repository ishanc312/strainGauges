import csv
import serial
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import calculationFunctions as cf

SERIAL_PORT = 'COM3'
BAUD_RATE = 9600
connection = serial.Serial(SERIAL_PORT, BAUD_RATE)
# initializes Serial Port of Arduino, and BAUD rate (info transfer rate)

rodArea = float(input("Please enter the cross sectional area of the rod."))
force_a = float(input("Please enter the force applied to the jig."))
# these are our independent variables we control per experiment
voltage_vals = []
strain_vals = []
tforce_vals = []
perror_vals = []
# based on values read from arduino, we read values into these arrays

def processData():
    v_diff = float(connection.readline().decode('utf-8').strip())
    # reads the voltage from the Arduino
    strain = cf.calcStrain(v_diff)
    force_t = cf.calcTheoreticalForce(strain, rodArea)
    p_error = cf.percentageError(force_t, force_a)
    # uses our calculation functions

    voltage_vals.append(v_diff)
    strain_vals.append(strain)
    tforce_vals.append(force_t)
    perror_vals.append(p_error)

def on_close(event):
    with open('strainGauges.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer = writer.writerow(["Voltage Difference", "Strain", "Theoretical Force", "Percent Error"])
        # the header
        for v, s, ft, pe in zip(voltage_vals, strain_vals, tforce_vals, perror_vals):
            writer.writerow([v, s, ft, pe])
            # writes our desired values to the row

def plot(frame):
    processData()
    # In every frame, we read the data from a line and update our value arrays
    plt.cla()
    plt.plot(voltage_vals, strain_vals, color='green', label='Strain')
    plt.plot(voltage_vals, tforce_vals, color='red', label='Theoretical Force')
    plt.plot(voltage_vals, perror_vals, color='blue', label='Percent Error')
    # we then plot our newly updated desired values accordingly
    plt.xlabel("Voltage Values")
    plt.ylabel("Important Quantities")
    plt.legend()
    # just some labeling of the graph

fig, ax = plt.subplots()
fig.canvas.mpl_connect('close_event', on_close)
# ensures that on_close() is called once the close_event occurs, which is connected to fig
# on_close() writes a CSV file based on our value arrays
animation = FuncAnimation(fig, plot, frames=60, interval=1000)
# updates the animation every 20 by calling the plot function
# plot function contains processData()
# thus, everytime we update the animation we process/create a new line of data
plt.show()
