import sys

with open(sys.argv[1], "w") as txt_file:
    perturbation_eps = float(sys.argv[2])
    # eps to approximate strict inequality but avoid very small temperature variations affect monotonicity
    eps1 = 0.2
    # very small eps to approximate strict inequality for maximum temperature
    eps2 = 1e-5
    # maximal Temperature
    maxT = 102
    pressure = [499.4, 499.6, 500.1, 500.3, 500.4, 499.9, 499.8, 499.8, 500.2, 500.2, 499.7, 499.7, 499.9, 499.6, 499.5, 500.0, 500.2, 500.5, 500.3, 500.2, 500.1, 500.2, 500.0, 499.9, 500.1, 500.1, 499.8, 499.8, 499.9, 500.0, 500.2, 500.5, 500.0, 499.8, 499.9, 499.9, 500.0, 500.0, 500.2, 500.1, 499.8, 499.9, 500.2, 500.2, 500.0, 500.1, 499.8, 499.8, 500.3, 500.2]
    level = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    temperature_bottom_flask = [69.8, 69.8, 69.8, 69.8, 69.8, 69.8, 69.8, 69.8, 69.8, 69.8, 69.8, 69.8, 69.8, 69.8, 69.8, 69.8, 69.8, 69.8, 69.8, 69.8, 69.8, 69.8, 69.8, 69.8, 69.8, 69.8, 69.8, 69.8, 69.8, 69.8, 69.8, 69.8, 69.8, 69.8, 69.8, 69.8, 69.8, 69.8, 69.8, 69.8, 69.8, 69.8, 69.8, 69.8, 69.8, 69.8, 69.8, 69.8, 69.8, 69.8]
    temperature_middle_mantle_heating = [82.7, 82.7, 82.7, 82.6, 82.6, 82.6, 82.6, 82.5, 82.5, 82.5, 82.4, 82.3, 82.4, 82.3, 82.3, 82.3, 82.3, 82.2, 82.2, 82.2, 82.1, 82.1, 82.1, 82.1, 82.0, 82.0, 82.0, 82.0, 82.0, 81.9, 81.9, 81.9, 81.8, 81.8, 81.8, 81.8, 81.8, 81.7, 81.7, 81.7, 81.6, 81.6, 81.6, 81.6, 81.5, 81.5, 81.5, 81.4, 81.4, 81.4]
    sample_ts = [pressure, level, temperature_bottom_flask, temperature_middle_mantle_heating]

    print(f"; bottom flask temperature increasing constraint for unnormalized data:", file=txt_file)
    # Declare Variables
    for i in range(0,4):
        for j in range(0, 50):
            print(f"(declare-const X_{i}_{j} Real)", file=txt_file)

    print(f"(declare-const Y_1 Real)", file=txt_file)
    print(f"(declare-const Y_0 Real\n)", file=txt_file)

    # Declare input constraints
    print(f"; Input constraints:", file=txt_file)
    for i in range(0,4):
        for j in range(0, 50):
            if i == 2:
                print(f"(assert (>= X_{i}_{j} {sample_ts[i][j] - perturbation_eps}))", file=txt_file)
                print(f"(assert (<= X_{i}_{j} {sample_ts[i][j] + perturbation_eps}))\n", file=txt_file)
            else:
                print(f"(assert (>= X_{i}_{j} {sample_ts[i][j]}))", file=txt_file)
                print(f"(assert (<= X_{i}_{j} {sample_ts[i][j]}))\n", file=txt_file)

    # Declare bottom flask temperature increasing constraint.
    print(f"; bottom flask temperature increasing constraint:", file=txt_file)
    print(f"(assert (or", file=txt_file)
    for j in range(0, 49):
        print(f"    (and (>= X_2_{j} (+ X_2_{j + 1} {eps1})))", file=txt_file)
        print(f"    (and (>= X_2_{j} {maxT + eps2}))", file=txt_file)
        if j == 48:
            print(f"    (and (>= X_2_{j + 1} {maxT + eps2}))", file=txt_file)
    print(f"))", file=txt_file)
    print(f"(assert (> Y_0 Y_1))", file=txt_file)
    print(f"VNNLIB file completed!")

    