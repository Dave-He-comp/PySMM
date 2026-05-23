import numpy as np
import matplotlib.pyplot as plt
from fractions import Fraction

def format_mS_label(m):
    """Convert mS to a fraction string; integer shows as integer."""
    if m % 1 == 0:
        return f"M$_S$={int(m)}"
    else:
        frac = Fraction(m).limit_denominator()
        return f"M$_S$={frac.numerator}/{frac.denominator}"

def plot_smm_barrier(D, S, save_path="SMM_potential_barrier.png"):
    # Continuous barrier curve
    mS_cont = np.linspace(-S, S, 400)
    energies_cont = -D * (mS_cont**2 - S*(S+1)/3)
    energies_cont -= np.min(energies_cont)

    # Discrete energy levels
    mS = np.arange(-S, S+1, 1)
    energies = -D * (mS**2 - S*(S+1)/3)
    energies -= np.min(energies)

    # Plot
    fig, ax = plt.subplots(figsize=(6,5))
    ax.plot(mS_cont, energies_cont, 'C0', lw=2)
    for i, E in enumerate(energies):
        ax.hlines(E, mS[i]-0.08, mS[i]+0.08, colors='C1', lw=2)
        ax.text(mS[i], E + 0.05*np.max(energies), format_mS_label(mS[i]),
                ha='center', va='bottom', fontsize=10, color='C1')

    ax.set_ylabel("Energy (cm$^{-1}$)")
    ax.set_xticks([])
    ax.set_title("SMM Spin Potential Barrier")
    ax.grid(False)

    fig.savefig(save_path, dpi=300, bbox_inches='tight')
    plt.close(fig)
    print(f"Barrier plot saved: {save_path}")

# Example usage
if __name__ == "__main__":
    D = 5
    S = 5/2
    plot_smm_barrier(D, S)
