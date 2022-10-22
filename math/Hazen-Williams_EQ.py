
# initial vals
LoxFlowRate = 1.02598  # lb/sec
LoxFlowRategpm = 7.376371  # gallons per minute
fuelFlowRate = 0.73285  # lb/sec
fuelFlowRategpm = 5.268888  # gallons per minute
C = 120  # pipe coeff.
Dl = .375  # diam of lox pipe in inches
Df = .375  # diam of fuel pipe in inches
Ll = 10  # length of lox pipe in inches
Lf = 30  # length of fuel pipe in inches

Ll1 = Ll/12  # convert to ft
Lf1 = Lf/12  # convert to ft


# Pressure drop operation
Plossf = 4.53*Lf1*(((fuelFlowRategpm/C)**1.852) / (Df**4.857))
Plossl = 4.53*Ll1*(((LoxFlowRategpm/C)**1.852) / (Dl**4.857))
print(str(Plossf) + "psi on fuel tubing")
print(str(Plossl) + "psi on lox tubing")
