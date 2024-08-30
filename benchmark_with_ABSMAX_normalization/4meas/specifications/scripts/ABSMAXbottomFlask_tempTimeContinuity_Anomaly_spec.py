import sys

with open(sys.argv[1], "w") as txt_file:
    perturbation_eps = float(sys.argv[2])
    # eps for time continuity constraint
    eps = 0.01
    pressure = [0.706964892412231, 0.7072480181200453, 0.707955832389581, 0.7082389580973952, 0.7083805209513023, 0.7076727066817667, 0.7075311438278596, 0.7075311438278596, 0.7080973952434881, 0.7080973952434881, 0.7073895809739524, 0.7073895809739524, 0.7076727066817667, 0.7072480181200453, 0.7071064552661381, 0.7078142695356738, 0.7080973952434881, 0.7085220838052095, 0.7082389580973952, 0.7080973952434881, 0.707955832389581, 0.7080973952434881, 0.7078142695356738, 0.7076727066817667, 0.707955832389581, 0.707955832389581, 0.7075311438278596, 0.7075311438278596, 0.7076727066817667, 0.7078142695356738, 0.7080973952434881, 0.7085220838052095, 0.7078142695356738, 0.7075311438278596, 0.7076727066817667, 0.7076727066817667, 0.7078142695356738, 0.7078142695356738, 0.7080973952434881, 0.707955832389581, 0.7075311438278596, 0.7076727066817667, 0.7080973952434881, 0.7080973952434881, 0.7078142695356738, 0.707955832389581, 0.7075311438278596, 0.7075311438278596, 0.7082389580973952, 0.7080973952434881]
    level = [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0]
    temperature_bottom_flask = [0.6959122632103689, 0.6959122632103689, 0.6959122632103689, 0.6959122632103689, 0.6959122632103689, 0.6959122632103689, 0.6959122632103689, 0.6959122632103689, 0.6959122632103689, 0.6959122632103689, 0.6959122632103689, 0.6959122632103689, 0.6959122632103689, 0.6959122632103689, 0.6959122632103689, 0.6959122632103689, 0.6959122632103689, 0.6959122632103689, 0.6959122632103689, 0.6959122632103689, 0.6959122632103689, 0.6959122632103689, 0.6959122632103689, 0.6959122632103689, 0.6959122632103689, 0.6959122632103689, 0.6959122632103689, 0.6959122632103689, 0.6959122632103689, 0.6959122632103689, 0.6959122632103689, 0.6959122632103689, 0.6959122632103689, 0.6959122632103689, 0.6959122632103689, 0.6959122632103689, 0.6959122632103689, 0.6959122632103689, 0.6959122632103689, 0.6959122632103689, 0.6959122632103689, 0.6959122632103689, 0.6959122632103689, 0.6959122632103689, 0.6959122632103689, 0.6959122632103689, 0.6959122632103689, 0.6959122632103689, 0.6959122632103689, 0.6959122632103689]
    temperature_middle_mantle_heating = [0.8552223371251293, 0.8552223371251293, 0.8552223371251293, 0.8541882109617372, 0.8541882109617372, 0.8541882109617372, 0.8541882109617372, 0.8531540847983454, 0.8531540847983454, 0.8531540847983454, 0.8521199586349535, 0.8510858324715614, 0.8521199586349535, 0.8510858324715614, 0.8510858324715614, 0.8510858324715614, 0.8510858324715614, 0.8500517063081696, 0.8500517063081696, 0.8500517063081696, 0.8490175801447776, 0.8490175801447776, 0.8490175801447776, 0.8490175801447776, 0.8479834539813857, 0.8479834539813857, 0.8479834539813857, 0.8479834539813857, 0.8479834539813857, 0.8469493278179938, 0.8469493278179938, 0.8469493278179938, 0.8459152016546018, 0.8459152016546018, 0.8459152016546018, 0.8459152016546018, 0.8459152016546018, 0.8448810754912099, 0.8448810754912099, 0.8448810754912099, 0.8438469493278179, 0.8438469493278179, 0.8438469493278179, 0.8438469493278179, 0.8428128231644261, 0.8428128231644261, 0.8428128231644261, 0.8417786970010341, 0.8417786970010341, 0.8417786970010341]
    sample_ts = [pressure, level, temperature_bottom_flask, temperature_middle_mantle_heating]

    print(f"; bottom flask temperature time continuity constraint for ABSMAX normalization:", file=txt_file)
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
                if j in [3, 5, 9, 11, 24, 26, 37, 39]:
                    print(f"(assert (>= X_{i}_{j} {-7 - perturbation_eps}))", file=txt_file)
                    print(f"(assert (<= X_{i}_{j} {-7 + perturbation_eps}))\n", file=txt_file)
                elif j in [4, 10, 25, 38]:
                    print(f"(assert (>= X_{i}_{j} {0.98 - perturbation_eps}))", file=txt_file)
                    print(f"(assert (<= X_{i}_{j} {0.98 + perturbation_eps}))\n", file=txt_file)
                else:
                    print(f"(assert (>= X_{i}_{j} {sample_ts[i][j] - perturbation_eps}))", file=txt_file)
                    print(f"(assert (<= X_{i}_{j} {sample_ts[i][j] + perturbation_eps}))\n", file=txt_file)
            else:
                print(f"(assert (>= X_{i}_{j} {sample_ts[i][j]}))", file=txt_file)
                print(f"(assert (<= X_{i}_{j} {sample_ts[i][j]}))\n", file=txt_file)

    # Declare bottom flask temperature time continuity constraint.
    print(f"; bottom flask temperature time continuity constraint:", file=txt_file)
    print(f"(assert (or", file=txt_file)
    for j in range(0, 49):
        print(f"    (and (>= X_2_{j} (+ X_2_{j + 1} {eps})))", file=txt_file)
        print(f"    (and (>= X_2_{j + 1} (+ X_2_{j} {eps})))", file=txt_file)
    print(f"))", file=txt_file)
    print(f"(assert (> Y_0 Y_1))", file=txt_file)
    print(f"VNNLIB file completed!")

    