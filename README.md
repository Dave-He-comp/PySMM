# PySMM
A Python script package for calculating and analyzing the properties of single-molecule magnets.


## Overview

This Python script package is designed to simulate and visualize the zero-field splitting energy level structure, spin reversal barrier, and magnetization relaxation dynamics of single-molecule magnets (SMMs).

Based on the axial zero-field splitting model, the scripts automatically generate spin energy level splitting diagrams, magnetization reversal barrier plots, and magnetization relaxation dynamics curves by inputting the zero-field splitting parameter ($D$) and the total spin quantum number ($S$). The program also calculates the effective energy barrier ($U_{\mathrm{eff}}$) and relaxation time ($\tau$).

The scripts support both integer and half-integer spin systems and can correctly describe easy-axis and easy-plane magnetic anisotropy corresponding to different signs of ($D$). They can be used for theoretical analysis and visualization in studies related to single-molecule magnets, spin dynamics, and molecular magnetism.


## Theoretical Background

### Spin Eigenstate Energies

The most commonly used zero-field splitting (Zero-Field Splitting, ZFS) Hamiltonian for single-molecule magnets and molecular spin systems is:

$$
\hat H_{\mathrm{ZFS}} = D\left(\hat S_z^2-\frac{S(S+1)}{3}\right)+E(\hat S_x^2-\hat S_y^2)
$$

where:

- $D$: axial zero-field splitting parameter (axial ZFS parameter)

It determines easy-axis anisotropy ($D<0$) and easy-plane anisotropy ($D>0$), and is also the primary origin of the magnetization reversal barrier in single-molecule magnets.

- $E$: transverse/rhombic zero-field splitting parameter (transverse/rhombic ZFS parameter)

It breaks cylindrical symmetry, mixes different ($M_S$) states, and induces quantum tunneling of magnetization (QTM). Typically: $E \ll |D|$.

- $(\hat S_x,\hat S_y,\hat S_z)$: total spin operators

- $S$: total spin quantum number

When only the axial ZFS term is considered, the simplified SMM model becomes:

$$
\hat H = D\hat S_z^2
$$

with the corresponding eigenenergies:

$$
E_{M_S}=DM_S^2
$$

The energy levels in this script are based on this simplified model.


### Spin Reversal Barrier

#### Integer Spin Systems

When $D<0$, the spin reversal barrier is:

$$
U=|D|S^2
$$

because the ground states are located at:

$$
M_S=\pm S
$$

while the top of the barrier is located at:

$$
M_S=0
$$

#### Half-Integer Spin Systems

Since the state:

$$
M_S=0
$$

does not exist, the smallest allowed value of $|M_S|$ is 1/2. Therefore:

$$
U=|D|\left(S^2-\frac14\right)
$$


### Spin Relaxation Dynamics Curve

In experiments, the effective energy barrier for magnetization relaxation is commonly described by $U_{eff}$. The spin relaxation dynamics curve is plotted based on the Arrhenius relation to obtain the theoretical spin relaxation time.

$$
\tau=\tau_0\exp\left(\frac{U_{eff}}{k_BT}\right)
$$

where:

- $\tau$: relaxation time
- $\tau_0$: pre-exponential factor
- $k_B$: Boltzmann constant
- $T$: temperature


## Usage

Modify the physical parameters at the end of the script:

```python
D = -0.5  # unit: cm^-1
S = 2
(T = 2.0)   # unit: K
```

Then run:

```bash
python script_name.py
```

## Example Results
