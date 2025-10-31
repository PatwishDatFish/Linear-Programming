import pyomo.environ as pyo

def main():
	m = pyo.ConcreteModel()
	
	# Scalars (fill with your numbers)
	D = 100
	lam = 0.0        # carbon price; set >0 or use an Emissions cap
	Ecap = None      # set to a float to enforce an emissions cap
	
	# Parameters (examples)
	a_ore_BF, a_ore_DRI, a_HBI_EAF = 1.6, 1.4, 1.0
	cBF_TP, cDRI_AU, cDRI_TP, cEAF_AU, cEAF_TP = 600, 350, 450, 120, 110
	cship_ore, cship_HBI, cship_steel = 10, 12, 25
	eBF_TP, eDRI_AU, eDRI_TP, eEAF_AU, eEAF_TP = 1.0, 0.05, 0.35, 0.05, 0.10
	eship_ore, eship_HBI, eship_steel = 0.10, 0.05, 0.12
	
	# Variables
	m.xBF = pyo.Var(domain=pyo.NonNegativeReals)
	m.yDRI_AU = pyo.Var(domain=pyo.NonNegativeReals)
	m.yDRI_TP = pyo.Var(domain=pyo.NonNegativeReals)
	m.xEAF_AU = pyo.Var(domain=pyo.NonNegativeReals)
	m.xEAF_TP = pyo.Var(domain=pyo.NonNegativeReals)
	m.f_ore = pyo.Var(domain=pyo.NonNegativeReals)
	m.f_HBI = pyo.Var(domain=pyo.NonNegativeReals)
	m.f_steel = pyo.Var(domain=pyo.NonNegativeReals)
	
	# Demand
	m.demand = pyo.Constraint(expr=m.xBF + m.xEAF_TP + m.f_steel == D)
	
	# Balances
	m.oreBF = pyo.Constraint(expr=m.f_ore == a_ore_BF * m.xBF)
	m.driBal = pyo.Constraint(expr=m.yDRI_AU + m.yDRI_TP == a_HBI_EAF*(m.xEAF_AU + m.xEAF_TP))
	m.hbiShip = pyo.Constraint(expr=m.f_HBI >= m.xEAF_TP - m.yDRI_TP)
	m.hbiFlow = pyo.Constraint(expr=m.f_HBI <= m.yDRI_AU)
	m.steelFlow = pyo.Constraint(expr=m.f_steel <= m.xEAF_AU)
	
	# Emissions expression
	m.Em = pyo.Expression(expr=
	    eBF_TP*m.xBF + eDRI_AU*m.yDRI_AU + eDRI_TP*m.yDRI_TP
	  + eEAF_AU*m.xEAF_AU + eEAF_TP*m.xEAF_TP
	  + eship_ore*m.f_ore + eship_HBI*m.f_HBI + eship_steel*m.f_steel)
	
	# Optional emissions cap
	if Ecap is not None:
	    m.cap = pyo.Constraint(expr=m.Em <= Ecap)
	
	# Cost + carbon price objective
	m.Obj = pyo.Objective(expr=
	    cBF_TP*m.xBF + cDRI_AU*m.yDRI_AU + cDRI_TP*m.yDRI_TP
	  + cEAF_AU*m.xEAF_AU + cEAF_TP*m.xEAF_TP
	  + cship_ore*m.f_ore + cship_HBI*m.f_HBI + cship_steel*m.f_steel
	  + lam*m.Em, sense=pyo.minimize)
	
	# Solve
	pyo.SolverFactory("glpk").solve(m, tee=False)
	for v in [m.xBF, m.yDRI_AU, m.yDRI_TP, m.xEAF_AU, m.xEAF_TP, m.f_ore, m.f_HBI, m.f_steel, m.Em]:
	    print(v, pyo.value(v))


if __name__ == "__main__":
    main()
