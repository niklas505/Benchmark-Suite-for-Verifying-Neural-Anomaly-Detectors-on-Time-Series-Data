import sys

with open(sys.argv[1], "w") as txt_file:
    perturbation_eps = float(sys.argv[2])
    # very small eps to approximate strict inequality
    eps = 1e-5
    pressure = [0.09130816505706751, 0.0921861281826164, 0.09438103599648828, 0.09525899912203695, 0.09569798068481128, 0.0935030728709394, 0.09306409130816506, 0.09306409130816506, 0.09482001755926239, 0.09482001755926239, 0.09262510974539073, 0.09262510974539073, 0.0935030728709394, 0.0921861281826164, 0.09174714661984207, 0.09394205443371373, 0.09482001755926239, 0.09613696224758561, 0.09525899912203695, 0.09482001755926239, 0.09438103599648828, 0.09482001755926239, 0.09394205443371373, 0.0935030728709394, 0.09438103599648828, 0.09438103599648828, 0.09306409130816506, 0.09306409130816506, 0.0935030728709394, 0.09394205443371373, 0.09482001755926239, 0.09613696224758561, 0.09394205443371373, 0.09306409130816506, 0.0935030728709394, 0.0935030728709394, 0.09394205443371373, 0.09394205443371373, 0.09482001755926239, 0.09438103599648828, 0.09306409130816506, 0.0935030728709394, 0.09482001755926239, 0.09482001755926239, 0.09394205443371373, 0.09438103599648828, 0.09306409130816506, 0.09306409130816506, 0.09525899912203695, 0.09482001755926239]
    level = [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0]
    temperature_bottom_flask = [-0.38636363636363635, -0.38636363636363635, -0.38636363636363635, -0.38636363636363635, -0.38636363636363635, -0.38636363636363635, -0.38636363636363635, -0.38636363636363635, -0.38636363636363635, -0.38636363636363635, -0.38636363636363635, -0.38636363636363635, -0.38636363636363635, -0.38636363636363635, -0.38636363636363635, -0.38636363636363635, -0.38636363636363635, -0.38636363636363635, -0.38636363636363635, -0.38636363636363635, -0.38636363636363635, -0.38636363636363635, -0.38636363636363635, -0.38636363636363635, -0.38636363636363635, -0.38636363636363635, -0.38636363636363635, -0.38636363636363635, -0.38636363636363635, -0.38636363636363635, -0.38636363636363635, -0.38636363636363635, -0.38636363636363635, -0.38636363636363635, -0.38636363636363635, -0.38636363636363635, -0.38636363636363635, -0.38636363636363635, -0.38636363636363635, -0.38636363636363635, -0.38636363636363635, -0.38636363636363635, -0.38636363636363635, -0.38636363636363635, -0.38636363636363635, -0.38636363636363635, -0.38636363636363635, -0.38636363636363635, -0.38636363636363635, -0.38636363636363635]
    temperature_middle_mantle_heating = [0.1384615384615384, 0.1384615384615384, 0.1384615384615384, 0.1323076923076918, 0.1323076923076918, 0.1323076923076918, 0.1323076923076918, 0.12615384615384606, 0.12615384615384606, 0.12615384615384606, 0.1200000000000001, 0.11384615384615349, 0.1200000000000001, 0.11384615384615349, 0.11384615384615349, 0.11384615384615349, 0.11384615384615349, 0.10769230769230775, 0.10769230769230775, 0.10769230769230775, 0.10153846153846091, 0.10153846153846091, 0.10153846153846091, 0.10153846153846091, 0.09538461538461518, 0.09538461538461518, 0.09538461538461518, 0.09538461538461518, 0.09538461538461518, 0.08923076923076945, 0.08923076923076945, 0.08923076923076945, 0.08307692307692283, 0.08307692307692283, 0.08307692307692283, 0.08307692307692283, 0.08307692307692283, 0.07692307692307687, 0.07692307692307687, 0.07692307692307687, 0.07076923076923025, 0.07076923076923025, 0.07076923076923025, 0.07076923076923025, 0.06461538461538452, 0.06461538461538452, 0.06461538461538452, 0.058461538461538565, 0.058461538461538565, 0.058461538461538565]
    v4 = [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0]
    v5 = [-1.0, -1.0, -1.0, 1.0, 1.0, 1.0, -1.0, -1.0, 1.0, 1.0, -1.0, -1.0, -1.0, -1.0, -1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, -1.0, 1.0, 1.0, -1.0, -1.0, -1.0, -1.0, 1.0, 1.0, 1.0, -1.0, -1.0, -1.0, 1.0, -1.0, 1.0, 1.0, -1.0, -1.0, 1.0, 1.0, 1.0, 1.0, -1.0, -1.0, 1.0, 1.0]
    v6 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    v7 = [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0]
    v8 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    v9 = [0.41176470588235303, 0.41176470588235303, 0.41176470588235303, 0.41176470588235303, 0.41176470588235303, 0.41176470588235303, 0.41176470588235303, 0.41176470588235303, 0.41176470588235303, 0.41176470588235303, 0.41176470588235303, 0.41176470588235303, 0.41176470588235303, 0.41176470588235303, 0.41176470588235303, 0.41176470588235303, 0.41176470588235303, 0.41176470588235303, 0.41176470588235303, 0.41176470588235303, 0.41176470588235303, 0.41176470588235303, 0.41176470588235303, 0.41176470588235303, 0.41176470588235303, 0.41176470588235303, 0.41176470588235303, 0.41176470588235303, 0.41176470588235303, 0.41176470588235303, 0.41176470588235303, 0.41176470588235303, 0.41176470588235303, 0.41176470588235303, 0.41176470588235303, 0.41176470588235303, 0.41176470588235303, 0.41176470588235303, 0.41176470588235303, 0.41176470588235303, 0.41176470588235303, 0.41176470588235303, 0.41176470588235303, 0.41176470588235303, 0.41176470588235303, 0.41176470588235303, 0.41176470588235303, 0.41176470588235303, 0.41176470588235303, 0.41176470588235303]
    v10 = [-1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0]
    v11 = [-1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0]
    v12 = [-1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0]
    v13 = [-1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0]
    v14 = [-0.5800000000000001, -0.584, -0.558, -0.514, -0.498, -0.52, -0.55, -0.546, -0.532, -0.504, -0.5660000000000001, -0.578, -0.556, -0.604, -0.626, -0.5860000000000001, -0.556, -0.508, -0.51, -0.51, -0.52, -0.502, -0.512, -0.532, -0.512, -0.508, -0.53, -0.548, -0.544, -0.54, -0.512, -0.46599999999999997, -0.502, -0.54, -0.528, -0.528, -0.516, -0.518, -0.502, -0.5, -0.53, -0.54, -0.502, -0.486, -0.502, -0.498, -0.526, -0.536, -0.494, -0.482]
    v15 = [-1.0, -1.0, -1.0, -1.0, -0.984, -0.954, -0.878, -0.802, -0.552, -0.63, -0.85, -0.968, -1.0, -1.0, -0.9359999999999999, -0.716, -0.744, -0.774, -0.792, -0.864, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -0.92, -0.772, -0.832, -0.766, -0.962, -0.962, -1.0, -1.0, -1.0, -1.0, -1.0, -0.964, -0.878, -0.774, -0.804, -0.718, -0.8, -1.0, -1.0, -1.0]
    v16 = [-1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -0.47, -1.0, -0.79, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, 1.0, -1.0, -1.0, -1.0, 1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, 1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, 0.706, 1.0, -1.0, -1.0, -1.0, -1.0]
    v17 = [0.6681055155875297, 0.6671462829736212, 0.6681055155875297, 0.6690647482014389, 0.6690647482014389, 0.6681055155875297, 0.6690647482014389, 0.6700239808153474, 0.6700239808153474, 0.6700239808153474, 0.6700239808153474, 0.6709832134292564, 0.6709832134292564, 0.6709832134292564, 0.6709832134292564, 0.6709832134292564, 0.6719424460431656, 0.6719424460431656, 0.6719424460431656, 0.6729016786570741, 0.6729016786570741, 0.6719424460431656, 0.6719424460431656, 0.6738609112709832, 0.6738609112709832, 0.6738609112709832, 0.6748201438848918, 0.6738609112709832, 0.6748201438848918, 0.6748201438848918, 0.6738609112709832, 0.6748201438848918, 0.6757793764988009, 0.6757793764988009, 0.6757793764988009, 0.6757793764988009, 0.6757793764988009, 0.6767386091127099, 0.6767386091127099, 0.6776978417266184, 0.6776978417266184, 0.6767386091127099, 0.6776978417266184, 0.6786570743405276, 0.6776978417266184, 0.6776978417266184, 0.6786570743405276, 0.6786570743405276, 0.6786570743405276, 0.6796163069544361]
    v18 = [-0.36032388663967574, -0.36032388663967574, -0.36032388663967574, -0.36032388663967574, -0.3684210526315792, -0.3684210526315792, -0.3684210526315792, -0.3684210526315792, -0.37651821862348167, -0.3684210526315792, -0.37651821862348167, -0.37651821862348167, -0.37651821862348167, -0.37651821862348167, -0.384615384615384, -0.37651821862348167, -0.37651821862348167, -0.384615384615384, -0.384615384615384, -0.384615384615384, -0.3927125506072875, -0.3927125506072875, -0.3927125506072875, -0.3927125506072875, -0.40080971659918985, -0.3927125506072875, -0.3927125506072875, -0.40080971659918985, -0.40080971659918985, -0.40080971659918985, -0.4089068825910934, -0.40080971659918985, -0.4089068825910934, -0.4089068825910934, -0.4089068825910934, -0.4089068825910934, -0.4089068825910934, -0.4170040485829958, -0.4170040485829958, -0.4170040485829958, -0.4170040485829958, -0.42510121457489813, -0.42510121457489813, -0.42510121457489813, -0.42510121457489813, -0.42510121457489813, -0.42510121457489813, -0.4331983805668017, -0.4331983805668017, -0.4331983805668017]
    v19 = [-0.15596330275229342, -0.16207951070336435, -0.16207951070336435, -0.16207951070336435, -0.16819571865443428, -0.16819571865443428, -0.16819571865443428, -0.16819571865443428, -0.17431192660550432, -0.17431192660550432, -0.17431192660550432, -0.18042813455657514, -0.18042813455657514, -0.18042813455657514, -0.18654434250764518, -0.18654434250764518, -0.18654434250764518, -0.18654434250764518, -0.192660550458716, -0.192660550458716, -0.192660550458716, -0.19877675840978604, -0.192660550458716, -0.19877675840978604, -0.20489296636085597, -0.20489296636085597, -0.20489296636085597, -0.20489296636085597, -0.20489296636085597, -0.2110091743119269, -0.2110091743119269, -0.2110091743119269, -0.21712538226299682, -0.21712538226299682, -0.22324159021406775, -0.22324159021406775, -0.22324159021406775, -0.22324159021406775, -0.22324159021406775, -0.22935779816513768, -0.22935779816513768, -0.22935779816513768, -0.22935779816513768, -0.23547400611620772, -0.23547400611620772, -0.23547400611620772, -0.23547400611620772, -0.24159021406727854, -0.24159021406727854, -0.24770642201834858]
    v20 = [0.23547400611620795, 0.23547400611620795, 0.22935779816513802, 0.22935779816513802, 0.2232415902140672, 0.22935779816513802, 0.22935779816513802, 0.2232415902140672, 0.2232415902140672, 0.2232415902140672, 0.21712538226299727, 0.21712538226299727, 0.21712538226299727, 0.21100917431192712, 0.21712538226299727, 0.21100917431192712, 0.2048929663608563, 0.21100917431192712, 0.21100917431192712, 0.2048929663608563, 0.2048929663608563, 0.2048929663608563, 0.2048929663608563, 0.19877675840978637, 0.19877675840978637, 0.19877675840978637, 0.19877675840978637, 0.19877675840978637, 0.19266055045871555, 0.1865443425076454, 0.19266055045871555, 0.1865443425076454, 0.1865443425076454, 0.1865443425076454, 0.18042813455657547, 0.18042813455657547, 0.18042813455657547, 0.18042813455657547, 0.18042813455657547, 0.18042813455657547, 0.17431192660550465, 0.17431192660550465, 0.17431192660550465, 0.16819571865443472, 0.16819571865443472, 0.16819571865443472, 0.16819571865443472, 0.1620795107033639, 0.1620795107033639, 0.1620795107033639]
    v21 = [-0.28421052631578947, -0.28421052631578947, -0.28421052631578947, -0.28421052631578947, -0.28421052631578947, -0.28421052631578947, -0.28421052631578947, -0.28421052631578947, -0.28421052631578947, -0.28421052631578947, -0.28421052631578947, -0.28421052631578947, -0.28421052631578947, -0.28421052631578947, -0.28421052631578947, -0.28421052631578947, -0.28421052631578947, -0.28421052631578947, -0.28421052631578947, -0.28421052631578947, -0.28421052631578947, -0.28421052631578947, -0.28421052631578947, -0.28421052631578947, -0.28421052631578947, -0.28421052631578947, -0.28421052631578947, -0.28421052631578947, -0.28421052631578947, -0.28421052631578947, -0.28421052631578947, -0.28421052631578947, -0.28421052631578947, -0.28421052631578947, -0.28421052631578947, -0.28421052631578947, -0.28421052631578947, -0.28421052631578947, -0.28421052631578947, -0.28421052631578947, -0.28421052631578947, -0.28421052631578947, -0.28421052631578947, -0.28000000000000025, -0.28000000000000025, -0.28421052631578947, -0.28421052631578947, -0.28421052631578947, -0.28000000000000025, -0.28421052631578947]
    v22 = [-0.3708333333333331, -0.3708333333333331, -0.3708333333333331, -0.3708333333333331, -0.3708333333333331, -0.3666666666666667, -0.3666666666666667, -0.3666666666666667, -0.3666666666666667, -0.3666666666666667, -0.3666666666666667, -0.3666666666666667, -0.3666666666666667, -0.3666666666666667, -0.3666666666666667, -0.3666666666666667, -0.3666666666666667, -0.3666666666666667, -0.3624999999999997, -0.3624999999999997, -0.3624999999999997, -0.3624999999999997, -0.3624999999999997, -0.3624999999999997, -0.3624999999999997, -0.3624999999999997, -0.3624999999999997, -0.3583333333333333, -0.3624999999999997, -0.3583333333333333, -0.3583333333333333, -0.3583333333333333, -0.3583333333333333, -0.3583333333333333, -0.3583333333333333, -0.3583333333333333, -0.3583333333333333, -0.3583333333333333, -0.3583333333333333, -0.3583333333333333, -0.3583333333333333, -0.3583333333333333, -0.35416666666666685, -0.3583333333333333, -0.35416666666666685, -0.35416666666666685, -0.35416666666666685, -0.35416666666666685, -0.35416666666666685, -0.35416666666666685]
    v23 = [-0.3971486761710793, -0.3971486761710793, -0.3971486761710793, -0.3971486761710793, -0.3971486761710793, -0.3971486761710793, -0.3971486761710793, -0.3971486761710793, -0.3971486761710793, -0.39307535641547864, -0.39307535641547864, -0.39307535641547864, -0.39307535641547864, -0.39307535641547864, -0.39307535641547864, -0.39307535641547864, -0.39307535641547864, -0.39307535641547864, -0.39307535641547864, -0.39307535641547864, -0.39307535641547864, -0.39307535641547864, -0.39307535641547864, -0.39307535641547864, -0.39307535641547864, -0.39307535641547864, -0.39307535641547864, -0.39307535641547864, -0.39307535641547864, -0.39307535641547864, -0.39307535641547864, -0.39307535641547864, -0.39307535641547864, -0.39307535641547864, -0.39307535641547864, -0.39307535641547864, -0.39307535641547864, -0.39307535641547864, -0.39307535641547864, -0.39307535641547864, -0.39307535641547864, -0.39307535641547864, -0.39307535641547864, -0.3890020366598781, -0.39307535641547864, -0.3890020366598781, -0.3890020366598781, -0.3890020366598781, -0.3890020366598781, -0.3890020366598781]
    v24 = [-0.34426229508196726, -0.34426229508196726, -0.34426229508196726, -0.34426229508196726, -0.34426229508196726, -0.34426229508196726, -0.34426229508196726, -0.3401639344262295, -0.34426229508196726, -0.3401639344262295, -0.34426229508196726, -0.34426229508196726, -0.3401639344262295, -0.34426229508196726, -0.34426229508196726, -0.34426229508196726, -0.3401639344262295, -0.34426229508196726, -0.34426229508196726, -0.34426229508196726, -0.3401639344262295, -0.3401639344262295, -0.3401639344262295, -0.3401639344262295, -0.3401639344262295, -0.3401639344262295, -0.3401639344262295, -0.3401639344262295, -0.3401639344262295, -0.3401639344262295, -0.3401639344262295, -0.3401639344262295, -0.3401639344262295, -0.3401639344262295, -0.3401639344262295, -0.3401639344262295, -0.3401639344262295, -0.3401639344262295, -0.3401639344262295, -0.3401639344262295, -0.3401639344262295, -0.3401639344262295, -0.3401639344262295, -0.3401639344262295, -0.3401639344262295, -0.3401639344262295, -0.3401639344262295, -0.3401639344262295, -0.3401639344262295, -0.3401639344262295]
    v25 = [-0.9365079365079365, -0.9365079365079365, -0.9365079365079365, -0.9365079365079365, -0.9365079365079365, -0.9365079365079365, -0.9365079365079365, -0.9365079365079365, -0.9365079365079365, -0.9365079365079365, -0.9365079365079365, -0.9047619047619048, -0.9047619047619048, -0.9365079365079365, -0.9682539682539683, -0.9682539682539683, -1.0, -1.0, -0.9365079365079365, -0.39682539682539686, -0.9047619047619048, -1.0, -0.9047619047619048, -0.39682539682539686, -0.9047619047619048, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -0.7777777777777778, -0.39682539682539686, -0.39682539682539686, -0.9365079365079365, -1.0, -0.9365079365079365, -0.9682539682539683, -0.9682539682539683, -1.0, -1.0, -1.0, -1.0, -1.0, -0.7142857142857142, -0.492063492063492, -0.9682539682539683, -1.0]
    v26 = [-1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -0.9682539682539683, -0.492063492063492, -0.9682539682539683, -0.5873015873015872, -0.5873015873015872, -0.8095238095238095, -0.9682539682539683, -1.0, -1.0, -0.9365079365079365, -0.746031746031746, -0.746031746031746, -0.746031746031746, -0.746031746031746, -0.9047619047619048, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -0.9047619047619048, -0.492063492063492, -0.9047619047619048, -0.9047619047619048, -0.8095238095238095, -0.9365079365079365, -0.9682539682539683, -1.0, -1.0, -1.0, -1.0, -0.9682539682539683, -0.873015873015873, -0.8095238095238095, -0.746031746031746, -0.746031746031746, -0.9047619047619048, -1.0]
    v27 = [-0.972318339100346, -0.972318339100346, -0.972318339100346, -0.972318339100346, -0.972318339100346, -0.972318339100346, -0.972318339100346, -0.972318339100346, -0.9700115340253749, -0.972318339100346, -0.9746251441753172, -0.9746251441753172, -0.972318339100346, -0.9746251441753172, -0.9746251441753172, -0.972318339100346, -0.972318339100346, -0.9700115340253749, -0.972318339100346, -0.972318339100346, -0.9700115340253749, -0.972318339100346, -0.972318339100346, -0.972318339100346, -0.972318339100346, -0.972318339100346, -0.972318339100346, -0.972318339100346, -0.972318339100346, -0.972318339100346, -0.972318339100346, -0.9700115340253749, -0.972318339100346, -0.972318339100346, -0.972318339100346, -0.972318339100346, -0.972318339100346, -0.972318339100346, -0.972318339100346, -0.972318339100346, -0.972318339100346, -0.9700115340253749, -0.9700115340253749, -0.972318339100346, -0.9700115340253749, -0.972318339100346, -0.9700115340253749, -0.972318339100346, -0.9700115340253749, -0.972318339100346]
    v28 = [0.07216494845360821, 0.09278350515463929, 0.09278350515463929, 0.11340206185567037, 0.11340206185567037, 0.11340206185567037, 0.13402061855670122, 0.13402061855670122, 0.17525773195876293, 0.17525773195876293, 0.13402061855670122, 0.11340206185567037, 0.09278350515463929, 0.09278350515463929, 0.11340206185567037, 0.15463917525773208, 0.15463917525773208, 0.15463917525773208, 0.13402061855670122, 0.13402061855670122, 0.09278350515463929, 0.07216494845360821, 0.07216494845360821, 0.07216494845360821, 0.030927835051546504, 0.05154639175257736, 0.05154639175257736, 0.07216494845360821, 0.09278350515463929, 0.11340206185567037, 0.11340206185567037, 0.15463917525773208, 0.13402061855670122, 0.15463917525773208, 0.11340206185567037, 0.11340206185567037, 0.09278350515463929, 0.09278350515463929, 0.09278350515463929, 0.09278350515463929, 0.09278350515463929, 0.11340206185567037, 0.13402061855670122, 0.15463917525773208, 0.13402061855670122, 0.15463917525773208, 0.13402061855670122, 0.09278350515463929, 0.07216494845360821, 0.07216494845360821]
    v29 = [-1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0]
    v30 = [-0.709148937202355, -0.7091694826750812, -0.709190562706587, -0.7092121836944058, -0.7092343520360713, -0.7092570741291172, -0.709280356371077, -0.7093042051594844, -0.709328626891873, -0.7093536279657764, -0.7093792147787282, -0.7094053937282621, -0.7094321658222316, -0.7094595105097704, -0.7094874018503321, -0.7095158139033705, -0.709544720728339, -0.7095740963846913, -0.7096039149318809, -0.7096341504293617, -0.7096647769365872, -0.709695768513011, -0.7097270992180867, -0.709758743111268, -0.7097906742520086, -0.7098228666997619, -0.7098552945139817, -0.7098879317541216, -0.7099207524796352, -0.7099537307499761, -0.709986840624598, -0.7100200561629545, -0.7100533514244992, -0.7100867004686859, -0.7101200773549678, -0.7101534561427991, -0.7101868108916329, -0.7102201156609234, -0.7102533445101236, -0.7102864714986874, -0.7103194706860687, -0.7103523161317207, -0.7103849818950971, -0.7104174420356519, -0.7104496706128383, -0.7104816416861102, -0.7105133293149208, -0.7105447075587243, -0.7105757504769741, -0.7106064321291239]
    v31 = [-0.1704228978399095, -0.1704279732901598, -0.17042826269762978, -0.17042364565177148, -0.1704140017420377, -0.17039921055788065, -0.17037915168875295, -0.17035370472410694, -0.17032274925339508, -0.17028616486606984, -0.1702438311515837, -0.170195627699389, -0.17014149165381154, -0.17008159037867054, -0.17001614879265892, -0.16994539181446944, -0.16986954436279433, -0.16978883135632683, -0.16970347771375938, -0.16961370835378442, -0.16951974819509508, -0.1694218221563839, -0.16932015515634358, -0.16921497211366643, -0.1691064979470458, -0.1689949575751738, -0.16888057591674366, -0.1687635778904477, -0.16864418841497875, -0.1685226324090292, -0.1683991347912922, -0.1682739204804602, -0.16814721439522584, -0.16801924145428204, -0.16789022657632124, -0.16776039468003645, -0.16762997068411978, -0.16749917950726456, -0.16736824606816303, -0.16723739528550818, -0.1671068520779927, -0.16697684136430901, -0.16684758806314992, -0.1667193170932083, -0.1665922533731764, -0.16646662182174743, -0.16634264735761384, -0.1662205548994684, -0.1661005693660036, -0.1659829156759124]
    v32 = [0.7660115484299159, 0.7660626819811172, 0.7661053305345307, 0.7661392665460409, 0.7661642624715304, 0.7661800907668828, 0.7661865238879826, 0.7661833342907114, 0.7661702944309541, 0.7661471767645938, 0.7661137537475136, 0.766069797835597, 0.7660151855946227, 0.7659502100299453, 0.7658752682568144, 0.7657907573904805, 0.7656970745461933, 0.7655946168392023, 0.7654837813847575, 0.7653649652981087, 0.7652385656945058, 0.7651049796891993, 0.7649646043974381, 0.764817836934472, 0.764665074415551, 0.7645067139559254, 0.7643431526708448, 0.7641747876755585, 0.7640020160853167, 0.7638252350153703, 0.7636448415809671, 0.7634612328973589, 0.7632748060797938, 0.7630859582435228, 0.7628950865037953, 0.7627025879758609, 0.7625088597749703, 0.7623142990163725, 0.7621193028153177, 0.7619242682870555, 0.7617295925468359, 0.761535672709909, 0.7613429058915235, 0.7611516892069308, 0.7609624197713802, 0.7607754947001208, 0.7605913111084033, 0.7604102661114769, 0.7602327568245926, 0.7600591803629981]
    sample_ts = [pressure, level, temperature_bottom_flask, temperature_middle_mantle_heating,v4,v5,v6,v7,v8,v9,v10,v11,v12,v13,v14,v15,v16,v17,v18,v19,v20,v21,v22,v23,v24,v25,v26,v27,v28,v29,v30,v31,v32]

    print(f"; Reactor level non-negativity constraint for MINMAX normalization:", file=txt_file)
    # Declare Variables
    for i in range(0,33):
        for j in range(0, 50):
            print(f"(declare-const X_{i}_{j} Real)", file=txt_file)

    print(f"(declare-const Y_1 Real)", file=txt_file)
    print(f"(declare-const Y_0 Real\n)", file=txt_file)

    # Declare input constraints
    print(f"; Input constraints:", file=txt_file)
    for i in range(0,33):
        for j in range(0, 50):
            if i == 1:
                print(f"(assert (>= X_{i}_{j} {sample_ts[i][j] - perturbation_eps}))", file=txt_file)
                print(f"(assert (<= X_{i}_{j} {sample_ts[i][j] - perturbation_eps}))\n", file=txt_file)
            else:
                print(f"(assert (>= X_{i}_{j} {sample_ts[i][j]}))", file=txt_file)
                print(f"(assert (<= X_{i}_{j} {sample_ts[i][j]}))\n", file=txt_file)

    # Declare reactor level non-negativity constraint. Zero is mapped to -1 during the normalization
    print(f"; Reactor level non-negativity constraint (reactor level zero mapped to -1 during input normalization):", file=txt_file)
    print(f"(assert (or", file=txt_file)
    for j in range(0, 50):
        print(f"    (and (<= X_1_{j} {-1 - eps}))", file=txt_file)
    print(f"))", file=txt_file)
    print(f"(assert (> Y_0 Y_1))", file=txt_file)
    print(f"VNNLIB file completed!")

    