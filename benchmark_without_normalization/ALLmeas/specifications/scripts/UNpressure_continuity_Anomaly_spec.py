import sys

with open(sys.argv[1], "w") as txt_file:
    perturbation_eps = float(sys.argv[2])
    # eps for continuity constraint
    eps = 1
    pressure = [499.4, 499.6, 500.1, 500.3, 500.4, 499.9, 499.8, 499.8, 500.2, 500.2, 499.7, 499.7, 499.9, 499.6, 499.5, 500.0, 500.2, 500.5, 500.3, 500.2, 500.1, 500.2, 500.0, 499.9, 500.1, 500.1, 499.8, 499.8, 499.9, 500.0, 500.2, 500.5, 500.0, 499.8, 499.9, 499.9, 500.0, 500.0, 500.2, 500.1, 499.8, 499.9, 500.2, 500.2, 500.0, 500.1, 499.8, 499.8, 500.3, 500.2]
    level = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    temperature_bottom_flask = [69.8, 69.8, 69.8, 69.8, 69.8, 69.8, 69.8, 69.8, 69.8, 69.8, 69.8, 69.8, 69.8, 69.8, 69.8, 69.8, 69.8, 69.8, 69.8, 69.8, 69.8, 69.8, 69.8, 69.8, 69.8, 69.8, 69.8, 69.8, 69.8, 69.8, 69.8, 69.8, 69.8, 69.8, 69.8, 69.8, 69.8, 69.8, 69.8, 69.8, 69.8, 69.8, 69.8, 69.8, 69.8, 69.8, 69.8, 69.8, 69.8, 69.8]
    temperature_middle_mantle_heating = [82.7, 82.7, 82.7, 82.6, 82.6, 82.6, 82.6, 82.5, 82.5, 82.5, 82.4, 82.3, 82.4, 82.3, 82.3, 82.3, 82.3, 82.2, 82.2, 82.2, 82.1, 82.1, 82.1, 82.1, 82.0, 82.0, 82.0, 82.0, 82.0, 81.9, 81.9, 81.9, 81.8, 81.8, 81.8, 81.8, 81.8, 81.7, 81.7, 81.7, 81.6, 81.6, 81.6, 81.6, 81.5, 81.5, 81.5, 81.4, 81.4, 81.4]
    v4 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    v5 = [0, 0, 0, 1, 1, 1, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 0, 1, 1, 0, 0, 1, 1, 1, 1, 0, 0, 1, 1]
    v6 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    v7 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    v8 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    v9 = [60, 60, 60, 60, 60, 60, 60, 60, 60, 60, 60, 60, 60, 60, 60, 60, 60, 60, 60, 60, 60, 60, 60, 60, 60, 60, 60, 60, 60, 60, 60, 60, 60, 60, 60, 60, 60, 60, 60, 60, 60, 60, 60, 60, 60, 60, 60, 60, 60, 60]
    v10 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    v11 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    v12 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    v13 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    v14 = [21.0, 20.8, 22.1, 24.3, 25.1, 24.0, 22.5, 22.7, 23.4, 24.8, 21.7, 21.1, 22.2, 19.8, 18.7, 20.7, 22.2, 24.6, 24.5, 24.5, 24.0, 24.9, 24.4, 23.4, 24.4, 24.6, 23.5, 22.6, 22.8, 23.0, 24.4, 26.7, 24.9, 23.0, 23.6, 23.6, 24.2, 24.1, 24.9, 25.0, 23.5, 23.0, 24.9, 25.7, 24.9, 25.1, 23.7, 23.2, 25.3, 25.9]
    v15 = [0.0, 0.0, 0.0, 0.0, 0.8, 2.3, 6.1, 9.9, 22.4, 18.5, 7.5, 1.6, 0.0, 0.0, 3.2, 14.2, 12.8, 11.3, 10.4, 6.8, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 4.0, 11.4, 8.4, 11.7, 1.9, 1.9, 0.0, 0.0, 0.0, 0.0, 0.0, 1.8, 6.1, 11.3, 9.8, 14.1, 10.0, 0.0, 0.0, 0.0]
    v16 = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 26.5, 0.0, 10.5, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 100.0, 0.0, 0.0, 0.0, 100.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 100.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 85.3, 100.0, 0.0, 0.0, 0.0, 0.0]
    v17 = [426.7, 426.6, 426.7, 426.8, 426.8, 426.7, 426.8, 426.9, 426.9, 426.9, 426.9, 427.0, 427.0, 427.0, 427.0, 427.0, 427.1, 427.1, 427.1, 427.2, 427.2, 427.1, 427.1, 427.3, 427.3, 427.3, 427.4, 427.3, 427.4, 427.4, 427.3, 427.4, 427.5, 427.5, 427.5, 427.5, 427.5, 427.6, 427.6, 427.7, 427.7, 427.6, 427.7, 427.8, 427.7, 427.7, 427.8, 427.8, 427.8, 427.9]
    v18 = [73.7, 73.7, 73.7, 73.7, 73.6, 73.6, 73.6, 73.6, 73.5, 73.6, 73.5, 73.5, 73.5, 73.5, 73.4, 73.5, 73.5, 73.4, 73.4, 73.4, 73.3, 73.3, 73.3, 73.3, 73.2, 73.3, 73.3, 73.2, 73.2, 73.2, 73.1, 73.2, 73.1, 73.1, 73.1, 73.1, 73.1, 73.0, 73.0, 73.0, 73.0, 72.9, 72.9, 72.9, 72.9, 72.9, 72.9, 72.8, 72.8, 72.8]
    v19 = [78.2, 78.1, 78.1, 78.1, 78.0, 78.0, 78.0, 78.0, 77.9, 77.9, 77.9, 77.8, 77.8, 77.8, 77.7, 77.7, 77.7, 77.7, 77.6, 77.6, 77.6, 77.5, 77.6, 77.5, 77.4, 77.4, 77.4, 77.4, 77.4, 77.3, 77.3, 77.3, 77.2, 77.2, 77.1, 77.1, 77.1, 77.1, 77.1, 77.0, 77.0, 77.0, 77.0, 76.9, 76.9, 76.9, 76.9, 76.8, 76.8, 76.7]
    v20 = [85.8, 85.8, 85.7, 85.7, 85.6, 85.7, 85.7, 85.6, 85.6, 85.6, 85.5, 85.5, 85.5, 85.4, 85.5, 85.4, 85.3, 85.4, 85.4, 85.3, 85.3, 85.3, 85.3, 85.2, 85.2, 85.2, 85.2, 85.2, 85.1, 85.0, 85.1, 85.0, 85.0, 85.0, 84.9, 84.9, 84.9, 84.9, 84.9, 84.9, 84.8, 84.8, 84.8, 84.7, 84.7, 84.7, 84.7, 84.6, 84.6, 84.6]
    v21 = [68.7, 68.7, 68.7, 68.7, 68.7, 68.7, 68.7, 68.7, 68.7, 68.7, 68.7, 68.7, 68.7, 68.7, 68.7, 68.7, 68.7, 68.7, 68.7, 68.7, 68.7, 68.7, 68.7, 68.7, 68.7, 68.7, 68.7, 68.7, 68.7, 68.7, 68.7, 68.7, 68.7, 68.7, 68.7, 68.7, 68.7, 68.7, 68.7, 68.7, 68.7, 68.7, 68.7, 68.8, 68.8, 68.7, 68.7, 68.7, 68.8, 68.7]
    v22 = [65.7, 65.7, 65.7, 65.7, 65.7, 65.8, 65.8, 65.8, 65.8, 65.8, 65.8, 65.8, 65.8, 65.8, 65.8, 65.8, 65.8, 65.8, 65.9, 65.9, 65.9, 65.9, 65.9, 65.9, 65.9, 65.9, 65.9, 66.0, 65.9, 66.0, 66.0, 66.0, 66.0, 66.0, 66.0, 66.0, 66.0, 66.0, 66.0, 66.0, 66.0, 66.0, 66.1, 66.0, 66.1, 66.1, 66.1, 66.1, 66.1, 66.1]
    v23 = [64.4, 64.4, 64.4, 64.4, 64.4, 64.4, 64.4, 64.4, 64.4, 64.5, 64.5, 64.5, 64.5, 64.5, 64.5, 64.5, 64.5, 64.5, 64.5, 64.5, 64.5, 64.5, 64.5, 64.5, 64.5, 64.5, 64.5, 64.5, 64.5, 64.5, 64.5, 64.5, 64.5, 64.5, 64.5, 64.5, 64.5, 64.5, 64.5, 64.5, 64.5, 64.5, 64.5, 64.6, 64.5, 64.6, 64.6, 64.6, 64.6, 64.6]
    v24 = [63.9, 63.9, 63.9, 63.9, 63.9, 63.9, 63.9, 64.0, 63.9, 64.0, 63.9, 63.9, 64.0, 63.9, 63.9, 63.9, 64.0, 63.9, 63.9, 63.9, 64.0, 64.0, 64.0, 64.0, 64.0, 64.0, 64.0, 64.0, 64.0, 64.0, 64.0, 64.0, 64.0, 64.0, 64.0, 64.0, 64.0, 64.0, 64.0, 64.0, 64.0, 64.0, 64.0, 64.0, 64.0, 64.0, 64.0, 64.0, 64.0, 64.0]
    v25 = [0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.3, 0.3, 0.2, 0.1, 0.1, 0.0, 0.0, 0.2, 1.9, 0.3, 0.0, 0.3, 1.9, 0.3, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.7, 1.9, 1.9, 0.2, 0.0, 0.2, 0.1, 0.1, 0.0, 0.0, 0.0, 0.0, 0.0, 0.9, 1.6, 0.1, 0.0]
    v26 = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.1, 1.6, 0.1, 1.3, 1.3, 0.6, 0.1, 0.0, 0.0, 0.2, 0.8, 0.8, 0.8, 0.8, 0.3, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.3, 1.6, 0.3, 0.3, 0.6, 0.2, 0.1, 0.0, 0.0, 0.0, 0.0, 0.1, 0.4, 0.6, 0.8, 0.8, 0.3, 0.0]
    v27 = [0.6, 0.6, 0.6, 0.6, 0.6, 0.6, 0.6, 0.6, 0.7, 0.6, 0.5, 0.5, 0.6, 0.5, 0.5, 0.6, 0.6, 0.7, 0.6, 0.6, 0.7, 0.6, 0.6, 0.6, 0.6, 0.6, 0.6, 0.6, 0.6, 0.6, 0.6, 0.7, 0.6, 0.6, 0.6, 0.6, 0.6, 0.6, 0.6, 0.6, 0.6, 0.7, 0.7, 0.6, 0.7, 0.6, 0.7, 0.6, 0.7, 0.6]
    v28 = [2.8, 2.9, 2.9, 3.0, 3.0, 3.0, 3.1, 3.1, 3.3, 3.3, 3.1, 3.0, 2.9, 2.9, 3.0, 3.2, 3.2, 3.2, 3.1, 3.1, 2.9, 2.8, 2.8, 2.8, 2.6, 2.7, 2.7, 2.8, 2.9, 3.0, 3.0, 3.2, 3.1, 3.2, 3.0, 3.0, 2.9, 2.9, 2.9, 2.9, 2.9, 3.0, 3.1, 3.2, 3.1, 3.2, 3.1, 2.9, 2.8, 2.8]
    v29 = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
    v30 = [16.53699369702508, 16.53582553779709, 16.534626985023067, 16.533397674956795, 16.532137243852052, 16.530845327962634, 16.52952156354232, 16.528165586844896, 16.526777034124148, 16.525355541633857, 16.523900745627817, 16.522412282359802, 16.520890094526035, 16.519335350592396, 16.517749525467213, 16.516134094058796, 16.514490531275474, 16.512820312025553, 16.51112491121736, 16.509405803759215, 16.507664464559422, 16.505902368526318, 16.504120990568204, 16.50232180559341, 16.50050628851025, 16.498675914227043, 16.496832157652104, 16.494976493693752, 16.493110397260306, 16.49123534326009, 16.48935280660141, 16.487464262192596, 16.485571184941957, 16.483675049757814, 16.481777331548493, 16.479879505222293, 16.477983045687555, 16.47608942785258, 16.474200126625696, 16.47231661691522, 16.47044037362946, 16.468572871676745, 16.466715585965392, 16.464869991403717, 16.463037562900038, 16.46121977536267, 16.45941810369994, 16.457634022820155, 16.455869007631645, 16.454124533042712]
    v31 = [33.45296424096426, 33.452675664783875, 33.45265920986891, 33.452921722432876, 33.45347004868922, 33.45431103485143, 33.45545152713297, 33.45689837174732, 33.458658414907966, 33.46073850282836, 33.463145481721995, 33.465886197802334, 33.468964224870625, 33.47237004707914, 33.47609087616791, 33.480113923876964, 33.48442640194636, 33.489015522116105, 33.493868496126254, 33.49897253571685, 33.504314852627914, 33.50988265859949, 33.5156631653716, 33.521643584684305, 33.52781112827761, 33.53415300789159, 33.54065643526624, 33.54730862214162, 33.55409678025776, 33.5610081213547, 33.568029857172476, 33.57514919945112, 33.582353359930664, 33.58962955035115, 33.59696498245261, 33.60434686797508, 33.611762418658614, 33.61919884624322, 33.626643362468954, 33.634083179075844, 33.64150550780392, 33.64889756039323, 33.65624654858381, 33.663539684115676, 33.6707641787289, 33.677907244163485, 33.68495609215948, 33.69189793445692, 33.69871998279584, 33.70540944891628]
    v32 = [50.01004206201067, 50.01149879741905, 50.01271380510802, 50.01368060261035, 50.01439270745874, 50.01484363718595, 50.01502690932473, 50.01493604140779, 50.014564550967904, 50.013905955537794, 50.0129537726502, 50.01170151983786, 50.01014568060335, 50.00829460232848, 50.006159598364896, 50.00375198206425, 50.00108306677819, 49.998164165858356, 49.99500659265639, 49.99162166052395, 49.98802068281266, 49.98421497287421, 49.98021584406021, 49.976034609722305, 49.97168258321214, 49.96717107788139, 49.96251140708168, 49.95771488416464, 49.95279282248193, 49.94775653538523, 49.94261733622613, 49.937386538356314, 49.9320754551274, 49.92669539989106, 49.921257685998924, 49.915773626802626, 49.910254535653856, 49.904711725904214, 49.89915651090537, 49.89360020400896, 49.888054118566636, 49.88252956793004, 49.87703786545081, 49.871590324480614, 49.86619825837109, 49.860872980473864, 49.8556258041406, 49.850468042722945, 49.84541100957255, 49.84046601804103]
    sample_ts = [pressure, level, temperature_bottom_flask, temperature_middle_mantle_heating,v4,v5,v6,v7,v8,v9,v10,v11,v12,v13,v14,v15,v16,v17,v18,v19,v20,v21,v22,v23,v24,v25,v26,v27,v28,v29,v30,v31,v32]

    print(f"; Pressure Continuity constraint for unnormalized data:", file=txt_file)
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
                if j in [3, 8, 15]:
                    print(f"(assert (>= X_{i}_{j} {0 - perturbation_eps}))", file=txt_file)
                    print(f"(assert (<= X_{i}_{j} {0 + perturbation_eps}))\n", file=txt_file)
                else:
                    print(f"(assert (>= X_{i}_{j} {sample_ts[i][j] - perturbation_eps}))", file=txt_file)
                    print(f"(assert (<= X_{i}_{j} {sample_ts[i][j] + perturbation_eps}))\n", file=txt_file)
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

    