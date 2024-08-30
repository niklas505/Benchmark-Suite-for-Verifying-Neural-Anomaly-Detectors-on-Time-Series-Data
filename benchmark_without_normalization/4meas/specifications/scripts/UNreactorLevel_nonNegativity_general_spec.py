import sys

with open(sys.argv[1], "w") as txt_file:
    # very small eps to approximate strict inequality
    eps = 1e-5
    pressure = [499.4, 499.6, 500.1, 500.3, 500.4, 499.9, 499.8, 499.8, 500.2, 500.2, 499.7, 499.7, 499.9, 499.6, 499.5, 500.0, 500.2, 500.5, 500.3, 500.2, 500.1, 500.2, 500.0, 499.9, 500.1, 500.1, 499.8, 499.8, 499.9, 500.0, 500.2, 500.5, 500.0, 499.8, 499.9, 499.9, 500.0, 500.0, 500.2, 500.1, 499.8, 499.9, 500.2, 500.2, 500.0, 500.1, 499.8, 499.8, 500.3, 500.2]
    level = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    temperature_bottom_flask = [69.8, 69.8, 69.8, 69.8, 69.8, 69.8, 69.8, 69.8, 69.8, 69.8, 69.8, 69.8, 69.8, 69.8, 69.8, 69.8, 69.8, 69.8, 69.8, 69.8, 69.8, 69.8, 69.8, 69.8, 69.8, 69.8, 69.8, 69.8, 69.8, 69.8, 69.8, 69.8, 69.8, 69.8, 69.8, 69.8, 69.8, 69.8, 69.8, 69.8, 69.8, 69.8, 69.8, 69.8, 69.8, 69.8, 69.8, 69.8, 69.8, 69.8]
    temperature_middle_mantle_heating = [82.7, 82.7, 82.7, 82.6, 82.6, 82.6, 82.6, 82.5, 82.5, 82.5, 82.4, 82.3, 82.4, 82.3, 82.3, 82.3, 82.3, 82.2, 82.2, 82.2, 82.1, 82.1, 82.1, 82.1, 82.0, 82.0, 82.0, 82.0, 82.0, 81.9, 81.9, 81.9, 81.8, 81.8, 81.8, 81.8, 81.8, 81.7, 81.7, 81.7, 81.6, 81.6, 81.6, 81.6, 81.5, 81.5, 81.5, 81.4, 81.4, 81.4]
    sample_ts = [pressure, level, temperature_bottom_flask, temperature_middle_mantle_heating]

    print(f"; Reactor level non-negativity constraint for unnormailzed data:", file=txt_file)
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
            if i == 1:
                print(f"(assert (>= X_{i}_{j} -100))", file=txt_file)
                print(f"(assert (<= X_{i}_{j} 100))\n", file=txt_file)
            else:
                print(f"(assert (>= X_{i}_{j} {sample_ts[i][j]}))", file=txt_file)
                print(f"(assert (<= X_{i}_{j} {sample_ts[i][j]}))\n", file=txt_file)

    # Declare reactor level non-negativity constraint.
    print(f"; Reactor level non-negativity constraint:", file=txt_file)
    print(f"(assert (or", file=txt_file)
    for j in range(0, 50):
        print(f"    (and (<= X_1_{j} {-eps}))", file=txt_file)
    print(f"))", file=txt_file)
    print(f"(assert (> Y_0 Y_1))", file=txt_file)
    print(f"VNNLIB file completed!")

    