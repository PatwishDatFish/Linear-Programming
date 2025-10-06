# LP for the Green-Iron / Green-Steel Deal

## Sets
- $R=\{\mathrm{AU},\mathrm{TP}\}$ &nbsp; (Australia, Trade Partner)

## Parameters (given, non-negative)
- $D$ — steel demand in TP (Mt/yr)  
- Input coefficients (t input / t output):  
  $a_{\mathrm{ore}\to \mathrm{BF}},\ a_{\mathrm{ore}\to \mathrm{DRI}},\ a_{\mathrm{HBI}\to \mathrm{EAF}}$
- Unit production costs (USD/t output):  
  $c_{\mathrm{TP}}^{\mathrm{BF}},\ c_{\mathrm{AU}}^{\mathrm{DRI}},\ c_{\mathrm{TP}}^{\mathrm{DRI}},\ c_{\mathrm{AU}}^{\mathrm{EAF}},\ c_{\mathrm{TP}}^{\mathrm{EAF}}$
- Unit shipping costs (USD/t):  
  $c_{\mathrm{ore}}^{\mathrm{ship}},\ c_{\mathrm{HBI}}^{\mathrm{ship}},\ c_{\mathrm{steel}}^{\mathrm{ship}}$
- Unit process emissions (tCO$_2$e/t output):  
  $e_{\mathrm{TP}}^{\mathrm{BF}},\ e_{\mathrm{AU}}^{\mathrm{DRI}},\ e_{\mathrm{TP}}^{\mathrm{DRI}},\ e_{\mathrm{AU}}^{\mathrm{EAF}},\ e_{\mathrm{TP}}^{\mathrm{EAF}}$
- Unit shipping emissions (tCO$_2$e/t):  
  $e_{\mathrm{ore}}^{\mathrm{ship}},\ e_{\mathrm{HBI}}^{\mathrm{ship}},\ e_{\mathrm{steel}}^{\mathrm{ship}}$
- Existing capacities (Mt/yr):  
  $\bar K_{\mathrm{TP}}^{\mathrm{BF}},\ \bar K_{\mathrm{AU}}^{\mathrm{DRI}},\ \bar K_{\mathrm{TP}}^{\mathrm{DRI}},\ \bar K_{\mathrm{AU}}^{\mathrm{EAF}},\ \bar K_{\mathrm{TP}}^{\mathrm{EAF}}$
- Renewable-electricity budget in AU (TWh/yr): $E_{\mathrm{AU}}^{\max}$  
  with intensities $p_{\mathrm{elec}}^{\mathrm{DRI}}$ and $p_{\mathrm{elec}}^{\mathrm{EAF}}$ (MWh/t)
- Scrap available in TP (t/yr): $S_{\mathrm{TP}}^{\max}$
- System emissions cap (Mt CO$_2$e/yr): $E^{\max}$ (optional)
- Carbon price (USD/t CO$_2$e): $\lambda$ (optional)
- Linear CAPEX for capacity additions (USD/t·yr): $k^{\cdot}$ (optional)

## Decision variables (all $\ge 0$)
- $x_{\mathrm{TP}}^{\mathrm{BF}}$ — steel via BF/BOF in TP  
- $y_{\mathrm{AU}}^{\mathrm{DRI}},\ y_{\mathrm{TP}}^{\mathrm{DRI}}$ — HBI (green iron) output  
- $x_{\mathrm{AU}}^{\mathrm{EAF}},\ x_{\mathrm{TP}}^{\mathrm{EAF}}$ — steel via EAF  
- $f_{\mathrm{ore}},\ f_{\mathrm{HBI}},\ f_{\mathrm{steel}}$ — AU$\to$TP shipments of ore, HBI, steel  
- $\Delta K^{\cdot}$ — capacity additions (optional)

---

## Derived totals

### Emissions

$$
\begin{aligned}
\mathrm{Em} \;=\;&
 e_{\mathrm{TP}}^{\mathrm{BF}}\,x_{\mathrm{TP}}^{\mathrm{BF}}
+ e_{\mathrm{AU}}^{\mathrm{DRI}}\,y_{\mathrm{AU}}^{\mathrm{DRI}}
+ e_{\mathrm{TP}}^{\mathrm{DRI}}\,y_{\mathrm{TP}}^{\mathrm{DRI}}
+ e_{\mathrm{AU}}^{\mathrm{EAF}}\,x_{\mathrm{AU}}^{\mathrm{EAF}}
+ e_{\mathrm{TP}}^{\mathrm{EAF}}\,x_{\mathrm{TP}}^{\mathrm{EAF}} \\
&+ e_{\mathrm{ore}}^{\mathrm{ship}}\, f_{\mathrm{ore}}
+ e_{\mathrm{HBI}}^{\mathrm{ship}}\, f_{\mathrm{HBI}}
+ e_{\mathrm{steel}}^{\mathrm{ship}}\, f_{\mathrm{steel}} .
\end{aligned}
$$

### Cost

$$
\begin{aligned}
\mathrm{Cost} \;=\;&
 c_{\mathrm{TP}}^{\mathrm{BF}}\,x_{\mathrm{TP}}^{\mathrm{BF}}
+ c_{\mathrm{AU}}^{\mathrm{DRI}}\,y_{\mathrm{AU}}^{\mathrm{DRI}}
+ c_{\mathrm{TP}}^{\mathrm{DRI}}\,y_{\mathrm{TP}}^{\mathrm{DRI}}
+ c_{\mathrm{AU}}^{\mathrm{EAF}}\,x_{\mathrm{AU}}^{\mathrm{EAF}}
+ c_{\mathrm{TP}}^{\mathrm{EAF}}\,x_{\mathrm{TP}}^{\mathrm{EAF}} \\
&+ c_{\mathrm{ore}}^{\mathrm{ship}}\, f_{\mathrm{ore}}
+ c_{\mathrm{HBI}}^{\mathrm{ship}}\, f_{\mathrm{HBI}}
+ c_{\mathrm{steel}}^{\mathrm{ship}}\, f_{\mathrm{steel}}
+ \sum k^{\cdot}\,\Delta K^{\cdot}.
\end{aligned}
$$

---

## Objective (choose one)

**(A) Single objective (cost + carbon price):**

$$
\min\ Z \;=\; \mathrm{Cost} + \lambda\,\mathrm{Em}.
$$

**(B) Cost minimization with emissions cap:**

$$
\min\ Z \;=\; \mathrm{Cost}
\quad \text{s.t.} \quad \mathrm{Em} \leq E^{\max}.
$$

---

## Constraints

### Demand (steel consumed in TP)

$$
x_{\mathrm{TP}}^{\mathrm{BF}} + x_{\mathrm{TP}}^{\mathrm{EAF}} + f_{\mathrm{steel}} \;=\; D .
$$

### Material balances

$$
f_{\mathrm{ore}} \;=\; a_{\mathrm{ore}\to\mathrm{BF}}\, x_{\mathrm{TP}}^{\mathrm{BF}} .
$$

$$
y_{\mathrm{AU}}^{\mathrm{DRI}} + y_{\mathrm{TP}}^{\mathrm{DRI}}
\;=\; a_{\mathrm{HBI}\to\mathrm{EAF}}\,(x_{\mathrm{AU}}^{\mathrm{EAF}} + x_{\mathrm{TP}}^{\mathrm{EAF}}) .
$$

$$
x_{\mathrm{TP}}^{\mathrm{EAF}} \;\leq\; y_{\mathrm{TP}}^{\mathrm{DRI}} + f_{\mathrm{HBI}},
\qquad
f_{\mathrm{HBI}} \;\leq\; y_{\mathrm{AU}}^{\mathrm{DRI}} .
$$

### Shipping consistency (finished steel)

$$
f_{\mathrm{steel}} \;\leq\; x_{\mathrm{AU}}^{\mathrm{EAF}} .
$$

### Capacity limits (with optional expansion)

$$
\begin{aligned}
x_{\mathrm{TP}}^{\mathrm{BF}} &\leq \bar K_{\mathrm{TP}}^{\mathrm{BF}} + \Delta K_{\mathrm{TP}}^{\mathrm{BF}},\\
y_{\mathrm{AU}}^{\mathrm{DRI}} &\leq \bar K_{\mathrm{AU}}^{\mathrm{DRI}} + \Delta K_{\mathrm{AU}}^{\mathrm{DRI}}, \qquad
y_{\mathrm{TP}}^{\mathrm{DRI}} &\leq \bar K_{\mathrm{TP}}^{\mathrm{DRI}} + \Delta K_{\mathrm{TP}}^{\mathrm{DRI}},\\
x_{\mathrm{AU}}^{\mathrm{EAF}} &\leq \bar K_{\mathrm{AU}}^{\mathrm{EAF}} + \Delta K_{\mathrm{AU}}^{\mathrm{EAF}}, \qquad
x_{\mathrm{TP}}^{\mathrm{EAF}} &\leq \bar K_{\mathrm{TP}}^{\mathrm{EAF}} + \Delta K_{\mathrm{TP}}^{\mathrm{EAF}}.
\end{aligned}
$$

### Resource limits (optional)

$$
p_{\mathrm{elec}}^{\mathrm{DRI}}\, y_{\mathrm{AU}}^{\mathrm{DRI}}
+ p_{\mathrm{elec}}^{\mathrm{EAF}}\, x_{\mathrm{AU}}^{\mathrm{EAF}}
\;\leq\; E_{\mathrm{AU}}^{\max} .
$$

$$
a_{\mathrm{scrap}}\, x_{\mathrm{TP}}^{\mathrm{EAF}}
\;\leq\; S_{\mathrm{TP}}^{\max} .
$$

### Emissions cap (only for Objective B)

$$
\mathrm{Em} \;\leq\; E^{\max}.
$$

---

## Policy switches (by fixing variables)
- Enforce “deal” (DRI in AU, EAF in TP): set $y_{\mathrm{TP}}^{\mathrm{DRI}}=0$, $x_{\mathrm{AU}}^{\mathrm{EAF}}=0$, $f_{\mathrm{steel}}=0$.
- Allow TP to build DRI: leave $y_{\mathrm{TP}}^{\mathrm{DRI}}$ free; costs/resources decide.
- Allow AU to export finished steel: leave $x_{\mathrm{AU}}^{\mathrm{EAF}}$ and $f_{\mathrm{steel}}$ free.