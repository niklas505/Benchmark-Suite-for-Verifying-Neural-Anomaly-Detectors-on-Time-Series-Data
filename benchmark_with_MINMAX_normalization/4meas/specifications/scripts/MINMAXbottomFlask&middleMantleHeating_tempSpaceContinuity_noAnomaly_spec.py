import sys

with open(sys.argv[1], "w") as txt_file:
    perturbation_eps = float(sys.argv[2])
    # eps for space continuity constraint
    eps = 35
    pressure = [0.09130816505706751, 0.0921861281826164, 0.09438103599648828, 0.09525899912203695, 0.09569798068481128, 0.0935030728709394, 0.09306409130816506, 0.09306409130816506, 0.09482001755926239, 0.09482001755926239, 0.09262510974539073, 0.09262510974539073, 0.0935030728709394, 0.0921861281826164, 0.09174714661984207, 0.09394205443371373, 0.09482001755926239, 0.09613696224758561, 0.09525899912203695, 0.09482001755926239, 0.09438103599648828, 0.09482001755926239, 0.09394205443371373, 0.0935030728709394, 0.09438103599648828, 0.09438103599648828, 0.09306409130816506, 0.09306409130816506, 0.0935030728709394, 0.09394205443371373, 0.09482001755926239, 0.09613696224758561, 0.09394205443371373, 0.09306409130816506, 0.0935030728709394, 0.0935030728709394, 0.09394205443371373, 0.09394205443371373, 0.09482001755926239, 0.09438103599648828, 0.09306409130816506, 0.0935030728709394, 0.09482001755926239, 0.09482001755926239, 0.09394205443371373, 0.09438103599648828, 0.09306409130816506, 0.09306409130816506, 0.09525899912203695, 0.09482001755926239]
    level = [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0]
    temperature_bottom_flask = [-0.38636363636363635, -0.38636363636363635, -0.38636363636363635, -0.38636363636363635, -0.38636363636363635, -0.38636363636363635, -0.38636363636363635, -0.38636363636363635, -0.38636363636363635, -0.38636363636363635, -0.38636363636363635, -0.38636363636363635, -0.38636363636363635, -0.38636363636363635, -0.38636363636363635, -0.38636363636363635, -0.38636363636363635, -0.38636363636363635, -0.38636363636363635, -0.38636363636363635, -0.38636363636363635, -0.38636363636363635, -0.38636363636363635, -0.38636363636363635, -0.38636363636363635, -0.38636363636363635, -0.38636363636363635, -0.38636363636363635, -0.38636363636363635, -0.38636363636363635, -0.38636363636363635, -0.38636363636363635, -0.38636363636363635, -0.38636363636363635, -0.38636363636363635, -0.38636363636363635, -0.38636363636363635, -0.38636363636363635, -0.38636363636363635, -0.38636363636363635, -0.38636363636363635, -0.38636363636363635, -0.38636363636363635, -0.38636363636363635, -0.38636363636363635, -0.38636363636363635, -0.38636363636363635, -0.38636363636363635, -0.38636363636363635, -0.38636363636363635]
    temperature_middle_mantle_heating = [0.1384615384615384, 0.1384615384615384, 0.1384615384615384, 0.1323076923076918, 0.1323076923076918, 0.1323076923076918, 0.1323076923076918, 0.12615384615384606, 0.12615384615384606, 0.12615384615384606, 0.1200000000000001, 0.11384615384615349, 0.1200000000000001, 0.11384615384615349, 0.11384615384615349, 0.11384615384615349, 0.11384615384615349, 0.10769230769230775, 0.10769230769230775, 0.10769230769230775, 0.10153846153846091, 0.10153846153846091, 0.10153846153846091, 0.10153846153846091, 0.09538461538461518, 0.09538461538461518, 0.09538461538461518, 0.09538461538461518, 0.09538461538461518, 0.08923076923076945, 0.08923076923076945, 0.08923076923076945, 0.08307692307692283, 0.08307692307692283, 0.08307692307692283, 0.08307692307692283, 0.08307692307692283, 0.07692307692307687, 0.07692307692307687, 0.07692307692307687, 0.07076923076923025, 0.07076923076923025, 0.07076923076923025, 0.07076923076923025, 0.06461538461538452, 0.06461538461538452, 0.06461538461538452, 0.058461538461538565, 0.058461538461538565, 0.058461538461538565]
    sample_ts = [pressure, level, temperature_bottom_flask, temperature_middle_mantle_heating]

    print(f"; bottom flask and middle mantle heating temperature space continuity constraint for MINMAX normalization:", file=txt_file)
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
            if i in [2,3]:
                print(f"(assert (>= X_{i}_{j} {sample_ts[i][j] - perturbation_eps}))", file=txt_file)
                print(f"(assert (<= X_{i}_{j} {sample_ts[i][j] + perturbation_eps}))\n", file=txt_file)
            else:
                print(f"(assert (>= X_{i}_{j} {sample_ts[i][j]}))", file=txt_file)
                print(f"(assert (<= X_{i}_{j} {sample_ts[i][j]}))\n", file=txt_file)

    # Declare bottom flask and middle mantle heating temperature space continuity constraint (normalization inverted to compare temperature measures).
    print(f"; bottom flask and middle mantle heating temperature space continuity constraint (normalization inverted to compare temperature measures):", file=txt_file)
    print(f"(assert (or", file=txt_file)
    for j in range(0, 50):
        print(f"    (and (>= (* X_2_{j} 22) (+ (* X_3_{j} 16.25) {2.15 + eps})))", file=txt_file)
        print(f"    (and (>= (* X_3_{j} 16.25) (+ (* X_2_{j} 22) {-2.15 + eps})))", file=txt_file)
    print(f"))", file=txt_file)
    print(f"(assert (> Y_0 Y_1))", file=txt_file)
    print(f"VNNLIB file completed!")

    