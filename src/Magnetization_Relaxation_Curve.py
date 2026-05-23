import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

def plot_relaxation_curve(D, S, T, tau0=1e-9, save_path="SMM_relaxation_curve.png"):
    # Calculate effective barrier
    if S % 1 == 0:
        U_eff = abs(D)*S**2
    else:
        U_eff = abs(D)*(S**2 - 0.25)

    kB = 0.695  # cm^-1/K
    tau = tau0 * np.exp(U_eff/(kB*T))

    # Single-exponential relaxation
    def dMdt(t, M):
        return -M/tau

    t_span = (0, 5*tau)
    t_eval = np.linspace(t_span[0], t_span[1], 500)
    sol = solve_ivp(dMdt, t_span, [1.0], t_eval=t_eval)

    # Plot
    fig, ax = plt.subplots(figsize=(6,4))
    ax.plot(sol.t*1e3, sol.y[0], 'C1', lw=2)
    ax.set_xlabel("Time (ms)")
    ax.set_ylabel("M(t)/M0")
    ax.set_title("Magnetization Relaxation Curve")
    ax.grid(False)

    fig.savefig(save_path, dpi=300, bbox_inches='tight')
    plt.close(fig)

    print(f"Relaxation curve saved: {save_path}")
    print(f"Effective barrier U_eff = {U_eff:.4f} cm^-1")
    print(f"Relaxation time tau = {tau:.3e} s")
    return tau

# Example usage
if __name__ == "__main__":
    D = 5
    S = 5/2
    T = 2.0
    plot_relaxation_curve(D, S, T, tau0=1e-9)
