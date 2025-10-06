# LP for the Green-Iron / Green-Steel Deal

## Sets
- $R=\{AU,TP\}$ &nbsp; (Australia, Trade Partner)

## Parameters (given, non-negative)
- $D$ — steel demand in TP (Mt/yr)  
- Input coefficients (t input / t output):  
  $a_{ore\to BF},\ a_{ore\to DRI},\ a_{HBI\to EAF}$
- Unit production costs (USD/t output):  
  $c_{TP}^{BF},\ c_{AU}^{DRI},\ c_{TP}^{DRI},\ c_{AU}^{EAF},\ c_{TP}^{EAF}$
- Unit shipping costs (USD/t):  
  $c_{ore}^{ship},\ c_{HBI}^{ship},\ c_{steel}^{ship}$
- Unit process emissions (tCO$_2$e/t output):  
  $e_{TP}^{BF},\ e_{AU}^{DRI},\ e_{TP}^{DRI},\ e_{AU}^{EAF},\ e_{TP}^{EAF}$
- Unit shipping emissions (tCO$_2$e/t):  
  $e_{ore}^{ship},\ e_{HBI}^{ship},\ e_{steel}^{ship}$
- Existing capacities (Mt/yr):  
  $\bar K_{TP}^{BF},\ \bar K_{AU}^{DRI},\ \bar K_{TP}^{DRI},\ \bar K_{AU}^{EAF},\ \bar K_{TP}^{EAF}$
- Renewable-electricity budget in AU (TWh/yr): $E_{AU}^{\max}$  
  with intensities $p_{elec}^{DRI}$ and $p_{elec}^{EAF}$ (MWh/t)
- Scrap available in TP (t/yr): $S_{TP}^{\max}$
- System emissions cap (Mt CO$_2$e/yr): $E^{\max}$ (optional)
- Carbon price (USD/t CO$_2$e): $\lambda$ (optional)
- Linear CAPEX for capacity additions (USD/t·yr): $k^{\cdot}$ (optional)

## Decision variables (all $\ge 0$)
- $x_{TP}^{BF}$ — steel via BF/BOF in TP  
- $y_{AU}^{DRI},\ y_{TP}^{DRI}$ — HBI (green iron) output  
- $x_{AU}^{EAF},\ x_{TP}^{EAF}$ — steel via EAF  
- $f_{ore},\ f_{HBI},\ f_{steel}$ — AU$\to $TP shipments of ore, HBI, steel  
- $\Delta K^{\cdot}$ — capacity additions (optional)

---

## Derived totals

### Emissions

$$
\begin{aligned}
Em \;=\;&
 e_{TP}^{BF}\,x_{TP}^{BF}
+ e_{AU}^{DRI}\,y_{AU}^{DRI}
+ e_{TP}^{DRI}\,y_{TP}^{DRI}
+ e_{AU}^{EAF}\,x_{AU}^{EAF}
+ e_{TP}^{EAF}\,x_{TP}^{EAF} \\
&+ e_{ore}^{ship}\, f_{ore}
+ e_{HBI}^{ship}\, f_{HBI}
+ e_{steel}^{ship}\, f_{steel} .
\end{aligned}
$$

### Cost

$$
\begin{aligned}
Cost \;=\;&
 c_{TP}^{BF}\,x_{TP}^{BF}
+ c_{AU}^{DRI}\,y_{AU}^{DRI}
+ c_{TP}^{DRI}\,y_{TP}^{DRI}
+ c_{AU}^{EAF}\,x_{AU}^{EAF}
+ c_{TP}^{EAF}\,x_{TP}^{EAF} \\
&+ c_{ore}^{ship}\, f_{ore}
+ c_{HBI}^{ship}\, f_{HBI}
+ c_{steel}^{ship}\, f_{steel}
+ \sum k^{\cdot}\,\Delta K^{\cdot}.
\end{aligned}
$$

---

## Objective (choose one)

**(A) Single objective (cost + carbon price):**

$$
\min\ Z \;=\; Cost + \lambda\,Em.
$$

**(B) Cost minimization with emissions cap:**

$$
\min\ Z \;=\; Cost
\quad \text{s.t.} \quad Em \leq E^{\max}.
$$

---

## Constraints

### Demand (steel consumed in TP)

$$
x_{TP}^{BF} + x_{TP}^{EAF} + f_{steel} \;=\; D .
$$

### Material balances

$$
f_{ore} \;=\; a_{ore\to BF}\, x_{TP}^{BF} .
$$

$$
y_{AU}^{DRI} + y_{TP}^{DRI}
\;=\; a_{HBI\to EAF}\,(x_{AU}^{EAF} + x_{TP}^{EAF}) .
$$

$$
x_{TP}^{EAF} \;\leq\; y_{TP}^{DRI} + f_{HBI},
\qquad
f_{HBI} \;\leq\; y_{AU}^{DRI} .
$$

### Shipping consistency (finished steel)

$$
f_{steel} \;\leq\; x_{AU}^{EAF} .
$$

### Capacity limits (with optional expansion)

$$
\begin{aligned}
x_{TP}^{BF} &\leq \bar K_{TP}^{BF} + \Delta K_{TP}^{BF},\\
y_{AU}^{DRI} &\leq \bar K_{AU}^{DRI} + \Delta K_{AU}^{DRI}, \qquad
y_{TP}^{DRI} &\leq \bar K_{TP}^{DRI} + \Delta K_{TP}^{DRI},\\
x_{AU}^{EAF} &\leq \bar K_{AU}^{EAF} + \Delta K_{AU}^{EAF}, \qquad
x_{TP}^{EAF} &\leq \bar K_{TP}^{EAF} + \Delta K_{TP}^{EAF}.
\end{aligned}
$$

### Resource limits (optional)

$$
p_{elec}^{DRI}\, y_{AU}^{DRI}
+ p_{elec}^{EAF}\, x_{AU}^{EAF}
\;\leq\; E_{AU}^{\max} .
$$

$$
a_{scrap}\, x_{TP}^{EAF}
\;\leq\; S_{TP}^{\max} .
$$

### Emissions cap (only for Objective B)

$$
Em \;\leq\; E^{\max}.
$$

---

## Policy switches (by fixing variables)
- Enforce “deal” (DRI in AU, EAF in TP): set $y_{TP}^{DRI}=0$, $x_{AU}^{EAF}=0$, $f_{steel}=0$.
- Allow TP to build DRI: leave $y_{TP}^{DRI}$ free; costs/resources decide.
- Allow AU to export finished steel: leave $x_{AU}^{EAF}$ and $f_{steel}$ free.