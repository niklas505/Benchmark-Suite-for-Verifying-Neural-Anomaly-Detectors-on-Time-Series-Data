import sys

with open(sys.argv[1], "w") as txt_file:
    pressure = [0.5456540825285338, 0.5460930640913082, 0.5471905179982441, 0.5476294995610185, 0.5478489903424056, 0.5467515364354697, 0.5465320456540825, 0.5465320456540825, 0.5474100087796312, 0.5474100087796312, 0.5463125548726954, 0.5463125548726954, 0.5467515364354697, 0.5460930640913082, 0.545873573309921, 0.5469710272168569, 0.5474100087796312, 0.5480684811237928, 0.5476294995610185, 0.5474100087796312, 0.5471905179982441, 0.5474100087796312, 0.5469710272168569, 0.5467515364354697, 0.5471905179982441, 0.5471905179982441, 0.5465320456540825, 0.5465320456540825, 0.5467515364354697, 0.5469710272168569, 0.5474100087796312, 0.5480684811237928, 0.5469710272168569, 0.5465320456540825, 0.5467515364354697, 0.5467515364354697, 0.5469710272168569, 0.5469710272168569, 0.5474100087796312, 0.5471905179982441, 0.5465320456540825, 0.5467515364354697, 0.5474100087796312, 0.5474100087796312, 0.5469710272168569, 0.5471905179982441, 0.5465320456540825, 0.5465320456540825, 0.5476294995610185, 0.5474100087796312]
    sample_ts = [pressure]

    print(f"; Pressure Positivity constraint for 01 normalization:", file=txt_file)
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
                print(f"(assert (>= X_{i}_{j} -1000))", file=txt_file)
                print(f"(assert (<= X_{i}_{j} 1000))\n", file=txt_file)
            else:
                print(f"(assert (>= X_{i}_{j} {sample_ts[i][j]}))", file=txt_file)
                print(f"(assert (<= X_{i}_{j} {sample_ts[i][j]}))\n", file=txt_file)

    # Declare pressure positvity constraint. Zero is mapped to aprox. -0.55048 during the normalization
    print(f"; Pressure positivity constraint (pressure zero mapped to aprox. -0.55048 during input normalization):", file=txt_file)
    print(f"(assert (or", file=txt_file)
    for j in range(0, 50):
        print(f"    (and (<= X_0_{j} -0.55048))", file=txt_file)
    print(f"))", file=txt_file)
    print(f"(assert (> Y_0 Y_1))", file=txt_file)
    print(f"VNNLIB file completed!")

    