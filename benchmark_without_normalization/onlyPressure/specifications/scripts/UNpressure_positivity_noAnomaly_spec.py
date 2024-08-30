import sys

with open(sys.argv[1], "w") as txt_file:
    robust_eps = float(sys.argv[2])
    pressure = [499.4, 499.6, 500.1, 500.3, 500.4, 499.9, 499.8, 499.8, 500.2, 500.2, 499.7, 499.7, 499.9, 499.6, 499.5, 500.0, 500.2, 500.5, 500.3, 500.2, 500.1, 500.2, 500.0, 499.9, 500.1, 500.1, 499.8, 499.8, 499.9, 500.0, 500.2, 500.5, 500.0, 499.8, 499.9, 499.9, 500.0, 500.0, 500.2, 500.1, 499.8, 499.9, 500.2, 500.2, 500.0, 500.1, 499.8, 499.8, 500.3, 500.2]
    sample_ts = [pressure]

    print(f"; Pressure Positivity constraint for unnormalized data:", file=txt_file)
    # Declare Variables
    for i in range(0,1):
        for j in range(0, 50):
            print(f"(declare-const X_{i}_{j} Real)", file=txt_file)

    print(f"(declare-const Y_1 Real)", file=txt_file)
    print(f"(declare-const Y_0 Real\n)", file=txt_file)

    # Declare input constraints
    print(f"; Input constraints:", file=txt_file)
    for i in range(0,1):
        for j in range(0, 50):
            if i == 0:
                print(f"(assert (>= X_{i}_{j} {sample_ts[i][j] - robust_eps}))", file=txt_file)
                print(f"(assert (<= X_{i}_{j} {sample_ts[i][j] + robust_eps}))\n", file=txt_file)
            else:
                print(f"(assert (>= X_{i}_{j} {sample_ts[i][j]}))", file=txt_file)
                print(f"(assert (<= X_{i}_{j} {sample_ts[i][j]}))\n", file=txt_file)

    # Declare pressure positvity constraint.
    print(f"; Pressure positivity constraint:", file=txt_file)
    print(f"(assert (or", file=txt_file)
    for j in range(0, 50):
        print(f"    (and (<= X_0_{j} 0))", file=txt_file)
    print(f"))", file=txt_file)
    print(f"(assert (> Y_0 Y_1))", file=txt_file)
    print(f"VNNLIB file completed!")