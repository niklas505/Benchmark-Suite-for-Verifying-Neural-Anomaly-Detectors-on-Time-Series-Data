import sys

with open(sys.argv[1], "w") as txt_file:
    perturbation_eps = float(sys.argv[2])
    # eps for space continuity constraint
    eps = 35
    pressure = [0.5456540825285338, 0.5460930640913082, 0.5471905179982441, 0.5476294995610185, 0.5478489903424056, 0.5467515364354697, 0.5465320456540825, 0.5465320456540825, 0.5474100087796312, 0.5474100087796312, 0.5463125548726954, 0.5463125548726954, 0.5467515364354697, 0.5460930640913082, 0.545873573309921, 0.5469710272168569, 0.5474100087796312, 0.5480684811237928, 0.5476294995610185, 0.5474100087796312, 0.5471905179982441, 0.5474100087796312, 0.5469710272168569, 0.5467515364354697, 0.5471905179982441, 0.5471905179982441, 0.5465320456540825, 0.5465320456540825, 0.5467515364354697, 0.5469710272168569, 0.5474100087796312, 0.5480684811237928, 0.5469710272168569, 0.5465320456540825, 0.5467515364354697, 0.5467515364354697, 0.5469710272168569, 0.5469710272168569, 0.5474100087796312, 0.5471905179982441, 0.5465320456540825, 0.5467515364354697, 0.5474100087796312, 0.5474100087796312, 0.5469710272168569, 0.5471905179982441, 0.5465320456540825, 0.5465320456540825, 0.5476294995610185, 0.5474100087796312]
    level = [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0]
    temperature_bottom_flask = [0.3068181818181818, 0.3068181818181818, 0.3068181818181818, 0.3068181818181818, 0.3068181818181818, 0.3068181818181818, 0.3068181818181818, 0.3068181818181818, 0.3068181818181818, 0.3068181818181818, 0.3068181818181818, 0.3068181818181818, 0.3068181818181818, 0.3068181818181818, 0.3068181818181818, 0.3068181818181818, 0.3068181818181818, 0.3068181818181818, 0.3068181818181818, 0.3068181818181818, 0.3068181818181818, 0.3068181818181818, 0.3068181818181818, 0.3068181818181818, 0.3068181818181818, 0.3068181818181818, 0.3068181818181818, 0.3068181818181818, 0.3068181818181818, 0.3068181818181818, 0.3068181818181818, 0.3068181818181818, 0.3068181818181818, 0.3068181818181818, 0.3068181818181818, 0.3068181818181818, 0.3068181818181818, 0.3068181818181818, 0.3068181818181818, 0.3068181818181818, 0.3068181818181818, 0.3068181818181818, 0.3068181818181818, 0.3068181818181818, 0.3068181818181818, 0.3068181818181818, 0.3068181818181818, 0.3068181818181818, 0.3068181818181818, 0.3068181818181818]
    temperature_middle_mantle_heating = [0.5692307692307692, 0.5692307692307692, 0.5692307692307692, 0.5661538461538459, 0.5661538461538459, 0.5661538461538459, 0.5661538461538459, 0.563076923076923, 0.563076923076923, 0.563076923076923, 0.56, 0.5569230769230767, 0.56, 0.5569230769230767, 0.5569230769230767, 0.5569230769230767, 0.5569230769230767, 0.5538461538461539, 0.5538461538461539, 0.5538461538461539, 0.5507692307692305, 0.5507692307692305, 0.5507692307692305, 0.5507692307692305, 0.5476923076923076, 0.5476923076923076, 0.5476923076923076, 0.5476923076923076, 0.5476923076923076, 0.5446153846153847, 0.5446153846153847, 0.5446153846153847, 0.5415384615384614, 0.5415384615384614, 0.5415384615384614, 0.5415384615384614, 0.5415384615384614, 0.5384615384615384, 0.5384615384615384, 0.5384615384615384, 0.5353846153846151, 0.5353846153846151, 0.5353846153846151, 0.5353846153846151, 0.5323076923076923, 0.5323076923076923, 0.5323076923076923, 0.5292307692307693, 0.5292307692307693, 0.5292307692307693]
    v4 = [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0]
    v5 = [0.0, 0.0, 0.0, 1.0, 1.0, 1.0, 0.0, 0.0, 1.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 0.0, 1.0, 1.0, 0.0, 0.0, 0.0, 0.0, 1.0, 1.0, 1.0, 0.0, 0.0, 0.0, 1.0, 0.0, 1.0, 1.0, 0.0, 0.0, 1.0, 1.0, 1.0, 1.0, 0.0, 0.0, 1.0, 1.0]
    v6 = [0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5]
    v7 = [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0]
    v8 = [0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5]
    v9 = [0.7058823529411765, 0.7058823529411765, 0.7058823529411765, 0.7058823529411765, 0.7058823529411765, 0.7058823529411765, 0.7058823529411765, 0.7058823529411765, 0.7058823529411765, 0.7058823529411765, 0.7058823529411765, 0.7058823529411765, 0.7058823529411765, 0.7058823529411765, 0.7058823529411765, 0.7058823529411765, 0.7058823529411765, 0.7058823529411765, 0.7058823529411765, 0.7058823529411765, 0.7058823529411765, 0.7058823529411765, 0.7058823529411765, 0.7058823529411765, 0.7058823529411765, 0.7058823529411765, 0.7058823529411765, 0.7058823529411765, 0.7058823529411765, 0.7058823529411765, 0.7058823529411765, 0.7058823529411765, 0.7058823529411765, 0.7058823529411765, 0.7058823529411765, 0.7058823529411765, 0.7058823529411765, 0.7058823529411765, 0.7058823529411765, 0.7058823529411765, 0.7058823529411765, 0.7058823529411765, 0.7058823529411765, 0.7058823529411765, 0.7058823529411765, 0.7058823529411765, 0.7058823529411765, 0.7058823529411765, 0.7058823529411765, 0.7058823529411765]
    v10 = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
    v11 = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
    v12 = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
    v13 = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
    v14 = [0.21, 0.20800000000000002, 0.221, 0.243, 0.251, 0.24, 0.225, 0.22699999999999998, 0.23399999999999999, 0.248, 0.217, 0.21100000000000002, 0.222, 0.198, 0.187, 0.207, 0.222, 0.24600000000000002, 0.245, 0.245, 0.24, 0.249, 0.244, 0.23399999999999999, 0.244, 0.24600000000000002, 0.235, 0.226, 0.228, 0.23, 0.244, 0.267, 0.249, 0.23, 0.23600000000000002, 0.23600000000000002, 0.242, 0.24100000000000002, 0.249, 0.25, 0.235, 0.23, 0.249, 0.257, 0.249, 0.251, 0.237, 0.23199999999999998, 0.253, 0.259]
    v15 = [0.0, 0.0, 0.0, 0.0, 0.008, 0.023, 0.061, 0.099, 0.22399999999999998, 0.185, 0.075, 0.016, 0.0, 0.0, 0.032, 0.142, 0.128, 0.113, 0.10400000000000001, 0.068, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.04, 0.114, 0.084, 0.11699999999999999, 0.019, 0.019, 0.0, 0.0, 0.0, 0.0, 0.0, 0.018000000000000002, 0.061, 0.113, 0.098, 0.141, 0.1, 0.0, 0.0, 0.0]
    v16 = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.265, 0.0, 0.105, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.853, 1.0, 0.0, 0.0, 0.0, 0.0]
    v17 = [0.8340527577937649, 0.8335731414868106, 0.8340527577937649, 0.8345323741007195, 0.8345323741007195, 0.8340527577937649, 0.8345323741007195, 0.8350119904076737, 0.8350119904076737, 0.8350119904076737, 0.8350119904076737, 0.8354916067146282, 0.8354916067146282, 0.8354916067146282, 0.8354916067146282, 0.8354916067146282, 0.8359712230215828, 0.8359712230215828, 0.8359712230215828, 0.836450839328537, 0.836450839328537, 0.8359712230215828, 0.8359712230215828, 0.8369304556354916, 0.8369304556354916, 0.8369304556354916, 0.8374100719424459, 0.8369304556354916, 0.8374100719424459, 0.8374100719424459, 0.8369304556354916, 0.8374100719424459, 0.8378896882494005, 0.8378896882494005, 0.8378896882494005, 0.8378896882494005, 0.8378896882494005, 0.8383693045563549, 0.8383693045563549, 0.8388489208633092, 0.8388489208633092, 0.8383693045563549, 0.8388489208633092, 0.8393285371702638, 0.8388489208633092, 0.8388489208633092, 0.8393285371702638, 0.8393285371702638, 0.8393285371702638, 0.839808153477218]
    v18 = [0.31983805668016213, 0.31983805668016213, 0.31983805668016213, 0.31983805668016213, 0.3157894736842104, 0.3157894736842104, 0.3157894736842104, 0.3157894736842104, 0.31174089068825916, 0.3157894736842104, 0.31174089068825916, 0.31174089068825916, 0.31174089068825916, 0.31174089068825916, 0.307692307692308, 0.31174089068825916, 0.31174089068825916, 0.307692307692308, 0.307692307692308, 0.307692307692308, 0.30364372469635625, 0.30364372469635625, 0.30364372469635625, 0.30364372469635625, 0.2995951417004051, 0.30364372469635625, 0.30364372469635625, 0.2995951417004051, 0.2995951417004051, 0.2995951417004051, 0.2955465587044533, 0.2995951417004051, 0.2955465587044533, 0.2955465587044533, 0.2955465587044533, 0.2955465587044533, 0.2955465587044533, 0.2914979757085021, 0.2914979757085021, 0.2914979757085021, 0.2914979757085021, 0.28744939271255093, 0.28744939271255093, 0.28744939271255093, 0.28744939271255093, 0.28744939271255093, 0.28744939271255093, 0.28340080971659914, 0.28340080971659914, 0.28340080971659914]
    v19 = [0.4220183486238533, 0.4189602446483178, 0.4189602446483178, 0.4189602446483178, 0.41590214067278286, 0.41590214067278286, 0.41590214067278286, 0.41590214067278286, 0.41284403669724784, 0.41284403669724784, 0.41284403669724784, 0.40978593272171243, 0.40978593272171243, 0.40978593272171243, 0.4067278287461774, 0.4067278287461774, 0.4067278287461774, 0.4067278287461774, 0.403669724770642, 0.403669724770642, 0.403669724770642, 0.400611620795107, 0.403669724770642, 0.400611620795107, 0.397553516819572, 0.397553516819572, 0.397553516819572, 0.397553516819572, 0.397553516819572, 0.39449541284403655, 0.39449541284403655, 0.39449541284403655, 0.3914373088685016, 0.3914373088685016, 0.3883792048929661, 0.3883792048929661, 0.3883792048929661, 0.3883792048929661, 0.3883792048929661, 0.38532110091743116, 0.38532110091743116, 0.38532110091743116, 0.38532110091743116, 0.38226299694189614, 0.38226299694189614, 0.38226299694189614, 0.38226299694189614, 0.37920489296636073, 0.37920489296636073, 0.3761467889908257]
    v20 = [0.617737003058104, 0.617737003058104, 0.614678899082569, 0.614678899082569, 0.6116207951070336, 0.614678899082569, 0.614678899082569, 0.6116207951070336, 0.6116207951070336, 0.6116207951070336, 0.6085626911314986, 0.6085626911314986, 0.6085626911314986, 0.6055045871559636, 0.6085626911314986, 0.6055045871559636, 0.6024464831804281, 0.6055045871559636, 0.6055045871559636, 0.6024464831804281, 0.6024464831804281, 0.6024464831804281, 0.6024464831804281, 0.5993883792048932, 0.5993883792048932, 0.5993883792048932, 0.5993883792048932, 0.5993883792048932, 0.5963302752293578, 0.5932721712538227, 0.5963302752293578, 0.5932721712538227, 0.5932721712538227, 0.5932721712538227, 0.5902140672782877, 0.5902140672782877, 0.5902140672782877, 0.5902140672782877, 0.5902140672782877, 0.5902140672782877, 0.5871559633027523, 0.5871559633027523, 0.5871559633027523, 0.5840978593272174, 0.5840978593272174, 0.5840978593272174, 0.5840978593272174, 0.581039755351682, 0.581039755351682, 0.581039755351682]
    v21 = [0.35789473684210527, 0.35789473684210527, 0.35789473684210527, 0.35789473684210527, 0.35789473684210527, 0.35789473684210527, 0.35789473684210527, 0.35789473684210527, 0.35789473684210527, 0.35789473684210527, 0.35789473684210527, 0.35789473684210527, 0.35789473684210527, 0.35789473684210527, 0.35789473684210527, 0.35789473684210527, 0.35789473684210527, 0.35789473684210527, 0.35789473684210527, 0.35789473684210527, 0.35789473684210527, 0.35789473684210527, 0.35789473684210527, 0.35789473684210527, 0.35789473684210527, 0.35789473684210527, 0.35789473684210527, 0.35789473684210527, 0.35789473684210527, 0.35789473684210527, 0.35789473684210527, 0.35789473684210527, 0.35789473684210527, 0.35789473684210527, 0.35789473684210527, 0.35789473684210527, 0.35789473684210527, 0.35789473684210527, 0.35789473684210527, 0.35789473684210527, 0.35789473684210527, 0.35789473684210527, 0.35789473684210527, 0.3599999999999999, 0.3599999999999999, 0.35789473684210527, 0.35789473684210527, 0.35789473684210527, 0.3599999999999999, 0.35789473684210527]
    v22 = [0.31458333333333344, 0.31458333333333344, 0.31458333333333344, 0.31458333333333344, 0.31458333333333344, 0.31666666666666665, 0.31666666666666665, 0.31666666666666665, 0.31666666666666665, 0.31666666666666665, 0.31666666666666665, 0.31666666666666665, 0.31666666666666665, 0.31666666666666665, 0.31666666666666665, 0.31666666666666665, 0.31666666666666665, 0.31666666666666665, 0.31875000000000014, 0.31875000000000014, 0.31875000000000014, 0.31875000000000014, 0.31875000000000014, 0.31875000000000014, 0.31875000000000014, 0.31875000000000014, 0.31875000000000014, 0.32083333333333336, 0.31875000000000014, 0.32083333333333336, 0.32083333333333336, 0.32083333333333336, 0.32083333333333336, 0.32083333333333336, 0.32083333333333336, 0.32083333333333336, 0.32083333333333336, 0.32083333333333336, 0.32083333333333336, 0.32083333333333336, 0.32083333333333336, 0.32083333333333336, 0.3229166666666666, 0.32083333333333336, 0.3229166666666666, 0.3229166666666666, 0.3229166666666666, 0.3229166666666666, 0.3229166666666666, 0.3229166666666666]
    v23 = [0.30142566191446035, 0.30142566191446035, 0.30142566191446035, 0.30142566191446035, 0.30142566191446035, 0.30142566191446035, 0.30142566191446035, 0.30142566191446035, 0.30142566191446035, 0.3034623217922607, 0.3034623217922607, 0.3034623217922607, 0.3034623217922607, 0.3034623217922607, 0.3034623217922607, 0.3034623217922607, 0.3034623217922607, 0.3034623217922607, 0.3034623217922607, 0.3034623217922607, 0.3034623217922607, 0.3034623217922607, 0.3034623217922607, 0.3034623217922607, 0.3034623217922607, 0.3034623217922607, 0.3034623217922607, 0.3034623217922607, 0.3034623217922607, 0.3034623217922607, 0.3034623217922607, 0.3034623217922607, 0.3034623217922607, 0.3034623217922607, 0.3034623217922607, 0.3034623217922607, 0.3034623217922607, 0.3034623217922607, 0.3034623217922607, 0.3034623217922607, 0.3034623217922607, 0.3034623217922607, 0.3034623217922607, 0.30549898167006095, 0.3034623217922607, 0.30549898167006095, 0.30549898167006095, 0.30549898167006095, 0.30549898167006095, 0.30549898167006095]
    v24 = [0.32786885245901637, 0.32786885245901637, 0.32786885245901637, 0.32786885245901637, 0.32786885245901637, 0.32786885245901637, 0.32786885245901637, 0.32991803278688525, 0.32786885245901637, 0.32991803278688525, 0.32786885245901637, 0.32786885245901637, 0.32991803278688525, 0.32786885245901637, 0.32786885245901637, 0.32786885245901637, 0.32991803278688525, 0.32786885245901637, 0.32786885245901637, 0.32786885245901637, 0.32991803278688525, 0.32991803278688525, 0.32991803278688525, 0.32991803278688525, 0.32991803278688525, 0.32991803278688525, 0.32991803278688525, 0.32991803278688525, 0.32991803278688525, 0.32991803278688525, 0.32991803278688525, 0.32991803278688525, 0.32991803278688525, 0.32991803278688525, 0.32991803278688525, 0.32991803278688525, 0.32991803278688525, 0.32991803278688525, 0.32991803278688525, 0.32991803278688525, 0.32991803278688525, 0.32991803278688525, 0.32991803278688525, 0.32991803278688525, 0.32991803278688525, 0.32991803278688525, 0.32991803278688525, 0.32991803278688525, 0.32991803278688525, 0.32991803278688525]
    v25 = [0.03174603174603175, 0.03174603174603175, 0.03174603174603175, 0.03174603174603175, 0.03174603174603175, 0.03174603174603175, 0.03174603174603175, 0.03174603174603175, 0.03174603174603175, 0.03174603174603175, 0.03174603174603175, 0.047619047619047616, 0.047619047619047616, 0.03174603174603175, 0.015873015873015876, 0.015873015873015876, 0.0, 0.0, 0.03174603174603175, 0.30158730158730157, 0.047619047619047616, 0.0, 0.047619047619047616, 0.30158730158730157, 0.047619047619047616, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.1111111111111111, 0.30158730158730157, 0.30158730158730157, 0.03174603174603175, 0.0, 0.03174603174603175, 0.015873015873015876, 0.015873015873015876, 0.0, 0.0, 0.0, 0.0, 0.0, 0.14285714285714288, 0.253968253968254, 0.015873015873015876, 0.0]
    v26 = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.015873015873015876, 0.253968253968254, 0.015873015873015876, 0.20634920634920637, 0.20634920634920637, 0.09523809523809523, 0.015873015873015876, 0.0, 0.0, 0.03174603174603175, 0.126984126984127, 0.126984126984127, 0.126984126984127, 0.126984126984127, 0.047619047619047616, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.047619047619047616, 0.253968253968254, 0.047619047619047616, 0.047619047619047616, 0.09523809523809523, 0.03174603174603175, 0.015873015873015876, 0.0, 0.0, 0.0, 0.0, 0.015873015873015876, 0.0634920634920635, 0.09523809523809523, 0.126984126984127, 0.126984126984127, 0.047619047619047616, 0.0]
    v27 = [0.013840830449826992, 0.013840830449826992, 0.013840830449826992, 0.013840830449826992, 0.013840830449826992, 0.013840830449826992, 0.013840830449826992, 0.013840830449826992, 0.014994232987312572, 0.013840830449826992, 0.01268742791234141, 0.01268742791234141, 0.013840830449826992, 0.01268742791234141, 0.01268742791234141, 0.013840830449826992, 0.013840830449826992, 0.014994232987312572, 0.013840830449826992, 0.013840830449826992, 0.014994232987312572, 0.013840830449826992, 0.013840830449826992, 0.013840830449826992, 0.013840830449826992, 0.013840830449826992, 0.013840830449826992, 0.013840830449826992, 0.013840830449826992, 0.013840830449826992, 0.013840830449826992, 0.014994232987312572, 0.013840830449826992, 0.013840830449826992, 0.013840830449826992, 0.013840830449826992, 0.013840830449826992, 0.013840830449826992, 0.013840830449826992, 0.013840830449826992, 0.013840830449826992, 0.014994232987312572, 0.014994232987312572, 0.013840830449826992, 0.014994232987312572, 0.013840830449826992, 0.014994232987312572, 0.013840830449826992, 0.014994232987312572, 0.013840830449826992]
    v28 = [0.5360824742268041, 0.5463917525773196, 0.5463917525773196, 0.5567010309278352, 0.5567010309278352, 0.5567010309278352, 0.5670103092783506, 0.5670103092783506, 0.5876288659793815, 0.5876288659793815, 0.5670103092783506, 0.5567010309278352, 0.5463917525773196, 0.5463917525773196, 0.5567010309278352, 0.577319587628866, 0.577319587628866, 0.577319587628866, 0.5670103092783506, 0.5670103092783506, 0.5463917525773196, 0.5360824742268041, 0.5360824742268041, 0.5360824742268041, 0.5154639175257733, 0.5257731958762887, 0.5257731958762887, 0.5360824742268041, 0.5463917525773196, 0.5567010309278352, 0.5567010309278352, 0.577319587628866, 0.5670103092783506, 0.577319587628866, 0.5567010309278352, 0.5567010309278352, 0.5463917525773196, 0.5463917525773196, 0.5463917525773196, 0.5463917525773196, 0.5463917525773196, 0.5567010309278352, 0.5670103092783506, 0.577319587628866, 0.5670103092783506, 0.577319587628866, 0.5670103092783506, 0.5463917525773196, 0.5360824742268041, 0.5360824742268041]
    v29 = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
    v30 = [0.14542553139882256, 0.1454152586624594, 0.1454047186467065, 0.14539390815279712, 0.1453828239819643, 0.1453714629354414, 0.1453598218144615, 0.14534789742025778, 0.1453356865540635, 0.14532318601711178, 0.14531039261063589, 0.14529730313586894, 0.14528391708888422, 0.1452702447451148, 0.14525629907483392, 0.14524209304831476, 0.14522763963583055, 0.14521295180765437, 0.14519804253405952, 0.14518292478531916, 0.14516761153170638, 0.14515211574349451, 0.14513645039095663, 0.145120628444366, 0.1451046628739957, 0.14508856665011907, 0.14507235274300917, 0.14505603412293921, 0.1450396237601824, 0.14502313462501196, 0.14500657968770098, 0.14498997191852275, 0.1449733242877504, 0.14495664976565706, 0.14493996132251608, 0.1449232719286004, 0.1449065945541835, 0.14488994216953832, 0.14487332774493822, 0.14485676425065627, 0.14484026465696567, 0.14482384193413966, 0.1448075090524514, 0.14479127898217406, 0.14477516469358087, 0.14475917915694494, 0.14474333534253955, 0.1447276462206378, 0.14471212476151296, 0.14469678393543808]
    v31 = [0.41478855108004525, 0.4147860133549201, 0.4147858686511851, 0.41478817717411426, 0.41479299912898115, 0.4148003947210597, 0.4148104241556235, 0.41482314763794653, 0.41483862537330246, 0.4148569175669651, 0.41487808442420815, 0.4149021861503055, 0.41492925417309423, 0.41495920481066473, 0.41499192560367054, 0.4150273040927653, 0.41506522781860283, 0.4151055843218366, 0.4151482611431203, 0.4151931458231078, 0.41524012590245246, 0.41528908892180805, 0.4153399224218282, 0.4153925139431668, 0.4154467510264771, 0.4155025212124131, 0.41555971204162817, 0.41561821105477614, 0.4156779057925106, 0.4157386837954854, 0.4158004326043539, 0.4158630397597699, 0.4159263928023871, 0.415990379272859, 0.4160548867118394, 0.4161198026599818, 0.4161850146579401, 0.4162504102463677, 0.4163158769659185, 0.4163813023572459, 0.41644657396100365, 0.4165115793178455, 0.41657620596842504, 0.41664034145339585, 0.4167038733134118, 0.4167666890891263, 0.4168286763211931, 0.4168897225502658, 0.4169497153169982, 0.4170085421620438]
    v32 = [0.883005774214958, 0.8830313409905586, 0.8830526652672653, 0.8830696332730205, 0.8830821312357652, 0.8830900453834414, 0.8830932619439913, 0.8830916671453557, 0.883085147215477, 0.8830735883822969, 0.8830568768737568, 0.8830348989177985, 0.8830075927973113, 0.8829751050149727, 0.8829376341284072, 0.8828953786952403, 0.8828485372730966, 0.8827973084196011, 0.8827418906923787, 0.8826824826490544, 0.8826192828472529, 0.8825524898445997, 0.882482302198719, 0.882408918467236, 0.8823325372077755, 0.8822533569779627, 0.8821715763354224, 0.8820873938377792, 0.8820010080426584, 0.8819126175076851, 0.8818224207904836, 0.8817306164486794, 0.8816374030398969, 0.8815429791217614, 0.8814475432518977, 0.8813512939879304, 0.8812544298874851, 0.8811571495081862, 0.8810596514076589, 0.8809621341435278, 0.880864796273418, 0.8807678363549545, 0.8806714529457618, 0.8805758446034654, 0.8804812098856901, 0.8803877473500604, 0.8802956555542016, 0.8802051330557384, 0.8801163784122963, 0.8800295901814991]
    sample_ts = [pressure, level, temperature_bottom_flask, temperature_middle_mantle_heating,v4,v5,v6,v7,v8,v9,v10,v11,v12,v13,v14,v15,v16,v17,v18,v19,v20,v21,v22,v23,v24,v25,v26,v27,v28,v29,v30,v31,v32]

    print(f"; bottom flask and middle mantle heating temperature space continuity constraint for 01 normalization:", file=txt_file)
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
            if i == 2:
                if j in [3,5,11,17,30,38,46,47,48]:
                    print(f"(assert (>= X_{i}_{j} {0.75 - perturbation_eps}))", file=txt_file)
                    print(f"(assert (<= X_{i}_{j} {0.75 + perturbation_eps}))\n", file=txt_file)
                else:
                    print(f"(assert (>= X_{i}_{j} {sample_ts[i][j] - perturbation_eps}))", file=txt_file)
                    print(f"(assert (<= X_{i}_{j} {sample_ts[i][j] + perturbation_eps}))\n", file=txt_file)
            elif i == 3:
                if j in [3,5,11,17,30,38,46,47,48]:
                    print(f"(assert (>= X_{i}_{j} {-0.9 - perturbation_eps}))", file=txt_file)
                    print(f"(assert (<= X_{i}_{j} {-0.9 + perturbation_eps}))\n", file=txt_file)
                else:
                    print(f"(assert (>= X_{i}_{j} {sample_ts[i][j] - perturbation_eps}))", file=txt_file)
                    print(f"(assert (<= X_{i}_{j} {sample_ts[i][j] + perturbation_eps}))\n", file=txt_file)
            else:
                print(f"(assert (>= X_{i}_{j} {sample_ts[i][j]}))", file=txt_file)
                print(f"(assert (<= X_{i}_{j} {sample_ts[i][j]}))\n", file=txt_file)

    # Declare bottom flask and middle mantle heating temperature space continuity constraint (normalization inverted to compare temperature measures).
    print(f"; bottom flask and middle mantle heating temperature space continuity constraint (normalization inverted to compare temperature measures):", file=txt_file)
    print(f"(assert (or", file=txt_file)
    for j in range(0, 50):
        print(f"    (and (>= (* X_2_{j} 44) (+ (* X_3_{j} 32.5) {7.9 + eps})))", file=txt_file)
        print(f"    (and (>= (* X_3_{j} 32.5) (+ (* X_2_{j} 44) {-7.9 + eps})))", file=txt_file)
    print(f"))", file=txt_file)
    print(f"(assert (> Y_0 Y_1))", file=txt_file)
    print(f"VNNLIB file completed!")

    