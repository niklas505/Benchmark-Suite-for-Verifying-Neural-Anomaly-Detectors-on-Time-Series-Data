import sys

with open(sys.argv[1], "w") as txt_file:
    perturbation_eps = float(sys.argv[2])
    pressure = [0.09130816505706751, 0.0921861281826164, 0.09438103599648828, 0.09525899912203695, 0.09569798068481128, 0.0935030728709394, 0.09306409130816506, 0.09306409130816506, 0.09482001755926239, 0.09482001755926239, 0.09262510974539073, 0.09262510974539073, 0.0935030728709394, 0.0921861281826164, 0.09174714661984207, 0.09394205443371373, 0.09482001755926239, 0.09613696224758561, 0.09525899912203695, 0.09482001755926239, 0.09438103599648828, 0.09482001755926239, 0.09394205443371373, 0.0935030728709394, 0.09438103599648828, 0.09438103599648828, 0.09306409130816506, 0.09306409130816506, 0.0935030728709394, 0.09394205443371373, 0.09482001755926239, 0.09613696224758561, 0.09394205443371373, 0.09306409130816506, 0.0935030728709394, 0.0935030728709394, 0.09394205443371373, 0.09394205443371373, 0.09482001755926239, 0.09438103599648828, 0.09306409130816506, 0.0935030728709394, 0.09482001755926239, 0.09482001755926239, 0.09394205443371373, 0.09438103599648828, 0.09306409130816506, 0.09306409130816506, 0.09525899912203695, 0.09482001755926239]
    sample_ts = [pressure]

    print(f"; Pressure Positivity constraint for MINMAX normalization:", file=txt_file)
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
                if j in [3, 4, 5, 7, 8, 10]:
                    print(f"(assert (>= X_{i}_{j} {-2.3 - perturbation_eps}))", file=txt_file)
                    print(f"(assert (<= X_{i}_{j} {-2.3 + perturbation_eps}))\n", file=txt_file)
                else:
                    print(f"(assert (>= X_{i}_{j} {sample_ts[i][j] - perturbation_eps}))", file=txt_file)
                    print(f"(assert (<= X_{i}_{j} {sample_ts[i][j] + perturbation_eps}))\n", file=txt_file)
            else:
                print(f"(assert (>= X_{i}_{j} {sample_ts[i][j]}))", file=txt_file)
                print(f"(assert (<= X_{i}_{j} {sample_ts[i][j]}))\n", file=txt_file)

    # Declare pressure positvity constraint. Zero is mapped to aprox. -2.10097 during the normalization
    print(f"; Pressure positivity constraint (pressure zero mapped to aprox. -2.10097 during input normalization):", file=txt_file)
    print(f"(assert (or", file=txt_file)
    for j in range(0, 50):
        print(f"    (and (<= X_0_{j} -2.10097))", file=txt_file)
    print(f"))", file=txt_file)
    print(f"(assert (> Y_0 Y_1))", file=txt_file)
    print(f"VNNLIB file completed!")