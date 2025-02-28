import numpy as np

def monte_carlo_simulation(num_trials=100000):
    people = ["K1", "K2"] + list(range(1, 9))  # Kardeşler + 8 kişi
    success_count = 0

    for _ in range(num_trials):
        np.random.shuffle(people)  # Rastgele sırala
        # Kardeşler yan yana mı?
        for i in range(len(people) - 1):
            if (people[i] == "K1" and people[i + 1] == "K2") or (people[i] == "K2" and people[i + 1] == "K1"):
                success_count += 1
                break

    probability = success_count / num_trials
    return probability

# Simülasyonu çalıştır
simulated_probability = monte_carlo_simulation()
print(f"Monte Carlo Simülasyonu Sonucu: {simulated_probability:.4f}")
