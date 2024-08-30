import sys

with open(sys.argv[1], "w") as txt_file:
    perturbation_eps = float(sys.argv[2])
    # eps to approximate strict inequality but avoid very small temperature variations affect monotonicity
    eps1 = 1e-2
    # very small eps to approximate strict inequality for maximum temperature
    eps2 = 1e-5
    # maximal Temperature
    maxT = 1
    pressure = [0.5456540825285338, 0.5460930640913082, 0.5471905179982441, 0.5476294995610185, 0.5478489903424056, 0.5467515364354697, 0.5465320456540825, 0.5465320456540825, 0.5474100087796312, 0.5474100087796312, 0.5463125548726954, 0.5463125548726954, 0.5467515364354697, 0.5460930640913082, 0.545873573309921, 0.5469710272168569, 0.5474100087796312, 0.5480684811237928, 0.5476294995610185, 0.5474100087796312, 0.5471905179982441, 0.5474100087796312, 0.5469710272168569, 0.5467515364354697, 0.5471905179982441, 0.5471905179982441, 0.5465320456540825, 0.5465320456540825, 0.5467515364354697, 0.5469710272168569, 0.5474100087796312, 0.5480684811237928, 0.5469710272168569, 0.5465320456540825, 0.5467515364354697, 0.5467515364354697, 0.5469710272168569, 0.5469710272168569, 0.5474100087796312, 0.5471905179982441, 0.5465320456540825, 0.5467515364354697, 0.5474100087796312, 0.5474100087796312, 0.5469710272168569, 0.5471905179982441, 0.5465320456540825, 0.5465320456540825, 0.5476294995610185, 0.5474100087796312]
    level = [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0]
    temperature_bottom_flask = [0.3068181818181818, 0.3068181818181818, 0.3068181818181818, 0.3068181818181818, 0.3068181818181818, 0.3068181818181818, 0.3068181818181818, 0.3068181818181818, 0.3068181818181818, 0.3068181818181818, 0.3068181818181818, 0.3068181818181818, 0.3068181818181818, 0.3068181818181818, 0.3068181818181818, 0.3068181818181818, 0.3068181818181818, 0.3068181818181818, 0.3068181818181818, 0.3068181818181818, 0.3068181818181818, 0.3068181818181818, 0.3068181818181818, 0.3068181818181818, 0.3068181818181818, 0.3068181818181818, 0.3068181818181818, 0.3068181818181818, 0.3068181818181818, 0.3068181818181818, 0.3068181818181818, 0.3068181818181818, 0.3068181818181818, 0.3068181818181818, 0.3068181818181818, 0.3068181818181818, 0.3068181818181818, 0.3068181818181818, 0.3068181818181818, 0.3068181818181818, 0.3068181818181818, 0.3068181818181818, 0.3068181818181818, 0.3068181818181818, 0.3068181818181818, 0.3068181818181818, 0.3068181818181818, 0.3068181818181818, 0.3068181818181818, 0.3068181818181818]
    temperature_middle_mantle_heating = [0.5692307692307692, 0.5692307692307692, 0.5692307692307692, 0.5661538461538459, 0.5661538461538459, 0.5661538461538459, 0.5661538461538459, 0.563076923076923, 0.563076923076923, 0.563076923076923, 0.56, 0.5569230769230767, 0.56, 0.5569230769230767, 0.5569230769230767, 0.5569230769230767, 0.5569230769230767, 0.5538461538461539, 0.5538461538461539, 0.5538461538461539, 0.5507692307692305, 0.5507692307692305, 0.5507692307692305, 0.5507692307692305, 0.5476923076923076, 0.5476923076923076, 0.5476923076923076, 0.5476923076923076, 0.5476923076923076, 0.5446153846153847, 0.5446153846153847, 0.5446153846153847, 0.5415384615384614, 0.5415384615384614, 0.5415384615384614, 0.5415384615384614, 0.5415384615384614, 0.5384615384615384, 0.5384615384615384, 0.5384615384615384, 0.5353846153846151, 0.5353846153846151, 0.5353846153846151, 0.5353846153846151, 0.5323076923076923, 0.5323076923076923, 0.5323076923076923, 0.5292307692307693, 0.5292307692307693, 0.5292307692307693]
    sample_ts = [pressure, level, temperature_bottom_flask, temperature_middle_mantle_heating]

    print(f"; bottom flask temperature increasing constraint for 01 normalization:", file=txt_file)
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

    