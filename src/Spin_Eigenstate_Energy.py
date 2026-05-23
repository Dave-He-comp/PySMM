import numpy as np
import matplotlib.pyplot as plt
from fractions import Fraction

def format_pm_fraction(m):
    # Display mS in ± fractional form
    frac = Fraction(abs(m)).limit_denominator()
    return f"±{frac.numerator}/{frac.denominator}" if frac.denominator != 1 else f"±{frac.numerator}"

def smm_energy_levels_pm_pair(D, S, save_path="SMM_energy_levels.png"):
    # Draw the energy level splitting diagram:
    # - Combine ±Ms labels on the same energy level
    # Discrete Ms values (keep only the non-negative part, handle 0 separately)
    mS_full = np.arange(-S, S+1, 1)
    energies_full = -D * (mS_full**2 - S*(S+1)/3)
    energies_full -= np.min(energies_full)

    # Symmetry treatment: combine positive and negative Ms
    mS_pos = mS_full[mS_full >= 0]
    energies_pos = energies_full[mS_full >= 0]

    fig, ax = plt.subplots(figsize=(4,5))

    # Draw horizontal energy level lines and ±Ms labels
    for i, E in enumerate(energies_pos):
        ax.hlines(E, 0, 1, colors='C2', lw=2)
        if mS_pos[i] == 0:
            label = "0"
        else:
            label = format_pm_fraction(mS_pos[i])
        ax.text(1.05, E,f"M$_S$={label}", va='center', fontsize=10)

    # Annotate the energy differences ΔE
    for i in range(len(energies_pos)-1):
        delta_E_factor = (mS_pos[i+1]**2 - mS_pos[i]**2)
        mid_E = (energies_pos[i+1] + energies_pos[i]) / 2
        ax.plot([0.5,0.5], [energies_pos[i], energies_pos[i+1]], 'k--', lw=1)
        ax.text(0.55, mid_E, f"{int(delta_E_factor)}D", va='center', fontsize=9, color='k')

    ax.set_xlim(0,1.5)
    ax.set_ylabel("Energy (cm$^{-1}$)")
    ax.set_xticks([])
    ax.set_title("Spin Eigenstates and Energy Differences (ΔE)")
    ax.grid(False)

    fig.savefig(save_path, dpi=300, bbox_inches='tight')
    plt.close(fig)
    print(f"Energy level splitting diagram saved:{save_path}")

# Example
D = 5
S = 5/2
smm_energy_levels_pm_pair(D, S)
