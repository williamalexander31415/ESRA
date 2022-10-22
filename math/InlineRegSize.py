
# initial vals
LoxFlowRate = 1.02598  # lb/sec
LoxFlowRategpm = 7.376371*8.02  # gallons per minute
fuelFlowRate = 0.73285  # lb/sec
fuelFlowRategpm = 5.268888*8.02  # gallons per minute


# Pressure drop operation
Plossf = fuelFlowRategpm
Plossl = LoxFlowRategpm
print(str(Plossf) + " SCFH")
print(str(Plossl) + " SCFH")

# 165 psi drop on fuel with two inline, inline set to 563 to hit flow rate
# 490 before check valve, 420 on lox with two inline, inline reg set to 482 to hit flow rate
