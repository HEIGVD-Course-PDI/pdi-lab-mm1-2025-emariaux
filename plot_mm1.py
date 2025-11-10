from matplotlib import pyplot as plt
from main_mm1 import main as mm1
import numpy as np

def plot_mm1():
    """Plot the results of the MM1 simulation."""

    # Parameters
    service_rate = 50.0
    arrival_rates = np.arange(1, service_rate, 1)  # From 1 to 49 with step of 1
    simulation_time = 10000.0

    response_times = []
    num_in_system = []
    utilizations = []

    for arrival_rate in arrival_rates:
        result = mm1(arrival_rate, service_rate, simulation_time)
        
        response_times.append(result['E[T]'])
        num_in_system.append(result['E[N]'])
        utilizations.append(arrival_rate / service_rate)  # ρ = λ/μ

    # Plot 1: Response Time vs Utilization
    plt.figure(figsize=(8, 6))
    plt.plot(utilizations, response_times, 'b-o', label='Simulation', markersize=4)
    plt.title('Average Response Time vs Utilization')
    plt.xlabel('Utilization ρ = λ/μ')
    plt.ylabel('Average Response Time E[T] [s]')
    plt.grid(True)
    plt.legend()
    plt.tight_layout()
    plt.savefig('mm1_t.png', dpi=300, bbox_inches='tight')
    plt.close()
    print("Saved: mm1_t.png")

    # Plot 2: Number in System vs Utilization
    plt.figure(figsize=(8, 6))
    plt.plot(utilizations, num_in_system, 'r-o', label='Simulation', markersize=4)
    plt.title('Average Number in System vs Utilization')
    plt.xlabel('Utilization ρ = λ/μ')
    plt.ylabel('Average Number in System E[N]')
    plt.grid(True)
    plt.legend()
    plt.tight_layout()
    plt.savefig('mm1_n.png', dpi=300, bbox_inches='tight')
    plt.close()
    print("Saved: mm1_n.png")

if __name__ == "__main__":
    plot_mm1()