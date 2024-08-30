import sys

with open(sys.argv[1], "w") as txt_file:
    # eps for continuity constraint
    eps = 0.01
    pressure = [0.706964892412231, 0.7072480181200453, 0.707955832389581, 0.7082389580973952, 0.7083805209513023, 0.7076727066817667, 0.7075311438278596, 0.7075311438278596, 0.7080973952434881, 0.7080973952434881, 0.7073895809739524, 0.7073895809739524, 0.7076727066817667, 0.7072480181200453, 0.7071064552661381, 0.7078142695356738, 0.7080973952434881, 0.7085220838052095, 0.7082389580973952, 0.7080973952434881, 0.707955832389581, 0.7080973952434881, 0.7078142695356738, 0.7076727066817667, 0.707955832389581, 0.707955832389581, 0.7075311438278596, 0.7075311438278596, 0.7076727066817667, 0.7078142695356738, 0.7080973952434881, 0.7085220838052095, 0.7078142695356738, 0.7075311438278596, 0.7076727066817667, 0.7076727066817667, 0.7078142695356738, 0.7078142695356738, 0.7080973952434881, 0.707955832389581, 0.7075311438278596, 0.7076727066817667, 0.7080973952434881, 0.7080973952434881, 0.7078142695356738, 0.707955832389581, 0.7075311438278596, 0.7075311438278596, 0.7082389580973952, 0.7080973952434881]
    sample_ts = [pressure]

    print(f"; Pressure Continuity constraint for MINMAX normalization:", file=txt_file)
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

    # Declare pressure continuity constraint.
    print(f"; Pressure continuity constraint:", file=txt_file)
    print(f"(assert (or", file=txt_file)
    for j in range(0, 49):
        print(f"    (and (>= X_0_{j} (+ X_0_{j + 1} {eps})))", file=txt_file)
        print(f"    (and (>= X_0_{j + 1} (+ X_0_{j} {eps})))", file=txt_file)
    print(f"))", file=txt_file)
    print(f"(assert (> Y_0 Y_1))", file=txt_file)
    print(f"VNNLIB file completed!")

    