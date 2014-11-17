//Maya ASCII 2012 scene
//Name: tmpJnt_2.ma
//Last modified: Wed, Oct 08, 2014 09:19:05 AM
//Codeset: 1252
requires maya "2012";
requires "Mayatomr" "2012.0m - 3.9.1.48 ";
requires "stereoCamera" "10.0";
currentUnit -l centimeter -a degree -t pal;
fileInfo "application" "maya";
fileInfo "product" "Maya 2012";
fileInfo "version" "2012 x64";
fileInfo "cutIdentifier" "201201172029-821146";
fileInfo "osv" "Microsoft Business Edition, 64-bit  (Build 9200)\n";
createNode transform -s -n "persp";
	setAttr ".v" no;
	setAttr ".t" -type "double3" -9.4787785487356651 43.34575429365605 48.248039641200975 ;
	setAttr ".r" -type "double3" -31.538352724168316 -11.400000000004864 -2.0278538504223842e-015 ;
	setAttr ".rp" -type "double3" -8.8817841970012523e-016 0 4.4408920985006262e-016 ;
	setAttr ".rpt" -type "double3" 2.8126683237378335e-016 2.2431188088968526e-016 3.0918274421899509e-016 ;
createNode camera -s -n "perspShape" -p "persp";
	setAttr -k off ".v" no;
	setAttr ".fl" 34.999999999999986;
	setAttr ".coi" 56.266752113092416;
	setAttr ".imn" -type "string" "persp";
	setAttr ".den" -type "string" "persp_depth";
	setAttr ".man" -type "string" "persp_mask";
	setAttr ".tp" -type "double3" -1.6662356916441468e-006 13.914349897720328 1.2385446699622067 ;
	setAttr ".hc" -type "string" "viewSet -p %camera";
createNode transform -s -n "top";
	setAttr ".v" no;
	setAttr ".t" -type "double3" 12.276151417100792 110.18710575203853 0.13043313392671838 ;
	setAttr ".r" -type "double3" -89.999999999999986 0 0 ;
createNode camera -s -n "topShape" -p "top";
	setAttr -k off ".v" no;
	setAttr ".rnd" no;
	setAttr ".coi" 100;
	setAttr ".ow" 4.9898484501056517;
	setAttr ".imn" -type "string" "top";
	setAttr ".den" -type "string" "top_depth";
	setAttr ".man" -type "string" "top_mask";
	setAttr ".hc" -type "string" "viewSet -t %camera";
	setAttr ".o" yes;
createNode transform -s -n "front";
	setAttr ".v" no;
	setAttr ".t" -type "double3" 0.00017339897155754791 25.82538890838623 112.18341456394401 ;
createNode camera -s -n "frontShape" -p "front";
	setAttr -k off ".v" no;
	setAttr ".rnd" no;
	setAttr ".coi" 100;
	setAttr ".ow" 3.7414176820453848;
	setAttr ".imn" -type "string" "front";
	setAttr ".den" -type "string" "front_depth";
	setAttr ".man" -type "string" "front_mask";
	setAttr ".hc" -type "string" "viewSet -f %camera";
	setAttr ".o" yes;
createNode transform -s -n "side";
	setAttr ".v" no;
	setAttr ".t" -type "double3" 110.07009365403803 19.382808762053212 0.80681343596465971 ;
	setAttr ".r" -type "double3" 0 89.999999999999986 0 ;
createNode camera -s -n "sideShape" -p "side";
	setAttr -k off ".v" no;
	setAttr ".rnd" no;
	setAttr ".coi" 100;
	setAttr ".ow" 30.063120659866495;
	setAttr ".imn" -type "string" "side";
	setAttr ".den" -type "string" "side_depth";
	setAttr ".man" -type "string" "side_mask";
	setAttr ".hc" -type "string" "viewSet -s %camera";
	setAttr ".o" yes;
createNode transform -n "placement_tmpCtrl";
	setAttr -l on -k off ".v";
	setAttr ".ove" yes;
createNode nurbsCurve -n "placement_tmpCtrlShape" -p "placement_tmpCtrl";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".ovc" 17;
	setAttr ".cc" -type "nurbsCurve" 
		1 28 0 no 3
		29 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27
		 28
		29
		0 0 -8.3889106600755863
		3.2587610636203759 0 -4.8463226863005477
		1.9552558730988776 0 -4.8463226863005477
		1.9552558730988776 0 -2.4231632558336402
		2.4231632558336402 0 -1.9552558730988776
		4.8463226863005477 0 -1.9552558730988776
		4.8463226863005477 0 -3.2587610636203759
		8.3889106600755863 0 0
		4.8463226863005477 0 3.2587610636203759
		4.8463226863005477 0 1.9552558730988776
		2.4231632558336402 0 1.9552558730988776
		1.9552558730988776 0 2.4231632558336402
		1.9552558730988776 0 4.8463226863005477
		3.2587610636203759 0 4.8463226863005477
		0 0 8.3889106600755863
		-3.2587610636203759 0 4.8463226863005477
		-1.9552558730988776 0 4.8463226863005477
		-1.9552558730988776 0 2.4231632558336402
		-2.4231632558336402 0 1.9552558730988776
		-4.8463226863005477 0 1.9552558730988776
		-4.8463226863005477 0 3.2587610636203759
		-8.3889106600755863 0 0
		-4.8463226863005477 0 -3.2587610636203759
		-4.8463226863005477 0 -1.9552558730988776
		-2.4231632558336402 0 -1.9552558730988776
		-1.9552558730988776 0 -2.4231632558336402
		-1.9552558730988776 0 -4.8463226863005477
		-3.2587610636203759 0 -4.8463226863005477
		0 0 -8.3889106600755863
		;
createNode joint -n "root_tmpJnt" -p "placement_tmpCtrl";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".uoc" yes;
	setAttr ".t" -type "double3" 0 15.505442761864726 0.063615864537270264 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jot" -type "string" "yxz";
	setAttr ".ssc" no;
	setAttr ".bps" -type "matrix" 1 0 0 0 0 1 0 0 0 0 1 0 0 15.73707328056101 0 1;
	setAttr -k on -cb off ".radi" 0.25;
createNode joint -n "spine1_tmpJnt" -p "root_tmpJnt";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".uoc" yes;
	setAttr ".oc" 1;
	setAttr ".t" -type "double3" 0 0.26873146179137564 -0.48627597847963089 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jot" -type "string" "yxz";
	setAttr ".bps" -type "matrix" 1 0 0 0 0 1 0 0 0 0 1 0 0 16.462721689908392 7.9790056857053538e-017 1;
	setAttr -k on -cb off ".radi" 0.25;
createNode joint -n "spine2_tmpJnt" -p "spine1_tmpJnt";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".uoc" yes;
	setAttr ".oc" 2;
	setAttr ".t" -type "double3" 0 1.758904679260306 0.30712167061871776 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jot" -type "string" "yxz";
	setAttr ".bps" -type "matrix" 1 0 0 0 0 1 0 0 0 0 1 0 0 18.962119031422834 1.1092698799812162e-016 1;
	setAttr -k on -cb off ".radi" 0.25;
createNode joint -n "spine3_tmpJnt" -p "spine2_tmpJnt";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".uoc" yes;
	setAttr ".oc" 1;
	setAttr ".t" -type "double3" 0 1.4530761259604255 1.3877787807814457e-017 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jot" -type "string" "yxz";
	setAttr ".bps" -type "matrix" 1 0 0 0 0 1 0 0 0 0 1 0 0 16.462721689908392 7.9790056857053538e-017 1;
	setAttr -k on -cb off ".radi" 0.25;
createNode joint -n "spine4_tmpJnt" -p "spine3_tmpJnt";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".uoc" yes;
	setAttr ".oc" 1;
	setAttr ".t" -type "double3" 0 2.2006222677456577 0 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jot" -type "string" "yxz";
	setAttr ".bps" -type "matrix" 1 0 0 0 0 1 0 0 0 0 1 0 0 16.462721689908392 7.9790056857053538e-017 1;
	setAttr -k on -cb off ".radi" 0.25;
createNode joint -n "clavLFT_tmpJnt" -p "spine4_tmpJnt";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".uoc" yes;
	setAttr ".oc" 3;
	setAttr ".t" -type "double3" 0.40396301701286447 1.4416030953551164 1.0474520441579007 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jot" -type "string" "yxz";
	setAttr ".jo" -type "double3" 0 0 -89.999999999999986 ;
	setAttr ".ssc" no;
	setAttr ".bps" -type "matrix" 2.2204460492503131e-016 -1 0 0 1 2.2204460492503131e-016 0 0
		 0 0 1 0 0.40396301701286447 22.628380391977608 0.93191360083425789 1;
	setAttr -k on -cb off ".radi" 0.25;
createNode joint -n "upArmLFT_tmpJnt" -p "clavLFT_tmpJnt";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".uoc" yes;
	setAttr ".oc" 4;
	setAttr ".t" -type "double3" 0.67756095292631713 2.2966067942568755 -1.168247839024535 ;
	setAttr ".ro" 4;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jot" -type "string" "yxz";
	setAttr ".bps" -type "matrix" 2.2204460492503131e-016 -1 0 0 1 2.2204460492503131e-016 0 0
		 0 0 1 0 2.6840862727483024 21.950819439051291 -0.34347723857962076 1;
	setAttr -k on -cb off ".radi" 0.25;
createNode joint -n "forearmLFT_tmpJnt" -p "upArmLFT_tmpJnt";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".uoc" yes;
	setAttr ".oc" 5;
	setAttr ".t" -type "double3" -8.8959825878486818e-012 4.1612241440250184 -0.088515713288596642 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jot" -type "string" "yxz";
	setAttr ".jo" -type "double3" -5.9496752756331675e-005 3.0165268339926366e-021 -4.6590156498107123e-018 ;
	setAttr ".bps" -type "matrix" 2.2204460492503131e-016 -1 0 0 0.99999999999946088 2.220446049249116e-016 -1.0384142298428127e-006 0
		 1.0384142298428127e-006 2.3057427741397801e-022 0.99999999999946088 0 6.7891781465089913 21.950819439060187 -0.42637972484178432 1;
	setAttr -k on -cb off ".radi" 0.25;
createNode joint -n "wristLFT_tmpJnt" -p "forearmLFT_tmpJnt";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".uoc" yes;
	setAttr ".oc" 6;
	setAttr ".t" -type "double3" -2.8542501695483224e-011 4.2833426195408011 -0.018618578932339147 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jot" -type "string" "yxz";
	setAttr ".jo" -type "double3" 5.9496757566919035e-005 1.9356335384351445e-021 4.6590156485705813e-018 ;
	setAttr ".bps" -type "matrix" 2.2204460492503131e-016 -1 0 0 1 2.2204460492503131e-016 8.3960588285190204e-014 0
		 -8.3960588285190204e-014 -1.8642995655058271e-029 1 0 11.145136555499452 21.950819439088733 -0.34347297829513029 1;
	setAttr -k on -cb off ".radi" 0.25;
createNode joint -n "handLFT_tmpJnt" -p "wristLFT_tmpJnt";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".uoc" yes;
	setAttr ".oc" 7;
	setAttr ".t" -type "double3" -5.2381680883956627e-012 1.6863614471528008 -7.7810335666099371e-007 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 0 -1.5875595915794364e-015 1.0869579718907721e-017 ;
	setAttr ".ssc" no;
	setAttr ".bps" -type "matrix" 2.2204460492503131e-016 -1 0 0 1 2.2204460492503131e-016 8.3960588285190204e-014 0
		 -8.3960588285190204e-014 -1.8642995655058271e-029 1 0 11.94334900537585 21.950819439093973 -0.34347375639834526 1;
	setAttr -k on -cb off ".radi" 0.25;
createNode joint -n "index1LFT_tmpJnt" -p "handLFT_tmpJnt";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".uoc" yes;
	setAttr ".t" -type "double3" -0.20508239243773999 -0.62951491508865509 0.71315381735367622 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jot" -type "string" "yxz";
	setAttr ".jo" -type "double3" 0 -89.999999999995168 0 ;
	setAttr ".ssc" no;
	setAttr ".bps" -type "matrix" -8.3960588285190191e-014 -8.437694987151191e-014 1 0
		 1 2.2204460492503131e-016 8.3960588285190204e-014 0 -2.2204460493211562e-016 1 8.4376949871511897e-014 0
		 11.915961054098767 22.155901831531715 0.36968006095532863 1;
	setAttr -k on -cb off ".radi" 0.25;
createNode joint -n "index2LFT_tmpJnt" -p "index1LFT_tmpJnt";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".uoc" yes;
	setAttr ".oc" 1;
	setAttr ".t" -type "double3" 7.4773520708504293e-014 0.9122361830583241 3.5527136788005009e-015 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jot" -type "string" "yxz";
	setAttr ".jo" -type "double3" -9.823505109939511e-025 -4.8344431158245438e-012 1.1642418809960575e-011 ;
	setAttr ".bps" -type "matrix" -8.3960588285190191e-014 -8.437694987151191e-014 1 0
		 1 2.2204460492503131e-016 8.3960588285190204e-014 0 -2.2204460493211562e-016 1 8.4376949871511897e-014 0
		 13.114219270621863 22.155901831531715 0.36968006095542938 1;
	setAttr -k on -cb off ".radi" 0.25;
createNode joint -n "index3LFT_tmpJnt" -p "index2LFT_tmpJnt";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".uoc" yes;
	setAttr ".oc" 2;
	setAttr ".t" -type "double3" 1.5363144784119475e-016 0.69156617067904635 0.05 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jot" -type "string" "yxz";
	setAttr ".bps" -type "matrix" -8.3960588285190191e-014 -8.437694987151191e-014 1 0
		 1 2.2204460492503131e-016 8.3960588285190204e-014 0 -2.2204460493211562e-016 1 8.4376949871511897e-014 0
		 13.805785441300909 22.155901831531718 0.3696800609554875 1;
	setAttr -k on -cb off ".radi" 0.25;
createNode joint -n "index4LFT_tmpJnt" -p "index3LFT_tmpJnt";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".uoc" yes;
	setAttr ".oc" 3;
	setAttr ".t" -type "double3" -1.1102230246251565e-016 0.46560890699183055 -0.049999999999997158 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jot" -type "string" "yxz";
	setAttr ".jo" -type "double3" -9.823505109939511e-025 -4.8344431158245438e-012 1.1642418809960575e-011 ;
	setAttr ".bps" -type "matrix" -8.3960588285190191e-014 -8.437694987151191e-014 1 0
		 1 2.2204460492503131e-016 8.3960588285190204e-014 0 -2.2204460493211562e-016 1 8.4376949871511897e-014 0
		 14.271394348292739 22.155901831531718 0.36968006095552658 1;
	setAttr -k on -cb off ".radi" 0.25;
createNode joint -n "index5LFT_tmpJnt" -p "index4LFT_tmpJnt";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".uoc" yes;
	setAttr ".oc" 4;
	setAttr ".t" -type "double3" -6.7681320617408798e-017 0.54092799488757359 4.4790560149721159e-015 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".bps" -type "matrix" -8.3960588285190191e-014 -8.437694987151191e-014 1 0
		 1 2.2204460492503131e-016 8.3960588285190204e-014 0 -2.2204460493211562e-016 1 8.4376949871511897e-014 0
		 14.812322343180313 22.155901831531722 0.36968006095557193 1;
	setAttr -k on -cb off ".radi" 0.25;
createNode joint -n "middle1LFT_tmpJnt" -p "handLFT_tmpJnt";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".uoc" yes;
	setAttr ".t" -type "double3" -0.21892904604566424 -0.66884242070650723 0.24266506054506679 ;
	setAttr ".r" -type "double3" -1.2722218725854067e-014 1.2722218725854067e-014 -1.4124500153760508e-030 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jot" -type "string" "yxz";
	setAttr ".jo" -type "double3" 0 -89.999999999995168 0 ;
	setAttr ".ssc" no;
	setAttr ".bps" -type "matrix" -8.3960588285190191e-014 -8.437694987151191e-014 1 0
		 1 2.2204460492503131e-016 8.3960588285190204e-014 0 -2.2204460493211562e-016 1 8.4376949871511897e-014 0
		 11.876633548480955 22.169748485139639 -0.10080869585328409 1;
	setAttr -k on -cb off ".radi" 0.25;
createNode joint -n "middle2LFT_tmpJnt" -p "middle1LFT_tmpJnt";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".uoc" yes;
	setAttr ".oc" 1;
	setAttr ".t" -type "double3" 7.4953931950005881e-014 0.94594547358787828 3.5527136788005009e-015 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jot" -type "string" "yxz";
	setAttr ".jo" -type "double3" -9.823505109939511e-025 -4.8344431158245438e-012 1.1642418809960575e-011 ;
	setAttr ".bps" -type "matrix" -8.3960588285190191e-014 -8.437694987151191e-014 1 0
		 1 2.2204460492503131e-016 8.3960588285190204e-014 0 -2.2204460493211562e-016 1 8.4376949871511897e-014 0
		 13.108601055533605 22.169748485139639 -0.10080869585318036 1;
	setAttr -k on -cb off ".radi" 0.25;
createNode joint -n "middle3LFT_tmpJnt" -p "middle2LFT_tmpJnt";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".uoc" yes;
	setAttr ".oc" 2;
	setAttr ".t" -type "double3" 2.5688815224328411e-016 0.79831225735596656 0.05 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jot" -type "string" "yxz";
	setAttr ".bps" -type "matrix" -8.3960588285190191e-014 -8.437694987151191e-014 1 0
		 1 2.2204460492503131e-016 8.3960588285190204e-014 0 -2.2204460493211562e-016 1 8.4376949871511897e-014 0
		 13.906913312889571 22.169748485139639 -0.10080869585311319 1;
	setAttr -k on -cb off ".radi" 0.25;
createNode joint -n "middle4LFT_tmpJnt" -p "middle3LFT_tmpJnt";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".uoc" yes;
	setAttr ".oc" 3;
	setAttr ".t" -type "double3" 1.3877787807814457e-017 0.50493641260964139 -0.050000000000000711 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jot" -type "string" "yxz";
	setAttr ".jo" -type "double3" -9.823505109939511e-025 -4.8344431158245438e-012 1.1642418809960575e-011 ;
	setAttr ".bps" -type "matrix" -8.3960588285190191e-014 -8.437694987151191e-014 1 0
		 1 2.2204460492503131e-016 8.3960588285190204e-014 0 -2.2204460493211562e-016 1 8.4376949871511897e-014 0
		 14.411849725499213 22.169748485139639 -0.10080869585307067 1;
	setAttr -k on -cb off ".radi" 0.25;
createNode joint -n "middle5LFT_tmpJnt" -p "middle4LFT_tmpJnt";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".uoc" yes;
	setAttr ".oc" 4;
	setAttr ".t" -type "double3" 1.4310791050450855e-016 0.67014694191752755 -3.3445468616832841e-015 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".bps" -type "matrix" -8.3960588285190191e-014 -8.437694987151191e-014 1 0
		 1 2.2204460492503131e-016 8.3960588285190204e-014 0 -2.2204460493211562e-016 1 8.4376949871511897e-014 0
		 15.081996667416741 22.169748485139635 -0.10080869585301426 1;
	setAttr -k on -cb off ".radi" 0.25;
createNode joint -n "ring1LFT_tmpJnt" -p "handLFT_tmpJnt";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".uoc" yes;
	setAttr ".t" -type "double3" -0.18574316183847542 -0.66884242070654643 -0.22491752024930325 ;
	setAttr ".r" -type "double3" -3.1805546814635168e-015 -3.1805546814635168e-015 -3.1805546814635168e-015 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jot" -type "string" "yxz";
	setAttr ".jo" -type "double3" 0 -89.999999999995168 0 ;
	setAttr ".ssc" no;
	setAttr ".bps" -type "matrix" -8.3960588285190191e-014 -8.437694987151191e-014 1 0
		 1 2.2204460492503131e-016 8.3960588285190204e-014 0 -2.2204460493211562e-016 1 8.4376949871511897e-014 0
		 11.876633548480955 22.13656260093245 -0.5683912766476541 1;
	setAttr -k on -cb off ".radi" 0.25;
createNode joint -n "ring2LFT_tmpJnt" -p "ring1LFT_tmpJnt";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".uoc" yes;
	setAttr ".oc" 1;
	setAttr ".t" -type "double3" 7.5051076464660582e-014 0.93482449628968745 3.5527136788005009e-015 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jot" -type "string" "yxz";
	setAttr ".jo" -type "double3" -9.823505109939511e-025 -4.8344431158245438e-012 1.1642418809960575e-011 ;
	setAttr ".bps" -type "matrix" -8.3960588285190191e-014 -8.437694987151191e-014 1 0
		 1 2.2204460492503131e-016 8.3960588285190204e-014 0 -2.2204460493211562e-016 1 8.4376949871511897e-014 0
		 13.097480078235414 22.13656260093245 -0.56839127664755129 1;
	setAttr -k on -cb off ".radi" 0.25;
createNode joint -n "ring3LFT_tmpJnt" -p "ring2LFT_tmpJnt";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".uoc" yes;
	setAttr ".oc" 2;
	setAttr ".t" -type "double3" 2.9024092157436796e-016 0.74826785951410546 0.05 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jot" -type "string" "yxz";
	setAttr ".bps" -type "matrix" -8.3960588285190191e-014 -8.437694987151191e-014 1 0
		 1 2.2204460492503131e-016 8.3960588285190204e-014 0 -2.2204460493211562e-016 1 8.4376949871511897e-014 0
		 13.845747937749518 22.136562600932457 -0.56839127664748834 1;
	setAttr -k on -cb off ".radi" 0.25;
createNode joint -n "ring4LFT_tmpJnt" -p "ring3LFT_tmpJnt";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".uoc" yes;
	setAttr ".oc" 3;
	setAttr ".t" -type "double3" 2.2204460492503131e-016 0.4993759239605442 -0.049999999999997158 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jot" -type "string" "yxz";
	setAttr ".jo" -type "double3" -9.823505109939511e-025 -4.8344431158245438e-012 1.1642418809960575e-011 ;
	setAttr ".bps" -type "matrix" -8.3960588285190191e-014 -8.437694987151191e-014 1 0
		 1 2.2204460492503131e-016 8.3960588285190204e-014 0 -2.2204460493211562e-016 1 8.4376949871511897e-014 0
		 14.345123861710062 22.136562600932454 -0.56839127664744615 1;
	setAttr -k on -cb off ".radi" 0.25;
createNode joint -n "ring5LFT_tmpJnt" -p "ring4LFT_tmpJnt";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".uoc" yes;
	setAttr ".oc" 4;
	setAttr ".t" -type "double3" 2.1141942363466794e-017 0.53113472569012909 2.2100377083944522e-015 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".bps" -type "matrix" -8.3960588285190191e-014 -8.437694987151191e-014 1 0
		 1 2.2204460492503131e-016 8.3960588285190204e-014 0 -2.2204460493211562e-016 1 8.4376949871511897e-014 0
		 14.876258587400191 22.136562600932457 -0.56839127664740152 1;
	setAttr -k on -cb off ".radi" 0.25;
createNode joint -n "pinky1LFT_tmpJnt" -p "handLFT_tmpJnt";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".uoc" yes;
	setAttr ".t" -type "double3" -0.070168979817287438 -0.66884242070657929 -0.61559710445405857 ;
	setAttr ".r" -type "double3" -9.5416640443905503e-015 -3.1805546814635176e-015 -9.5416640443905503e-015 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jot" -type "string" "yxz";
	setAttr ".jo" -type "double3" 0 -89.999999999995168 0 ;
	setAttr ".ssc" no;
	setAttr ".bps" -type "matrix" -8.3960588285190191e-014 -8.437694987151191e-014 1 0
		 1 2.2204460492503131e-016 8.3960588285190204e-014 0 -2.2204460493211562e-016 1 8.4376949871511897e-014 0
		 11.876633548480955 22.020988418911262 -0.95907086085240945 1;
	setAttr -k on -cb off ".radi" 0.25;
createNode joint -n "pinky2LFT_tmpJnt" -p "pinky1LFT_tmpJnt";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".uoc" yes;
	setAttr ".oc" 1;
	setAttr ".t" -type "double3" 7.5051076464660582e-014 0.92044479840069648 3.5527136788005009e-015 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jot" -type "string" "yxz";
	setAttr ".jo" -type "double3" -9.823505109939511e-025 -4.8344431158245438e-012 1.1642418809960575e-011 ;
	setAttr ".bps" -type "matrix" -8.3960588285190191e-014 -8.437694987151191e-014 1 0
		 1 2.2204460492503131e-016 8.3960588285190204e-014 0 -2.2204460493211562e-016 1 8.4376949871511897e-014 0
		 13.083100380346423 22.020988418911262 -0.95907086085230775 1;
	setAttr -k on -cb off ".radi" 0.25;
createNode joint -n "pinky3LFT_tmpJnt" -p "pinky2LFT_tmpJnt";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".uoc" yes;
	setAttr ".oc" 2;
	setAttr ".t" -type "double3" 1.3351949754158972e-016 0.51819269329026851 0.05 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jot" -type "string" "yxz";
	setAttr ".bps" -type "matrix" -8.3960588285190191e-014 -8.437694987151191e-014 1 0
		 1 2.2204460492503131e-016 8.3960588285190204e-014 0 -2.2204460493211562e-016 1 8.4376949871511897e-014 0
		 13.601293073636691 22.020988418911262 -0.95907086085226423 1;
	setAttr -k on -cb off ".radi" 0.25;
createNode joint -n "pinky4LFT_tmpJnt" -p "pinky3LFT_tmpJnt";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".uoc" yes;
	setAttr ".oc" 3;
	setAttr ".t" -type "double3" 0 0.37714849190413702 -0.050000000000000711 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jot" -type "string" "yxz";
	setAttr ".jo" -type "double3" -9.823505109939511e-025 -4.8344431158245438e-012 1.1642418809960575e-011 ;
	setAttr ".bps" -type "matrix" -8.3960588285190191e-014 -8.437694987151191e-014 1 0
		 1 2.2204460492503131e-016 8.3960588285190204e-014 0 -2.2204460493211562e-016 1 8.4376949871511897e-014 0
		 13.978441565540829 22.020988418911262 -0.95907086085223248 1;
	setAttr -k on -cb off ".radi" 0.25;
createNode joint -n "pinky5LFT_tmpJnt" -p "pinky4LFT_tmpJnt";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".uoc" yes;
	setAttr ".oc" 4;
	setAttr ".t" -type "double3" 2.0822102722584103e-016 0.45923623624518384 3.4694469519536142e-016 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".bps" -type "matrix" -8.3960588285190191e-014 -8.437694987151191e-014 1 0
		 1 2.2204460492503131e-016 8.3960588285190204e-014 0 -2.2204460493211562e-016 1 8.4376949871511897e-014 0
		 14.437677801786013 22.020988418911262 -0.95907086085219373 1;
	setAttr -k on -cb off ".radi" 0.25;
createNode joint -n "thumb1LFT_tmpJnt" -p "handLFT_tmpJnt";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".uoc" yes;
	setAttr ".t" -type "double3" 0.045389719457208599 -1.3128526620028929 0.66914900059116733 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jot" -type "string" "yxz";
	setAttr ".jo" -type "double3" 23.149018263985369 -2.8646367838908361e-012 -36.547276247142648 ;
	setAttr ".ssc" no;
	setAttr ".bps" -type "matrix" -0.59548586752167076 -0.80336578317847407 -4.9997343752636337e-014 0
		 0.73868319246536318 -0.54754062333671982 0.39312390790336815 0 -0.31582229615899904 0.23409973134130962 0.91948550452673483 0
		 11.518645340649305 21.905429719636764 0.32567524419271171 1;
	setAttr -k on -cb off ".radi" 0.25;
createNode joint -n "thumb2LFT_tmpJnt" -p "thumb1LFT_tmpJnt";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".uoc" yes;
	setAttr ".oc" 1;
	setAttr ".t" -type "double3" -4.0523140398818214e-015 0.68722392561716927 -4.8672003927219265e-015 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jot" -type "string" "yxz";
	setAttr ".jo" -type "double3" 1.8123570865566035e-015 5.1492481437703705e-016 -2.6927091040474237e-015 ;
	setAttr ".ssc" no;
	setAttr ".bps" -type "matrix" -0.59548586752167076 -0.80336578317847407 -4.9997343752636337e-014 0
		 0.73868319246536318 -0.54754062333671982 0.39312390790336815 0 -0.31582229615899904 0.23409973134130962 0.91948550452673483 0
		 12.026286103962779 21.529146703032435 0.59583939943602238 1;
	setAttr -k on -cb off ".radi" 0.25;
createNode joint -n "thumb3LFT_tmpJnt" -p "thumb2LFT_tmpJnt";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".uoc" yes;
	setAttr ".oc" 2;
	setAttr ".t" -type "double3" -1.0657707355532513e-015 0.94582760545164868 2.3297336282368519e-015 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jot" -type "string" "yxz";
	setAttr ".ssc" no;
	setAttr ".bps" -type "matrix" -0.59548586752167076 -0.80336578317847407 -4.9997343752636337e-014 0
		 0.73868319246536318 -0.54754062333671982 0.39312390790336815 0 -0.31582229615899904 0.23409973134130962 0.91948550452673483 0
		 12.724953059079672 21.011267666374362 0.96766684389406166 1;
	setAttr -k on -cb off ".radi" 0.25;
createNode joint -n "thumb4LFT_tmpJnt" -p "thumb3LFT_tmpJnt";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".uoc" yes;
	setAttr ".oc" 3;
	setAttr ".t" -type "double3" 2.3917499925030287e-016 0.80585684881561115 -2.5621865740177441e-015 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".ssc" no;
	setAttr ".bps" -type "matrix" -0.59548586752167076 -0.80336578317847407 -4.9997343752636337e-014 0
		 0.73868319246536318 -0.54754062333671982 0.39312390790336815 0 -0.31582229615899904 0.23409973134130962 0.91948550452673483 0
		 13.320225968832865 20.570028305053697 1.2844684375111461 1;
	setAttr -k on -cb off ".radi" 0.25;
createNode joint -n "elbowIkLFT_tmpJnt" -p "forearmLFT_tmpJnt";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".uoc" yes;
	setAttr ".oc" 2;
	setAttr ".t" -type "double3" 8.8959950517164543e-012 0 -5 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jot" -type "string" "yxz";
	setAttr ".jo" -type "double3" -1.3210932960106684e-020 5.9496752756331675e-005 -90.000000000000014 ;
	setAttr ".bps" -type "matrix" -1 -1.2246467991473532e-016 0 0 1.2246467991473532e-016 -1 0 0
		 0 0 1 0 1.3486489690923307 14.656585133659888 1.5144370407379352e-017 1;
	setAttr -k on -cb off ".radi" 0.25;
createNode joint -n "clavRGT_tmpJnt" -p "spine4_tmpJnt";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".uoc" yes;
	setAttr ".oc" 3;
	setAttr ".t" -type "double3" -0.403963 1.441622703377508 1.047452443323643 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jot" -type "string" "yxz";
	setAttr ".jo" -type "double3" -180 0 89.999999999999986 ;
	setAttr ".ssc" no;
	setAttr ".bps" -type "matrix" 2.2204460492503131e-016 -1 0 0 1 2.2204460492503131e-016 0 0
		 0 0 1 0 0.40396301701286447 22.628380391977608 0.93191360083425789 1;
	setAttr -k on -cb off ".radi" 0.25;
createNode joint -n "upArmRGT_tmpJnt" -p "clavRGT_tmpJnt";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".uoc" yes;
	setAttr ".oc" 4;
	setAttr ".t" -type "double3" -0.6775999999999982 -2.296607 1.1682480000000004 ;
	setAttr ".ro" 4;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jot" -type "string" "yxz";
	setAttr ".bps" -type "matrix" 2.2204460492503131e-016 -1 0 0 1 2.2204460492503131e-016 0 0
		 0 0 1 0 2.6840862727483024 21.950819439051291 -0.34347723857962076 1;
	setAttr -k on -cb off ".radi" 0.25;
createNode joint -n "forearmRGT_tmpJnt" -p "upArmRGT_tmpJnt";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".uoc" yes;
	setAttr ".oc" 5;
	setAttr ".t" -type "double3" 0 -4.16122 0.088516000000000483 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jot" -type "string" "yxz";
	setAttr ".jo" -type "double3" -5.9495221286656017e-005 0 0 ;
	setAttr ".bps" -type "matrix" 2.2204460492503131e-016 -1 0 0 0.99999999999946088 2.220446049249116e-016 -1.0384142298428127e-006 0
		 1.0384142298428127e-006 2.3057427741397801e-022 0.99999999999946088 0 6.7891781465089913 21.950819439060187 -0.42637972484178432 1;
	setAttr -k on -cb off ".radi" 0.25;
createNode joint -n "wristRGT_tmpJnt" -p "forearmRGT_tmpJnt";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".uoc" yes;
	setAttr ".oc" 6;
	setAttr ".t" -type "double3" -3.5527136788005009e-015 -4.2833100193355804 0.018618552264424992 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jot" -type "string" "yxz";
	setAttr ".jo" -type "double3" 5.9495221286656017e-005 0 0 ;
	setAttr ".bps" -type "matrix" 2.2204460492503131e-016 -1 0 0 1 2.2204460492503131e-016 8.3960588285190204e-014 0
		 -8.3960588285190204e-014 -1.8642995655058271e-029 1 0 11.145136555499452 21.950819439088733 -0.34347297829513029 1;
	setAttr -k on -cb off ".radi" 0.25;
createNode joint -n "handRGT_tmpJnt" -p "wristRGT_tmpJnt";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".uoc" yes;
	setAttr ".oc" 7;
	setAttr ".t" -type "double3" 3.5527136788005009e-015 -1.6864000000000008 1.0000000001952891e-006 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".ssc" no;
	setAttr ".bps" -type "matrix" 2.2204460492503131e-016 -1 0 0 1 2.2204460492503131e-016 8.3960588285190204e-014 0
		 -8.3960588285190204e-014 -1.8642995655058271e-029 1 0 11.94334900537585 21.950819439093973 -0.34347375639834526 1;
	setAttr -k on -cb off ".radi" 0.25;
createNode joint -n "index1RGT_tmpJnt" -p "handRGT_tmpJnt";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".uoc" yes;
	setAttr ".t" -type "double3" 0.20509999999999806 0.62950000000000017 -0.71315400000000007 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jot" -type "string" "yxz";
	setAttr ".jo" -type "double3" -4.8035706460884312e-012 -89.999999999993193 0 ;
	setAttr ".ssc" no;
	setAttr ".bps" -type "matrix" -8.3960588285190191e-014 -8.437694987151191e-014 1 0
		 1 2.2204460492503131e-016 8.3960588285190204e-014 0 -2.2204460493211562e-016 1 8.4376949871511897e-014 0
		 11.915961054098767 22.155901831531715 0.36968006095532863 1;
	setAttr -k on -cb off ".radi" 0.25;
createNode joint -n "index2RGT_tmpJnt" -p "index1RGT_tmpJnt";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".uoc" yes;
	setAttr ".oc" 1;
	setAttr ".t" -type "double3" 1.1102230246251565e-016 -0.91220000000000034 0 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jot" -type "string" "yxz";
	setAttr ".bps" -type "matrix" -8.3960588285190191e-014 -8.437694987151191e-014 1 0
		 1 2.2204460492503131e-016 8.3960588285190204e-014 0 -2.2204460493211562e-016 1 8.4376949871511897e-014 0
		 13.114219270621863 22.155901831531715 0.36968006095542938 1;
	setAttr -k on -cb off ".radi" 0.25;
createNode joint -n "index3RGT_tmpJnt" -p "index2RGT_tmpJnt";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".uoc" yes;
	setAttr ".oc" 2;
	setAttr ".t" -type "double3" 5.9952043329758453e-015 -0.69159999999999933 -0.050000000000000711 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jot" -type "string" "yxz";
	setAttr ".bps" -type "matrix" -8.3960588285190191e-014 -8.437694987151191e-014 1 0
		 1 2.2204460492503131e-016 8.3960588285190204e-014 0 -2.2204460493211562e-016 1 8.4376949871511897e-014 0
		 13.805785441300909 22.155901831531718 0.3696800609554875 1;
	setAttr -k on -cb off ".radi" 0.25;
createNode joint -n "index4RGT_tmpJnt" -p "index3RGT_tmpJnt";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".uoc" yes;
	setAttr ".oc" 3;
	setAttr ".t" -type "double3" -5.8286708792820718e-015 -0.46560000000000024 0.050000000000000711 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jot" -type "string" "yxz";
	setAttr ".bps" -type "matrix" -8.3960588285190191e-014 -8.437694987151191e-014 1 0
		 1 2.2204460492503131e-016 8.3960588285190204e-014 0 -2.2204460493211562e-016 1 8.4376949871511897e-014 0
		 14.271394348292739 22.155901831531718 0.36968006095552658 1;
	setAttr -k on -cb off ".radi" 0.25;
createNode joint -n "index5RGT_tmpJnt" -p "index4RGT_tmpJnt";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".uoc" yes;
	setAttr ".oc" 4;
	setAttr ".t" -type "double3" 1.1102230246251565e-016 -0.5409000000000006 0 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".bps" -type "matrix" -8.3960588285190191e-014 -8.437694987151191e-014 1 0
		 1 2.2204460492503131e-016 8.3960588285190204e-014 0 -2.2204460493211562e-016 1 8.4376949871511897e-014 0
		 14.812322343180313 22.155901831531722 0.36968006095557193 1;
	setAttr -k on -cb off ".radi" 0.25;
createNode joint -n "middle1RGT_tmpJnt" -p "handRGT_tmpJnt";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".uoc" yes;
	setAttr ".t" -type "double3" 0.21889999999999787 0.66880000000000095 -0.24266500000000002 ;
	setAttr ".r" -type "double3" -1.2722218725854067e-014 1.2722218725854067e-014 -1.4124500153760508e-030 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jot" -type "string" "yxz";
	setAttr ".jo" -type "double3" -4.8035706460884312e-012 -89.999999999993193 0 ;
	setAttr ".ssc" no;
	setAttr ".bps" -type "matrix" -8.3960588285190191e-014 -8.437694987151191e-014 1 0
		 1 2.2204460492503131e-016 8.3960588285190204e-014 0 -2.2204460493211562e-016 1 8.4376949871511897e-014 0
		 11.876633548480955 22.169748485139639 -0.10080869585328409 1;
	setAttr -k on -cb off ".radi" 0.25;
createNode joint -n "middle2RGT_tmpJnt" -p "middle1RGT_tmpJnt";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".uoc" yes;
	setAttr ".oc" 1;
	setAttr ".t" -type "double3" 1.1102230246251565e-016 -0.9459 0 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jot" -type "string" "yxz";
	setAttr ".bps" -type "matrix" -8.3960588285190191e-014 -8.437694987151191e-014 1 0
		 1 2.2204460492503131e-016 8.3960588285190204e-014 0 -2.2204460493211562e-016 1 8.4376949871511897e-014 0
		 13.108601055533605 22.169748485139639 -0.10080869585318036 1;
	setAttr -k on -cb off ".radi" 0.25;
createNode joint -n "middle3RGT_tmpJnt" -p "middle2RGT_tmpJnt";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".uoc" yes;
	setAttr ".oc" 2;
	setAttr ".t" -type "double3" 6.0229599085914742e-015 -0.79830000000000112 -0.050000000000000711 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jot" -type "string" "yxz";
	setAttr ".bps" -type "matrix" -8.3960588285190191e-014 -8.437694987151191e-014 1 0
		 1 2.2204460492503131e-016 8.3960588285190204e-014 0 -2.2204460493211562e-016 1 8.4376949871511897e-014 0
		 13.906913312889571 22.169748485139639 -0.10080869585311319 1;
	setAttr -k on -cb off ".radi" 0.25;
createNode joint -n "middle4RGT_tmpJnt" -p "middle3RGT_tmpJnt";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".uoc" yes;
	setAttr ".oc" 3;
	setAttr ".t" -type "double3" -5.8841820305133297e-015 -0.50489999999999924 0.050000000000000711 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jot" -type "string" "yxz";
	setAttr ".bps" -type "matrix" -8.3960588285190191e-014 -8.437694987151191e-014 1 0
		 1 2.2204460492503131e-016 8.3960588285190204e-014 0 -2.2204460493211562e-016 1 8.4376949871511897e-014 0
		 14.411849725499213 22.169748485139639 -0.10080869585307067 1;
	setAttr -k on -cb off ".radi" 0.25;
createNode joint -n "middle5RGT_tmpJnt" -p "middle4RGT_tmpJnt";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".uoc" yes;
	setAttr ".oc" 4;
	setAttr ".t" -type "double3" 8.3266726846886741e-017 -0.67020000000000124 0 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".bps" -type "matrix" -8.3960588285190191e-014 -8.437694987151191e-014 1 0
		 1 2.2204460492503131e-016 8.3960588285190204e-014 0 -2.2204460493211562e-016 1 8.4376949871511897e-014 0
		 15.081996667416741 22.169748485139635 -0.10080869585301426 1;
	setAttr -k on -cb off ".radi" 0.25;
createNode joint -n "ring1RGT_tmpJnt" -p "handRGT_tmpJnt";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".uoc" yes;
	setAttr ".t" -type "double3" 0.18580000000000041 0.66880000000000095 0.22491699999999992 ;
	setAttr ".r" -type "double3" -3.1805546814635168e-015 -3.1805546814635168e-015 -3.1805546814635168e-015 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jot" -type "string" "yxz";
	setAttr ".jo" -type "double3" -4.8035706460884312e-012 -89.999999999993193 0 ;
	setAttr ".ssc" no;
	setAttr ".bps" -type "matrix" -8.3960588285190191e-014 -8.437694987151191e-014 1 0
		 1 2.2204460492503131e-016 8.3960588285190204e-014 0 -2.2204460493211562e-016 1 8.4376949871511897e-014 0
		 11.876633548480955 22.13656260093245 -0.5683912766476541 1;
	setAttr -k on -cb off ".radi" 0.25;
createNode joint -n "ring2RGT_tmpJnt" -p "ring1RGT_tmpJnt";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".uoc" yes;
	setAttr ".oc" 1;
	setAttr ".t" -type "double3" 2.2204460492503131e-016 -0.93480000000000096 0 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jot" -type "string" "yxz";
	setAttr ".bps" -type "matrix" -8.3960588285190191e-014 -8.437694987151191e-014 1 0
		 1 2.2204460492503131e-016 8.3960588285190204e-014 0 -2.2204460493211562e-016 1 8.4376949871511897e-014 0
		 13.097480078235414 22.13656260093245 -0.56839127664755129 1;
	setAttr -k on -cb off ".radi" 0.25;
createNode joint -n "ring3RGT_tmpJnt" -p "ring2RGT_tmpJnt";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".uoc" yes;
	setAttr ".oc" 2;
	setAttr ".t" -type "double3" 5.9952043329758453e-015 -0.74820000000000064 -0.049999999999997158 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jot" -type "string" "yxz";
	setAttr ".bps" -type "matrix" -8.3960588285190191e-014 -8.437694987151191e-014 1 0
		 1 2.2204460492503131e-016 8.3960588285190204e-014 0 -2.2204460493211562e-016 1 8.4376949871511897e-014 0
		 13.845747937749518 22.136562600932457 -0.56839127664748834 1;
	setAttr -k on -cb off ".radi" 0.25;
createNode joint -n "ring4RGT_tmpJnt" -p "ring3RGT_tmpJnt";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".uoc" yes;
	setAttr ".oc" 3;
	setAttr ".t" -type "double3" -5.9952043329758453e-015 -0.49939999999999962 0.049999999999997158 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jot" -type "string" "yxz";
	setAttr ".bps" -type "matrix" -8.3960588285190191e-014 -8.437694987151191e-014 1 0
		 1 2.2204460492503131e-016 8.3960588285190204e-014 0 -2.2204460493211562e-016 1 8.4376949871511897e-014 0
		 14.345123861710062 22.136562600932454 -0.56839127664744615 1;
	setAttr -k on -cb off ".radi" 0.25;
createNode joint -n "ring5RGT_tmpJnt" -p "ring4RGT_tmpJnt";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".uoc" yes;
	setAttr ".oc" 4;
	setAttr ".t" -type "double3" 1.1102230246251565e-016 -0.53120000000000012 0 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".bps" -type "matrix" -8.3960588285190191e-014 -8.437694987151191e-014 1 0
		 1 2.2204460492503131e-016 8.3960588285190204e-014 0 -2.2204460493211562e-016 1 8.4376949871511897e-014 0
		 14.876258587400191 22.136562600932457 -0.56839127664740152 1;
	setAttr -k on -cb off ".radi" 0.25;
createNode joint -n "pinky1RGT_tmpJnt" -p "handRGT_tmpJnt";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".uoc" yes;
	setAttr ".t" -type "double3" 0.070199999999999818 0.66880000000000095 0.615597 ;
	setAttr ".r" -type "double3" -9.5416640443905503e-015 -3.1805546814635176e-015 -9.5416640443905503e-015 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jot" -type "string" "yxz";
	setAttr ".jo" -type "double3" -4.8035706460884312e-012 -89.999999999993193 0 ;
	setAttr ".ssc" no;
	setAttr ".bps" -type "matrix" -8.3960588285190191e-014 -8.437694987151191e-014 1 0
		 1 2.2204460492503131e-016 8.3960588285190204e-014 0 -2.2204460493211562e-016 1 8.4376949871511897e-014 0
		 11.876633548480955 22.020988418911262 -0.95907086085240945 1;
	setAttr -k on -cb off ".radi" 0.25;
createNode joint -n "pinky2RGT_tmpJnt" -p "pinky1RGT_tmpJnt";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".uoc" yes;
	setAttr ".oc" 1;
	setAttr ".t" -type "double3" 2.2204460492503131e-016 -0.92040000000000077 0 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jot" -type "string" "yxz";
	setAttr ".bps" -type "matrix" -8.3960588285190191e-014 -8.437694987151191e-014 1 0
		 1 2.2204460492503131e-016 8.3960588285190204e-014 0 -2.2204460493211562e-016 1 8.4376949871511897e-014 0
		 13.083100380346423 22.020988418911262 -0.95907086085230775 1;
	setAttr -k on -cb off ".radi" 0.25;
createNode joint -n "pinky3RGT_tmpJnt" -p "pinky2RGT_tmpJnt";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".uoc" yes;
	setAttr ".oc" 2;
	setAttr ".t" -type "double3" 5.9952043329758453e-015 -0.51820000000000022 -0.050000000000000711 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jot" -type "string" "yxz";
	setAttr ".bps" -type "matrix" -8.3960588285190191e-014 -8.437694987151191e-014 1 0
		 1 2.2204460492503131e-016 8.3960588285190204e-014 0 -2.2204460493211562e-016 1 8.4376949871511897e-014 0
		 13.601293073636691 22.020988418911262 -0.95907086085226423 1;
	setAttr -k on -cb off ".radi" 0.25;
createNode joint -n "pinky4RGT_tmpJnt" -p "pinky3RGT_tmpJnt";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".uoc" yes;
	setAttr ".oc" 3;
	setAttr ".t" -type "double3" -5.9952043329758453e-015 -0.37710000000000043 0.050000000000000711 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jot" -type "string" "yxz";
	setAttr ".bps" -type "matrix" -8.3960588285190191e-014 -8.437694987151191e-014 1 0
		 1 2.2204460492503131e-016 8.3960588285190204e-014 0 -2.2204460493211562e-016 1 8.4376949871511897e-014 0
		 13.978441565540829 22.020988418911262 -0.95907086085223248 1;
	setAttr -k on -cb off ".radi" 0.25;
createNode joint -n "pinky5RGT_tmpJnt" -p "pinky4RGT_tmpJnt";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".uoc" yes;
	setAttr ".oc" 4;
	setAttr ".t" -type "double3" 1.1102230246251565e-016 -0.45929999999999893 0 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".bps" -type "matrix" -8.3960588285190191e-014 -8.437694987151191e-014 1 0
		 1 2.2204460492503131e-016 8.3960588285190204e-014 0 -2.2204460493211562e-016 1 8.4376949871511897e-014 0
		 14.437677801786013 22.020988418911262 -0.95907086085219373 1;
	setAttr -k on -cb off ".radi" 0.25;
createNode joint -n "thumb1RGT_tmpJnt" -p "handRGT_tmpJnt";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".uoc" yes;
	setAttr ".t" -type "double3" -0.045400000000000773 1.3129000000000008 -0.6691490000000001 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jot" -type "string" "yxz";
	setAttr ".jo" -type "double3" 23.149018263989252 2.8617040746467993e-012 -36.547276247142662 ;
	setAttr ".ssc" no;
	setAttr ".bps" -type "matrix" -0.59548586752167076 -0.80336578317847407 -4.9997343752636337e-014 0
		 0.73868319246536318 -0.54754062333671982 0.39312390790336815 0 -0.31582229615899904 0.23409973134130962 0.91948550452673483 0
		 11.518645340649305 21.905429719636764 0.32567524419271171 1;
	setAttr -k on -cb off ".radi" 0.25;
createNode joint -n "thumb2RGT_tmpJnt" -p "thumb1RGT_tmpJnt";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".uoc" yes;
	setAttr ".oc" 1;
	setAttr ".t" -type "double3" 2.1630730699939704e-005 -0.68727692083108138 2.2826818697474494e-005 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jot" -type "string" "yxz";
	setAttr ".ssc" no;
	setAttr ".bps" -type "matrix" -0.59548586752167076 -0.80336578317847407 -4.9997343752636337e-014 0
		 0.73868319246536318 -0.54754062333671982 0.39312390790336815 0 -0.31582229615899904 0.23409973134130962 0.91948550452673483 0
		 12.026286103962779 21.529146703032435 0.59583939943602238 1;
	setAttr -k on -cb off ".radi" 0.25;
createNode joint -n "thumb3RGT_tmpJnt" -p "thumb2RGT_tmpJnt";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".uoc" yes;
	setAttr ".oc" 2;
	setAttr ".t" -type "double3" 8.3173107576328675e-005 -0.94580895776719398 -8.5769623434650555e-006 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jot" -type "string" "yxz";
	setAttr ".ssc" no;
	setAttr ".bps" -type "matrix" -0.59548586752167076 -0.80336578317847407 -4.9997343752636337e-014 0
		 0.73868319246536318 -0.54754062333671982 0.39312390790336815 0 -0.31582229615899904 0.23409973134130962 0.91948550452673483 0
		 12.724953059079672 21.011267666374362 0.96766684389406166 1;
	setAttr -k on -cb off ".radi" 0.25;
createNode joint -n "thumb4RGT_tmpJnt" -p "thumb3RGT_tmpJnt";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".uoc" yes;
	setAttr ".oc" 3;
	setAttr ".t" -type "double3" -9.213176776512455e-005 -0.80583674662938987 -1.0124175824799408e-005 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".ssc" no;
	setAttr ".bps" -type "matrix" -0.59548586752167076 -0.80336578317847407 -4.9997343752636337e-014 0
		 0.73868319246536318 -0.54754062333671982 0.39312390790336815 0 -0.31582229615899904 0.23409973134130962 0.91948550452673483 0
		 13.320225968832865 20.570028305053697 1.2844684375111461 1;
	setAttr -k on -cb off ".radi" 0.25;
createNode joint -n "elbowIkRGT_tmpJnt" -p "forearmRGT_tmpJnt";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".uoc" yes;
	setAttr ".oc" 2;
	setAttr ".t" -type "double3" 0 -5.1919375021469705e-006 4.9999999999973035 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jot" -type "string" "yxz";
	setAttr ".jo" -type "double3" -6.1262578697007117e-009 5.9495221279639311e-005 -90 ;
	setAttr ".bps" -type "matrix" -1 -1.2246467991473532e-016 0 0 1.2246467991473532e-016 -1 0 0
		 0 0 1 0 1.3486489690923307 14.656585133659888 1.5144370407379352e-017 1;
	setAttr -k on -cb off ".radi" 0.25;
createNode joint -n "neck1_tmpJnt" -p "spine4_tmpJnt";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".uoc" yes;
	setAttr ".oc" 3;
	setAttr ".t" -type "double3" 0 1.7237813257288295 -0.051186945103120537 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jot" -type "string" "yxz";
	setAttr ".bps" -type "matrix" 1 0 0 0 0 1 0 0 0 0 1 0 0 22.764810214551506 1.2852494451027699e-016 1;
	setAttr -k on -cb off ".radi" 0.25;
createNode joint -n "head1_tmpJnt" -p "neck1_tmpJnt";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".uoc" yes;
	setAttr ".oc" 5;
	setAttr ".t" -type "double3" 0 2.2052330826240336 0.20474778041247604 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jot" -type "string" "yxz";
	setAttr ".ssc" no;
	setAttr ".bps" -type "matrix" 1 0 0 0 0 1 0 0 0 0 1 0 0 25.118764441136726 1.5379363139276727e-016 1;
	setAttr -k on -cb off ".radi" 0.25;
createNode joint -n "head2_tmpJnt" -p "head1_tmpJnt";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".uoc" yes;
	setAttr ".oc" 6;
	setAttr ".t" -type "double3" 0 2.7129080904653051 0 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".ssc" no;
	setAttr ".bps" -type "matrix" 1 0 0 0 0 1 0 0 0 0 1 0 0 27.864768711571326 -1.9234515956468954e-015 1;
	setAttr -k on -cb off ".radi" 0.25;
createNode joint -n "eyeLFT_tmpJnt" -p "head1_tmpJnt";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".uoc" yes;
	setAttr ".oc" 6;
	setAttr ".t" -type "double3" 0.53134679794311523 0.70959720341087618 1.4460411141406913 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" -4.1670624195165749e-014 0 0 ;
	setAttr ".ssc" no;
	setAttr ".bps" -type "matrix" 1 0 0 0 0 1 0 0 0 0 1 0 0.53833165295886931 25.828273426804412 1.4860476249829009 1;
	setAttr -k on -cb off ".radi" 0.25;
createNode joint -n "eyeRGT_tmpJnt" -p "head1_tmpJnt";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".uoc" yes;
	setAttr ".oc" 6;
	setAttr ".t" -type "double3" -0.531 0.70959720341087618 1.4460411141406913 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".ssc" no;
	setAttr ".bps" -type "matrix" 1 0 0 0 0 1 0 0 0 0 1 0 -0.53833200000000003 25.828300000000006 1.4860499999999996 1;
	setAttr -k on -cb off ".radi" 0.25;
createNode joint -n "jaw1UPR_tmpJnt" -p "head1_tmpJnt";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".uoc" yes;
	setAttr ".oc" 6;
	setAttr ".t" -type "double3" 0 -0.73126747433220951 0.55021567872571853 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jot" -type "string" "yxz";
	setAttr ".jo" -type "double3" 4.1670624195165749e-014 5.1031796539081984e-030 180 ;
	setAttr ".ssc" no;
	setAttr ".bps" -type "matrix" -1 1.2246467991473532e-016 0 0 -1.2246467991473532e-016 -1 0 0
		 0 0 1 0 0 24.387496966804516 0.55021567872571864 1;
	setAttr -k on -cb off ".radi" 0.25;
createNode joint -n "jaw2UPR_tmpJnt" -p "jaw1UPR_tmpJnt";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".uoc" yes;
	setAttr ".oc" 7;
	setAttr ".t" -type "double3" 3.2163030071266839e-032 0 1.5274370352040776 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".bps" -type "matrix" -1 1.2246467991473532e-016 0 0 -1.2246467991473532e-016 -1 0 0
		 0 0 1 0 -3.2163030071266839e-032 24.387496966804516 2.0776527139297962 1;
	setAttr -k on -cb off ".radi" 0.25;
createNode joint -n "jaw1LWR_tmpJnt" -p "head1_tmpJnt";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".uoc" yes;
	setAttr ".oc" 6;
	setAttr ".t" -type "double3" 0 -0.013698665726888255 0.43032997634803516 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jot" -type "string" "yxz";
	setAttr ".ssc" no;
	setAttr ".bps" -type "matrix" 1 0 0 0 0 1 0 0 0 0 1 0 0 25.105065775409837 0.43032997634803533 1;
	setAttr -k on -cb off ".radi" 0.25;
createNode joint -n "jaw2LWR_tmpJnt" -p "jaw1LWR_tmpJnt";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".uoc" yes;
	setAttr ".oc" 7;
	setAttr ".t" -type "double3" 0 -0.93605513924329387 0.11988570237768331 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jot" -type "string" "yxz";
	setAttr ".ssc" no;
	setAttr ".bps" -type "matrix" 1 0 0 0 0 1 0 0 0 0 1 0 0 24.169010636166544 0.55021567872571864 1;
	setAttr -k on -cb off ".radi" 0.25;
createNode joint -n "jaw3LWR_tmpJnt" -p "jaw2LWR_tmpJnt";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".uoc" yes;
	setAttr ".t" -type "double3" 0 0 1.5274370352040778 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".ssc" no;
	setAttr ".bps" -type "matrix" 1 0 0 0 0 1 0 0 0 0 1 0 0 24.169010636166544 2.0776527139297967 1;
	setAttr -k on -cb off ".radi" 0.25;
createNode joint -n "eye_tmpJnt" -p "head1_tmpJnt";
	setAttr ".t" -type "double3" 0.00017339897155760342 0.70959720341087618 9.961977608014287 ;
	setAttr ".radi" 0.25;
createNode joint -n "eyeTrgtLFT_tmpJnt" -p "eye_tmpJnt";
	setAttr ".t" -type "double3" 0.53117339897155769 1.3286597795314492e-005 0 ;
	setAttr ".radi" 0.25;
createNode joint -n "eyeTrgtRGT_tmpJnt" -p "eye_tmpJnt";
	setAttr ".t" -type "double3" -0.53117339897155769 -1.3286597798867206e-005 0 ;
	setAttr ".radi" 0.25;
createNode joint -n "pelvis_tmpJnt" -p "root_tmpJnt";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".uoc" yes;
	setAttr ".oc" 1;
	setAttr ".t" -type "double3" 0 -0.41864620666000363 -1.3877787807814457e-017 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jot" -type "string" "yxz";
	setAttr ".ssc" no;
	setAttr ".bps" -type "matrix" 1 0 0 0 0 1 0 0 0 0 1 0 0 15.4830611404753 0 1;
	setAttr -k on -cb off ".radi" 0.25;
createNode joint -n "upLegLFT_tmpJnt" -p "pelvis_tmpJnt";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".uoc" yes;
	setAttr ".oc" 2;
	setAttr ".t" -type "double3" 1.4465929924704308 -0.35883737924314651 -0.05916049400752818 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jot" -type "string" "yxz";
	setAttr ".jo" -type "double3" 0 0 -180 ;
	setAttr ".bps" -type "matrix" -1 -1.2246467991473532e-016 0 0 1.2246467991473532e-016 -1 0 0
		 0 0 1 0 1.3486489690923307 14.656585133659888 1.5144370407379352e-017 1;
	setAttr -k on -cb off ".radi" 0.25;
createNode joint -n "lowLegLFT_tmpJnt" -p "upLegLFT_tmpJnt";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".uoc" yes;
	setAttr ".oc" 3;
	setAttr ".t" -type "double3" 8.8817841970012523e-016 6.9522740178170706 0.20072182203671363 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jot" -type "string" "yxz";
	setAttr ".bps" -type "matrix" -1 -1.2246467991473532e-016 0 0 1.2246467991473532e-016 -1 0 0
		 0 0 1 0 1.3486489690923305 7.7535119809750004 0.15259281481888803 1;
	setAttr -k on -cb off ".radi" 0.25;
createNode joint -n "ankleLFT_tmpJnt" -p "lowLegLFT_tmpJnt";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".uoc" yes;
	setAttr ".oc" 4;
	setAttr ".t" -type "double3" 6.6613381477509392e-016 6.7044348909480549 -0.31620128789802227 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jot" -type "string" "yxz";
	setAttr ".bps" -type "matrix" -1 -1.2246467991473532e-016 0 0 1.2246467991473532e-016 -1 0 0
		 0 0 1 0 1.348648969092332 1.0615915425310156 0 1;
	setAttr -k on -cb off ".radi" 0.25;
createNode joint -n "ballLFT_tmpJnt" -p "ankleLFT_tmpJnt";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".uoc" yes;
	setAttr ".oc" 5;
	setAttr ".t" -type "double3" 4.4408920985006262e-016 1.0712502671964508 1.8459647738948022 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jot" -type "string" "yxz";
	setAttr ".jo" -type "double3" 89.999999999999986 0 0 ;
	setAttr ".bps" -type "matrix" -1 -1.2246467991473532e-016 0 0 2.7192621468937821e-032 -2.2204460492503131e-016 1 0
		 -1.2246467991473532e-016 1 2.2204460492503131e-016 0 1.3486489690923311 5.5511151231257827e-015 1.476681409489522 1;
	setAttr -k on -cb off ".radi" 0.25;
createNode joint -n "toeLFT_tmpJnt" -p "ballLFT_tmpJnt";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".uoc" yes;
	setAttr ".oc" 6;
	setAttr ".t" -type "double3" 0 1.565348722578374 3.4757723867481744e-016 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".bps" -type "matrix" -1 -1.2246467991473532e-016 0 0 2.7192621468937821e-032 -2.2204460492503131e-016 1 0
		 -1.2246467991473532e-016 1 2.2204460492503131e-016 0 1.3486489690923309 5.0024078434460801e-015 3.3551152167720435 1;
	setAttr -k on -cb off ".radi" 0.25;
createNode joint -n "footInLFT_tmpJnt" -p "ankleLFT_tmpJnt";
	setAttr ".t" -type "double3" 1.022336296852294 1.0615915425310094 1.4035839081952437 ;
	setAttr ".jo" -type "double3" 0 0 -1.4033418597069752e-014 ;
	setAttr ".radi" 0.25;
createNode joint -n "footOutLFT_tmpJnt" -p "ankleLFT_tmpJnt";
	setAttr ".t" -type "double3" -0.93225006942885824 1.0615915425310154 1.4051603966008885 ;
	setAttr ".jo" -type "double3" 0 0 -1.4033418597069752e-014 ;
	setAttr ".radi" 0.25;
createNode joint -n "heelLFT_tmpJnt" -p "ankleLFT_tmpJnt";
	setAttr ".t" -type "double3" 1.1102230246251565e-015 1.0615915425310101 -1.1652082853112362 ;
	setAttr ".jo" -type "double3" 0 0 -1.4033418597069752e-014 ;
	setAttr ".radi" 0.25;
createNode joint -n "kneeIkLFT_tmpJnt" -p "lowLegLFT_tmpJnt";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".uoc" yes;
	setAttr ".oc" 2;
	setAttr ".t" -type "double3" -8.8817841970012523e-016 0 5 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jot" -type "string" "yxz";
	setAttr ".bps" -type "matrix" -1 -1.2246467991473532e-016 0 0 1.2246467991473532e-016 -1 0 0
		 0 0 1 0 1.3486489690923307 14.656585133659888 1.5144370407379352e-017 1;
	setAttr -k on -cb off ".radi" 0.25;
createNode joint -n "upLegRGT_tmpJnt" -p "pelvis_tmpJnt";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".uoc" yes;
	setAttr ".oc" 2;
	setAttr ".t" -type "double3" -1.44659 -0.35879655520472298 -0.05916049453727025 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jot" -type "string" "yxz";
	setAttr ".jo" -type "double3" 0 180 0 ;
	setAttr ".bps" -type "matrix" -1 -1.2246467991473532e-016 0 0 1.2246467991473532e-016 -1 0 0
		 0 0 1 0 1.3486489690923307 14.656585133659888 1.5144370407379352e-017 1;
	setAttr -k on -cb off ".radi" 0.25;
createNode joint -n "lowLegRGT_tmpJnt" -p "upLegRGT_tmpJnt";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".uoc" yes;
	setAttr ".oc" 3;
	setAttr ".t" -type "double3" 0 -6.95231 -0.20072162999999998 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jot" -type "string" "yxz";
	setAttr ".bps" -type "matrix" -1 -1.2246467991473532e-016 0 0 1.2246467991473532e-016 -1 0 0
		 0 0 1 0 1.3486489690923305 7.7535119809750004 0.15259281481888803 1;
	setAttr -k on -cb off ".radi" 0.25;
createNode joint -n "ankleRGT_tmpJnt" -p "lowLegRGT_tmpJnt";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".uoc" yes;
	setAttr ".oc" 4;
	setAttr ".t" -type "double3" 0 -6.70444 0.31620099999999995 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jot" -type "string" "yxz";
	setAttr ".bps" -type "matrix" -1 -1.2246467991473532e-016 0 0 1.2246467991473532e-016 -1 0 0
		 0 0 1 0 1.348648969092332 1.0615915425310156 0 1;
	setAttr -k on -cb off ".radi" 0.25;
createNode joint -n "ballRGT_tmpJnt" -p "ankleRGT_tmpJnt";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".uoc" yes;
	setAttr ".oc" 5;
	setAttr ".t" -type "double3" -2.2204460492503131e-016 -1.07125 -1.845964 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jot" -type "string" "yxz";
	setAttr ".jo" -type "double3" 89.999999999999986 1.403341859706975e-014 -1.4124500153760508e-030 ;
	setAttr ".bps" -type "matrix" -1 -1.2246467991473532e-016 0 0 2.7192621468937821e-032 -2.2204460492503131e-016 1 0
		 -1.2246467991473532e-016 1 2.2204460492503131e-016 0 1.3486489690923311 5.5511151231257827e-015 1.476681409489522 1;
	setAttr -k on -cb off ".radi" 0.25;
createNode joint -n "toeRGT_tmpJnt" -p "ballRGT_tmpJnt";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".uoc" yes;
	setAttr ".oc" 6;
	setAttr ".t" -type "double3" -2.2204460492503131e-016 -1.5653499999999998 -3.4757752231939771e-016 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".bps" -type "matrix" -1 -1.2246467991473532e-016 0 0 2.7192621468937821e-032 -2.2204460492503131e-016 1 0
		 -1.2246467991473532e-016 1 2.2204460492503131e-016 0 1.3486489690923309 5.0024078434460801e-015 3.3551152167720435 1;
	setAttr -k on -cb off ".radi" 0.25;
createNode joint -n "footInRGT_tmpJnt" -p "ankleRGT_tmpJnt";
	setAttr ".t" -type "double3" -1.0223330000000002 -1.06159128 -1.4035839999999997 ;
	setAttr ".radi" 0.25;
createNode joint -n "footOutRGT_tmpJnt" -p "ankleRGT_tmpJnt";
	setAttr ".t" -type "double3" 0.9322499999999998 -1.06159128 -1.405164 ;
	setAttr ".radi" 0.25;
createNode joint -n "heelRGT_tmpJnt" -p "ankleRGT_tmpJnt";
	setAttr ".t" -type "double3" 2.2204460492503131e-016 -1.06159128 1.165206 ;
	setAttr ".radi" 0.25;
createNode joint -n "kneeIkRGT_tmpJnt" -p "lowLegRGT_tmpJnt";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".uoc" yes;
	setAttr ".oc" 2;
	setAttr ".t" -type "double3" -6.6613381477509392e-016 0 -5.000003 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jot" -type "string" "yxz";
	setAttr ".bps" -type "matrix" -1 -1.2246467991473532e-016 0 0 1.2246467991473532e-016 -1 0 0
		 0 0 1 0 1.3486489690923307 14.656585133659888 1.5144370407379352e-017 1;
	setAttr -k on -cb off ".radi" 0.25;
connectAttr "root_tmpJnt.s" "spine1_tmpJnt.is";
connectAttr "spine1_tmpJnt.s" "spine2_tmpJnt.is";
connectAttr "spine3_tmpJnt.s" "spine4_tmpJnt.is";
connectAttr "spine4_tmpJnt.s" "clavLFT_tmpJnt.is";
connectAttr "clavLFT_tmpJnt.s" "upArmLFT_tmpJnt.is";
connectAttr "upArmLFT_tmpJnt.s" "forearmLFT_tmpJnt.is";
connectAttr "forearmLFT_tmpJnt.s" "wristLFT_tmpJnt.is";
connectAttr "wristLFT_tmpJnt.s" "handLFT_tmpJnt.is";
connectAttr "handLFT_tmpJnt.s" "index1LFT_tmpJnt.is";
connectAttr "index1LFT_tmpJnt.s" "index2LFT_tmpJnt.is";
connectAttr "index2LFT_tmpJnt.s" "index3LFT_tmpJnt.is";
connectAttr "index3LFT_tmpJnt.s" "index4LFT_tmpJnt.is";
connectAttr "index4LFT_tmpJnt.s" "index5LFT_tmpJnt.is";
connectAttr "handLFT_tmpJnt.s" "middle1LFT_tmpJnt.is";
connectAttr "middle1LFT_tmpJnt.s" "middle2LFT_tmpJnt.is";
connectAttr "middle2LFT_tmpJnt.s" "middle3LFT_tmpJnt.is";
connectAttr "middle3LFT_tmpJnt.s" "middle4LFT_tmpJnt.is";
connectAttr "middle4LFT_tmpJnt.s" "middle5LFT_tmpJnt.is";
connectAttr "handLFT_tmpJnt.s" "ring1LFT_tmpJnt.is";
connectAttr "ring1LFT_tmpJnt.s" "ring2LFT_tmpJnt.is";
connectAttr "ring2LFT_tmpJnt.s" "ring3LFT_tmpJnt.is";
connectAttr "ring3LFT_tmpJnt.s" "ring4LFT_tmpJnt.is";
connectAttr "ring4LFT_tmpJnt.s" "ring5LFT_tmpJnt.is";
connectAttr "handLFT_tmpJnt.s" "pinky1LFT_tmpJnt.is";
connectAttr "pinky1LFT_tmpJnt.s" "pinky2LFT_tmpJnt.is";
connectAttr "pinky2LFT_tmpJnt.s" "pinky3LFT_tmpJnt.is";
connectAttr "pinky3LFT_tmpJnt.s" "pinky4LFT_tmpJnt.is";
connectAttr "pinky4LFT_tmpJnt.s" "pinky5LFT_tmpJnt.is";
connectAttr "handLFT_tmpJnt.s" "thumb1LFT_tmpJnt.is";
connectAttr "thumb1LFT_tmpJnt.s" "thumb2LFT_tmpJnt.is";
connectAttr "thumb2LFT_tmpJnt.s" "thumb3LFT_tmpJnt.is";
connectAttr "thumb3LFT_tmpJnt.s" "thumb4LFT_tmpJnt.is";
connectAttr "spine4_tmpJnt.s" "clavRGT_tmpJnt.is";
connectAttr "clavRGT_tmpJnt.s" "upArmRGT_tmpJnt.is";
connectAttr "upArmRGT_tmpJnt.s" "forearmRGT_tmpJnt.is";
connectAttr "forearmRGT_tmpJnt.s" "wristRGT_tmpJnt.is";
connectAttr "wristRGT_tmpJnt.s" "handRGT_tmpJnt.is";
connectAttr "handRGT_tmpJnt.s" "index1RGT_tmpJnt.is";
connectAttr "index1RGT_tmpJnt.s" "index2RGT_tmpJnt.is";
connectAttr "index2RGT_tmpJnt.s" "index3RGT_tmpJnt.is";
connectAttr "index3RGT_tmpJnt.s" "index4RGT_tmpJnt.is";
connectAttr "index4RGT_tmpJnt.s" "index5RGT_tmpJnt.is";
connectAttr "handRGT_tmpJnt.s" "middle1RGT_tmpJnt.is";
connectAttr "middle1RGT_tmpJnt.s" "middle2RGT_tmpJnt.is";
connectAttr "middle2RGT_tmpJnt.s" "middle3RGT_tmpJnt.is";
connectAttr "middle3RGT_tmpJnt.s" "middle4RGT_tmpJnt.is";
connectAttr "middle4RGT_tmpJnt.s" "middle5RGT_tmpJnt.is";
connectAttr "handRGT_tmpJnt.s" "ring1RGT_tmpJnt.is";
connectAttr "ring1RGT_tmpJnt.s" "ring2RGT_tmpJnt.is";
connectAttr "ring2RGT_tmpJnt.s" "ring3RGT_tmpJnt.is";
connectAttr "ring3RGT_tmpJnt.s" "ring4RGT_tmpJnt.is";
connectAttr "ring4RGT_tmpJnt.s" "ring5RGT_tmpJnt.is";
connectAttr "handRGT_tmpJnt.s" "pinky1RGT_tmpJnt.is";
connectAttr "pinky1RGT_tmpJnt.s" "pinky2RGT_tmpJnt.is";
connectAttr "pinky2RGT_tmpJnt.s" "pinky3RGT_tmpJnt.is";
connectAttr "pinky3RGT_tmpJnt.s" "pinky4RGT_tmpJnt.is";
connectAttr "pinky4RGT_tmpJnt.s" "pinky5RGT_tmpJnt.is";
connectAttr "handRGT_tmpJnt.s" "thumb1RGT_tmpJnt.is";
connectAttr "thumb1RGT_tmpJnt.s" "thumb2RGT_tmpJnt.is";
connectAttr "thumb2RGT_tmpJnt.s" "thumb3RGT_tmpJnt.is";
connectAttr "thumb3RGT_tmpJnt.s" "thumb4RGT_tmpJnt.is";
connectAttr "spine4_tmpJnt.s" "neck1_tmpJnt.is";
connectAttr "neck1_tmpJnt.s" "head1_tmpJnt.is";
connectAttr "head1_tmpJnt.s" "head2_tmpJnt.is";
connectAttr "head1_tmpJnt.s" "eyeLFT_tmpJnt.is";
connectAttr "head1_tmpJnt.s" "eyeRGT_tmpJnt.is";
connectAttr "head1_tmpJnt.s" "jaw1UPR_tmpJnt.is";
connectAttr "jaw1UPR_tmpJnt.s" "jaw2UPR_tmpJnt.is";
connectAttr "head1_tmpJnt.s" "jaw1LWR_tmpJnt.is";
connectAttr "jaw1LWR_tmpJnt.s" "jaw2LWR_tmpJnt.is";
connectAttr "jaw2LWR_tmpJnt.s" "jaw3LWR_tmpJnt.is";
connectAttr "head1_tmpJnt.s" "eye_tmpJnt.is";
connectAttr "eye_tmpJnt.s" "eyeTrgtLFT_tmpJnt.is";
connectAttr "eye_tmpJnt.s" "eyeTrgtRGT_tmpJnt.is";
connectAttr "root_tmpJnt.s" "pelvis_tmpJnt.is";
connectAttr "pelvis_tmpJnt.s" "upLegLFT_tmpJnt.is";
connectAttr "upLegLFT_tmpJnt.s" "lowLegLFT_tmpJnt.is";
connectAttr "lowLegLFT_tmpJnt.s" "ankleLFT_tmpJnt.is";
connectAttr "ballLFT_tmpJnt.s" "toeLFT_tmpJnt.is";
connectAttr "ankleLFT_tmpJnt.s" "footInLFT_tmpJnt.is";
connectAttr "ankleLFT_tmpJnt.s" "footOutLFT_tmpJnt.is";
connectAttr "ankleLFT_tmpJnt.s" "heelLFT_tmpJnt.is";
connectAttr "lowLegLFT_tmpJnt.s" "kneeIkLFT_tmpJnt.is";
connectAttr "pelvis_tmpJnt.s" "upLegRGT_tmpJnt.is";
connectAttr "upLegRGT_tmpJnt.s" "lowLegRGT_tmpJnt.is";
connectAttr "lowLegRGT_tmpJnt.s" "ankleRGT_tmpJnt.is";
connectAttr "ballRGT_tmpJnt.s" "toeRGT_tmpJnt.is";
connectAttr "ankleRGT_tmpJnt.s" "footInRGT_tmpJnt.is";
connectAttr "ankleRGT_tmpJnt.s" "footOutRGT_tmpJnt.is";
connectAttr "ankleRGT_tmpJnt.s" "heelRGT_tmpJnt.is";
connectAttr "lowLegRGT_tmpJnt.s" "kneeIkRGT_tmpJnt.is";

// End of tmpJnt_2.ma
