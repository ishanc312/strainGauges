SUPPLY_VOLTAGE = 5
# Voltage powering our circuit
YOUNGS_MODULUS = 69
# in the unit of gPA
GAUGE_FACTOR = 2.08

# helper functions that execute necessary equations
def calcStrain(voltageDifference):
    return (voltageDifference/SUPPLY_VOLTAGE) * (4/GAUGE_FACTOR)

def calcTheoreticalForce(strain, rodArea):
    return (YOUNGS_MODULUS*strain*rodArea)

def percentageError(theoretical, true):
    error = abs(theoretical-true) / abs(true)
    return (error*100)