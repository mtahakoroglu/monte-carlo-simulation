import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats

# Parameters of the normal distribution
mu = 5       # Mean
sigma = 0.1  # Standard deviation
num_samples = 100000  # Monte Carlo sample size

# Generate Monte Carlo samples
samples = np.random.normal(mu, sigma, num_samples)

# Plot histogram of the Monte Carlo samples
plt.hist(samples, bins=50, density=True, alpha=0.5, label="MCS Histogram", color="blue")

# Generate x values for the normal distribution curve
x = np.linspace(mu - 4*sigma, mu + 4*sigma, 1000)
pdf = stats.norm.pdf(x, mu, sigma)  # Probability Density Function

# Plot the normal distribution curve
plt.plot(x, pdf, 'r-', label="Normal Dağılım PDF")

# Shade the acceptable region (4.9 to 5.1)
x_shade = np.linspace(4.9, 5.1, 100)
pdf_shade = stats.norm.pdf(x_shade, mu, sigma)
plt.fill_between(x_shade, pdf_shade, color='green', alpha=0.5, label="İlgilendiğimiz Aralık")

# Labels and title
plt.xlabel("Vida Çapı [mm]", fontsize=16)
# plt.ylabel("Olasılık", fontsize=16)
plt.title("Monte Carlo Simülasyonu vs. Normal Dağılım")
plt.legend()
plt.grid(True, linestyle='--')
plt.tight_layout()
# plt.subplots_adjust(left=0.11)  # Increase left margin specifically
plt.xticks(fontsize=16)  # Makes x-axis numbers bigger
plt.yticks(fontsize=16)  # Makes y-axis numbers bigger
plt.legend(fontsize=10)
plt.savefig(f"screws.png", dpi=500)
# Show the plot
plt.show()