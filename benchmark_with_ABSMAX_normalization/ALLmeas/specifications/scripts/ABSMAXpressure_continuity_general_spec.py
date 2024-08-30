import sys

with open(sys.argv[1], "w") as txt_file:
    # eps for continuity constraint
    eps = 0.01
    pressure = [0.706964892412231, 0.7072480181200453, 0.707955832389581, 0.7082389580973952, 0.7083805209513023, 0.7076727066817667, 0.7075311438278596, 0.7075311438278596, 0.7080973952434881, 0.7080973952434881, 0.7073895809739524, 0.7073895809739524, 0.7076727066817667, 0.7072480181200453, 0.7071064552661381, 0.7078142695356738, 0.7080973952434881, 0.7085220838052095, 0.7082389580973952, 0.7080973952434881, 0.707955832389581, 0.7080973952434881, 0.7078142695356738, 0.7076727066817667, 0.707955832389581, 0.707955832389581, 0.7075311438278596, 0.7075311438278596, 0.7076727066817667, 0.7078142695356738, 0.7080973952434881, 0.7085220838052095, 0.7078142695356738, 0.7075311438278596, 0.7076727066817667, 0.7076727066817667, 0.7078142695356738, 0.7078142695356738, 0.7080973952434881, 0.707955832389581, 0.7075311438278596, 0.7076727066817667, 0.7080973952434881, 0.7080973952434881, 0.7078142695356738, 0.707955832389581, 0.7075311438278596, 0.7075311438278596, 0.7082389580973952, 0.7080973952434881]
    level = [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0]
    temperature_bottom_flask = [0.6959122632103689, 0.6959122632103689, 0.6959122632103689, 0.6959122632103689, 0.6959122632103689, 0.6959122632103689, 0.6959122632103689, 0.6959122632103689, 0.6959122632103689, 0.6959122632103689, 0.6959122632103689, 0.6959122632103689, 0.6959122632103689, 0.6959122632103689, 0.6959122632103689, 0.6959122632103689, 0.6959122632103689, 0.6959122632103689, 0.6959122632103689, 0.6959122632103689, 0.6959122632103689, 0.6959122632103689, 0.6959122632103689, 0.6959122632103689, 0.6959122632103689, 0.6959122632103689, 0.6959122632103689, 0.6959122632103689, 0.6959122632103689, 0.6959122632103689, 0.6959122632103689, 0.6959122632103689, 0.6959122632103689, 0.6959122632103689, 0.6959122632103689, 0.6959122632103689, 0.6959122632103689, 0.6959122632103689, 0.6959122632103689, 0.6959122632103689, 0.6959122632103689, 0.6959122632103689, 0.6959122632103689, 0.6959122632103689, 0.6959122632103689, 0.6959122632103689, 0.6959122632103689, 0.6959122632103689, 0.6959122632103689, 0.6959122632103689]
    temperature_middle_mantle_heating = [0.8552223371251293, 0.8552223371251293, 0.8552223371251293, 0.8541882109617372, 0.8541882109617372, 0.8541882109617372, 0.8541882109617372, 0.8531540847983454, 0.8531540847983454, 0.8531540847983454, 0.8521199586349535, 0.8510858324715614, 0.8521199586349535, 0.8510858324715614, 0.8510858324715614, 0.8510858324715614, 0.8510858324715614, 0.8500517063081696, 0.8500517063081696, 0.8500517063081696, 0.8490175801447776, 0.8490175801447776, 0.8490175801447776, 0.8490175801447776, 0.8479834539813857, 0.8479834539813857, 0.8479834539813857, 0.8479834539813857, 0.8479834539813857, 0.8469493278179938, 0.8469493278179938, 0.8469493278179938, 0.8459152016546018, 0.8459152016546018, 0.8459152016546018, 0.8459152016546018, 0.8459152016546018, 0.8448810754912099, 0.8448810754912099, 0.8448810754912099, 0.8438469493278179, 0.8438469493278179, 0.8438469493278179, 0.8438469493278179, 0.8428128231644261, 0.8428128231644261, 0.8428128231644261, 0.8417786970010341, 0.8417786970010341, 0.8417786970010341]
    v4 = [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0]
    v5 = [0.0, 0.0, 0.0, 1.0, 1.0, 1.0, 0.0, 0.0, 1.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 0.0, 1.0, 1.0, 0.0, 0.0, 0.0, 0.0, 1.0, 1.0, 1.0, 0.0, 0.0, 0.0, 1.0, 0.0, 1.0, 1.0, 0.0, 0.0, 1.0, 1.0, 1.0, 1.0, 0.0, 0.0, 1.0, 1.0]
    v6 = [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0]
    v7 = [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0]
    v8 = [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0]
    v9 = [0.7058823529411765, 0.7058823529411765, 0.7058823529411765, 0.7058823529411765, 0.7058823529411765, 0.7058823529411765, 0.7058823529411765, 0.7058823529411765, 0.7058823529411765, 0.7058823529411765, 0.7058823529411765, 0.7058823529411765, 0.7058823529411765, 0.7058823529411765, 0.7058823529411765, 0.7058823529411765, 0.7058823529411765, 0.7058823529411765, 0.7058823529411765, 0.7058823529411765, 0.7058823529411765, 0.7058823529411765, 0.7058823529411765, 0.7058823529411765, 0.7058823529411765, 0.7058823529411765, 0.7058823529411765, 0.7058823529411765, 0.7058823529411765, 0.7058823529411765, 0.7058823529411765, 0.7058823529411765, 0.7058823529411765, 0.7058823529411765, 0.7058823529411765, 0.7058823529411765, 0.7058823529411765, 0.7058823529411765, 0.7058823529411765, 0.7058823529411765, 0.7058823529411765, 0.7058823529411765, 0.7058823529411765, 0.7058823529411765, 0.7058823529411765, 0.7058823529411765, 0.7058823529411765, 0.7058823529411765, 0.7058823529411765, 0.7058823529411765]
    v10 = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
    v11 = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
    v12 = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
    v13 = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
    v14 = [0.21, 0.20800000000000002, 0.221, 0.243, 0.251, 0.24, 0.225, 0.22699999999999998, 0.23399999999999999, 0.248, 0.217, 0.21100000000000002, 0.222, 0.198, 0.187, 0.207, 0.222, 0.24600000000000002, 0.245, 0.245, 0.24, 0.249, 0.244, 0.23399999999999999, 0.244, 0.24600000000000002, 0.235, 0.226, 0.228, 0.23, 0.244, 0.267, 0.249, 0.23, 0.23600000000000002, 0.23600000000000002, 0.242, 0.24100000000000002, 0.249, 0.25, 0.235, 0.23, 0.249, 0.257, 0.249, 0.251, 0.237, 0.23199999999999998, 0.253, 0.259]
    v15 = [0.0, 0.0, 0.0, 0.0, 0.008, 0.023, 0.061, 0.099, 0.22399999999999998, 0.185, 0.075, 0.016, 0.0, 0.0, 0.032, 0.142, 0.128, 0.113, 0.10400000000000001, 0.068, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.04, 0.114, 0.084, 0.11699999999999999, 0.019, 0.019, 0.0, 0.0, 0.0, 0.0, 0.0, 0.018000000000000002, 0.061, 0.113, 0.098, 0.141, 0.1, 0.0, 0.0, 0.0]
    v16 = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.265, 0.0, 0.105, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.853, 1.0, 0.0, 0.0, 0.0, 0.0]
    v17 = [0.9249945805332754, 0.9247778018642966, 0.9249945805332754, 0.9252113592022545, 0.9252113592022545, 0.9249945805332754, 0.9252113592022545, 0.9254281378712333, 0.9254281378712333, 0.9254281378712333, 0.9254281378712333, 0.9256449165402124, 0.9256449165402124, 0.9256449165402124, 0.9256449165402124, 0.9256449165402124, 0.9258616952091915, 0.9258616952091915, 0.9258616952091915, 0.9260784738781703, 0.9260784738781703, 0.9258616952091915, 0.9258616952091915, 0.9262952525471494, 0.9262952525471494, 0.9262952525471494, 0.9265120312161282, 0.9262952525471494, 0.9265120312161282, 0.9265120312161282, 0.9262952525471494, 0.9265120312161282, 0.9267288098851073, 0.9267288098851073, 0.9267288098851073, 0.9267288098851073, 0.9267288098851073, 0.9269455885540863, 0.9269455885540863, 0.9271623672230652, 0.9271623672230652, 0.9269455885540863, 0.9271623672230652, 0.9273791458920442, 0.9271623672230652, 0.9271623672230652, 0.9273791458920442, 0.9273791458920442, 0.9273791458920442, 0.9275959245610231]
    v18 = [0.814364640883978, 0.814364640883978, 0.814364640883978, 0.814364640883978, 0.8132596685082872, 0.8132596685082872, 0.8132596685082872, 0.8132596685082872, 0.8121546961325967, 0.8132596685082872, 0.8121546961325967, 0.8121546961325967, 0.8121546961325967, 0.8121546961325967, 0.8110497237569061, 0.8121546961325967, 0.8121546961325967, 0.8110497237569061, 0.8110497237569061, 0.8110497237569061, 0.8099447513812155, 0.8099447513812155, 0.8099447513812155, 0.8099447513812155, 0.8088397790055248, 0.8099447513812155, 0.8099447513812155, 0.8088397790055248, 0.8088397790055248, 0.8088397790055248, 0.8077348066298342, 0.8088397790055248, 0.8077348066298342, 0.8077348066298342, 0.8077348066298342, 0.8077348066298342, 0.8077348066298342, 0.8066298342541437, 0.8066298342541437, 0.8066298342541437, 0.8066298342541437, 0.8055248618784531, 0.8055248618784531, 0.8055248618784531, 0.8055248618784531, 0.8055248618784531, 0.8055248618784531, 0.8044198895027624, 0.8044198895027624, 0.8044198895027624]
    v19 = [0.8053553038105047, 0.8043254376930998, 0.8043254376930998, 0.8043254376930998, 0.8032955715756952, 0.8032955715756952, 0.8032955715756952, 0.8032955715756952, 0.8022657054582906, 0.8022657054582906, 0.8022657054582906, 0.8012358393408857, 0.8012358393408857, 0.8012358393408857, 0.800205973223481, 0.800205973223481, 0.800205973223481, 0.800205973223481, 0.7991761071060762, 0.7991761071060762, 0.7991761071060762, 0.7981462409886715, 0.7991761071060762, 0.7981462409886715, 0.7971163748712669, 0.7971163748712669, 0.7971163748712669, 0.7971163748712669, 0.7971163748712669, 0.796086508753862, 0.796086508753862, 0.796086508753862, 0.7950566426364574, 0.7950566426364574, 0.7940267765190525, 0.7940267765190525, 0.7940267765190525, 0.7940267765190525, 0.7940267765190525, 0.7929969104016479, 0.7929969104016479, 0.7929969104016479, 0.7929969104016479, 0.7919670442842431, 0.7919670442842431, 0.7919670442842431, 0.7919670442842431, 0.7909371781668383, 0.7909371781668383, 0.7899073120494337]
    v20 = [0.8728382502543235, 0.8728382502543235, 0.8718209562563581, 0.8718209562563581, 0.8708036622583927, 0.8718209562563581, 0.8718209562563581, 0.8708036622583927, 0.8708036622583927, 0.8708036622583927, 0.8697863682604273, 0.8697863682604273, 0.8697863682604273, 0.868769074262462, 0.8697863682604273, 0.868769074262462, 0.8677517802644964, 0.868769074262462, 0.868769074262462, 0.8677517802644964, 0.8677517802644964, 0.8677517802644964, 0.8677517802644964, 0.866734486266531, 0.866734486266531, 0.866734486266531, 0.866734486266531, 0.866734486266531, 0.8657171922685656, 0.8646998982706002, 0.8657171922685656, 0.8646998982706002, 0.8646998982706002, 0.8646998982706002, 0.8636826042726349, 0.8636826042726349, 0.8636826042726349, 0.8636826042726349, 0.8636826042726349, 0.8636826042726349, 0.8626653102746694, 0.8626653102746694, 0.8626653102746694, 0.8616480162767041, 0.8616480162767041, 0.8616480162767041, 0.8616480162767041, 0.8606307222787385, 0.8606307222787385, 0.8606307222787385]
    v21 = [0.6925403225806451, 0.6925403225806451, 0.6925403225806451, 0.6925403225806451, 0.6925403225806451, 0.6925403225806451, 0.6925403225806451, 0.6925403225806451, 0.6925403225806451, 0.6925403225806451, 0.6925403225806451, 0.6925403225806451, 0.6925403225806451, 0.6925403225806451, 0.6925403225806451, 0.6925403225806451, 0.6925403225806451, 0.6925403225806451, 0.6925403225806451, 0.6925403225806451, 0.6925403225806451, 0.6925403225806451, 0.6925403225806451, 0.6925403225806451, 0.6925403225806451, 0.6925403225806451, 0.6925403225806451, 0.6925403225806451, 0.6925403225806451, 0.6925403225806451, 0.6925403225806451, 0.6925403225806451, 0.6925403225806451, 0.6925403225806451, 0.6925403225806451, 0.6925403225806451, 0.6925403225806451, 0.6925403225806451, 0.6925403225806451, 0.6925403225806451, 0.6925403225806451, 0.6925403225806451, 0.6925403225806451, 0.6935483870967741, 0.6935483870967741, 0.6925403225806451, 0.6925403225806451, 0.6925403225806451, 0.6935483870967741, 0.6925403225806451]
    v22 = [0.6663286004056795, 0.6663286004056795, 0.6663286004056795, 0.6663286004056795, 0.6663286004056795, 0.667342799188641, 0.667342799188641, 0.667342799188641, 0.667342799188641, 0.667342799188641, 0.667342799188641, 0.667342799188641, 0.667342799188641, 0.667342799188641, 0.667342799188641, 0.667342799188641, 0.667342799188641, 0.667342799188641, 0.6683569979716025, 0.6683569979716025, 0.6683569979716025, 0.6683569979716025, 0.6683569979716025, 0.6683569979716025, 0.6683569979716025, 0.6683569979716025, 0.6683569979716025, 0.6693711967545639, 0.6683569979716025, 0.6693711967545639, 0.6693711967545639, 0.6693711967545639, 0.6693711967545639, 0.6693711967545639, 0.6693711967545639, 0.6693711967545639, 0.6693711967545639, 0.6693711967545639, 0.6693711967545639, 0.6693711967545639, 0.6693711967545639, 0.6693711967545639, 0.6703853955375253, 0.6693711967545639, 0.6703853955375253, 0.6703853955375253, 0.6703853955375253, 0.6703853955375253, 0.6703853955375253, 0.6703853955375253]
    v23 = [0.6524822695035462, 0.6524822695035462, 0.6524822695035462, 0.6524822695035462, 0.6524822695035462, 0.6524822695035462, 0.6524822695035462, 0.6524822695035462, 0.6524822695035462, 0.6534954407294833, 0.6534954407294833, 0.6534954407294833, 0.6534954407294833, 0.6534954407294833, 0.6534954407294833, 0.6534954407294833, 0.6534954407294833, 0.6534954407294833, 0.6534954407294833, 0.6534954407294833, 0.6534954407294833, 0.6534954407294833, 0.6534954407294833, 0.6534954407294833, 0.6534954407294833, 0.6534954407294833, 0.6534954407294833, 0.6534954407294833, 0.6534954407294833, 0.6534954407294833, 0.6534954407294833, 0.6534954407294833, 0.6534954407294833, 0.6534954407294833, 0.6534954407294833, 0.6534954407294833, 0.6534954407294833, 0.6534954407294833, 0.6534954407294833, 0.6534954407294833, 0.6534954407294833, 0.6534954407294833, 0.6534954407294833, 0.6545086119554204, 0.6534954407294833, 0.6545086119554204, 0.6545086119554204, 0.6545086119554204, 0.6545086119554204, 0.6545086119554204]
    v24 = [0.6608066184074457, 0.6608066184074457, 0.6608066184074457, 0.6608066184074457, 0.6608066184074457, 0.6608066184074457, 0.6608066184074457, 0.6618407445708376, 0.6608066184074457, 0.6618407445708376, 0.6608066184074457, 0.6608066184074457, 0.6618407445708376, 0.6608066184074457, 0.6608066184074457, 0.6608066184074457, 0.6618407445708376, 0.6608066184074457, 0.6608066184074457, 0.6608066184074457, 0.6618407445708376, 0.6618407445708376, 0.6618407445708376, 0.6618407445708376, 0.6618407445708376, 0.6618407445708376, 0.6618407445708376, 0.6618407445708376, 0.6618407445708376, 0.6618407445708376, 0.6618407445708376, 0.6618407445708376, 0.6618407445708376, 0.6618407445708376, 0.6618407445708376, 0.6618407445708376, 0.6618407445708376, 0.6618407445708376, 0.6618407445708376, 0.6618407445708376, 0.6618407445708376, 0.6618407445708376, 0.6618407445708376, 0.6618407445708376, 0.6618407445708376, 0.6618407445708376, 0.6618407445708376, 0.6618407445708376, 0.6618407445708376, 0.6618407445708376]
    v25 = [0.03174603174603175, 0.03174603174603175, 0.03174603174603175, 0.03174603174603175, 0.03174603174603175, 0.03174603174603175, 0.03174603174603175, 0.03174603174603175, 0.03174603174603175, 0.03174603174603175, 0.03174603174603175, 0.047619047619047616, 0.047619047619047616, 0.03174603174603175, 0.015873015873015876, 0.015873015873015876, 0.0, 0.0, 0.03174603174603175, 0.30158730158730157, 0.047619047619047616, 0.0, 0.047619047619047616, 0.30158730158730157, 0.047619047619047616, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.1111111111111111, 0.30158730158730157, 0.30158730158730157, 0.03174603174603175, 0.0, 0.03174603174603175, 0.015873015873015876, 0.015873015873015876, 0.0, 0.0, 0.0, 0.0, 0.0, 0.14285714285714288, 0.253968253968254, 0.015873015873015876, 0.0]
    v26 = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.015873015873015876, 0.253968253968254, 0.015873015873015876, 0.20634920634920637, 0.20634920634920637, 0.09523809523809523, 0.015873015873015876, 0.0, 0.0, 0.03174603174603175, 0.126984126984127, 0.126984126984127, 0.126984126984127, 0.126984126984127, 0.047619047619047616, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.047619047619047616, 0.253968253968254, 0.047619047619047616, 0.047619047619047616, 0.09523809523809523, 0.03174603174603175, 0.015873015873015876, 0.0, 0.0, 0.0, 0.0, 0.015873015873015876, 0.0634920634920635, 0.09523809523809523, 0.126984126984127, 0.126984126984127, 0.047619047619047616, 0.0]
    v27 = [0.006968641114982578, 0.006968641114982578, 0.006968641114982578, 0.006968641114982578, 0.006968641114982578, 0.006968641114982578, 0.006968641114982578, 0.006968641114982578, 0.008130081300813009, 0.006968641114982578, 0.005807200929152149, 0.005807200929152149, 0.006968641114982578, 0.005807200929152149, 0.005807200929152149, 0.006968641114982578, 0.006968641114982578, 0.008130081300813009, 0.006968641114982578, 0.006968641114982578, 0.008130081300813009, 0.006968641114982578, 0.006968641114982578, 0.006968641114982578, 0.006968641114982578, 0.006968641114982578, 0.006968641114982578, 0.006968641114982578, 0.006968641114982578, 0.006968641114982578, 0.006968641114982578, 0.008130081300813009, 0.006968641114982578, 0.006968641114982578, 0.006968641114982578, 0.006968641114982578, 0.006968641114982578, 0.006968641114982578, 0.006968641114982578, 0.006968641114982578, 0.006968641114982578, 0.008130081300813009, 0.008130081300813009, 0.006968641114982578, 0.008130081300813009, 0.006968641114982578, 0.008130081300813009, 0.006968641114982578, 0.008130081300813009, 0.006968641114982578]
    v28 = [0.3835616438356164, 0.3972602739726027, 0.3972602739726027, 0.4109589041095891, 0.4109589041095891, 0.4109589041095891, 0.4246575342465754, 0.4246575342465754, 0.4520547945205479, 0.4520547945205479, 0.4246575342465754, 0.4109589041095891, 0.3972602739726027, 0.3972602739726027, 0.4109589041095891, 0.4383561643835617, 0.4383561643835617, 0.4383561643835617, 0.4246575342465754, 0.4246575342465754, 0.3972602739726027, 0.3835616438356164, 0.3835616438356164, 0.3835616438356164, 0.35616438356164387, 0.36986301369863017, 0.36986301369863017, 0.3835616438356164, 0.3972602739726027, 0.4109589041095891, 0.4109589041095891, 0.4383561643835617, 0.4246575342465754, 0.4383561643835617, 0.4109589041095891, 0.4109589041095891, 0.3972602739726027, 0.3972602739726027, 0.3972602739726027, 0.3972602739726027, 0.3972602739726027, 0.4109589041095891, 0.4246575342465754, 0.4383561643835617, 0.4246575342465754, 0.4383561643835617, 0.4246575342465754, 0.3972602739726027, 0.3835616438356164, 0.3835616438356164]
    v29 = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
    v30 = [0.14542553139882256, 0.1454152586624594, 0.1454047186467065, 0.14539390815279712, 0.1453828239819643, 0.1453714629354414, 0.1453598218144615, 0.14534789742025778, 0.1453356865540635, 0.14532318601711178, 0.14531039261063589, 0.14529730313586894, 0.14528391708888422, 0.1452702447451148, 0.14525629907483392, 0.14524209304831476, 0.14522763963583055, 0.14521295180765437, 0.14519804253405952, 0.14518292478531916, 0.14516761153170638, 0.14515211574349451, 0.14513645039095663, 0.145120628444366, 0.1451046628739957, 0.14508856665011907, 0.14507235274300917, 0.14505603412293921, 0.1450396237601824, 0.14502313462501196, 0.14500657968770098, 0.14498997191852275, 0.1449733242877504, 0.14495664976565706, 0.14493996132251608, 0.1449232719286004, 0.1449065945541835, 0.14488994216953832, 0.14487332774493822, 0.14485676425065627, 0.14484026465696567, 0.14482384193413966, 0.1448075090524514, 0.14479127898217406, 0.14477516469358087, 0.14475917915694494, 0.14474333534253955, 0.1447276462206378, 0.14471212476151296, 0.14469678393543808]
    v31 = [0.3345296424096426, 0.33452675664783876, 0.3345265920986891, 0.33452921722432877, 0.3345347004868922, 0.3345431103485143, 0.33455451527132973, 0.33456898371747323, 0.33458658414907966, 0.33460738502828363, 0.33463145481721995, 0.33465886197802336, 0.33468964224870623, 0.33472370047079136, 0.3347609087616791, 0.33480113923876964, 0.3348442640194636, 0.33489015522116106, 0.33493868496126256, 0.33498972535716853, 0.33504314852627914, 0.3350988265859949, 0.335156631653716, 0.3352164358468431, 0.3352781112827761, 0.3353415300789159, 0.3354065643526624, 0.3354730862214162, 0.3355409678025776, 0.335610081213547, 0.33568029857172477, 0.3357514919945112, 0.33582353359930667, 0.33589629550351147, 0.3359696498245261, 0.3360434686797508, 0.33611762418658614, 0.3361919884624322, 0.33626643362468955, 0.33634083179075847, 0.3364150550780392, 0.3364889756039323, 0.33656246548583807, 0.3366353968411568, 0.336707641787289, 0.33677907244163485, 0.3368495609215948, 0.33691897934456916, 0.33698719982795844, 0.3370540944891628]
    v32 = [0.8823832486594039, 0.8824089514756601, 0.882430389218712, 0.8824474475111214, 0.882460011975449, 0.8824679682342563, 0.882471201910105, 0.8824695986255557, 0.8824630440031703, 0.8824514236655099, 0.8824346232351357, 0.8824125283346089, 0.8823850769184227, 0.8823524162687941, 0.8823147459998718, 0.882272265725805, 0.8822251750607424, 0.8821736736188326, 0.8821179610142246, 0.8820582368610672, 0.8819947007735092, 0.8819275523656999, 0.8818569912517873, 0.8817832170459206, 0.8817064293622484, 0.88162682781492, 0.881544612018084, 0.8814599815858888, 0.8813731361324836, 0.8812842752720177, 0.8811935986186389, 0.8811013057864968, 0.8810075963897397, 0.8809126700425167, 0.8808167263589767, 0.880719964953268, 0.8806225854395403, 0.8805247874319416, 0.8804267705446213, 0.8803287343917278, 0.88023087858741, 0.880133402745817, 0.880036506481097, 0.8799403894073995, 0.8798452511388732, 0.8797512912896664, 0.8796587094739285, 0.8795677053058081, 0.8794784783994541, 0.879391228369015]
    sample_ts = [pressure, level, temperature_bottom_flask, temperature_middle_mantle_heating,v4,v5,v6,v7,v8,v9,v10,v11,v12,v13,v14,v15,v16,v17,v18,v19,v20,v21,v22,v23,v24,v25,v26,v27,v28,v29,v30,v31,v32]

    print(f"; Pressure Continuity constraint for MINMAX normalization:", file=txt_file)
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

    