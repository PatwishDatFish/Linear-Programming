# LP for the Green-Iron / Green-Steel Deal

## Sets
- $R=\{\mathrm{AU},\mathrm{TP}\}$ &nbsp; (Australia, Trade Partner)

## Parameters (given, non-negative)
- $D$ — steel demand in TP (Mt/yr)  
- Input coefficients (t input / t output):  
  $a_{\mathrm{ore}\to \mathrm{BF}},\ a_{\mathrm{ore}\to \mathrm{DRI}},\ a_{\mathrm{HBI}\to \mathrm{EAF}}$
- Unit production costs (USD/t output):  
  $c^{\mathrm{BF}}_{\mathrm{TP}},\ c^{\mathrm{DRI}}_{\mathrm{AU}},\ c^{\mathrm{DRI}}_{\mathrm{TP}},\ c^{\mathrm{EAF}}_{\mathrm{AU}},\ c^{\mathrm{EAF}}_{\mathrm{TP}}$
- Unit shipping costs (USD/t):  
  $c^{\mathrm{ship}}_{\mathrm{ore}},\ c^{\mathrm{ship}}_{\mathrm{HBI}},\ c^{\mathrm{ship}}_{\mathrm{steel}}$
- Unit process emissions (tCO$_2$e/t output):  
  $e^{\mathrm{BF}}_{\mathrm{TP}},\ e^{\mathrm{DRI}}_{\mathrm{AU}},\ e^{\mathrm{DRI}}_{\mathrm{TP}},\ e^{\mathrm{EAF}}_{\mathrm{AU}},\ e^{\mathrm{EAF}}_{\mathrm{TP}}$
- Unit shipping emissions (tCO$_2$e/t):  
  $e^{\mathrm{ship}}_{\mathrm{ore}},\ e^{\mathrm{ship}}_{\mathrm{HBI}},\ e^{\mathrm{ship}}_{\mathrm{steel}}$
- Existing capacities (Mt/yr):  
  $\bar K^{\mathrm{BF}}_{\mathrm{TP}},\ \bar K^{\mathrm{DRI}}_{\mathrm{AU}},\ \bar K^{\mathrm{DRI}}_{\mathrm{TP}},\ \bar K^{\mathrm{EAF}}_{\mathrm{AU}},\ \bar K^{\mathrm{EAF}}_{\mathrm{TP}}$
- Renewable-electricity budget in AU (TWh/yr): $E^{\max}_{\mathrm{AU}}$  
  with intensities $p^{\mathrm{DRI}}_{\mathrm{elec}}$ and $p^{\mathrm{EAF}}_{\mathrm{elec}}$ (MWh/t)
- Scrap available in TP (t/yr): $S^{\max}_{\mathrm{TP}}$
- System emissions cap (Mt CO$_2$e/yr): $E^{\max}$ (optional)
- Carbon price (USD/t CO$_2$e): $\lambda$ (optional)
- Linear CAPEX for capacity additions (USD/t·yr): $k^{\cdot}$ (optional)

## Decision variables (all $\ge 0$)
- $x^{\mathrm{BF}}_{\mathrm{TP}}$ — steel via BF/BOF in TP  
- $y^{\mathrm{DRI}}_{\mathrm{AU}},\ y^{\mathrm{DRI}}_{\mathrm{TP}}$ — HBI (green iron) output  
- $x^{\mathrm{EAF}}_{\mathrm{AU}},\ x^{\mathrm{EAF}}_{\mathrm{TP}}$ — steel via EAF  
- $f_{\mathrm{ore}},\ f_{\mathrm{HBI}},\ f_{\mathrm{steel}}$ — AU$\to$TP shipments of ore, HBI, steel  
- $\Delta K^{\cdot}$ — capacity additions (optional)

---

## Derived totals

### Emissions

$$
\begin{aligned}
\mathrm{Em} \;=\;&
 e^{\mathrm{BF}}_{\mathrm{TP}}\,x^{\mathrm{BF}}_{\mathrm{TP}}
+ e^{\mathrm{DRI}}_{\mathrm{AU}}\,y^{\mathrm{DRI}}_{\mathrm{AU}}
+ e^{\mathrm{DRI}}_{\mathrm{TP}}\,y^{\mathrm{DRI}}_{\mathrm{TP}}
+ e^{\mathrm{EAF}}_{\mathrm{AU}}\,x^{\mathrm{EAF}}_{\mathrm{AU}}
+ e^{\mathrm{EAF}}_{\mathrm{TP}}\,x^{\mathrm{EAF}}_{\mathrm{TP}} \\
&+ e^{\mathrm{ship}}_{\mathrm{ore}}\, f_{\mathrm{ore}}
+ e^{\mathrm{ship}}_{\mathrm{HBI}}\, f_{\mathrm{HBI}}
+ e^{\mathrm{ship}}_{\mathrm{steel}}\, f_{\mathrm{steel}} .
\end{aligned}
$$

### Cost

$$
\begin{aligned}
\mathrm{Cost} \;=\;&
 c^{\mathrm{BF}}_{\mathrm{TP}}\,x^{\mathrm{BF}}_{\mathrm{TP}}
+ c^{\mathrm{DRI}}_{\mathrm{AU}}\,y^{\mathrm{DRI}}_{\mathrm{AU}}
+ c^{\mathrm{DRI}}_{\mathrm{TP}}\,y^{\mathrm{DRI}}_{\mathrm{TP}}
+ c^{\mathrm{EAF}}_{\mathrm{AU}}\,x^{\mathrm{EAF}}_{\mathrm{AU}}
+ c^{\mathrm{EAF}}_{\mathrm{TP}}\,x^{\mathrm{EAF}}_{\mathrm{TP}} \\
&+ c^{\mathrm{ship}}_{\mathrm{ore}}\, f_{\mathrm{ore}}
+ c^{\mathrm{ship}}_{\mathrm{HBI}}\, f_{\mathrm{HBI}}
+ c^{\mathrm{ship}}_{\mathrm{steel}}\, f_{\mathrm{steel}}
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
x^{\mathrm{BF}}_{\mathrm{TP}} + x^{\mathrm{EAF}}_{\mathrm{TP}} + f_{\mathrm{steel}} \;=\; D .
$$

### Material balances

$$
f_{\mathrm{ore}} \;=\; a_{\mathrm{ore}\to\mathrm{BF}}\, x^{\mathrm{BF}}_{\mathrm{TP}} .
$$

$$
y^{\mathrm{DRI}}_{\mathrm{AU}} + y^{\mathrm{DRI}}_{\mathrm{TP}}
\;=\; a_{\mathrm{HBI}\to\mathrm{EAF}}\,(x^{\mathrm{EAF}}_{\mathrm{AU}} + x^{\mathrm{EAF}}_{\mathrm{TP}}) .
$$

$$
x^{\mathrm{EAF}}_{\mathrm{TP}} \;\leq\; y^{\mathrm{DRI}}_{\mathrm{TP}} + f_{\mathrm{HBI}},
\qquad
f_{\mathrm{HBI}} \;\leq\; y^{\mathrm{DRI}}_{\mathrm{AU}} .
$$

### Shipping consistency (finished steel)

$$
f_{\mathrm{steel}} \;\leq\; x^{\mathrm{EAF}}_{\mathrm{AU}} .
$$

### Capacity limits (with optional expansion)

$$
\begin{aligned}
x^{\mathrm{BF}}_{\mathrm{TP}} &\leq \bar K^{\mathrm{BF}}_{\mathrm{TP}} + \Delta K^{\mathrm{BF}}_{\mathrm{TP}},\\
y^{\mathrm{DRI}}_{\mathrm{AU}} &\leq \bar K^{\mathrm{DRI}}_{\mathrm{AU}} + \Delta K^{\mathrm{DRI}}_{\mathrm{AU}}, \qquad
y^{\mathrm{DRI}}_{\mathrm{TP}} &\leq \bar K^{\mathrm{DRI}}_{\mathrm{TP}} + \Delta K^{\mathrm{DRI}}_{\mathrm{TP}},\\
x^{\mathrm{EAF}}_{\mathrm{AU}} &\leq \bar K^{\mathrm{EAF}}_{\mathrm{AU}} + \Delta K^{\mathrm{EAF}}_{\mathrm{AU}}, \qquad
x^{\mathrm{EAF}}_{\mathrm{TP}} &\leq \bar K^{\mathrm{EAF}}_{\mathrm{TP}} + \Delta K^{\mathrm{EAF}}_{\mathrm{TP}}.
\end{aligned}
$$

### Resource limits (optional)

$$
p^{\mathrm{DRI}}_{\mathrm{elec}}\, y^{\mathrm{DRI}}_{\mathrm{AU}}
+ p^{\mathrm{EAF}}_{\mathrm{elec}}\, x^{\mathrm{EAF}}_{\mathrm{AU}}
\;\leq\; E^{\max}_{\mathrm{AU}} .
$$

$$
a_{\mathrm{scrap}}\, x^{\mathrm{EAF}}_{\mathrm{TP}}
\;\leq\; S^{\max}_{\mathrm{TP}} .
$$

### Emissions cap (only for Objective B)

$$
\mathrm{Em} \;\leq\; E^{\max}.
$$

---

## Policy switches (by fixing variables)
- Enforce “deal” (DRI in AU, EAF in TP): set $y^{\mathrm{DRI}}_{\mathrm{TP}}=0$, $x^{\mathrm{EAF}}_{\mathrm{AU}}=0$, $f_{\mathrm{steel}}=0$.
- Allow TP to build DRI: leave $y^{\mathrm{DRI}}_{\mathrm{TP}}$ free; costs/resources decide.
- Allow AU to export finished steel: leave $x^{\mathrm{EAF}}_{\mathrm{AU}}$ and $f_{\mathrm{steel}}$ free.