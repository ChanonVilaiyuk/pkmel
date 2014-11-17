//Maya ASCII 2012 scene
//Name: tmpJnt_3.ma
//Last modified: Sat, Dec 14, 2013 02:24:15 PM
//Codeset: 1252
requires maya "2012";
currentUnit -l centimeter -a degree -t film;
fileInfo "application" "maya";
fileInfo "product" "Maya 2012";
fileInfo "version" "2012 x64";
fileInfo "cutIdentifier" "201201172029-821146";
fileInfo "osv" "Microsoft Windows 7 Ultimate Edition, 64-bit Windows 7 Service Pack 1 (Build 7601)\n";
createNode transform -s -n "persp";
	setAttr ".v" no;
	setAttr ".t" -type "double3" 186.15197386928679 332.0341646260714 104.43481057504142 ;
	setAttr ".r" -type "double3" -33.938352729906448 56.599999999999582 2.8888882479089059e-015 ;
createNode camera -s -n "perspShape" -p "persp";
	setAttr -k off ".v" no;
	setAttr ".fl" 34.999999999999986;
	setAttr ".coi" 283.35687943027011;
	setAttr ".imn" -type "string" "persp";
	setAttr ".den" -type "string" "persp_depth";
	setAttr ".man" -type "string" "persp_mask";
	setAttr ".tp" -type "double3" 52.809104106248171 138.08254839774656 -19.744340790556244 ;
	setAttr ".hc" -type "string" "viewSet -p %camera";
createNode transform -s -n "top";
	setAttr ".v" no;
	setAttr ".t" -type "double3" 54.135907630128855 204.69151289319464 -5.2545486996621333 ;
	setAttr ".r" -type "double3" -89.999999999999986 0 0 ;
createNode camera -s -n "topShape" -p "top";
	setAttr -k off ".v" no;
	setAttr ".rnd" no;
	setAttr ".coi" 100.1;
	setAttr ".ow" 246.51246573288051;
	setAttr ".imn" -type "string" "top";
	setAttr ".den" -type "string" "top_depth";
	setAttr ".man" -type "string" "top_mask";
	setAttr ".hc" -type "string" "viewSet -t %camera";
	setAttr ".o" yes;
createNode transform -s -n "front";
	setAttr ".v" no;
	setAttr ".t" -type "double3" -1.9331925602166007 237.41421681372321 444.23182000780548 ;
createNode camera -s -n "frontShape" -p "front";
	setAttr -k off ".v" no;
	setAttr ".rnd" no;
	setAttr ".coi" 100.1;
	setAttr ".ow" 108.21048560626565;
	setAttr ".imn" -type "string" "front";
	setAttr ".den" -type "string" "front_depth";
	setAttr ".man" -type "string" "front_mask";
	setAttr ".hc" -type "string" "viewSet -f %camera";
	setAttr ".o" yes;
createNode transform -s -n "side";
	setAttr ".v" no;
	setAttr ".t" -type "double3" 270.98389163595147 173.71196684712496 3.3518764279859101 ;
	setAttr ".r" -type "double3" 0 89.999999999999986 0 ;
createNode camera -s -n "sideShape" -p "side";
	setAttr -k off ".v" no;
	setAttr ".rnd" no;
	setAttr ".coi" 100.1;
	setAttr ".ow" 171.2397598688531;
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
		0 0 -75.061480697744486
		29.158425996790644 0 -43.363455818411595
		17.49504875242533 0 -43.363455818411595
		17.49504875242533 0 -21.681745023328407
		21.681745023328407 0 -17.49504875242533
		43.363455818411595 0 -17.49504875242533
		43.363455818411595 0 -29.158425996790644
		75.061480697744486 0 0
		43.363455818411595 0 29.158425996790644
		43.363455818411595 0 17.49504875242533
		21.681745023328407 0 17.49504875242533
		17.49504875242533 0 21.681745023328407
		17.49504875242533 0 43.363455818411595
		29.158425996790644 0 43.363455818411595
		0 0 75.061480697744486
		-29.158425996790644 0 43.363455818411595
		-17.49504875242533 0 43.363455818411595
		-17.49504875242533 0 21.681745023328407
		-21.681745023328407 0 17.49504875242533
		-43.363455818411595 0 17.49504875242533
		-43.363455818411595 0 29.158425996790644
		-75.061480697744486 0 0
		-43.363455818411595 0 -29.158425996790644
		-43.363455818411595 0 -17.49504875242533
		-21.681745023328407 0 -17.49504875242533
		-17.49504875242533 0 -21.681745023328407
		-17.49504875242533 0 -43.363455818411595
		-29.158425996790644 0 -43.363455818411595
		0 0 -75.061480697744486
		;
createNode joint -n "root_tmpJnt" -p "placement_tmpCtrl";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".t" -type "double3" 0 131.53786930564431 -6.4206670408197333 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jot" -type "string" "yxz";
	setAttr ".bps" -type "matrix" 1 0 0 0 0 1 0 0 0 0 1 0 0 15.73707328056101 0 1;
	setAttr -k on -cb off ".radi" 0.5;
createNode joint -n "spine1_tmpJnt" -p "root_tmpJnt";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".oc" 1;
	setAttr ".t" -type "double3" 0 4.2464115497985233 -4.3510530093184645 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jot" -type "string" "yxz";
	setAttr ".bps" -type "matrix" 1 0 0 0 0 1 0 0 0 0 1 0 0 16.462721689908392 7.9790056857053538e-017 1;
	setAttr -k on -cb off ".radi" 0.5;
createNode joint -n "spine2_tmpJnt" -p "spine1_tmpJnt";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".oc" 2;
	setAttr ".t" -type "double3" 0 15.094825175122111 2.748033479569588 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jot" -type "string" "yxz";
	setAttr ".bps" -type "matrix" 1 0 0 0 0 1 0 0 0 0 1 0 0 18.962119031422834 1.1092698799812162e-016 1;
	setAttr -k on -cb off ".radi" 0.5;
createNode joint -n "spine3_tmpJnt" -p "spine2_tmpJnt";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".oc" 1;
	setAttr ".t" -type "double3" 0 13.001693545291488 2.2204460492503131e-016 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jot" -type "string" "yxz";
	setAttr ".bps" -type "matrix" 1 0 0 0 0 1 0 0 0 0 1 0 0 16.462721689908392 7.9790056857053538e-017 1;
	setAttr -k on -cb off ".radi" 0.5;
createNode joint -n "spine4_tmpJnt" -p "spine3_tmpJnt";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".oc" 1;
	setAttr ".t" -type "double3" 0 29.491082300780903 0 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jot" -type "string" "yxz";
	setAttr ".bps" -type "matrix" 1 0 0 0 0 1 0 0 0 0 1 0 0 16.462721689908392 7.9790056857053538e-017 1;
	setAttr -k on -cb off ".radi" 0.5;
createNode joint -n "neck1_tmpJnt" -p "spine4_tmpJnt";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".oc" 3;
	setAttr ".t" -type "double3" 0 12.888620025236179 -0.45800557992827273 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jot" -type "string" "yxz";
	setAttr ".bps" -type "matrix" 1 0 0 0 0 1 0 0 0 0 1 0 0 22.764810214551506 1.2852494451027699e-016 1;
	setAttr -k on -cb off ".radi" 0.5;
createNode joint -n "head1_tmpJnt" -p "neck1_tmpJnt";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".oc" 5;
	setAttr ".t" -type "double3" 0 23.832317846750357 5.3681309458082715 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jot" -type "string" "yxz";
	setAttr ".bps" -type "matrix" 1 0 0 0 0 1 0 0 0 0 1 0 0 25.118764441136726 1.5379363139276727e-016 1;
	setAttr -k on -cb off ".radi" 0.5;
createNode joint -n "head2_tmpJnt" -p "head1_tmpJnt";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".oc" 6;
	setAttr ".t" -type "double3" 0 18.724199386379894 0 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".bps" -type "matrix" 1 0 0 0 0 1 0 0 0 0 1 0 0 27.864768711571326 -1.9234515956468954e-015 1;
	setAttr -k on -cb off ".radi" 0.5;
createNode joint -n "eyeLFT_tmpJnt" -p "head1_tmpJnt";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".oc" 6;
	setAttr ".t" -type "double3" 4.412286208157842 3.3225283165901942 13.492111861117575 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".bps" -type "matrix" 1 0 0 0 0 1 0 0 0 0 1 0 0.53833165295886931 25.828273426804412 1.4860476249829009 1;
	setAttr -k on -cb off ".radi" 0.5;
createNode joint -n "eyeRGT_tmpJnt" -p "head1_tmpJnt";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".oc" 6;
	setAttr ".t" -type "double3" -4.412000791842158 3.3225283165901942 13.492111861117575 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".bps" -type "matrix" 1 0 0 0 0 1 0 0 0 0 1 0 -0.53833200000000003 25.828300000000006 1.4860499999999996 1;
	setAttr -k on -cb off ".radi" 0.5;
createNode joint -n "jaw1UPR_tmpJnt" -p "head1_tmpJnt";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".oc" 6;
	setAttr ".t" -type "double3" 0 -3.2581377705621435 16.123145903402438 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jot" -type "string" "yxz";
	setAttr ".jo" -type "double3" 0 0 180 ;
	setAttr ".bps" -type "matrix" -1 1.2246467991473532e-016 0 0 -1.2246467991473532e-016 -1 0 0
		 0 0 1 0 0 24.387496966804516 0.55021567872571864 1;
	setAttr -k on -cb off ".radi" 0.5;
createNode joint -n "jaw2UPR_tmpJnt" -p "jaw1UPR_tmpJnt";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".oc" 7;
	setAttr ".t" -type "double3" 0 2.8421709430404007e-014 2.4535995728020303 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".bps" -type "matrix" -1 1.2246467991473532e-016 0 0 -1.2246467991473532e-016 -1 0 0
		 0 0 1 0 -3.2163030071266839e-032 24.387496966804516 2.0776527139297962 1;
	setAttr -k on -cb off ".radi" 0.5;
createNode joint -n "jaw1LWR_tmpJnt" -p "head1_tmpJnt";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".oc" 6;
	setAttr ".t" -type "double3" 0 -1.076662022458919 5.0589793462619328 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jot" -type "string" "yxz";
	setAttr ".bps" -type "matrix" 1 0 0 0 0 1 0 0 0 0 1 0 0 25.105065775409837 0.43032997634803533 1;
	setAttr -k on -cb off ".radi" 0.5;
createNode joint -n "jaw2LWR_tmpJnt" -p "jaw1LWR_tmpJnt";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".oc" 7;
	setAttr ".t" -type "double3" 0 -6.5511692948412019 9.6940775491334374 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jot" -type "string" "yxz";
	setAttr ".bps" -type "matrix" 1 0 0 0 0 1 0 0 0 0 1 0 0 24.169010636166544 0.55021567872571864 1;
	setAttr -k on -cb off ".radi" 0.5;
createNode joint -n "jaw3LWR_tmpJnt" -p "jaw2LWR_tmpJnt";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".t" -type "double3" 0 0 2.7318812587611543 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".bps" -type "matrix" 1 0 0 0 0 1 0 0 0 0 1 0 0 24.169010636166544 2.0776527139297967 1;
	setAttr -k on -cb off ".radi" 0.5;
createNode joint -n "eye_tmpJnt" -p "head1_tmpJnt";
	setAttr ".t" -type "double3" 0.00014270815784200863 3.3225283165901089 45.628830666962457 ;
	setAttr ".radi" 0.5;
createNode joint -n "eyeTrgtLFT_tmpJnt" -p "eye_tmpJnt";
	setAttr ".t" -type "double3" 4.4121435 0 0 ;
	setAttr ".radi" 0.5;
createNode joint -n "eyeTrgtRGT_tmpJnt" -p "eye_tmpJnt";
	setAttr ".t" -type "double3" -4.4121435 0 0 ;
	setAttr ".radi" 0.5;
createNode joint -n "clavLFT_tmpJnt" -p "spine4_tmpJnt";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".oc" 3;
	setAttr ".ove" yes;
	setAttr ".t" -type "double3" 3.1555620376668276 6.3367149233849318 9.3722897501524773 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jot" -type "string" "yxz";
	setAttr ".jo" -type "double3" 0 0 -89.999999999999986 ;
	setAttr ".bps" -type "matrix" 2.2204460492503131e-016 -1 0 0 1 2.2204460492503131e-016 0 0
		 0 0 1 0 0.40396301701286447 22.628380391977608 0.93191360083425789 1;
	setAttr -k on -cb off ".radi" 0.5;
createNode joint -n "upArmLFT_tmpJnt" -p "clavLFT_tmpJnt";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".oc" 4;
	setAttr ".t" -type "double3" 0.51311781940783951 31.183957751276001 -7.747881624695161 ;
	setAttr ".ro" 4;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jot" -type "string" "yxz";
	setAttr ".jo" -type "double3" 0 0 -60.256087290344929 ;
	setAttr ".bps" -type "matrix" 2.2204460492503131e-016 -1 0 0 1 2.2204460492503131e-016 0 0
		 0 0 1 0 2.6840862727483024 21.950819439051291 -0.34347723857962076 1;
	setAttr -k on -cb off ".radi" 0.5;
createNode joint -n "forearmLFT_tmpJnt" -p "upArmLFT_tmpJnt";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".oc" 5;
	setAttr ".t" -type "double3" -3.1263880373444408e-013 48.137623052556862 -3.5544063246902251 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jot" -type "string" "yxz";
	setAttr ".jo" -type "double3" 0 0 9.5416640443905503e-015 ;
	setAttr ".bps" -type "matrix" 2.2204460492503131e-016 -1 0 0 0.99999999999946088 2.220446049249116e-016 -1.0384142298428127e-006 0
		 1.0384142298428127e-006 2.3057427741397801e-022 0.99999999999946088 0 6.7891781465089913 21.950819439060187 -0.42637972484178432 1;
	setAttr -k on -cb off ".radi" 0.5;
createNode joint -n "elbowIkLFT_tmpJnt" -p "forearmLFT_tmpJnt";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".oc" 2;
	setAttr ".t" -type "double3" -4.594744869623552e-005 2.8421709430404007e-014 -44.247707160185328 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jot" -type "string" "yxz";
	setAttr ".jo" -type "double3" 0 5.9496752756331688e-005 0 ;
	setAttr ".bps" -type "matrix" -1 -1.2246467991473532e-016 0 0 1.2246467991473532e-016 -1 0 0
		 0 0 1 0 1.3486489690923307 14.656585133659888 1.5144370407379352e-017 1;
	setAttr -k on -cb off ".radi" 0.5;
createNode joint -n "wristLFT_tmpJnt" -p "forearmLFT_tmpJnt";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".oc" 6;
	setAttr ".t" -type "double3" -1.8405899027129635e-010 43.016822054004294 3.5544063246902251 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jot" -type "string" "yxz";
	setAttr ".bps" -type "matrix" 2.2204460492503131e-016 -1 0 0 1 2.2204460492503131e-016 8.3960588285190204e-014 0
		 -8.3960588285190204e-014 -1.8642995655058271e-029 1 0 11.145136555499452 21.950819439088733 -0.34347297829513029 1;
	setAttr -k on -cb off ".radi" 0.5;
createNode joint -n "handLFT_tmpJnt" -p "wristLFT_tmpJnt";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".oc" 7;
	setAttr ".t" -type "double3" -4.7009507397888228e-011 15.668991870597274 -6.9622377001365976e-006 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".bps" -type "matrix" 2.2204460492503131e-016 -1 0 0 1 2.2204460492503131e-016 8.3960588285190204e-014 0
		 -8.3960588285190204e-014 -1.8642995655058271e-029 1 0 11.94334900537585 21.950819439093973 -0.34347375639834526 1;
	setAttr -k on -cb off ".radi" 0.5;
createNode joint -n "thumb1LFT_tmpJnt" -p "handLFT_tmpJnt";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".t" -type "double3" 4.3060097990622808 -8.176297544096947 7.6676818136191986 ;
	setAttr ".r" -type "double3" 29.82992934827168 -22.43886925947923 -54.610386034323412 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jot" -type "string" "yxz";
	setAttr ".jo" -type "double3" 1.7315079359008299 0 -9.4898210030826931e-011 ;
	setAttr ".bps" -type "matrix" -0.59548586752167076 -0.80336578317847407 -4.9997343752636337e-014 0
		 0.73868319246536318 -0.54754062333671982 0.39312390790336815 0 -0.31582229615899904 0.23409973134130962 0.91948550452673483 0
		 11.518645340649305 21.905429719636764 0.32567524419271171 1;
	setAttr -k on -cb off ".radi" 0.5;
createNode joint -n "thumb2LFT_tmpJnt" -p "thumb1LFT_tmpJnt";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".oc" 1;
	setAttr ".t" -type "double3" -0.033150250360044708 3.4518260054233565 4.598701061205972 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jot" -type "string" "yxz";
	setAttr ".jo" -type "double3" 6.3611093629270304e-015 6.3611093629270304e-015 -3.1805546814635152e-015 ;
	setAttr ".bps" -type "matrix" -0.59548586752167076 -0.80336578317847407 -4.9997343752636337e-014 0
		 0.73868319246536318 -0.54754062333671982 0.39312390790336815 0 -0.31582229615899904 0.23409973134130962 0.91948550452673483 0
		 12.026286103962779 21.529146703032435 0.59583939943602238 1;
	setAttr -k on -cb off ".radi" 0.5;
createNode joint -n "thumb3LFT_tmpJnt" -p "thumb2LFT_tmpJnt";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".oc" 2;
	setAttr ".t" -type "double3" 7.1054273576010019e-015 8.3264097460236854 6.3948846218409017e-014 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jot" -type "string" "yxz";
	setAttr ".bps" -type "matrix" -0.59548586752167076 -0.80336578317847407 -4.9997343752636337e-014 0
		 0.73868319246536318 -0.54754062333671982 0.39312390790336815 0 -0.31582229615899904 0.23409973134130962 0.91948550452673483 0
		 12.724953059079672 21.011267666374362 0.96766684389406166 1;
	setAttr -k on -cb off ".radi" 0.5;
createNode joint -n "thumb4LFT_tmpJnt" -p "thumb3LFT_tmpJnt";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".oc" 3;
	setAttr ".t" -type "double3" -6.7501559897209518e-014 8.0300159890467739 -4.2632564145606011e-014 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".bps" -type "matrix" -0.59548586752167076 -0.80336578317847407 -4.9997343752636337e-014 0
		 0.73868319246536318 -0.54754062333671982 0.39312390790336815 0 -0.31582229615899904 0.23409973134130962 0.91948550452673483 0
		 13.320225968832865 20.570028305053697 1.2844684375111461 1;
	setAttr -k on -cb off ".radi" 0.5;
createNode joint -n "index1LFT_tmpJnt" -p "handLFT_tmpJnt";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".t" -type "double3" -1.7040437948290048 -8.9857927170791214 8.2172190811360402 ;
	setAttr ".r" -type "double3" 89.99999999993301 -85.861080851320125 -89.99999999993311 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jot" -type "string" "yxz";
	setAttr ".jo" -type "double3" 1.7315079359008299 0 -9.4898210030826931e-011 ;
	setAttr ".bps" -type "matrix" -8.3960588285190191e-014 -8.437694987151191e-014 1 0
		 1 2.2204460492503131e-016 8.3960588285190204e-014 0 -2.2204460493211562e-016 1 8.4376949871511897e-014 0
		 11.915961054098767 22.155901831531715 0.36968006095532863 1;
	setAttr -k on -cb off ".radi" 0.5;
createNode joint -n "index2LFT_tmpJnt" -p "index1LFT_tmpJnt";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".oc" 1;
	setAttr ".t" -type "double3" 6.6435745793569367e-013 13.410955098179812 0.43834823339980744 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jot" -type "string" "yxz";
	setAttr ".bps" -type "matrix" -8.3960588285190191e-014 -8.437694987151191e-014 1 0
		 1 2.2204460492503131e-016 8.3960588285190204e-014 0 -2.2204460493211562e-016 1 8.4376949871511897e-014 0
		 13.114219270621863 22.155901831531715 0.36968006095542938 1;
	setAttr -k on -cb off ".radi" 0.5;
createNode joint -n "index3LFT_tmpJnt" -p "index2LFT_tmpJnt";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".oc" 2;
	setAttr ".t" -type "double3" 1.7763568394002505e-015 8.1330392340700328 0 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jot" -type "string" "yxz";
	setAttr ".bps" -type "matrix" -8.3960588285190191e-014 -8.437694987151191e-014 1 0
		 1 2.2204460492503131e-016 8.3960588285190204e-014 0 -2.2204460493211562e-016 1 8.4376949871511897e-014 0
		 13.805785441300909 22.155901831531718 0.3696800609554875 1;
	setAttr -k on -cb off ".radi" 0.5;
createNode joint -n "index4LFT_tmpJnt" -p "index3LFT_tmpJnt";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".oc" 3;
	setAttr ".t" -type "double3" -2.6645352591003757e-015 5.2324469242788361 -0.611814486601304 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jot" -type "string" "yxz";
	setAttr ".bps" -type "matrix" -8.3960588285190191e-014 -8.437694987151191e-014 1 0
		 1 2.2204460492503131e-016 8.3960588285190204e-014 0 -2.2204460493211562e-016 1 8.4376949871511897e-014 0
		 14.271394348292739 22.155901831531718 0.36968006095552658 1;
	setAttr -k on -cb off ".radi" 0.5;
createNode joint -n "index5LFT_tmpJnt" -p "index4LFT_tmpJnt";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".oc" 4;
	setAttr ".t" -type "double3" 2.6645352591003757e-015 5.6900180626550778 -2.8421709430404007e-014 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".bps" -type "matrix" -8.3960588285190191e-014 -8.437694987151191e-014 1 0
		 1 2.2204460492503131e-016 8.3960588285190204e-014 0 -2.2204460493211562e-016 1 8.4376949871511897e-014 0
		 14.812322343180313 22.155901831531722 0.36968006095557193 1;
	setAttr -k on -cb off ".radi" 0.5;
createNode joint -n "middle1LFT_tmpJnt" -p "handLFT_tmpJnt";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".t" -type "double3" -2.2932684104245027 -10.027582728451385 3.0747069340087676 ;
	setAttr ".r" -type "double3" 2.9509382362211799e-016 -89.999999999995168 0 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jot" -type "string" "yxz";
	setAttr ".jo" -type "double3" 1.7315079359008299 0 -9.4898210030826931e-011 ;
	setAttr ".bps" -type "matrix" -8.3960588285190191e-014 -8.437694987151191e-014 1 0
		 1 2.2204460492503131e-016 8.3960588285190204e-014 0 -2.2204460493211562e-016 1 8.4376949871511897e-014 0
		 11.876633548480955 22.169748485139639 -0.10080869585328409 1;
	setAttr -k on -cb off ".radi" 0.5;
createNode joint -n "middle2LFT_tmpJnt" -p "middle1LFT_tmpJnt";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".oc" 1;
	setAttr ".t" -type "double3" 6.6968652845389443e-013 14.443157116598059 -5.6843418860808015e-014 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jot" -type "string" "yxz";
	setAttr ".bps" -type "matrix" -8.3960588285190191e-014 -8.437694987151191e-014 1 0
		 1 2.2204460492503131e-016 8.3960588285190204e-014 0 -2.2204460493211562e-016 1 8.4376949871511897e-014 0
		 13.108601055533605 22.169748485139639 -0.10080869585318036 1;
	setAttr -k on -cb off ".radi" 0.5;
createNode joint -n "middle3LFT_tmpJnt" -p "middle2LFT_tmpJnt";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".oc" 2;
	setAttr ".t" -type "double3" 6.6613381477509392e-016 9.2163201458935191 -0.39209217718965306 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jot" -type "string" "yxz";
	setAttr ".bps" -type "matrix" -8.3960588285190191e-014 -8.437694987151191e-014 1 0
		 1 2.2204460492503131e-016 8.3960588285190204e-014 0 -2.2204460493211562e-016 1 8.4376949871511897e-014 0
		 13.906913312889571 22.169748485139639 -0.10080869585311319 1;
	setAttr -k on -cb off ".radi" 0.5;
createNode joint -n "middle4LFT_tmpJnt" -p "middle3LFT_tmpJnt";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".oc" 3;
	setAttr ".t" -type "double3" 1.7763568394002505e-015 5.9722812343420912 -0.44331851583089588 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jot" -type "string" "yxz";
	setAttr ".bps" -type "matrix" -8.3960588285190191e-014 -8.437694987151191e-014 1 0
		 1 2.2204460492503131e-016 8.3960588285190204e-014 0 -2.2204460493211562e-016 1 8.4376949871511897e-014 0
		 14.411849725499213 22.169748485139639 -0.10080869585307067 1;
	setAttr -k on -cb off ".radi" 0.5;
createNode joint -n "middle5LFT_tmpJnt" -p "middle4LFT_tmpJnt";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".oc" 4;
	setAttr ".t" -type "double3" 4.4408920985006262e-016 6.4373939722224272 2.8421709430404007e-014 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".bps" -type "matrix" -8.3960588285190191e-014 -8.437694987151191e-014 1 0
		 1 2.2204460492503131e-016 8.3960588285190204e-014 0 -2.2204460493211562e-016 1 8.4376949871511897e-014 0
		 15.081996667416741 22.169748485139635 -0.10080869585301426 1;
	setAttr -k on -cb off ".radi" 0.5;
createNode joint -n "ring1LFT_tmpJnt" -p "handLFT_tmpJnt";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".t" -type "double3" -2.2948756136636916 -10.144412008638106 -1.613452492813205 ;
	setAttr ".r" -type "double3" -89.999999999947804 -84.700386817738419 89.999999999948017 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jot" -type "string" "yxz";
	setAttr ".jo" -type "double3" 1.7315079359008299 0 -9.4898210030826931e-011 ;
	setAttr ".bps" -type "matrix" -8.3960588285190191e-014 -8.437694987151191e-014 1 0
		 1 2.2204460492503131e-016 8.3960588285190204e-014 0 -2.2204460493211562e-016 1 8.4376949871511897e-014 0
		 11.876633548480955 22.13656260093245 -0.5683912766476541 1;
	setAttr -k on -cb off ".radi" 0.5;
createNode joint -n "ring2LFT_tmpJnt" -p "ring1LFT_tmpJnt";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".oc" 1;
	setAttr ".t" -type "double3" 6.7501559897209518e-013 14.066511192182652 2.8421709430404007e-014 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jot" -type "string" "yxz";
	setAttr ".bps" -type "matrix" -8.3960588285190191e-014 -8.437694987151191e-014 1 0
		 1 2.2204460492503131e-016 8.3960588285190204e-014 0 -2.2204460493211562e-016 1 8.4376949871511897e-014 0
		 13.097480078235414 22.13656260093245 -0.56839127664755129 1;
	setAttr -k on -cb off ".radi" 0.5;
createNode joint -n "ring3LFT_tmpJnt" -p "ring2LFT_tmpJnt";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".oc" 2;
	setAttr ".t" -type "double3" 3.5527136788005009e-015 8.9124476780162354 -0.40901000956944245 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jot" -type "string" "yxz";
	setAttr ".bps" -type "matrix" -8.3960588285190191e-014 -8.437694987151191e-014 1 0
		 1 2.2204460492503131e-016 8.3960588285190204e-014 0 -2.2204460493211562e-016 1 8.4376949871511897e-014 0
		 13.845747937749518 22.136562600932457 -0.56839127664748834 1;
	setAttr -k on -cb off ".radi" 0.5;
createNode joint -n "ring4LFT_tmpJnt" -p "ring3LFT_tmpJnt";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".oc" 3;
	setAttr ".t" -type "double3" 7.1054273576010019e-015 5.6875683986997956 -0.52267946472153426 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jot" -type "string" "yxz";
	setAttr ".bps" -type "matrix" -8.3960588285190191e-014 -8.437694987151191e-014 1 0
		 1 2.2204460492503131e-016 8.3960588285190204e-014 0 -2.2204460493211562e-016 1 8.4376949871511897e-014 0
		 14.345123861710062 22.136562600932454 -0.56839127664744615 1;
	setAttr -k on -cb off ".radi" 0.5;
createNode joint -n "ring5LFT_tmpJnt" -p "ring4LFT_tmpJnt";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".oc" 4;
	setAttr ".t" -type "double3" 5.3290705182007514e-015 6.0257708161884409 0 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".bps" -type "matrix" -8.3960588285190191e-014 -8.437694987151191e-014 1 0
		 1 2.2204460492503131e-016 8.3960588285190204e-014 0 -2.2204460493211562e-016 1 8.4376949871511897e-014 0
		 14.876258587400191 22.136562600932457 -0.56839127664740152 1;
	setAttr -k on -cb off ".radi" 0.5;
createNode joint -n "pinky1LFT_tmpJnt" -p "handLFT_tmpJnt";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".t" -type "double3" -1.6298107927442516 -9.3467397248491935 -6.8163900944860396 ;
	setAttr ".r" -type "double3" -89.999999999969219 -80.961428166628806 89.999999999969603 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jot" -type "string" "yxz";
	setAttr ".jo" -type "double3" 1.7315079359008299 0 -9.4898210030826931e-011 ;
	setAttr ".bps" -type "matrix" -8.3960588285190191e-014 -8.437694987151191e-014 1 0
		 1 2.2204460492503131e-016 8.3960588285190204e-014 0 -2.2204460493211562e-016 1 8.4376949871511897e-014 0
		 11.876633548480955 22.020988418911262 -0.95907086085240945 1;
	setAttr -k on -cb off ".radi" 0.5;
createNode joint -n "pinky2LFT_tmpJnt" -p "pinky1LFT_tmpJnt";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".oc" 1;
	setAttr ".t" -type "double3" 6.6791017161449417e-013 11.374903164681356 1.1368683772161603e-013 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jot" -type "string" "yxz";
	setAttr ".bps" -type "matrix" -8.3960588285190191e-014 -8.437694987151191e-014 1 0
		 1 2.2204460492503131e-016 8.3960588285190204e-014 0 -2.2204460493211562e-016 1 8.4376949871511897e-014 0
		 13.083100380346423 22.020988418911262 -0.95907086085230775 1;
	setAttr -k on -cb off ".radi" 0.5;
createNode joint -n "pinky3LFT_tmpJnt" -p "pinky2LFT_tmpJnt";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".oc" 2;
	setAttr ".t" -type "double3" 0 7.8797944686734454 0 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jot" -type "string" "yxz";
	setAttr ".bps" -type "matrix" -8.3960588285190191e-014 -8.437694987151191e-014 1 0
		 1 2.2204460492503131e-016 8.3960588285190204e-014 0 -2.2204460493211562e-016 1 8.4376949871511897e-014 0
		 13.601293073636691 22.020988418911262 -0.95907086085226423 1;
	setAttr -k on -cb off ".radi" 0.5;
createNode joint -n "pinky4LFT_tmpJnt" -p "pinky3LFT_tmpJnt";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".oc" 3;
	setAttr ".t" -type "double3" 0 4.8300719434212169 -0.69350724067240321 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jot" -type "string" "yxz";
	setAttr ".bps" -type "matrix" -8.3960588285190191e-014 -8.437694987151191e-014 1 0
		 1 2.2204460492503131e-016 8.3960588285190204e-014 0 -2.2204460493211562e-016 1 8.4376949871511897e-014 0
		 13.978441565540829 22.020988418911262 -0.95907086085223248 1;
	setAttr -k on -cb off ".radi" 0.5;
createNode joint -n "pinky5LFT_tmpJnt" -p "pinky4LFT_tmpJnt";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".oc" 4;
	setAttr ".t" -type "double3" 3.5527136788005009e-015 5.1778438480077682 2.8421709430404007e-014 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".bps" -type "matrix" -8.3960588285190191e-014 -8.437694987151191e-014 1 0
		 1 2.2204460492503131e-016 8.3960588285190204e-014 0 -2.2204460493211562e-016 1 8.4376949871511897e-014 0
		 14.437677801786013 22.020988418911262 -0.95907086085219373 1;
	setAttr -k on -cb off ".radi" 0.5;
createNode joint -n "clavRGT_tmpJnt" -p "spine4_tmpJnt";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".oc" 3;
	setAttr ".ove" yes;
	setAttr ".t" -type "double3" -3.15556 6.3371181233626714 9.37228657056861 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jot" -type "string" "yxz";
	setAttr ".jo" -type "double3" -180 7.0622500768802494e-031 89.999999999999972 ;
	setAttr ".bps" -type "matrix" 2.2204460492503131e-016 -1 0 0 1 2.2204460492503131e-016 0 0
		 0 0 1 0 0.40396301701286447 22.628380391977608 0.93191360083425789 1;
	setAttr -k on -cb off ".radi" 0.5;
createNode joint -n "upArmRGT_tmpJnt" -p "clavRGT_tmpJnt";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".oc" 4;
	setAttr ".t" -type "double3" -0.51400000000003843 -31.183939999999996 7.7478800000000039 ;
	setAttr ".ro" 4;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jot" -type "string" "yxz";
	setAttr ".jo" -type "double3" 3.5355495859311147e-015 -6.0922685787389807e-015 -60.256087290344951 ;
	setAttr ".bps" -type "matrix" 2.2204460492503131e-016 -1 0 0 1 2.2204460492503131e-016 0 0
		 0 0 1 0 2.6840862727483024 21.950819439051291 -0.34347723857962076 1;
	setAttr -k on -cb off ".radi" 0.5;
createNode joint -n "forearmRGT_tmpJnt" -p "upArmRGT_tmpJnt";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".oc" 5;
	setAttr ".t" -type "double3" 0.00033002503673174033 -48.137161093910407 3.5544000000000029 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jot" -type "string" "yxz";
	setAttr ".bps" -type "matrix" 2.2204460492503131e-016 -1 0 0 0.99999999999946088 2.220446049249116e-016 -1.0384142298428127e-006 0
		 1.0384142298428127e-006 2.3057427741397801e-022 0.99999999999946088 0 6.7891781465089913 21.950819439060187 -0.42637972484178432 1;
	setAttr -k on -cb off ".radi" 0.5;
createNode joint -n "elbowIkRGT_tmpJnt" -p "forearmRGT_tmpJnt";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".oc" 2;
	setAttr ".t" -type "double3" -2.8421709430404007e-014 1.4210854715202004e-014 44.24772 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jot" -type "string" "yxz";
	setAttr ".bps" -type "matrix" -1 -1.2246467991473532e-016 0 0 1.2246467991473532e-016 -1 0 0
		 0 0 1 0 1.3486489690923307 14.656585133659888 1.5144370407379352e-017 1;
	setAttr -k on -cb off ".radi" 0.5;
createNode joint -n "wristRGT_tmpJnt" -p "forearmRGT_tmpJnt";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".oc" 6;
	setAttr ".t" -type "double3" -0.00027747178830850316 -43.017329749915987 -3.5543999999999976 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jot" -type "string" "yxz";
	setAttr ".bps" -type "matrix" 2.2204460492503131e-016 -1 0 0 1 2.2204460492503131e-016 8.3960588285190204e-014 0
		 -8.3960588285190204e-014 -1.8642995655058271e-029 1 0 11.145136555499452 21.950819439088733 -0.34347297829513029 1;
	setAttr -k on -cb off ".radi" 0.5;
createNode joint -n "handRGT_tmpJnt" -p "wristRGT_tmpJnt";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".oc" 7;
	setAttr ".t" -type "double3" 0.00025247166533404197 -15.668414968536496 1.000000000139778e-005 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".bps" -type "matrix" 2.2204460492503131e-016 -1 0 0 1 2.2204460492503131e-016 8.3960588285190204e-014 0
		 -8.3960588285190204e-014 -1.8642995655058271e-029 1 0 11.94334900537585 21.950819439093973 -0.34347375639834526 1;
	setAttr -k on -cb off ".radi" 0.5;
createNode joint -n "thumb1RGT_tmpJnt" -p "handRGT_tmpJnt";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".t" -type "double3" -4.305842790264137 8.1764705634846067 -7.66769 ;
	setAttr ".r" -type "double3" 29.82992934827168 -22.43886925947923 -54.610386034323412 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jot" -type "string" "yxz";
	setAttr ".jo" -type "double3" 1.7315079359005356 -2.7817602715362473e-018 1.8408346802882949e-016 ;
	setAttr ".bps" -type "matrix" -0.59548586752167076 -0.80336578317847407 -4.9997343752636337e-014 0
		 0.73868319246536318 -0.54754062333671982 0.39312390790336815 0 -0.31582229615899904 0.23409973134130962 0.91948550452673483 0
		 11.518645340649305 21.905429719636764 0.32567524419271171 1;
	setAttr -k on -cb off ".radi" 0.5;
createNode joint -n "thumb2RGT_tmpJnt" -p "thumb1RGT_tmpJnt";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".oc" 1;
	setAttr ".t" -type "double3" 0.033399729003487977 -3.4524293515596298 -4.598443924915486 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jot" -type "string" "yxz";
	setAttr ".bps" -type "matrix" -0.59548586752167076 -0.80336578317847407 -4.9997343752636337e-014 0
		 0.73868319246536318 -0.54754062333671982 0.39312390790336815 0 -0.31582229615899904 0.23409973134130962 0.91948550452673483 0
		 12.026286103962779 21.529146703032435 0.59583939943602238 1;
	setAttr -k on -cb off ".radi" 0.5;
createNode joint -n "thumb3RGT_tmpJnt" -p "thumb2RGT_tmpJnt";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".oc" 2;
	setAttr ".t" -type "double3" -0.00030838561308499379 -8.3257995999178576 -0.00023854939929890406 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jot" -type "string" "yxz";
	setAttr ".bps" -type "matrix" -0.59548586752167076 -0.80336578317847407 -4.9997343752636337e-014 0
		 0.73868319246536318 -0.54754062333671982 0.39312390790336815 0 -0.31582229615899904 0.23409973134130962 0.91948550452673483 0
		 12.724953059079672 21.011267666374362 0.96766684389406166 1;
	setAttr -k on -cb off ".radi" 0.5;
createNode joint -n "thumb4RGT_tmpJnt" -p "thumb3RGT_tmpJnt";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".oc" 3;
	setAttr ".t" -type "double3" 0.00017222821995233062 -8.0303312596087437 0.00010624807080716892 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".bps" -type "matrix" -0.59548586752167076 -0.80336578317847407 -4.9997343752636337e-014 0
		 0.73868319246536318 -0.54754062333671982 0.39312390790336815 0 -0.31582229615899904 0.23409973134130962 0.91948550452673483 0
		 13.320225968832865 20.570028305053697 1.2844684375111461 1;
	setAttr -k on -cb off ".radi" 0.5;
createNode joint -n "index1RGT_tmpJnt" -p "handRGT_tmpJnt";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".t" -type "double3" 1.703899301572477 8.98547708361113 -8.21722 ;
	setAttr ".r" -type "double3" 89.99999999993301 -85.861080851320125 -89.99999999993311 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jot" -type "string" "yxz";
	setAttr ".jo" -type "double3" 1.7315079359005356 -2.7817602715362473e-018 1.8408346802882949e-016 ;
	setAttr ".bps" -type "matrix" -8.3960588285190191e-014 -8.437694987151191e-014 1 0
		 1 2.2204460492503131e-016 8.3960588285190204e-014 0 -2.2204460493211562e-016 1 8.4376949871511897e-014 0
		 11.915961054098767 22.155901831531715 0.36968006095532863 1;
	setAttr -k on -cb off ".radi" 0.5;
createNode joint -n "index2RGT_tmpJnt" -p "index1RGT_tmpJnt";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".oc" 1;
	setAttr ".t" -type "double3" -4.7797475373201337e-005 -13.410484504895734 -0.43861388175378124 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jot" -type "string" "yxz";
	setAttr ".bps" -type "matrix" -8.3960588285190191e-014 -8.437694987151191e-014 1 0
		 1 2.2204460492503131e-016 8.3960588285190204e-014 0 -2.2204460493211562e-016 1 8.4376949871511897e-014 0
		 13.114219270621863 22.155901831531715 0.36968006095542938 1;
	setAttr -k on -cb off ".radi" 0.5;
createNode joint -n "index3RGT_tmpJnt" -p "index2RGT_tmpJnt";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".oc" 2;
	setAttr ".t" -type "double3" 2.5546444466506557e-005 -8.1332873569336286 0.00018571779170883929 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jot" -type "string" "yxz";
	setAttr ".bps" -type "matrix" -8.3960588285190191e-014 -8.437694987151191e-014 1 0
		 1 2.2204460492503131e-016 8.3960588285190204e-014 0 -2.2204460493211562e-016 1 8.4376949871511897e-014 0
		 13.805785441300909 22.155901831531718 0.3696800609554875 1;
	setAttr -k on -cb off ".radi" 0.5;
createNode joint -n "index4RGT_tmpJnt" -p "index3RGT_tmpJnt";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".oc" 3;
	setAttr ".t" -type "double3" 4.8288094287585182e-006 -5.2324936193771308 0.61175054724469646 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jot" -type "string" "yxz";
	setAttr ".bps" -type "matrix" -8.3960588285190191e-014 -8.437694987151191e-014 1 0
		 1 2.2204460492503131e-016 8.3960588285190204e-014 0 -2.2204460493211562e-016 1 8.4376949871511897e-014 0
		 14.271394348292739 22.155901831531718 0.36968006095552658 1;
	setAttr -k on -cb off ".radi" 0.5;
createNode joint -n "index5RGT_tmpJnt" -p "index4RGT_tmpJnt";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".oc" 4;
	setAttr ".t" -type "double3" 1.0760959918698632e-006 -5.6900285532324624 6.5559454526464833e-005 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".bps" -type "matrix" -8.3960588285190191e-014 -8.437694987151191e-014 1 0
		 1 2.2204460492503131e-016 8.3960588285190204e-014 0 -2.2204460493211562e-016 1 8.4376949871511897e-014 0
		 14.812322343180313 22.155901831531722 0.36968006095557193 1;
	setAttr -k on -cb off ".radi" 0.5;
createNode joint -n "middle1RGT_tmpJnt" -p "handRGT_tmpJnt";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".t" -type "double3" 2.2931583084096019 10.027403622701748 -3.07471 ;
	setAttr ".r" -type "double3" 2.9509382362211799e-016 -89.999999999995168 0 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jot" -type "string" "yxz";
	setAttr ".jo" -type "double3" 1.7315079359005356 -2.7817602715362473e-018 1.8408346802882949e-016 ;
	setAttr ".bps" -type "matrix" -8.3960588285190191e-014 -8.437694987151191e-014 1 0
		 1 2.2204460492503131e-016 8.3960588285190204e-014 0 -2.2204460493211562e-016 1 8.4376949871511897e-014 0
		 11.876633548480955 22.169748485139639 -0.10080869585328409 1;
	setAttr -k on -cb off ".radi" 0.5;
createNode joint -n "middle2RGT_tmpJnt" -p "middle1RGT_tmpJnt";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".oc" 1;
	setAttr ".t" -type "double3" -1.0612797685327635e-005 -14.442700001390072 -0.0003432706817250164 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jot" -type "string" "yxz";
	setAttr ".bps" -type "matrix" -8.3960588285190191e-014 -8.437694987151191e-014 1 0
		 1 2.2204460492503131e-016 8.3960588285190204e-014 0 -2.2204460493211562e-016 1 8.4376949871511897e-014 0
		 13.108601055533605 22.169748485139639 -0.10080869585318036 1;
	setAttr -k on -cb off ".radi" 0.5;
createNode joint -n "middle3RGT_tmpJnt" -p "middle2RGT_tmpJnt";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".oc" 2;
	setAttr ".t" -type "double3" 1.0910141541309315e-005 -9.2166961495142061 0.39232737326236133 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jot" -type "string" "yxz";
	setAttr ".bps" -type "matrix" -8.3960588285190191e-014 -8.437694987151191e-014 1 0
		 1 2.2204460492503131e-016 8.3960588285190204e-014 0 -2.2204460493211562e-016 1 8.4376949871511897e-014 0
		 13.906913312889571 22.169748485139639 -0.10080869585311319 1;
	setAttr -k on -cb off ".radi" 0.5;
createNode joint -n "middle4RGT_tmpJnt" -p "middle3RGT_tmpJnt";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".oc" 3;
	setAttr ".t" -type "double3" -2.7689804094066517e-007 -5.9723402287288003 0.44338527705318143 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jot" -type "string" "yxz";
	setAttr ".bps" -type "matrix" -8.3960588285190191e-014 -8.437694987151191e-014 1 0
		 1 2.2204460492503131e-016 8.3960588285190204e-014 0 -2.2204460493211562e-016 1 8.4376949871511897e-014 0
		 14.411849725499213 22.169748485139639 -0.10080869585307067 1;
	setAttr -k on -cb off ".radi" 0.5;
createNode joint -n "middle5RGT_tmpJnt" -p "middle4RGT_tmpJnt";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".oc" 4;
	setAttr ".t" -type "double3" 5.7505161032977981e-006 -6.4375263657947528 -0.00028242556365398741 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".bps" -type "matrix" -8.3960588285190191e-014 -8.437694987151191e-014 1 0
		 1 2.2204460492503131e-016 8.3960588285190204e-014 0 -2.2204460493211562e-016 1 8.4376949871511897e-014 0
		 15.081996667416741 22.169748485139635 -0.10080869585301426 1;
	setAttr -k on -cb off ".radi" 0.5;
createNode joint -n "ring1RGT_tmpJnt" -p "handRGT_tmpJnt";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".t" -type "double3" 2.2947067715886362 10.143996299409075 1.6134500000000012 ;
	setAttr ".r" -type "double3" -89.999999999947804 -84.700386817738419 89.999999999948017 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jot" -type "string" "yxz";
	setAttr ".jo" -type "double3" 1.7315079359005356 -2.7817602715362473e-018 1.8408346802882949e-016 ;
	setAttr ".bps" -type "matrix" -8.3960588285190191e-014 -8.437694987151191e-014 1 0
		 1 2.2204460492503131e-016 8.3960588285190204e-014 0 -2.2204460493211562e-016 1 8.4376949871511897e-014 0
		 11.876633548480955 22.13656260093245 -0.5683912766476541 1;
	setAttr -k on -cb off ".radi" 0.5;
createNode joint -n "ring2RGT_tmpJnt" -p "ring1RGT_tmpJnt";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".oc" 1;
	setAttr ".t" -type "double3" 3.3947273134771194e-005 -14.065991242760433 -0.00028693902217469258 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jot" -type "string" "yxz";
	setAttr ".bps" -type "matrix" -8.3960588285190191e-014 -8.437694987151191e-014 1 0
		 1 2.2204460492503131e-016 8.3960588285190204e-014 0 -2.2204460493211562e-016 1 8.4376949871511897e-014 0
		 13.097480078235414 22.13656260093245 -0.56839127664755129 1;
	setAttr -k on -cb off ".radi" 0.5;
createNode joint -n "ring3RGT_tmpJnt" -p "ring2RGT_tmpJnt";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".oc" 2;
	setAttr ".t" -type "double3" -1.8705140867325554e-005 -8.9126569490729324 0.40911463355902811 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jot" -type "string" "yxz";
	setAttr ".bps" -type "matrix" -8.3960588285190191e-014 -8.437694987151191e-014 1 0
		 1 2.2204460492503131e-016 8.3960588285190204e-014 0 -2.2204460493211562e-016 1 8.4376949871511897e-014 0
		 13.845747937749518 22.136562600932457 -0.56839127664748834 1;
	setAttr -k on -cb off ".radi" 0.5;
createNode joint -n "ring4RGT_tmpJnt" -p "ring3RGT_tmpJnt";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".oc" 3;
	setAttr ".t" -type "double3" 5.1561960887624991e-006 -5.6875583845711724 0.52273525131528231 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jot" -type "string" "yxz";
	setAttr ".bps" -type "matrix" -8.3960588285190191e-014 -8.437694987151191e-014 1 0
		 1 2.2204460492503131e-016 8.3960588285190204e-014 0 -2.2204460493211562e-016 1 8.4376949871511897e-014 0
		 14.345123861710062 22.136562600932454 -0.56839127664744615 1;
	setAttr -k on -cb off ".radi" 0.5;
createNode joint -n "ring5RGT_tmpJnt" -p "ring4RGT_tmpJnt";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".oc" 4;
	setAttr ".t" -type "double3" -9.2598071184113451e-006 -6.0257026507719189 0.00023322650790191801 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".bps" -type "matrix" -8.3960588285190191e-014 -8.437694987151191e-014 1 0
		 1 2.2204460492503131e-016 8.3960588285190204e-014 0 -2.2204460493211562e-016 1 8.4376949871511897e-014 0
		 14.876258587400191 22.136562600932457 -0.56839127664740152 1;
	setAttr -k on -cb off ".radi" 0.5;
createNode joint -n "pinky1RGT_tmpJnt" -p "handRGT_tmpJnt";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".t" -type "double3" 1.6299064743878091 9.3467890146696178 6.81641 ;
	setAttr ".r" -type "double3" -89.999999999969219 -80.961428166628806 89.999999999969603 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jot" -type "string" "yxz";
	setAttr ".jo" -type "double3" 1.7315079359005356 -2.7817602715362473e-018 1.8408346802882949e-016 ;
	setAttr ".bps" -type "matrix" -8.3960588285190191e-014 -8.437694987151191e-014 1 0
		 1 2.2204460492503131e-016 8.3960588285190204e-014 0 -2.2204460493211562e-016 1 8.4376949871511897e-014 0
		 11.876633548480955 22.020988418911262 -0.95907086085240945 1;
	setAttr -k on -cb off ".radi" 0.5;
createNode joint -n "pinky2RGT_tmpJnt" -p "pinky1RGT_tmpJnt";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".oc" 1;
	setAttr ".t" -type "double3" -2.8471315509648321e-005 -11.374821455265462 -4.6780937452695071e-006 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jot" -type "string" "yxz";
	setAttr ".bps" -type "matrix" -8.3960588285190191e-014 -8.437694987151191e-014 1 0
		 1 2.2204460492503131e-016 8.3960588285190204e-014 0 -2.2204460493211562e-016 1 8.4376949871511897e-014 0
		 13.083100380346423 22.020988418911262 -0.95907086085230775 1;
	setAttr -k on -cb off ".radi" 0.5;
createNode joint -n "pinky3RGT_tmpJnt" -p "pinky2RGT_tmpJnt";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".oc" 2;
	setAttr ".t" -type "double3" -4.1243287217440638e-005 -7.880064183170802 0.00016555234759607629 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jot" -type "string" "yxz";
	setAttr ".bps" -type "matrix" -8.3960588285190191e-014 -8.437694987151191e-014 1 0
		 1 2.2204460492503131e-016 8.3960588285190204e-014 0 -2.2204460493211562e-016 1 8.4376949871511897e-014 0
		 13.601293073636691 22.020988418911262 -0.95907086085226423 1;
	setAttr -k on -cb off ".radi" 0.5;
createNode joint -n "pinky4RGT_tmpJnt" -p "pinky3RGT_tmpJnt";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".oc" 3;
	setAttr ".t" -type "double3" -1.7908552841561232e-005 -4.8300397258857117 0.69350884352331832 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jot" -type "string" "yxz";
	setAttr ".bps" -type "matrix" -8.3960588285190191e-014 -8.437694987151191e-014 1 0
		 1 2.2204460492503131e-016 8.3960588285190204e-014 0 -2.2204460493211562e-016 1 8.4376949871511897e-014 0
		 13.978441565540829 22.020988418911262 -0.95907086085223248 1;
	setAttr -k on -cb off ".radi" 0.5;
createNode joint -n "pinky5RGT_tmpJnt" -p "pinky4RGT_tmpJnt";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".oc" 4;
	setAttr ".t" -type "double3" 4.0845075172768475e-005 -5.1778878510622413 1.2406359218175567e-005 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".bps" -type "matrix" -8.3960588285190191e-014 -8.437694987151191e-014 1 0
		 1 2.2204460492503131e-016 8.3960588285190204e-014 0 -2.2204460493211562e-016 1 8.4376949871511897e-014 0
		 14.437677801786013 22.020988418911262 -0.95907086085219373 1;
	setAttr -k on -cb off ".radi" 0.5;
createNode joint -n "pelvis_tmpJnt" -p "root_tmpJnt";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".oc" 1;
	setAttr ".t" -type "double3" 0 -4.224591079648917 0 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jot" -type "string" "yxz";
	setAttr ".bps" -type "matrix" 1 0 0 0 0 1 0 0 0 0 1 0 0 15.4830611404753 0 1;
	setAttr -k on -cb off ".radi" 0.5;
createNode joint -n "upLegLFT_tmpJnt" -p "pelvis_tmpJnt";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".oc" 2;
	setAttr ".t" -type "double3" 17.750767661381602 -0.64694965445488606 -0.52935052701766327 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jot" -type "string" "yxz";
	setAttr ".jo" -type "double3" 0 0 -180 ;
	setAttr ".bps" -type "matrix" -1 -1.2246467991473532e-016 0 0 1.2246467991473532e-016 -1 0 0
		 0 0 1 0 1.3486489690923307 14.656585133659888 1.5144370407379352e-017 1;
	setAttr -k on -cb off ".radi" 0.5;
createNode joint -n "lowLegLFT_tmpJnt" -p "upLegLFT_tmpJnt";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".oc" 3;
	setAttr ".t" -type "double3" 1.0658141036401503e-014 56.103814638662513 1.7959992400597482 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jot" -type "string" "yxz";
	setAttr ".bps" -type "matrix" -1 -1.2246467991473532e-016 0 0 1.2246467991473532e-016 -1 0 0
		 0 0 1 0 1.3486489690923305 7.7535119809750004 0.15259281481888803 1;
	setAttr -k on -cb off ".radi" 0.5;
createNode joint -n "kneeIkLFT_tmpJnt" -p "lowLegLFT_tmpJnt";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".oc" 2;
	setAttr ".t" -type "double3" -7.1054273576010019e-015 0 44.738514772231561 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jot" -type "string" "yxz";
	setAttr ".bps" -type "matrix" -1 -1.2246467991473532e-016 0 0 1.2246467991473532e-016 -1 0 0
		 0 0 1 0 1.3486489690923307 14.656585133659888 1.5144370407379352e-017 1;
	setAttr -k on -cb off ".radi" 0.5;
createNode joint -n "ankleLFT_tmpJnt" -p "lowLegLFT_tmpJnt";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".oc" 4;
	setAttr ".t" -type "double3" 0 60.977284752132903 -7.2354126693773653 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jot" -type "string" "yxz";
	setAttr ".bps" -type "matrix" -1 -1.2246467991473532e-016 0 0 1.2246467991473532e-016 -1 0 0
		 0 0 1 0 1.348648969092332 1.0615915425310156 0 1;
	setAttr -k on -cb off ".radi" 0.5;
createNode joint -n "ballLFT_tmpJnt" -p "ankleLFT_tmpJnt";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".oc" 5;
	setAttr ".t" -type "double3" 1.9539925233402755e-014 9.5852291807450829 18.260965040256298 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jot" -type "string" "yxz";
	setAttr ".jo" -type "double3" 89.999999999999986 0 0 ;
	setAttr ".bps" -type "matrix" -1 -1.2246467991473532e-016 0 0 2.7192621468937821e-032 -2.2204460492503131e-016 1 0
		 -1.2246467991473532e-016 1 2.2204460492503131e-016 0 1.3486489690923311 5.5511151231257827e-015 1.476681409489522 1;
	setAttr -k on -cb off ".radi" 0.5;
createNode joint -n "toeLFT_tmpJnt" -p "ballLFT_tmpJnt";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".oc" 6;
	setAttr ".t" -type "double3" 1.7763568394002505e-015 19.09779450547375 4.2405622359073494e-015 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".bps" -type "matrix" -1 -1.2246467991473532e-016 0 0 2.7192621468937821e-032 -2.2204460492503131e-016 1 0
		 -1.2246467991473532e-016 1 2.2204460492503131e-016 0 1.3486489690923309 5.0024078434460801e-015 3.3551152167720435 1;
	setAttr -k on -cb off ".radi" 0.5;
createNode joint -n "footInLFT_tmpJnt" -p "ankleLFT_tmpJnt";
	setAttr ".t" -type "double3" 9.2514115349220472 9.4988057815199358 11.548286301470995 ;
	setAttr ".radi" 0.5;
createNode joint -n "footOutLFT_tmpJnt" -p "ankleLFT_tmpJnt";
	setAttr ".t" -type "double3" -16.298857766659992 9.4988057815199767 11.562392251435819 ;
	setAttr ".radi" 0.5;
createNode joint -n "heelLFT_tmpJnt" -p "ankleLFT_tmpJnt";
	setAttr ".t" -type "double3" 1.7763568394002505e-014 9.4988057815199358 -9.0826705558493011 ;
	setAttr ".radi" 0.5;
createNode joint -n "upLegRGT_tmpJnt" -p "pelvis_tmpJnt";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".oc" 2;
	setAttr ".t" -type "double3" -17.7508 -0.64727822599539309 -0.52935295918026704 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jot" -type "string" "yxz";
	setAttr ".jo" -type "double3" 0 180 0 ;
	setAttr ".bps" -type "matrix" -1 -1.2246467991473532e-016 0 0 1.2246467991473532e-016 -1 0 0
		 0 0 1 0 1.3486489690923307 14.656585133659888 1.5144370407379352e-017 1;
	setAttr -k on -cb off ".radi" 0.5;
createNode joint -n "lowLegRGT_tmpJnt" -p "upLegRGT_tmpJnt";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".oc" 3;
	setAttr ".t" -type "double3" 0 -56.1035 -1.7960000000000003 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jot" -type "string" "yxz";
	setAttr ".bps" -type "matrix" -1 -1.2246467991473532e-016 0 0 1.2246467991473532e-016 -1 0 0
		 0 0 1 0 1.3486489690923305 7.7535119809750004 0.15259281481888803 1;
	setAttr -k on -cb off ".radi" 0.5;
createNode joint -n "kneeIkRGT_tmpJnt" -p "lowLegRGT_tmpJnt";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".oc" 2;
	setAttr ".t" -type "double3" -3.5527136788005009e-015 0 -44.738519999999994 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jot" -type "string" "yxz";
	setAttr ".bps" -type "matrix" -1 -1.2246467991473532e-016 0 0 1.2246467991473532e-016 -1 0 0
		 0 0 1 0 1.3486489690923307 14.656585133659888 1.5144370407379352e-017 1;
	setAttr -k on -cb off ".radi" 0.5;
createNode joint -n "ankleRGT_tmpJnt" -p "lowLegRGT_tmpJnt";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".oc" 4;
	setAttr ".t" -type "double3" 0 -60.977270000000004 7.23538 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jot" -type "string" "yxz";
	setAttr ".bps" -type "matrix" -1 -1.2246467991473532e-016 0 0 1.2246467991473532e-016 -1 0 0
		 0 0 1 0 1.348648969092332 1.0615915425310156 0 1;
	setAttr -k on -cb off ".radi" 0.5;
createNode joint -n "ballRGT_tmpJnt" -p "ankleRGT_tmpJnt";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".oc" 5;
	setAttr ".t" -type "double3" 0 -9.5852299999999904 -18.260930000000002 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jot" -type "string" "yxz";
	setAttr ".jo" -type "double3" 89.999999999999986 1.403341859706975e-014 -1.4124500153760508e-030 ;
	setAttr ".bps" -type "matrix" -1 -1.2246467991473532e-016 0 0 2.7192621468937821e-032 -2.2204460492503131e-016 1 0
		 -1.2246467991473532e-016 1 2.2204460492503131e-016 0 1.3486489690923311 5.5511151231257827e-015 1.476681409489522 1;
	setAttr -k on -cb off ".radi" 0.5;
createNode joint -n "toeRGT_tmpJnt" -p "ballRGT_tmpJnt";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".oc" 6;
	setAttr ".t" -type "double3" -7.1054273576010019e-015 -19.097769999999997 -4.240556276398362e-015 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".bps" -type "matrix" -1 -1.2246467991473532e-016 0 0 2.7192621468937821e-032 -2.2204460492503131e-016 1 0
		 -1.2246467991473532e-016 1 2.2204460492503131e-016 0 1.3486489690923309 5.0024078434460801e-015 3.3551152167720435 1;
	setAttr -k on -cb off ".radi" 0.5;
createNode joint -n "footInRGT_tmpJnt" -p "ankleRGT_tmpJnt";
	setAttr ".t" -type "double3" -9.2514400000000023 -9.4988065999999964 -11.548255 ;
	setAttr ".radi" 0.5;
createNode joint -n "footOutRGT_tmpJnt" -p "ankleRGT_tmpJnt";
	setAttr ".t" -type "double3" 16.298799999999996 -9.4988065999999964 -11.562361000000003 ;
	setAttr ".radi" 0.5;
createNode joint -n "heelRGT_tmpJnt" -p "ankleRGT_tmpJnt";
	setAttr ".t" -type "double3" 3.5527136788005009e-015 -9.4988065999999964 9.0826999999999991 ;
	setAttr ".radi" 0.5;
createNode transform -n "addJnt_grp";
createNode joint -n "lowerTeeth_jnt" -p "addJnt_grp";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".t" -type "double3" 0 223.88262395048474 12.418563328530155 ;
	setAttr ".bps" -type "matrix" 1 0 0 0 0 1 0 0 0 0 1 0 0 223.88262395048474 12.418563328530155 1;
	setAttr ".radi" 0.5;
createNode joint -n "upperTeeth_jnt" -p "addJnt_grp";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".t" -type "double3" -2.5021681837478968e-030 226.2211830093936 12.418563328530155 ;
	setAttr ".bps" -type "matrix" 1 0 0 0 0 1 0 0 0 0 1 0 -2.5021681837478968e-030 226.2211830093936 12.418563328530155 1;
	setAttr ".radi" 0.5;
createNode joint -n "tongue1_jnt" -p "addJnt_grp";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".t" -type "double3" 0 222.64327363418465 -1.3727481207023438 ;
	setAttr ".r" -type "double3" 2.798888119687894e-013 0 0 ;
	setAttr ".jo" -type "double3" 32.38843485659649 0 0 ;
	setAttr ".bps" -type "matrix" 1 0 0 0 0 0.84443606484883982 0.53565635661551347 0
		 0 -0.53565635661551347 0.84443606484883982 0 0 222.64327363418465 -1.3727481207023438 1;
	setAttr ".radi" 0.5;
	setAttr ".liw" yes;
createNode joint -n "tongue2_jnt" -p "tongue1_jnt";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".t" -type "double3" 0 3.3835996885814268 2.8421709430404007e-014 ;
	setAttr ".r" -type "double3" 2.8243325571396029e-012 0 0 ;
	setAttr ".jo" -type "double3" 52.785353509946113 0 0 ;
	setAttr ".bps" -type "matrix" 1 0 0 0 0 0.084133709421899183 0.99645447409247523 0
		 0 -0.99645447409247523 0.084133709421899183 0 0 225.5005072402341 0.43969856072858127 1;
	setAttr ".radi" 0.5;
	setAttr ".liw" yes;
createNode joint -n "tongue3_jnt" -p "tongue2_jnt";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".t" -type "double3" 0 2.578616554025416 1.7053025658242404e-013 ;
	setAttr ".r" -type "double3" -1.3867218411180933e-012 0 0 ;
	setAttr ".jo" -type "double3" 9.5040328481669594 0 0 ;
	setAttr ".bps" -type "matrix" 1 0 0 0 0 -0.081552711316839971 0.99666902995772477 0
		 0 -0.99666902995772477 -0.081552711316839971 0 0 225.71745581610085 3.0091725629561377 1;
	setAttr ".radi" 0.5;
	setAttr ".liw" yes;
createNode joint -n "tongue4_jnt" -p "tongue3_jnt";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".t" -type "double3" 0 3.0154019044469429 -8.5265128291212022e-014 ;
	setAttr ".r" -type "double3" 8.6988170538027179e-013 0 0 ;
	setAttr ".jo" -type "double3" 1.0001348544728366 0 0 ;
	setAttr ".bps" -type "matrix" 1 0 0 0 0 -0.098936905545293025 0.99509370851248047 0
		 0 -0.99509370851248047 -0.098936905545293025 0 0 225.47154161508337 6.0145302539939607 1;
	setAttr ".radi" 0.5;
	setAttr ".liw" yes;
createNode joint -n "tongue5_jnt" -p "tongue4_jnt";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".t" -type "double3" 0 3.1566281257245592 5.6843418860808015e-014 ;
	setAttr ".r" -type "double3" -9.5834088245847598e-013 0 0 ;
	setAttr ".jo" -type "double3" 1.1085356221394158 0 0 ;
	setAttr ".bps" -type "matrix" 1 0 0 0 0 -0.11816985903832641 0.9929933959573255 0
		 0 -0.9929933959573255 -0.11816985903832641 0 0 225.1592345963669 9.1556710420160119 1;
	setAttr ".radi" 0.5;
createNode joint -n "tongue6_jnt" -p "tongue5_jnt";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".t" -type "double3" 0 3.1766923264381965 -5.6843418860808015e-014 ;
	setAttr ".r" -type "double3" 5.9635400277440939e-016 0 0 ;
	setAttr ".jo" -type "double3" 7.9513867036587899e-016 0 0 ;
	setAttr ".bps" -type "matrix" 1 0 0 0 0 -0.11816985903832641 0.9929933959573255 0
		 0 -0.9929933959573255 -0.11816985903832641 0 0 224.78384531194365 12.310105543157466 1;
	setAttr ".radi" 0.5;
createNode joint -n "thumbToe1LFT_jnt" -p "addJnt_grp";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".oc" 3;
	setAttr ".t" -type "double3" 14.483562389251162 3.3809123766256186 18.1141638774779 ;
	setAttr ".ro" 1;
	setAttr ".jo" -type "double3" 89.999999999999886 -2.0913097891518739e-006 -179.99999891859255 ;
	setAttr ".bps" -type "matrix" -0.99999999999999911 -1.887412057596498e-008 3.6500241499888554e-008 0
		 3.6500241499888581e-008 -1.4172455962248266e-015 0.99999999999999933 0 -1.887412057596492e-008 0.99999999999999978 1.9984014443252818e-015 0
		 14.483562389251162 3.3809123766256186 18.1141638774779 1;
	setAttr ".liw" yes;
createNode joint -n "thumbToe2LFT_jnt" -p "thumbToe1LFT_jnt";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".oc" 4;
	setAttr ".t" -type "double3" -5.3290705182007514e-015 2.0569100600225703 1.2721686567090251e-014 ;
	setAttr ".ro" 1;
	setAttr ".bps" -type "matrix" -0.99999999999999911 -1.887412057596498e-008 3.6500241499888554e-008 0
		 3.6500241499888581e-008 -1.4172455962248266e-015 0.99999999999999933 0 -1.887412057596492e-008 0.99999999999999978 1.9984014443252818e-015 0
		 14.483562464328882 3.3809123766256284 20.17107393750047 1;
	setAttr ".liw" yes;
createNode joint -n "thumbToe3LFT_jnt" -p "thumbToe2LFT_jnt";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".oc" 5;
	setAttr ".t" -type "double3" -3.5527136788005009e-015 5.0344324666648639 8.8817836676056603e-016 ;
	setAttr ".ro" 1;
	setAttr ".bps" -type "matrix" -0.99999999999999911 -1.887412057596498e-008 3.6500241499888554e-008 0
		 3.6500241499888581e-008 -1.4172455962248266e-015 0.99999999999999933 0 -1.887412057596492e-008 0.99999999999999978 1.9984014443252818e-015 0
		 14.483562648086886 3.3809123766256222 25.20550640416533 1;
	setAttr ".liw" yes;
createNode joint -n "indexToe1LFT_jnt" -p "addJnt_grp";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".oc" 3;
	setAttr ".t" -type "double3" 19.654736265256656 3.5823867347681335 18.867787120980601 ;
	setAttr ".ro" 1;
	setAttr ".jo" -type "double3" 89.999999999999886 -2.0913097891518739e-006 -179.99999891859255 ;
	setAttr ".bps" -type "matrix" -0.99999999999999911 -1.887412057596498e-008 3.6500241499888554e-008 0
		 3.6500241499888581e-008 -1.4172455962248266e-015 0.99999999999999933 0 -1.887412057596492e-008 0.99999999999999978 1.9984014443252818e-015 0
		 19.654736265256656 3.5823867347681335 18.867787120980601 1;
	setAttr ".liw" yes;
createNode joint -n "indexToe2LFT_jnt" -p "indexToe1LFT_jnt";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".oc" 4;
	setAttr ".t" -type "double3" -1.4210854715202004e-014 2.1939949029313119 -0.54670248540499178 ;
	setAttr ".ro" 1;
	setAttr ".bps" -type "matrix" -0.99999999999999911 -1.887412057596498e-008 3.6500241499888554e-008 0
		 3.6500241499888581e-008 -1.4172455962248266e-015 0.99999999999999933 0 -1.887412057596492e-008 0.99999999999999978 1.9984014443252818e-015 0
		 19.654736355656542 3.0356842493631389 21.06178202391191 1;
	setAttr ".liw" yes;
createNode joint -n "indexToe3LFT_jnt" -p "indexToe2LFT_jnt";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".oc" 5;
	setAttr ".t" -type "double3" -8.8817841970012523e-015 3.8888952575023765 5.2939559203393771e-023 ;
	setAttr ".ro" 1;
	setAttr ".bps" -type "matrix" -0.99999999999999911 -1.887412057596498e-008 3.6500241499888554e-008 0
		 3.6500241499888581e-008 -1.4172455962248266e-015 0.99999999999999933 0 -1.887412057596492e-008 0.99999999999999978 1.9984014443252818e-015 0
		 19.654736497602165 3.0356842493631335 24.950677281414283 1;
	setAttr ".liw" yes;
createNode joint -n "middleToe1LFT_jnt" -p "addJnt_grp";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".oc" 3;
	setAttr ".t" -type "double3" 23.833229097571561 3.545618914658315 18.322361793410607 ;
	setAttr ".ro" 1;
	setAttr ".jo" -type "double3" 89.999999999999886 2.2499929316109859 -179.99999891859255 ;
	setAttr ".bps" -type "matrix" -0.99922904108406752 -1.8859569321739476e-008 -0.03925969248751842 0
		 -0.039259692487518413 -7.4099427431652264e-010 0.99922904108406774 0 -1.887412057596492e-008 0.99999999999999978 1.9984014443252818e-015 0
		 23.833229097571561 3.545618914658315 18.322361793410607 1;
	setAttr ".liw" yes;
createNode joint -n "middleToe2LFT_jnt" -p "middleToe1LFT_jnt";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".oc" 4;
	setAttr ".t" -type "double3" -1.4210854715202004e-014 2.3970558260817398 -0.99465231890338601 ;
	setAttr ".ro" 1;
	setAttr ".bps" -type "matrix" -0.99922904108406752 -1.8859569321739476e-008 -0.03925969248751842 0
		 -0.039259692487518413 -7.4099427431652264e-010 0.99922904108406774 0 -1.887412057596492e-008 0.99999999999999978 1.9984014443252818e-015 0
		 23.739121441737378 2.5509665939787247 20.717569587931241 1;
	setAttr ".liw" yes;
createNode joint -n "middleToe3LFT_jnt" -p "middleToe2LFT_jnt";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".oc" 5;
	setAttr ".t" -type "double3" 0 2.7074992189431768 9.0177843364079948e-016 ;
	setAttr ".ro" 1;
	setAttr ".bps" -type "matrix" -0.99922904108406752 -1.8859569321739476e-008 -0.03925969248751842 0
		 -0.039259692487518413 -7.4099427431652264e-010 0.99922904108406774 0 -1.887412057596492e-008 0.99999999999999978 1.9984014443252818e-015 0
		 23.632825854991474 2.5509665919724842 23.422981436211693 1;
	setAttr ".liw" yes;
createNode joint -n "ringToe1LFT_jnt" -p "addJnt_grp";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".oc" 3;
	setAttr ".t" -type "double3" 27.387754888646541 3.2321558806201516 16.882020110151402 ;
	setAttr ".ro" 1;
	setAttr ".jo" -type "double3" 89.999999999999886 2.2499929316109859 -179.99999891859255 ;
	setAttr ".bps" -type "matrix" -0.99922904108406752 -1.8859569321739476e-008 -0.03925969248751842 0
		 -0.039259692487518413 -7.4099427431652264e-010 0.99922904108406774 0 -1.887412057596492e-008 0.99999999999999978 1.9984014443252818e-015 0
		 27.387754888646541 3.2321558806201516 16.882020110151402 1;
	setAttr ".liw" yes;
createNode joint -n "ringToe2LFT_jnt" -p "ringToe1LFT_jnt";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".oc" 4;
	setAttr ".t" -type "double3" -3.5527136788005009e-015 1.4170005800390584 -0.35186750734648808 ;
	setAttr ".ro" 1;
	setAttr ".bps" -type "matrix" -0.99922904108406752 -1.8859569321739476e-008 -0.03925969248751842 0
		 -0.039259692487518413 -7.4099427431652264e-010 0.99922904108406774 0 -1.887412057596492e-008 0.99999999999999978 1.9984014443252818e-015 0
		 27.332123888260764 2.8802883722236743 18.297928240959397 1;
	setAttr ".liw" yes;
createNode joint -n "ringToe3LFT_jnt" -p "ringToe2LFT_jnt";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".oc" 5;
	setAttr ".t" -type "double3" 0 2.7074992189431768 9.0177843364079948e-016 ;
	setAttr ".ro" 1;
	setAttr ".bps" -type "matrix" -0.99922904108406752 -1.8859569321739476e-008 -0.03925969248751842 0
		 -0.039259692487518413 -7.4099427431652264e-010 0.99922904108406774 0 -1.887412057596492e-008 0.99999999999999978 1.9984014443252818e-015 0
		 27.225828301514859 2.8802883702174338 21.003340089239849 1;
	setAttr ".liw" yes;
createNode joint -n "pinkyToe1LFT_jnt" -p "addJnt_grp";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".oc" 3;
	setAttr ".t" -type "double3" 31.048633193268319 2.0419543052267 12.753471087826441 ;
	setAttr ".ro" 1;
	setAttr ".jo" -type "double3" 89.999999999999886 8.3039791409633263 -179.99999891859258 ;
	setAttr ".bps" -type "matrix" -0.98951576127278995 -1.8676239485899002e-008 -0.14442492233936116 0
		 -0.14442492233936111 -2.7258954824815886e-009 0.98951576127279017 0 -1.887412057596492e-008 0.99999999999999978 1.9984014443252818e-015 0
		 31.048633193268319 2.0419543052267 12.753471087826441 1;
	setAttr ".liw" yes;
createNode joint -n "pinkyToe2LFT_jnt" -p "pinkyToe1LFT_jnt";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".oc" 4;
	setAttr ".t" -type "double3" -1.4210854715202004e-014 2.3328462012016793 1.2434497875801753e-014 ;
	setAttr ".ro" 1;
	setAttr ".bps" -type "matrix" -0.98951576127278995 -1.8676239485899002e-008 -0.14442492233936113 0
		 -0.14442492233936108 -2.7258954824815882e-009 0.98951576127279017 0 -1.887412057596492e-008 0.99999999999999978 1.9984014443252818e-015 0
		 30.711712061830106 2.0419542988676174 15.06185917254086 1;
	setAttr ".liw" yes;
createNode joint -n "pinkyToe3LFT_jnt" -p "pinkyToe2LFT_jnt";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".oc" 5;
	setAttr ".t" -type "double3" 0 2.7074992189431768 0 ;
	setAttr ".ro" 1;
	setAttr ".bps" -type "matrix" -0.98951576127278995 -1.8676239485899002e-008 -0.14442492233936113 0
		 -0.14442492233936108 -2.7258954824815882e-009 0.98951576127279017 0 -1.887412057596492e-008 0.99999999999999978 1.9984014443252818e-015 0
		 30.320681697400357 2.0419542914872575 17.740972323318903 1;
	setAttr ".liw" yes;
createNode joint -n "thumbToe1RGT_jnt" -p "addJnt_grp";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".oc" 3;
	setAttr ".t" -type "double3" -14.4836 3.38091 18.1142 ;
	setAttr ".ro" 1;
	setAttr ".jo" -type "double3" -90.000000000000114 1.0099023361094196e-006 179.9999990861555 ;
	setAttr ".bps" -type "matrix" -0.99999999999999911 -1.887412057596498e-008 3.6500241499888554e-008 0
		 3.6500241499888581e-008 -1.4172455962248266e-015 0.99999999999999933 0 -1.887412057596492e-008 0.99999999999999978 1.9984014443252818e-015 0
		 14.483562389251162 3.3809123766256186 18.1141638774779 1;
	setAttr ".liw" yes;
createNode joint -n "thumbToe2RGT_jnt" -p "thumbToe1RGT_jnt";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".oc" 4;
	setAttr ".t" -type "double3" 0 -2.0569000000000024 -3.9968028886505635e-015 ;
	setAttr ".ro" 1;
	setAttr ".jo" -type "double3" 1.9090959104164216e-006 6.968246186966522e-014 -5.5831976835717288e-015 ;
	setAttr ".bps" -type "matrix" -0.99999999999999911 -1.887412057596498e-008 3.6500241499888554e-008 0
		 3.6500241499888581e-008 -1.4172455962248266e-015 0.99999999999999933 0 -1.887412057596492e-008 0.99999999999999978 1.9984014443252818e-015 0
		 14.483562464328882 3.3809123766256284 20.17107393750047 1;
	setAttr ".liw" yes;
createNode joint -n "thumbToe3RGT_jnt" -p "thumbToe2RGT_jnt";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".oc" 5;
	setAttr ".t" -type "double3" 0 -5.0343999999999944 1.6774624489457324e-007 ;
	setAttr ".ro" 1;
	setAttr ".jo" -type "double3" 2.8316468405101563e-006 1.0335579344972235e-013 -8.2812230545338435e-015 ;
	setAttr ".bps" -type "matrix" -0.99999999999999911 -1.887412057596498e-008 3.6500241499888554e-008 0
		 3.6500241499888581e-008 -1.4172455962248266e-015 0.99999999999999933 0 -1.887412057596492e-008 0.99999999999999978 1.9984014443252818e-015 0
		 14.483562648086886 3.3809123766256222 25.20550640416533 1;
	setAttr ".liw" yes;
createNode joint -n "indexToe1RGT_jnt" -p "addJnt_grp";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".oc" 3;
	setAttr ".t" -type "double3" -19.6547 3.58239 18.8678 ;
	setAttr ".ro" 1;
	setAttr ".jo" -type "double3" -90.000000000000114 1.0099023361094196e-006 179.9999990861555 ;
	setAttr ".bps" -type "matrix" -0.99999999999999911 -1.887412057596498e-008 3.6500241499888554e-008 0
		 3.6500241499888581e-008 -1.4172455962248266e-015 0.99999999999999933 0 -1.887412057596492e-008 0.99999999999999978 1.9984014443252818e-015 0
		 19.654736265256656 3.5823867347681335 18.867787120980601 1;
	setAttr ".liw" yes;
createNode joint -n "indexToe2RGT_jnt" -p "indexToe1RGT_jnt";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".oc" 4;
	setAttr ".t" -type "double3" -8.7198053222437011e-009 -2.1940000000000062 0.54670999999999559 ;
	setAttr ".ro" 1;
	setAttr ".jo" -type "double3" 1.9090959104164216e-006 6.968246186966522e-014 -5.5831976835717288e-015 ;
	setAttr ".bps" -type "matrix" -0.99999999999999911 -1.887412057596498e-008 3.6500241499888554e-008 0
		 3.6500241499888581e-008 -1.4172455962248266e-015 0.99999999999999933 0 -1.887412057596492e-008 0.99999999999999978 1.9984014443252818e-015 0
		 19.654736355656542 3.0356842493631389 21.06178202391191 1;
	setAttr ".liw" yes;
createNode joint -n "indexToe3RGT_jnt" -p "indexToe2RGT_jnt";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".oc" 5;
	setAttr ".t" -type "double3" 3.5527136788005009e-015 -3.8888999999999889 1.2957817618897138e-007 ;
	setAttr ".ro" 1;
	setAttr ".jo" -type "double3" 2.8316468405101563e-006 1.0335579344972235e-013 -8.2812230545338435e-015 ;
	setAttr ".bps" -type "matrix" -0.99999999999999911 -1.887412057596498e-008 3.6500241499888554e-008 0
		 3.6500241499888581e-008 -1.4172455962248266e-015 0.99999999999999933 0 -1.887412057596492e-008 0.99999999999999978 1.9984014443252818e-015 0
		 19.654736497602165 3.0356842493631335 24.950677281414283 1;
	setAttr ".liw" yes;
createNode joint -n "middleToe1RGT_jnt" -p "addJnt_grp";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".oc" 3;
	setAttr ".t" -type "double3" -23.8332 3.54562 18.3224 ;
	setAttr ".ro" 1;
	setAttr ".jo" -type "double3" -90.000000000000114 -2.2499929316109859 179.99999891859267 ;
	setAttr ".bps" -type "matrix" -0.99922904108406752 -1.8859569321739476e-008 -0.03925969248751842 0
		 -0.039259692487518413 -7.4099427431652264e-010 0.99922904108406774 0 -1.887412057596492e-008 0.99999999999999978 1.9984014443252818e-015 0
		 23.833229097571561 3.545618914658315 18.322361793410607 1;
	setAttr ".liw" yes;
createNode joint -n "middleToe2RGT_jnt" -p "middleToe1RGT_jnt";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".oc" 4;
	setAttr ".t" -type "double3" 7.3439214247628115e-006 -2.3970477370046659 0.9946499982239394 ;
	setAttr ".ro" 1;
	setAttr ".bps" -type "matrix" -0.99922904108406752 -1.8859569321739476e-008 -0.03925969248751842 0
		 -0.039259692487518413 -7.4099427431652264e-010 0.99922904108406774 0 -1.887412057596492e-008 0.99999999999999978 1.9984014443252818e-015 0
		 23.739121441737378 2.5509665939787247 20.717569587931241 1;
	setAttr ".liw" yes;
createNode joint -n "middleToe3RGT_jnt" -p "middleToe2RGT_jnt";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".oc" 5;
	setAttr ".t" -type "double3" -4.8750115020368412e-006 -2.7074875530602576 -2.006323551739797e-009 ;
	setAttr ".ro" 1;
	setAttr ".bps" -type "matrix" -0.99922904108406752 -1.8859569321739476e-008 -0.03925969248751842 0
		 -0.039259692487518413 -7.4099427431652264e-010 0.99922904108406774 0 -1.887412057596492e-008 0.99999999999999978 1.9984014443252818e-015 0
		 23.632825854991474 2.5509665919724842 23.422981436211693 1;
	setAttr ".liw" yes;
createNode joint -n "ringToe1RGT_jnt" -p "addJnt_grp";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".oc" 3;
	setAttr ".t" -type "double3" -27.3878 3.23216 16.882 ;
	setAttr ".ro" 1;
	setAttr ".jo" -type "double3" -90.000000000000114 -2.2499929316109859 179.99999891859267 ;
	setAttr ".bps" -type "matrix" -0.99922904108406752 -1.8859569321739476e-008 -0.03925969248751842 0
		 -0.039259692487518413 -7.4099427431652264e-010 0.99922904108406774 0 -1.887412057596492e-008 0.99999999999999978 1.9984014443252818e-015 0
		 27.387754888646541 3.2321558806201516 16.882020110151402 1;
	setAttr ".liw" yes;
createNode joint -n "ringToe2RGT_jnt" -p "ringToe1RGT_jnt";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".oc" 4;
	setAttr ".t" -type "double3" -6.9265631417181339e-005 -1.4169951644032164 0.35186999894870796 ;
	setAttr ".ro" 1;
	setAttr ".bps" -type "matrix" -0.99922904108406752 -1.8859569321739476e-008 -0.03925969248751842 0
		 -0.039259692487518413 -7.4099427431652264e-010 0.99922904108406774 0 -1.887412057596492e-008 0.99999999999999978 1.9984014443252818e-015 0
		 27.332123888260764 2.8802883722236743 18.297928240959397 1;
	setAttr ".liw" yes;
createNode joint -n "ringToe3RGT_jnt" -p "ringToe2RGT_jnt";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".oc" 5;
	setAttr ".t" -type "double3" -4.8750115055895549e-006 -2.7074875530602611 -2.0063244399182167e-009 ;
	setAttr ".ro" 1;
	setAttr ".bps" -type "matrix" -0.99922904108406752 -1.8859569321739476e-008 -0.03925969248751842 0
		 -0.039259692487518413 -7.4099427431652264e-010 0.99922904108406774 0 -1.887412057596492e-008 0.99999999999999978 1.9984014443252818e-015 0
		 27.225828301514859 2.8802883702174338 21.003340089239849 1;
	setAttr ".liw" yes;
createNode joint -n "pinkyToe1RGT_jnt" -p "addJnt_grp";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".oc" 3;
	setAttr ".t" -type "double3" -31.0486 2.04195 12.7535 ;
	setAttr ".ro" 1;
	setAttr ".jo" -type "double3" -90.000000000000128 -8.3039791409633299 179.99999891859264 ;
	setAttr ".bps" -type "matrix" -0.98951576127278995 -1.8676239485899002e-008 -0.14442492233936116 0
		 -0.14442492233936111 -2.7258954824815886e-009 0.98951576127279017 0 -1.887412057596492e-008 0.99999999999999978 1.9984014443252818e-015 0
		 31.048633193268319 2.0419543052267 12.753471087826441 1;
	setAttr ".liw" yes;
createNode joint -n "pinkyToe2RGT_jnt" -p "pinkyToe1RGT_jnt";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".oc" 4;
	setAttr ".t" -type "double3" 2.263075537456416e-005 -2.3328549396582385 -6.3586957921302201e-009 ;
	setAttr ".ro" 1;
	setAttr ".bps" -type "matrix" -0.98951576127278995 -1.8676239485899002e-008 -0.14442492233936113 0
		 -0.14442492233936108 -2.7258954824815882e-009 0.98951576127279017 0 -1.887412057596492e-008 0.99999999999999978 1.9984014443252818e-015 0
		 30.711712061830106 2.0419542988676174 15.06185917254086 1;
	setAttr ".liw" yes;
createNode joint -n "pinkyToe3RGT_jnt" -p "pinkyToe2RGT_jnt";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".oc" 5;
	setAttr ".t" -type "double3" 2.8146781723137337e-005 -2.707481820660627 -7.3797861155355804e-009 ;
	setAttr ".ro" 1;
	setAttr ".bps" -type "matrix" -0.98951576127278995 -1.8676239485899002e-008 -0.14442492233936113 0
		 -0.14442492233936108 -2.7258954824815882e-009 0.98951576127279017 0 -1.887412057596492e-008 0.99999999999999978 1.9984014443252818e-015 0
		 30.320681697400357 2.0419542914872575 17.740972323318903 1;
	setAttr ".liw" yes;
createNode lightLinker -s -n "lightLinker1";
	setAttr -s 8 ".lnk";
	setAttr -s 8 ".slnk";
createNode displayLayerManager -n "layerManager";
	setAttr ".cdl" 5;
	setAttr -s 6 ".dli[1:5]"  4 2 1 3 5;
createNode displayLayer -n "defaultLayer";
createNode renderLayerManager -n "renderLayerManager";
createNode renderLayer -n "defaultRenderLayer";
	setAttr ".g" yes;
createNode groupId -n "groupId442";
	setAttr ".ihi" 0;
createNode groupId -n "groupId443";
	setAttr ".ihi" 0;
createNode groupId -n "groupId463";
	setAttr ".ihi" 0;
createNode groupId -n "groupId475";
	setAttr ".ihi" 0;
createNode groupId -n "groupId476";
	setAttr ".ihi" 0;
createNode groupId -n "groupId478";
	setAttr ".ihi" 0;
createNode groupId -n "groupId481";
	setAttr ".ihi" 0;
createNode groupId -n "groupId3";
	setAttr ".ihi" 0;
createNode groupId -n "groupId2";
	setAttr ".ihi" 0;
createNode groupId -n "groupId19";
	setAttr ".ihi" 0;
createNode groupId -n "groupId20";
	setAttr ".ihi" 0;
createNode groupId -n "groupId27";
	setAttr ".ihi" 0;
createNode groupId -n "groupId492";
	setAttr ".ihi" 0;
createNode groupId -n "groupId1623";
	setAttr ".ihi" 0;
createNode groupId -n "groupId1624";
	setAttr ".ihi" 0;
createNode groupId -n "groupId1080";
	setAttr ".ihi" 0;
createNode groupId -n "groupId1616";
	setAttr ".ihi" 0;
createNode groupId -n "groupId1620";
	setAttr ".ihi" 0;
createNode groupId -n "groupId1078";
	setAttr ".ihi" 0;
createNode groupId -n "groupId1621";
	setAttr ".ihi" 0;
createNode groupId -n "groupId1622";
	setAttr ".ihi" 0;
createNode groupId -n "groupId1079";
	setAttr ".ihi" 0;
createNode groupId -n "groupId17";
	setAttr ".ihi" 0;
createNode groupId -n "groupId15";
	setAttr ".ihi" 0;
createNode groupId -n "groupId22";
	setAttr ".ihi" 0;
createNode groupId -n "groupId31";
	setAttr ".ihi" 0;
createNode groupId -n "groupId32";
	setAttr ".ihi" 0;
createNode groupId -n "groupId51";
	setAttr ".ihi" 0;
createNode groupId -n "groupId145";
	setAttr ".ihi" 0;
createNode groupId -n "groupId146";
	setAttr ".ihi" 0;
createNode groupId -n "groupId147";
	setAttr ".ihi" 0;
createNode groupId -n "groupId148";
	setAttr ".ihi" 0;
createNode shadingEngine -n "eyeSpecMat_sg";
	setAttr ".ihi" 0;
	setAttr ".ro" yes;
createNode shadingEngine -n "eyeMat_sg";
	setAttr ".ihi" 0;
	setAttr ".ro" yes;
createNode shadingEngine -n "corneaMat_sg";
	setAttr ".ihi" 0;
	setAttr ".ro" yes;
createNode groupId -n "groupId1642";
	setAttr ".ihi" 0;
createNode groupId -n "groupId1643";
	setAttr ".ihi" 0;
createNode groupId -n "groupId1637";
	setAttr ".ihi" 0;
createNode groupId -n "groupId1638";
	setAttr ".ihi" 0;
createNode groupId -n "groupId1639";
	setAttr ".ihi" 0;
createNode groupId -n "groupId1635";
	setAttr ".ihi" 0;
createNode groupId -n "groupId1640";
	setAttr ".ihi" 0;
createNode groupId -n "groupId1641";
	setAttr ".ihi" 0;
createNode groupId -n "groupId1636";
	setAttr ".ihi" 0;
createNode groupId -n "groupId1626";
	setAttr ".ihi" 0;
createNode groupId -n "groupId1625";
	setAttr ".ihi" 0;
createNode groupId -n "groupId1627";
	setAttr ".ihi" 0;
createNode groupId -n "groupId1628";
	setAttr ".ihi" 0;
createNode groupId -n "groupId1629";
	setAttr ".ihi" 0;
createNode groupId -n "groupId1630";
	setAttr ".ihi" 0;
createNode groupId -n "groupId1631";
	setAttr ".ihi" 0;
createNode groupId -n "groupId1632";
	setAttr ".ihi" 0;
createNode groupId -n "groupId1633";
	setAttr ".ihi" 0;
createNode groupId -n "groupId1634";
	setAttr ".ihi" 0;
createNode shadingEngine -n "eyeSpecMat_sg1";
	setAttr ".ihi" 0;
	setAttr ".ro" yes;
createNode shadingEngine -n "eyeMat_sg1";
	setAttr ".ihi" 0;
	setAttr ".ro" yes;
createNode shadingEngine -n "corneaMat_sg1";
	setAttr ".ihi" 0;
	setAttr ".ro" yes;
createNode script -n "sceneConfigurationScriptNode";
	setAttr ".b" -type "string" "playbackOptions -min 1 -max 24 -ast 1 -aet 48 ";
	setAttr ".st" 6;
createNode script -n "uiConfigurationScriptNode";
	setAttr ".b" -type "string" (
		"// Maya Mel UI Configuration File.\n//\n//  This script is machine generated.  Edit at your own risk.\n//\n//\n\nglobal string $gMainPane;\nif (`paneLayout -exists $gMainPane`) {\n\n\tglobal int $gUseScenePanelConfig;\n\tint    $useSceneConfig = $gUseScenePanelConfig;\n\tint    $menusOkayInPanels = `optionVar -q allowMenusInPanels`;\tint    $nVisPanes = `paneLayout -q -nvp $gMainPane`;\n\tint    $nPanes = 0;\n\tstring $editorName;\n\tstring $panelName;\n\tstring $itemFilterName;\n\tstring $panelConfig;\n\n\t//\n\t//  get current state of the UI\n\t//\n\tsceneUIReplacement -update $gMainPane;\n\n\t$panelName = `sceneUIReplacement -getNextPanel \"modelPanel\" (localizedPanelLabel(\"Top View\")) `;\n\tif (\"\" == $panelName) {\n\t\tif ($useSceneConfig) {\n\t\t\t$panelName = `modelPanel -unParent -l (localizedPanelLabel(\"Top View\")) -mbv $menusOkayInPanels `;\n\t\t\t$editorName = $panelName;\n            modelEditor -e \n                -camera \"top\" \n                -useInteractiveMode 0\n                -displayLights \"default\" \n                -displayAppearance \"wireframe\" \n"
		+ "                -activeOnly 0\n                -ignorePanZoom 0\n                -wireframeOnShaded 0\n                -headsUpDisplay 1\n                -selectionHiliteDisplay 1\n                -useDefaultMaterial 0\n                -bufferMode \"double\" \n                -twoSidedLighting 1\n                -backfaceCulling 0\n                -xray 0\n                -jointXray 0\n                -activeComponentsXray 0\n                -displayTextures 0\n                -smoothWireframe 0\n                -lineWidth 1\n                -textureAnisotropic 0\n                -textureHilight 1\n                -textureSampling 2\n                -textureDisplay \"modulate\" \n                -textureMaxSize 16384\n                -fogging 0\n                -fogSource \"fragment\" \n                -fogMode \"linear\" \n                -fogStart 0\n                -fogEnd 100\n                -fogDensity 0.1\n                -fogColor 0.5 0.5 0.5 1 \n                -maxConstantTransparency 1\n                -rendererName \"base_OpenGL_Renderer\" \n"
		+ "                -objectFilterShowInHUD 1\n                -isFiltered 0\n                -colorResolution 256 256 \n                -bumpResolution 512 512 \n                -textureCompression 0\n                -transparencyAlgorithm \"frontAndBackCull\" \n                -transpInShadows 0\n                -cullingOverride \"none\" \n                -lowQualityLighting 0\n                -maximumNumHardwareLights 1\n                -occlusionCulling 0\n                -shadingModel 0\n                -useBaseRenderer 0\n                -useReducedRenderer 0\n                -smallObjectCulling 0\n                -smallObjectThreshold -1 \n                -interactiveDisableShadows 0\n                -interactiveBackFaceCull 0\n                -sortTransparent 1\n                -nurbsCurves 1\n                -nurbsSurfaces 1\n                -polymeshes 1\n                -subdivSurfaces 1\n                -planes 1\n                -lights 1\n                -cameras 1\n                -controlVertices 1\n                -hulls 1\n                -grid 1\n"
		+ "                -joints 1\n                -ikHandles 1\n                -deformers 1\n                -dynamics 1\n                -fluids 1\n                -hairSystems 1\n                -follicles 1\n                -nCloths 1\n                -nParticles 1\n                -nRigids 1\n                -dynamicConstraints 1\n                -locators 1\n                -manipulators 1\n                -dimensions 1\n                -handles 1\n                -pivots 1\n                -textures 1\n                -strokes 1\n                -motionTrails 1\n                -shadows 0\n                $editorName;\nmodelEditor -e -viewSelected 0 $editorName;\n\t\t}\n\t} else {\n\t\t$label = `panel -q -label $panelName`;\n\t\tmodelPanel -edit -l (localizedPanelLabel(\"Top View\")) -mbv $menusOkayInPanels  $panelName;\n\t\t$editorName = $panelName;\n        modelEditor -e \n            -camera \"top\" \n            -useInteractiveMode 0\n            -displayLights \"default\" \n            -displayAppearance \"wireframe\" \n            -activeOnly 0\n            -ignorePanZoom 0\n"
		+ "            -wireframeOnShaded 0\n            -headsUpDisplay 1\n            -selectionHiliteDisplay 1\n            -useDefaultMaterial 0\n            -bufferMode \"double\" \n            -twoSidedLighting 1\n            -backfaceCulling 0\n            -xray 0\n            -jointXray 0\n            -activeComponentsXray 0\n            -displayTextures 0\n            -smoothWireframe 0\n            -lineWidth 1\n            -textureAnisotropic 0\n            -textureHilight 1\n            -textureSampling 2\n            -textureDisplay \"modulate\" \n            -textureMaxSize 16384\n            -fogging 0\n            -fogSource \"fragment\" \n            -fogMode \"linear\" \n            -fogStart 0\n            -fogEnd 100\n            -fogDensity 0.1\n            -fogColor 0.5 0.5 0.5 1 \n            -maxConstantTransparency 1\n            -rendererName \"base_OpenGL_Renderer\" \n            -objectFilterShowInHUD 1\n            -isFiltered 0\n            -colorResolution 256 256 \n            -bumpResolution 512 512 \n            -textureCompression 0\n"
		+ "            -transparencyAlgorithm \"frontAndBackCull\" \n            -transpInShadows 0\n            -cullingOverride \"none\" \n            -lowQualityLighting 0\n            -maximumNumHardwareLights 1\n            -occlusionCulling 0\n            -shadingModel 0\n            -useBaseRenderer 0\n            -useReducedRenderer 0\n            -smallObjectCulling 0\n            -smallObjectThreshold -1 \n            -interactiveDisableShadows 0\n            -interactiveBackFaceCull 0\n            -sortTransparent 1\n            -nurbsCurves 1\n            -nurbsSurfaces 1\n            -polymeshes 1\n            -subdivSurfaces 1\n            -planes 1\n            -lights 1\n            -cameras 1\n            -controlVertices 1\n            -hulls 1\n            -grid 1\n            -joints 1\n            -ikHandles 1\n            -deformers 1\n            -dynamics 1\n            -fluids 1\n            -hairSystems 1\n            -follicles 1\n            -nCloths 1\n            -nParticles 1\n            -nRigids 1\n            -dynamicConstraints 1\n"
		+ "            -locators 1\n            -manipulators 1\n            -dimensions 1\n            -handles 1\n            -pivots 1\n            -textures 1\n            -strokes 1\n            -motionTrails 1\n            -shadows 0\n            $editorName;\nmodelEditor -e -viewSelected 0 $editorName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextPanel \"modelPanel\" (localizedPanelLabel(\"Side View\")) `;\n\tif (\"\" == $panelName) {\n\t\tif ($useSceneConfig) {\n\t\t\t$panelName = `modelPanel -unParent -l (localizedPanelLabel(\"Side View\")) -mbv $menusOkayInPanels `;\n\t\t\t$editorName = $panelName;\n            modelEditor -e \n                -camera \"side\" \n                -useInteractiveMode 0\n                -displayLights \"default\" \n                -displayAppearance \"wireframe\" \n                -activeOnly 0\n                -ignorePanZoom 0\n                -wireframeOnShaded 0\n                -headsUpDisplay 1\n                -selectionHiliteDisplay 1\n                -useDefaultMaterial 0\n"
		+ "                -bufferMode \"double\" \n                -twoSidedLighting 1\n                -backfaceCulling 0\n                -xray 0\n                -jointXray 0\n                -activeComponentsXray 0\n                -displayTextures 0\n                -smoothWireframe 0\n                -lineWidth 1\n                -textureAnisotropic 0\n                -textureHilight 1\n                -textureSampling 2\n                -textureDisplay \"modulate\" \n                -textureMaxSize 16384\n                -fogging 0\n                -fogSource \"fragment\" \n                -fogMode \"linear\" \n                -fogStart 0\n                -fogEnd 100\n                -fogDensity 0.1\n                -fogColor 0.5 0.5 0.5 1 \n                -maxConstantTransparency 1\n                -rendererName \"base_OpenGL_Renderer\" \n                -objectFilterShowInHUD 1\n                -isFiltered 0\n                -colorResolution 256 256 \n                -bumpResolution 512 512 \n                -textureCompression 0\n                -transparencyAlgorithm \"frontAndBackCull\" \n"
		+ "                -transpInShadows 0\n                -cullingOverride \"none\" \n                -lowQualityLighting 0\n                -maximumNumHardwareLights 1\n                -occlusionCulling 0\n                -shadingModel 0\n                -useBaseRenderer 0\n                -useReducedRenderer 0\n                -smallObjectCulling 0\n                -smallObjectThreshold -1 \n                -interactiveDisableShadows 0\n                -interactiveBackFaceCull 0\n                -sortTransparent 1\n                -nurbsCurves 1\n                -nurbsSurfaces 1\n                -polymeshes 1\n                -subdivSurfaces 1\n                -planes 1\n                -lights 1\n                -cameras 1\n                -controlVertices 1\n                -hulls 1\n                -grid 1\n                -joints 1\n                -ikHandles 1\n                -deformers 1\n                -dynamics 1\n                -fluids 1\n                -hairSystems 1\n                -follicles 1\n                -nCloths 1\n                -nParticles 1\n"
		+ "                -nRigids 1\n                -dynamicConstraints 1\n                -locators 1\n                -manipulators 1\n                -dimensions 1\n                -handles 1\n                -pivots 1\n                -textures 1\n                -strokes 1\n                -motionTrails 1\n                -shadows 0\n                $editorName;\nmodelEditor -e -viewSelected 0 $editorName;\n\t\t}\n\t} else {\n\t\t$label = `panel -q -label $panelName`;\n\t\tmodelPanel -edit -l (localizedPanelLabel(\"Side View\")) -mbv $menusOkayInPanels  $panelName;\n\t\t$editorName = $panelName;\n        modelEditor -e \n            -camera \"side\" \n            -useInteractiveMode 0\n            -displayLights \"default\" \n            -displayAppearance \"wireframe\" \n            -activeOnly 0\n            -ignorePanZoom 0\n            -wireframeOnShaded 0\n            -headsUpDisplay 1\n            -selectionHiliteDisplay 1\n            -useDefaultMaterial 0\n            -bufferMode \"double\" \n            -twoSidedLighting 1\n            -backfaceCulling 0\n"
		+ "            -xray 0\n            -jointXray 0\n            -activeComponentsXray 0\n            -displayTextures 0\n            -smoothWireframe 0\n            -lineWidth 1\n            -textureAnisotropic 0\n            -textureHilight 1\n            -textureSampling 2\n            -textureDisplay \"modulate\" \n            -textureMaxSize 16384\n            -fogging 0\n            -fogSource \"fragment\" \n            -fogMode \"linear\" \n            -fogStart 0\n            -fogEnd 100\n            -fogDensity 0.1\n            -fogColor 0.5 0.5 0.5 1 \n            -maxConstantTransparency 1\n            -rendererName \"base_OpenGL_Renderer\" \n            -objectFilterShowInHUD 1\n            -isFiltered 0\n            -colorResolution 256 256 \n            -bumpResolution 512 512 \n            -textureCompression 0\n            -transparencyAlgorithm \"frontAndBackCull\" \n            -transpInShadows 0\n            -cullingOverride \"none\" \n            -lowQualityLighting 0\n            -maximumNumHardwareLights 1\n            -occlusionCulling 0\n"
		+ "            -shadingModel 0\n            -useBaseRenderer 0\n            -useReducedRenderer 0\n            -smallObjectCulling 0\n            -smallObjectThreshold -1 \n            -interactiveDisableShadows 0\n            -interactiveBackFaceCull 0\n            -sortTransparent 1\n            -nurbsCurves 1\n            -nurbsSurfaces 1\n            -polymeshes 1\n            -subdivSurfaces 1\n            -planes 1\n            -lights 1\n            -cameras 1\n            -controlVertices 1\n            -hulls 1\n            -grid 1\n            -joints 1\n            -ikHandles 1\n            -deformers 1\n            -dynamics 1\n            -fluids 1\n            -hairSystems 1\n            -follicles 1\n            -nCloths 1\n            -nParticles 1\n            -nRigids 1\n            -dynamicConstraints 1\n            -locators 1\n            -manipulators 1\n            -dimensions 1\n            -handles 1\n            -pivots 1\n            -textures 1\n            -strokes 1\n            -motionTrails 1\n            -shadows 0\n            $editorName;\n"
		+ "modelEditor -e -viewSelected 0 $editorName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextPanel \"modelPanel\" (localizedPanelLabel(\"Front View\")) `;\n\tif (\"\" == $panelName) {\n\t\tif ($useSceneConfig) {\n\t\t\t$panelName = `modelPanel -unParent -l (localizedPanelLabel(\"Front View\")) -mbv $menusOkayInPanels `;\n\t\t\t$editorName = $panelName;\n            modelEditor -e \n                -camera \"front\" \n                -useInteractiveMode 0\n                -displayLights \"default\" \n                -displayAppearance \"wireframe\" \n                -activeOnly 0\n                -ignorePanZoom 0\n                -wireframeOnShaded 0\n                -headsUpDisplay 1\n                -selectionHiliteDisplay 1\n                -useDefaultMaterial 0\n                -bufferMode \"double\" \n                -twoSidedLighting 1\n                -backfaceCulling 0\n                -xray 0\n                -jointXray 0\n                -activeComponentsXray 0\n                -displayTextures 0\n"
		+ "                -smoothWireframe 0\n                -lineWidth 1\n                -textureAnisotropic 0\n                -textureHilight 1\n                -textureSampling 2\n                -textureDisplay \"modulate\" \n                -textureMaxSize 16384\n                -fogging 0\n                -fogSource \"fragment\" \n                -fogMode \"linear\" \n                -fogStart 0\n                -fogEnd 100\n                -fogDensity 0.1\n                -fogColor 0.5 0.5 0.5 1 \n                -maxConstantTransparency 1\n                -rendererName \"base_OpenGL_Renderer\" \n                -objectFilterShowInHUD 1\n                -isFiltered 0\n                -colorResolution 256 256 \n                -bumpResolution 512 512 \n                -textureCompression 0\n                -transparencyAlgorithm \"frontAndBackCull\" \n                -transpInShadows 0\n                -cullingOverride \"none\" \n                -lowQualityLighting 0\n                -maximumNumHardwareLights 1\n                -occlusionCulling 0\n"
		+ "                -shadingModel 0\n                -useBaseRenderer 0\n                -useReducedRenderer 0\n                -smallObjectCulling 0\n                -smallObjectThreshold -1 \n                -interactiveDisableShadows 0\n                -interactiveBackFaceCull 0\n                -sortTransparent 1\n                -nurbsCurves 1\n                -nurbsSurfaces 1\n                -polymeshes 1\n                -subdivSurfaces 1\n                -planes 1\n                -lights 1\n                -cameras 1\n                -controlVertices 1\n                -hulls 1\n                -grid 1\n                -joints 1\n                -ikHandles 1\n                -deformers 1\n                -dynamics 1\n                -fluids 1\n                -hairSystems 1\n                -follicles 1\n                -nCloths 1\n                -nParticles 1\n                -nRigids 1\n                -dynamicConstraints 1\n                -locators 1\n                -manipulators 1\n                -dimensions 1\n                -handles 1\n"
		+ "                -pivots 1\n                -textures 1\n                -strokes 1\n                -motionTrails 1\n                -shadows 0\n                $editorName;\nmodelEditor -e -viewSelected 0 $editorName;\n\t\t}\n\t} else {\n\t\t$label = `panel -q -label $panelName`;\n\t\tmodelPanel -edit -l (localizedPanelLabel(\"Front View\")) -mbv $menusOkayInPanels  $panelName;\n\t\t$editorName = $panelName;\n        modelEditor -e \n            -camera \"front\" \n            -useInteractiveMode 0\n            -displayLights \"default\" \n            -displayAppearance \"wireframe\" \n            -activeOnly 0\n            -ignorePanZoom 0\n            -wireframeOnShaded 0\n            -headsUpDisplay 1\n            -selectionHiliteDisplay 1\n            -useDefaultMaterial 0\n            -bufferMode \"double\" \n            -twoSidedLighting 1\n            -backfaceCulling 0\n            -xray 0\n            -jointXray 0\n            -activeComponentsXray 0\n            -displayTextures 0\n            -smoothWireframe 0\n            -lineWidth 1\n            -textureAnisotropic 0\n"
		+ "            -textureHilight 1\n            -textureSampling 2\n            -textureDisplay \"modulate\" \n            -textureMaxSize 16384\n            -fogging 0\n            -fogSource \"fragment\" \n            -fogMode \"linear\" \n            -fogStart 0\n            -fogEnd 100\n            -fogDensity 0.1\n            -fogColor 0.5 0.5 0.5 1 \n            -maxConstantTransparency 1\n            -rendererName \"base_OpenGL_Renderer\" \n            -objectFilterShowInHUD 1\n            -isFiltered 0\n            -colorResolution 256 256 \n            -bumpResolution 512 512 \n            -textureCompression 0\n            -transparencyAlgorithm \"frontAndBackCull\" \n            -transpInShadows 0\n            -cullingOverride \"none\" \n            -lowQualityLighting 0\n            -maximumNumHardwareLights 1\n            -occlusionCulling 0\n            -shadingModel 0\n            -useBaseRenderer 0\n            -useReducedRenderer 0\n            -smallObjectCulling 0\n            -smallObjectThreshold -1 \n            -interactiveDisableShadows 0\n"
		+ "            -interactiveBackFaceCull 0\n            -sortTransparent 1\n            -nurbsCurves 1\n            -nurbsSurfaces 1\n            -polymeshes 1\n            -subdivSurfaces 1\n            -planes 1\n            -lights 1\n            -cameras 1\n            -controlVertices 1\n            -hulls 1\n            -grid 1\n            -joints 1\n            -ikHandles 1\n            -deformers 1\n            -dynamics 1\n            -fluids 1\n            -hairSystems 1\n            -follicles 1\n            -nCloths 1\n            -nParticles 1\n            -nRigids 1\n            -dynamicConstraints 1\n            -locators 1\n            -manipulators 1\n            -dimensions 1\n            -handles 1\n            -pivots 1\n            -textures 1\n            -strokes 1\n            -motionTrails 1\n            -shadows 0\n            $editorName;\nmodelEditor -e -viewSelected 0 $editorName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextPanel \"modelPanel\" (localizedPanelLabel(\"Persp View\")) `;\n"
		+ "\tif (\"\" == $panelName) {\n\t\tif ($useSceneConfig) {\n\t\t\t$panelName = `modelPanel -unParent -l (localizedPanelLabel(\"Persp View\")) -mbv $menusOkayInPanels `;\n\t\t\t$editorName = $panelName;\n            modelEditor -e \n                -camera \"front\" \n                -useInteractiveMode 0\n                -displayLights \"default\" \n                -displayAppearance \"smoothShaded\" \n                -activeOnly 0\n                -ignorePanZoom 0\n                -wireframeOnShaded 0\n                -headsUpDisplay 1\n                -selectionHiliteDisplay 1\n                -useDefaultMaterial 0\n                -bufferMode \"double\" \n                -twoSidedLighting 1\n                -backfaceCulling 0\n                -xray 0\n                -jointXray 0\n                -activeComponentsXray 0\n                -displayTextures 0\n                -smoothWireframe 0\n                -lineWidth 1\n                -textureAnisotropic 0\n                -textureHilight 1\n                -textureSampling 2\n                -textureDisplay \"modulate\" \n"
		+ "                -textureMaxSize 16384\n                -fogging 0\n                -fogSource \"fragment\" \n                -fogMode \"linear\" \n                -fogStart 0\n                -fogEnd 100\n                -fogDensity 0.1\n                -fogColor 0.5 0.5 0.5 1 \n                -maxConstantTransparency 1\n                -rendererName \"base_OpenGL_Renderer\" \n                -objectFilterShowInHUD 1\n                -isFiltered 0\n                -colorResolution 256 256 \n                -bumpResolution 512 512 \n                -textureCompression 0\n                -transparencyAlgorithm \"frontAndBackCull\" \n                -transpInShadows 0\n                -cullingOverride \"none\" \n                -lowQualityLighting 0\n                -maximumNumHardwareLights 1\n                -occlusionCulling 0\n                -shadingModel 0\n                -useBaseRenderer 0\n                -useReducedRenderer 0\n                -smallObjectCulling 0\n                -smallObjectThreshold -1 \n                -interactiveDisableShadows 0\n"
		+ "                -interactiveBackFaceCull 0\n                -sortTransparent 1\n                -nurbsCurves 1\n                -nurbsSurfaces 1\n                -polymeshes 1\n                -subdivSurfaces 1\n                -planes 1\n                -lights 1\n                -cameras 1\n                -controlVertices 1\n                -hulls 1\n                -grid 1\n                -joints 1\n                -ikHandles 1\n                -deformers 1\n                -dynamics 1\n                -fluids 1\n                -hairSystems 1\n                -follicles 1\n                -nCloths 1\n                -nParticles 1\n                -nRigids 1\n                -dynamicConstraints 1\n                -locators 1\n                -manipulators 1\n                -dimensions 1\n                -handles 1\n                -pivots 1\n                -textures 1\n                -strokes 1\n                -motionTrails 1\n                -shadows 0\n                $editorName;\nmodelEditor -e -viewSelected 0 $editorName;\n\t\t}\n\t} else {\n"
		+ "\t\t$label = `panel -q -label $panelName`;\n\t\tmodelPanel -edit -l (localizedPanelLabel(\"Persp View\")) -mbv $menusOkayInPanels  $panelName;\n\t\t$editorName = $panelName;\n        modelEditor -e \n            -camera \"front\" \n            -useInteractiveMode 0\n            -displayLights \"default\" \n            -displayAppearance \"smoothShaded\" \n            -activeOnly 0\n            -ignorePanZoom 0\n            -wireframeOnShaded 0\n            -headsUpDisplay 1\n            -selectionHiliteDisplay 1\n            -useDefaultMaterial 0\n            -bufferMode \"double\" \n            -twoSidedLighting 1\n            -backfaceCulling 0\n            -xray 0\n            -jointXray 0\n            -activeComponentsXray 0\n            -displayTextures 0\n            -smoothWireframe 0\n            -lineWidth 1\n            -textureAnisotropic 0\n            -textureHilight 1\n            -textureSampling 2\n            -textureDisplay \"modulate\" \n            -textureMaxSize 16384\n            -fogging 0\n            -fogSource \"fragment\" \n            -fogMode \"linear\" \n"
		+ "            -fogStart 0\n            -fogEnd 100\n            -fogDensity 0.1\n            -fogColor 0.5 0.5 0.5 1 \n            -maxConstantTransparency 1\n            -rendererName \"base_OpenGL_Renderer\" \n            -objectFilterShowInHUD 1\n            -isFiltered 0\n            -colorResolution 256 256 \n            -bumpResolution 512 512 \n            -textureCompression 0\n            -transparencyAlgorithm \"frontAndBackCull\" \n            -transpInShadows 0\n            -cullingOverride \"none\" \n            -lowQualityLighting 0\n            -maximumNumHardwareLights 1\n            -occlusionCulling 0\n            -shadingModel 0\n            -useBaseRenderer 0\n            -useReducedRenderer 0\n            -smallObjectCulling 0\n            -smallObjectThreshold -1 \n            -interactiveDisableShadows 0\n            -interactiveBackFaceCull 0\n            -sortTransparent 1\n            -nurbsCurves 1\n            -nurbsSurfaces 1\n            -polymeshes 1\n            -subdivSurfaces 1\n            -planes 1\n            -lights 1\n"
		+ "            -cameras 1\n            -controlVertices 1\n            -hulls 1\n            -grid 1\n            -joints 1\n            -ikHandles 1\n            -deformers 1\n            -dynamics 1\n            -fluids 1\n            -hairSystems 1\n            -follicles 1\n            -nCloths 1\n            -nParticles 1\n            -nRigids 1\n            -dynamicConstraints 1\n            -locators 1\n            -manipulators 1\n            -dimensions 1\n            -handles 1\n            -pivots 1\n            -textures 1\n            -strokes 1\n            -motionTrails 1\n            -shadows 0\n            $editorName;\nmodelEditor -e -viewSelected 0 $editorName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextPanel \"outlinerPanel\" (localizedPanelLabel(\"Outliner\")) `;\n\tif (\"\" == $panelName) {\n\t\tif ($useSceneConfig) {\n\t\t\t$panelName = `outlinerPanel -unParent -l (localizedPanelLabel(\"Outliner\")) -mbv $menusOkayInPanels `;\n\t\t\t$editorName = $panelName;\n            outlinerEditor -e \n"
		+ "                -docTag \"isolOutln_fromSeln\" \n                -showShapes 0\n                -showAttributes 0\n                -showConnected 0\n                -showAnimCurvesOnly 0\n                -showMuteInfo 0\n                -organizeByLayer 1\n                -showAnimLayerWeight 1\n                -autoExpandLayers 1\n                -autoExpand 0\n                -showDagOnly 0\n                -showAssets 1\n                -showContainedOnly 1\n                -showPublishedAsConnected 0\n                -showContainerContents 1\n                -ignoreDagHierarchy 0\n                -expandConnections 0\n                -showUpstreamCurves 1\n                -showUnitlessCurves 1\n                -showCompounds 1\n                -showLeafs 1\n                -showNumericAttrsOnly 0\n                -highlightActive 1\n                -autoSelectNewObjects 0\n                -doNotSelectNewObjects 0\n                -dropIsParent 1\n                -transmitFilters 0\n                -setFilter \"defaultSetFilter\" \n                -showSetMembers 1\n"
		+ "                -allowMultiSelection 1\n                -alwaysToggleSelect 0\n                -directSelect 0\n                -displayMode \"DAG\" \n                -expandObjects 0\n                -setsIgnoreFilters 1\n                -containersIgnoreFilters 0\n                -editAttrName 0\n                -showAttrValues 0\n                -highlightSecondary 0\n                -showUVAttrsOnly 0\n                -showTextureNodesOnly 0\n                -attrAlphaOrder \"default\" \n                -animLayerFilterOptions \"allAffecting\" \n                -sortOrder \"none\" \n                -longNames 0\n                -niceNames 1\n                -showNamespace 1\n                -showPinIcons 0\n                -mapMotionTrails 0\n                $editorName;\n\t\t}\n\t} else {\n\t\t$label = `panel -q -label $panelName`;\n\t\toutlinerPanel -edit -l (localizedPanelLabel(\"Outliner\")) -mbv $menusOkayInPanels  $panelName;\n\t\t$editorName = $panelName;\n        outlinerEditor -e \n            -docTag \"isolOutln_fromSeln\" \n            -showShapes 0\n"
		+ "            -showAttributes 0\n            -showConnected 0\n            -showAnimCurvesOnly 0\n            -showMuteInfo 0\n            -organizeByLayer 1\n            -showAnimLayerWeight 1\n            -autoExpandLayers 1\n            -autoExpand 0\n            -showDagOnly 0\n            -showAssets 1\n            -showContainedOnly 1\n            -showPublishedAsConnected 0\n            -showContainerContents 1\n            -ignoreDagHierarchy 0\n            -expandConnections 0\n            -showUpstreamCurves 1\n            -showUnitlessCurves 1\n            -showCompounds 1\n            -showLeafs 1\n            -showNumericAttrsOnly 0\n            -highlightActive 1\n            -autoSelectNewObjects 0\n            -doNotSelectNewObjects 0\n            -dropIsParent 1\n            -transmitFilters 0\n            -setFilter \"defaultSetFilter\" \n            -showSetMembers 1\n            -allowMultiSelection 1\n            -alwaysToggleSelect 0\n            -directSelect 0\n            -displayMode \"DAG\" \n            -expandObjects 0\n"
		+ "            -setsIgnoreFilters 1\n            -containersIgnoreFilters 0\n            -editAttrName 0\n            -showAttrValues 0\n            -highlightSecondary 0\n            -showUVAttrsOnly 0\n            -showTextureNodesOnly 0\n            -attrAlphaOrder \"default\" \n            -animLayerFilterOptions \"allAffecting\" \n            -sortOrder \"none\" \n            -longNames 0\n            -niceNames 1\n            -showNamespace 1\n            -showPinIcons 0\n            -mapMotionTrails 0\n            $editorName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"graphEditor\" (localizedPanelLabel(\"Graph Editor\")) `;\n\tif (\"\" == $panelName) {\n\t\tif ($useSceneConfig) {\n\t\t\t$panelName = `scriptedPanel -unParent  -type \"graphEditor\" -l (localizedPanelLabel(\"Graph Editor\")) -mbv $menusOkayInPanels `;\n\n\t\t\t$editorName = ($panelName+\"OutlineEd\");\n            outlinerEditor -e \n                -showShapes 1\n                -showAttributes 1\n                -showConnected 1\n"
		+ "                -showAnimCurvesOnly 1\n                -showMuteInfo 0\n                -organizeByLayer 1\n                -showAnimLayerWeight 1\n                -autoExpandLayers 1\n                -autoExpand 1\n                -showDagOnly 0\n                -showAssets 1\n                -showContainedOnly 0\n                -showPublishedAsConnected 0\n                -showContainerContents 0\n                -ignoreDagHierarchy 0\n                -expandConnections 1\n                -showUpstreamCurves 1\n                -showUnitlessCurves 1\n                -showCompounds 0\n                -showLeafs 1\n                -showNumericAttrsOnly 1\n                -highlightActive 0\n                -autoSelectNewObjects 1\n                -doNotSelectNewObjects 0\n                -dropIsParent 1\n                -transmitFilters 1\n                -setFilter \"0\" \n                -showSetMembers 0\n                -allowMultiSelection 1\n                -alwaysToggleSelect 0\n                -directSelect 0\n                -displayMode \"DAG\" \n"
		+ "                -expandObjects 0\n                -setsIgnoreFilters 1\n                -containersIgnoreFilters 0\n                -editAttrName 0\n                -showAttrValues 0\n                -highlightSecondary 0\n                -showUVAttrsOnly 0\n                -showTextureNodesOnly 0\n                -attrAlphaOrder \"default\" \n                -animLayerFilterOptions \"allAffecting\" \n                -sortOrder \"none\" \n                -longNames 0\n                -niceNames 1\n                -showNamespace 1\n                -showPinIcons 1\n                -mapMotionTrails 1\n                $editorName;\n\n\t\t\t$editorName = ($panelName+\"GraphEd\");\n            animCurveEditor -e \n                -displayKeys 1\n                -displayTangents 0\n                -displayActiveKeys 0\n                -displayActiveKeyTangents 1\n                -displayInfinities 0\n                -autoFit 0\n                -snapTime \"integer\" \n                -snapValue \"none\" \n                -showResults \"off\" \n                -showBufferCurves \"off\" \n"
		+ "                -smoothness \"fine\" \n                -resultSamples 1\n                -resultScreenSamples 0\n                -resultUpdate \"delayed\" \n                -showUpstreamCurves 1\n                -stackedCurves 0\n                -stackedCurvesMin -1\n                -stackedCurvesMax 1\n                -stackedCurvesSpace 0.2\n                -displayNormalized 0\n                -preSelectionHighlight 1\n                -constrainDrag 0\n                -classicMode 1\n                $editorName;\n\t\t}\n\t} else {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Graph Editor\")) -mbv $menusOkayInPanels  $panelName;\n\n\t\t\t$editorName = ($panelName+\"OutlineEd\");\n            outlinerEditor -e \n                -showShapes 1\n                -showAttributes 1\n                -showConnected 1\n                -showAnimCurvesOnly 1\n                -showMuteInfo 0\n                -organizeByLayer 1\n                -showAnimLayerWeight 1\n                -autoExpandLayers 1\n                -autoExpand 1\n"
		+ "                -showDagOnly 0\n                -showAssets 1\n                -showContainedOnly 0\n                -showPublishedAsConnected 0\n                -showContainerContents 0\n                -ignoreDagHierarchy 0\n                -expandConnections 1\n                -showUpstreamCurves 1\n                -showUnitlessCurves 1\n                -showCompounds 0\n                -showLeafs 1\n                -showNumericAttrsOnly 1\n                -highlightActive 0\n                -autoSelectNewObjects 1\n                -doNotSelectNewObjects 0\n                -dropIsParent 1\n                -transmitFilters 1\n                -setFilter \"0\" \n                -showSetMembers 0\n                -allowMultiSelection 1\n                -alwaysToggleSelect 0\n                -directSelect 0\n                -displayMode \"DAG\" \n                -expandObjects 0\n                -setsIgnoreFilters 1\n                -containersIgnoreFilters 0\n                -editAttrName 0\n                -showAttrValues 0\n                -highlightSecondary 0\n"
		+ "                -showUVAttrsOnly 0\n                -showTextureNodesOnly 0\n                -attrAlphaOrder \"default\" \n                -animLayerFilterOptions \"allAffecting\" \n                -sortOrder \"none\" \n                -longNames 0\n                -niceNames 1\n                -showNamespace 1\n                -showPinIcons 1\n                -mapMotionTrails 1\n                $editorName;\n\n\t\t\t$editorName = ($panelName+\"GraphEd\");\n            animCurveEditor -e \n                -displayKeys 1\n                -displayTangents 0\n                -displayActiveKeys 0\n                -displayActiveKeyTangents 1\n                -displayInfinities 0\n                -autoFit 0\n                -snapTime \"integer\" \n                -snapValue \"none\" \n                -showResults \"off\" \n                -showBufferCurves \"off\" \n                -smoothness \"fine\" \n                -resultSamples 1\n                -resultScreenSamples 0\n                -resultUpdate \"delayed\" \n                -showUpstreamCurves 1\n                -stackedCurves 0\n"
		+ "                -stackedCurvesMin -1\n                -stackedCurvesMax 1\n                -stackedCurvesSpace 0.2\n                -displayNormalized 0\n                -preSelectionHighlight 1\n                -constrainDrag 0\n                -classicMode 1\n                $editorName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"dopeSheetPanel\" (localizedPanelLabel(\"Dope Sheet\")) `;\n\tif (\"\" == $panelName) {\n\t\tif ($useSceneConfig) {\n\t\t\t$panelName = `scriptedPanel -unParent  -type \"dopeSheetPanel\" -l (localizedPanelLabel(\"Dope Sheet\")) -mbv $menusOkayInPanels `;\n\n\t\t\t$editorName = ($panelName+\"OutlineEd\");\n            outlinerEditor -e \n                -showShapes 1\n                -showAttributes 1\n                -showConnected 1\n                -showAnimCurvesOnly 1\n                -showMuteInfo 0\n                -organizeByLayer 1\n                -showAnimLayerWeight 1\n                -autoExpandLayers 1\n                -autoExpand 0\n"
		+ "                -showDagOnly 0\n                -showAssets 1\n                -showContainedOnly 0\n                -showPublishedAsConnected 0\n                -showContainerContents 0\n                -ignoreDagHierarchy 0\n                -expandConnections 1\n                -showUpstreamCurves 1\n                -showUnitlessCurves 0\n                -showCompounds 1\n                -showLeafs 1\n                -showNumericAttrsOnly 1\n                -highlightActive 0\n                -autoSelectNewObjects 0\n                -doNotSelectNewObjects 1\n                -dropIsParent 1\n                -transmitFilters 0\n                -setFilter \"0\" \n                -showSetMembers 0\n                -allowMultiSelection 1\n                -alwaysToggleSelect 0\n                -directSelect 0\n                -displayMode \"DAG\" \n                -expandObjects 0\n                -setsIgnoreFilters 1\n                -containersIgnoreFilters 0\n                -editAttrName 0\n                -showAttrValues 0\n                -highlightSecondary 0\n"
		+ "                -showUVAttrsOnly 0\n                -showTextureNodesOnly 0\n                -attrAlphaOrder \"default\" \n                -animLayerFilterOptions \"allAffecting\" \n                -sortOrder \"none\" \n                -longNames 0\n                -niceNames 1\n                -showNamespace 1\n                -showPinIcons 0\n                -mapMotionTrails 1\n                $editorName;\n\n\t\t\t$editorName = ($panelName+\"DopeSheetEd\");\n            dopeSheetEditor -e \n                -displayKeys 1\n                -displayTangents 0\n                -displayActiveKeys 0\n                -displayActiveKeyTangents 0\n                -displayInfinities 0\n                -autoFit 0\n                -snapTime \"integer\" \n                -snapValue \"none\" \n                -outliner \"dopeSheetPanel1OutlineEd\" \n                -showSummary 1\n                -showScene 0\n                -hierarchyBelow 0\n                -showTicks 1\n                -selectionWindow 0 0 0 0 \n                $editorName;\n\t\t}\n\t} else {\n\t\t$label = `panel -q -label $panelName`;\n"
		+ "\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Dope Sheet\")) -mbv $menusOkayInPanels  $panelName;\n\n\t\t\t$editorName = ($panelName+\"OutlineEd\");\n            outlinerEditor -e \n                -showShapes 1\n                -showAttributes 1\n                -showConnected 1\n                -showAnimCurvesOnly 1\n                -showMuteInfo 0\n                -organizeByLayer 1\n                -showAnimLayerWeight 1\n                -autoExpandLayers 1\n                -autoExpand 0\n                -showDagOnly 0\n                -showAssets 1\n                -showContainedOnly 0\n                -showPublishedAsConnected 0\n                -showContainerContents 0\n                -ignoreDagHierarchy 0\n                -expandConnections 1\n                -showUpstreamCurves 1\n                -showUnitlessCurves 0\n                -showCompounds 1\n                -showLeafs 1\n                -showNumericAttrsOnly 1\n                -highlightActive 0\n                -autoSelectNewObjects 0\n                -doNotSelectNewObjects 1\n"
		+ "                -dropIsParent 1\n                -transmitFilters 0\n                -setFilter \"0\" \n                -showSetMembers 0\n                -allowMultiSelection 1\n                -alwaysToggleSelect 0\n                -directSelect 0\n                -displayMode \"DAG\" \n                -expandObjects 0\n                -setsIgnoreFilters 1\n                -containersIgnoreFilters 0\n                -editAttrName 0\n                -showAttrValues 0\n                -highlightSecondary 0\n                -showUVAttrsOnly 0\n                -showTextureNodesOnly 0\n                -attrAlphaOrder \"default\" \n                -animLayerFilterOptions \"allAffecting\" \n                -sortOrder \"none\" \n                -longNames 0\n                -niceNames 1\n                -showNamespace 1\n                -showPinIcons 0\n                -mapMotionTrails 1\n                $editorName;\n\n\t\t\t$editorName = ($panelName+\"DopeSheetEd\");\n            dopeSheetEditor -e \n                -displayKeys 1\n                -displayTangents 0\n"
		+ "                -displayActiveKeys 0\n                -displayActiveKeyTangents 0\n                -displayInfinities 0\n                -autoFit 0\n                -snapTime \"integer\" \n                -snapValue \"none\" \n                -outliner \"dopeSheetPanel1OutlineEd\" \n                -showSummary 1\n                -showScene 0\n                -hierarchyBelow 0\n                -showTicks 1\n                -selectionWindow 0 0 0 0 \n                $editorName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"clipEditorPanel\" (localizedPanelLabel(\"Trax Editor\")) `;\n\tif (\"\" == $panelName) {\n\t\tif ($useSceneConfig) {\n\t\t\t$panelName = `scriptedPanel -unParent  -type \"clipEditorPanel\" -l (localizedPanelLabel(\"Trax Editor\")) -mbv $menusOkayInPanels `;\n\n\t\t\t$editorName = clipEditorNameFromPanel($panelName);\n            clipEditor -e \n                -displayKeys 0\n                -displayTangents 0\n                -displayActiveKeys 0\n                -displayActiveKeyTangents 0\n"
		+ "                -displayInfinities 0\n                -autoFit 0\n                -snapTime \"none\" \n                -snapValue \"none\" \n                -manageSequencer 0 \n                $editorName;\n\t\t}\n\t} else {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Trax Editor\")) -mbv $menusOkayInPanels  $panelName;\n\n\t\t\t$editorName = clipEditorNameFromPanel($panelName);\n            clipEditor -e \n                -displayKeys 0\n                -displayTangents 0\n                -displayActiveKeys 0\n                -displayActiveKeyTangents 0\n                -displayInfinities 0\n                -autoFit 0\n                -snapTime \"none\" \n                -snapValue \"none\" \n                -manageSequencer 0 \n                $editorName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"sequenceEditorPanel\" (localizedPanelLabel(\"Camera Sequencer\")) `;\n\tif (\"\" == $panelName) {\n\t\tif ($useSceneConfig) {\n\t\t\t$panelName = `scriptedPanel -unParent  -type \"sequenceEditorPanel\" -l (localizedPanelLabel(\"Camera Sequencer\")) -mbv $menusOkayInPanels `;\n"
		+ "\t\t\t$editorName = sequenceEditorNameFromPanel($panelName);\n            clipEditor -e \n                -displayKeys 0\n                -displayTangents 0\n                -displayActiveKeys 0\n                -displayActiveKeyTangents 0\n                -displayInfinities 0\n                -autoFit 0\n                -snapTime \"none\" \n                -snapValue \"none\" \n                -manageSequencer 1 \n                $editorName;\n\t\t}\n\t} else {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Camera Sequencer\")) -mbv $menusOkayInPanels  $panelName;\n\n\t\t\t$editorName = sequenceEditorNameFromPanel($panelName);\n            clipEditor -e \n                -displayKeys 0\n                -displayTangents 0\n                -displayActiveKeys 0\n                -displayActiveKeyTangents 0\n                -displayInfinities 0\n                -autoFit 0\n                -snapTime \"none\" \n                -snapValue \"none\" \n                -manageSequencer 1 \n                $editorName;\n\t\tif (!$useSceneConfig) {\n"
		+ "\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"hyperGraphPanel\" (localizedPanelLabel(\"Hypergraph Hierarchy\")) `;\n\tif (\"\" == $panelName) {\n\t\tif ($useSceneConfig) {\n\t\t\t$panelName = `scriptedPanel -unParent  -type \"hyperGraphPanel\" -l (localizedPanelLabel(\"Hypergraph Hierarchy\")) -mbv $menusOkayInPanels `;\n\n\t\t\t$editorName = ($panelName+\"HyperGraphEd\");\n            hyperGraph -e \n                -graphLayoutStyle \"hierarchicalLayout\" \n                -orientation \"horiz\" \n                -mergeConnections 0\n                -zoom 0.84729\n                -animateTransition 0\n                -showRelationships 1\n                -showShapes 0\n                -showDeformers 0\n                -showExpressions 0\n                -showConstraints 0\n                -showUnderworld 0\n                -showInvisible 1\n                -transitionFrames 5\n                -currentNode \"placement_tmpCtrl\" \n                -opaqueContainers 0\n                -freeform 0\n                -imagePosition 0 0 \n"
		+ "                -imageScale 1\n                -imageEnabled 0\n                -graphType \"DAG\" \n                -heatMapDisplay 0\n                -updateSelection 1\n                -updateNodeAdded 1\n                -useDrawOverrideColor 0\n                -limitGraphTraversal -1\n                -range 0 0 \n                -iconSize \"largeIcons\" \n                -showCachedConnections 0\n                $editorName;\n\t\t}\n\t} else {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Hypergraph Hierarchy\")) -mbv $menusOkayInPanels  $panelName;\n\n\t\t\t$editorName = ($panelName+\"HyperGraphEd\");\n            hyperGraph -e \n                -graphLayoutStyle \"hierarchicalLayout\" \n                -orientation \"horiz\" \n                -mergeConnections 0\n                -zoom 0.84729\n                -animateTransition 0\n                -showRelationships 1\n                -showShapes 0\n                -showDeformers 0\n                -showExpressions 0\n                -showConstraints 0\n                -showUnderworld 0\n"
		+ "                -showInvisible 1\n                -transitionFrames 5\n                -currentNode \"placement_tmpCtrl\" \n                -opaqueContainers 0\n                -freeform 0\n                -imagePosition 0 0 \n                -imageScale 1\n                -imageEnabled 0\n                -graphType \"DAG\" \n                -heatMapDisplay 0\n                -updateSelection 1\n                -updateNodeAdded 1\n                -useDrawOverrideColor 0\n                -limitGraphTraversal -1\n                -range 0 0 \n                -iconSize \"largeIcons\" \n                -showCachedConnections 0\n                $editorName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"hyperShadePanel\" (localizedPanelLabel(\"Hypershade\")) `;\n\tif (\"\" == $panelName) {\n\t\tif ($useSceneConfig) {\n\t\t\t$panelName = `scriptedPanel -unParent  -type \"hyperShadePanel\" -l (localizedPanelLabel(\"Hypershade\")) -mbv $menusOkayInPanels `;\n\t\t}\n\t} else {\n\t\t$label = `panel -q -label $panelName`;\n"
		+ "\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Hypershade\")) -mbv $menusOkayInPanels  $panelName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"visorPanel\" (localizedPanelLabel(\"Visor\")) `;\n\tif (\"\" == $panelName) {\n\t\tif ($useSceneConfig) {\n\t\t\t$panelName = `scriptedPanel -unParent  -type \"visorPanel\" -l (localizedPanelLabel(\"Visor\")) -mbv $menusOkayInPanels `;\n\t\t}\n\t} else {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Visor\")) -mbv $menusOkayInPanels  $panelName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"createNodePanel\" (localizedPanelLabel(\"Create Node\")) `;\n\tif (\"\" == $panelName) {\n\t\tif ($useSceneConfig) {\n\t\t\t$panelName = `scriptedPanel -unParent  -type \"createNodePanel\" -l (localizedPanelLabel(\"Create Node\")) -mbv $menusOkayInPanels `;\n\t\t}\n\t} else {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Create Node\")) -mbv $menusOkayInPanels  $panelName;\n"
		+ "\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"polyTexturePlacementPanel\" (localizedPanelLabel(\"UV Texture Editor\")) `;\n\tif (\"\" == $panelName) {\n\t\tif ($useSceneConfig) {\n\t\t\t$panelName = `scriptedPanel -unParent  -type \"polyTexturePlacementPanel\" -l (localizedPanelLabel(\"UV Texture Editor\")) -mbv $menusOkayInPanels `;\n\t\t}\n\t} else {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"UV Texture Editor\")) -mbv $menusOkayInPanels  $panelName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"renderWindowPanel\" (localizedPanelLabel(\"Render View\")) `;\n\tif (\"\" == $panelName) {\n\t\tif ($useSceneConfig) {\n\t\t\t$panelName = `scriptedPanel -unParent  -type \"renderWindowPanel\" -l (localizedPanelLabel(\"Render View\")) -mbv $menusOkayInPanels `;\n\t\t}\n\t} else {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Render View\")) -mbv $menusOkayInPanels  $panelName;\n"
		+ "\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextPanel \"blendShapePanel\" (localizedPanelLabel(\"Blend Shape\")) `;\n\tif (\"\" == $panelName) {\n\t\tif ($useSceneConfig) {\n\t\t\tblendShapePanel -unParent -l (localizedPanelLabel(\"Blend Shape\")) -mbv $menusOkayInPanels ;\n\t\t}\n\t} else {\n\t\t$label = `panel -q -label $panelName`;\n\t\tblendShapePanel -edit -l (localizedPanelLabel(\"Blend Shape\")) -mbv $menusOkayInPanels  $panelName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"dynRelEdPanel\" (localizedPanelLabel(\"Dynamic Relationships\")) `;\n\tif (\"\" == $panelName) {\n\t\tif ($useSceneConfig) {\n\t\t\t$panelName = `scriptedPanel -unParent  -type \"dynRelEdPanel\" -l (localizedPanelLabel(\"Dynamic Relationships\")) -mbv $menusOkayInPanels `;\n\t\t}\n\t} else {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Dynamic Relationships\")) -mbv $menusOkayInPanels  $panelName;\n\t\tif (!$useSceneConfig) {\n"
		+ "\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"relationshipPanel\" (localizedPanelLabel(\"Relationship Editor\")) `;\n\tif (\"\" == $panelName) {\n\t\tif ($useSceneConfig) {\n\t\t\t$panelName = `scriptedPanel -unParent  -type \"relationshipPanel\" -l (localizedPanelLabel(\"Relationship Editor\")) -mbv $menusOkayInPanels `;\n\t\t}\n\t} else {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Relationship Editor\")) -mbv $menusOkayInPanels  $panelName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"referenceEditorPanel\" (localizedPanelLabel(\"Reference Editor\")) `;\n\tif (\"\" == $panelName) {\n\t\tif ($useSceneConfig) {\n\t\t\t$panelName = `scriptedPanel -unParent  -type \"referenceEditorPanel\" -l (localizedPanelLabel(\"Reference Editor\")) -mbv $menusOkayInPanels `;\n\t\t}\n\t} else {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Reference Editor\")) -mbv $menusOkayInPanels  $panelName;\n"
		+ "\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"componentEditorPanel\" (localizedPanelLabel(\"Component Editor\")) `;\n\tif (\"\" == $panelName) {\n\t\tif ($useSceneConfig) {\n\t\t\t$panelName = `scriptedPanel -unParent  -type \"componentEditorPanel\" -l (localizedPanelLabel(\"Component Editor\")) -mbv $menusOkayInPanels `;\n\t\t}\n\t} else {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Component Editor\")) -mbv $menusOkayInPanels  $panelName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"dynPaintScriptedPanelType\" (localizedPanelLabel(\"Paint Effects\")) `;\n\tif (\"\" == $panelName) {\n\t\tif ($useSceneConfig) {\n\t\t\t$panelName = `scriptedPanel -unParent  -type \"dynPaintScriptedPanelType\" -l (localizedPanelLabel(\"Paint Effects\")) -mbv $menusOkayInPanels `;\n\t\t}\n\t} else {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Paint Effects\")) -mbv $menusOkayInPanels  $panelName;\n"
		+ "\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"scriptEditorPanel\" (localizedPanelLabel(\"Script Editor\")) `;\n\tif (\"\" == $panelName) {\n\t\tif ($useSceneConfig) {\n\t\t\t$panelName = `scriptedPanel -unParent  -type \"scriptEditorPanel\" -l (localizedPanelLabel(\"Script Editor\")) -mbv $menusOkayInPanels `;\n\t\t}\n\t} else {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Script Editor\")) -mbv $menusOkayInPanels  $panelName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"delightShaderAssignmentPanel\" (localizedPanelLabel(\"3Delight Assignment\")) `;\n\tif (\"\" == $panelName) {\n\t\tif ($useSceneConfig) {\n\t\t\t$panelName = `scriptedPanel -unParent  -type \"delightShaderAssignmentPanel\" -l (localizedPanelLabel(\"3Delight Assignment\")) -mbv $menusOkayInPanels `;\n\t\t}\n\t} else {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"3Delight Assignment\")) -mbv $menusOkayInPanels  $panelName;\n"
		+ "\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"delightExplorerPanel\" (localizedPanelLabel(\"3Delight Relationship Editor\")) `;\n\tif (\"\" == $panelName) {\n\t\tif ($useSceneConfig) {\n\t\t\t$panelName = `scriptedPanel -unParent  -type \"delightExplorerPanel\" -l (localizedPanelLabel(\"3Delight Relationship Editor\")) -mbv $menusOkayInPanels `;\n\t\t}\n\t} else {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"3Delight Relationship Editor\")) -mbv $menusOkayInPanels  $panelName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextPanel \"modelPanel\" (localizedPanelLabel(\"Model Panel5\")) `;\n\tif (\"\" == $panelName) {\n\t\tif ($useSceneConfig) {\n\t\t\t$panelName = `modelPanel -unParent -l (localizedPanelLabel(\"Model Panel5\")) -mbv $menusOkayInPanels `;\n\t\t\t$editorName = $panelName;\n            modelEditor -e \n                -camera \"persp\" \n                -useInteractiveMode 0\n"
		+ "                -displayLights \"default\" \n                -displayAppearance \"smoothShaded\" \n                -activeOnly 0\n                -ignorePanZoom 0\n                -wireframeOnShaded 0\n                -headsUpDisplay 1\n                -selectionHiliteDisplay 1\n                -useDefaultMaterial 0\n                -bufferMode \"double\" \n                -twoSidedLighting 1\n                -backfaceCulling 0\n                -xray 0\n                -jointXray 0\n                -activeComponentsXray 0\n                -displayTextures 0\n                -smoothWireframe 0\n                -lineWidth 1\n                -textureAnisotropic 0\n                -textureHilight 1\n                -textureSampling 2\n                -textureDisplay \"modulate\" \n                -textureMaxSize 16384\n                -fogging 0\n                -fogSource \"fragment\" \n                -fogMode \"linear\" \n                -fogStart 0\n                -fogEnd 100\n                -fogDensity 0.1\n                -fogColor 0.5 0.5 0.5 1 \n"
		+ "                -maxConstantTransparency 1\n                -rendererName \"base_OpenGL_Renderer\" \n                -objectFilterShowInHUD 1\n                -isFiltered 0\n                -colorResolution 256 256 \n                -bumpResolution 512 512 \n                -textureCompression 0\n                -transparencyAlgorithm \"frontAndBackCull\" \n                -transpInShadows 0\n                -cullingOverride \"none\" \n                -lowQualityLighting 0\n                -maximumNumHardwareLights 1\n                -occlusionCulling 0\n                -shadingModel 0\n                -useBaseRenderer 0\n                -useReducedRenderer 0\n                -smallObjectCulling 0\n                -smallObjectThreshold -1 \n                -interactiveDisableShadows 0\n                -interactiveBackFaceCull 0\n                -sortTransparent 1\n                -nurbsCurves 1\n                -nurbsSurfaces 1\n                -polymeshes 1\n                -subdivSurfaces 1\n                -planes 1\n                -lights 1\n"
		+ "                -cameras 1\n                -controlVertices 1\n                -hulls 1\n                -grid 1\n                -joints 1\n                -ikHandles 1\n                -deformers 1\n                -dynamics 1\n                -fluids 1\n                -hairSystems 1\n                -follicles 1\n                -nCloths 1\n                -nParticles 1\n                -nRigids 1\n                -dynamicConstraints 1\n                -locators 1\n                -manipulators 1\n                -dimensions 1\n                -handles 1\n                -pivots 1\n                -textures 1\n                -strokes 1\n                -motionTrails 1\n                -shadows 0\n                $editorName;\nmodelEditor -e -viewSelected 0 $editorName;\n\t\t}\n\t} else {\n\t\t$label = `panel -q -label $panelName`;\n\t\tmodelPanel -edit -l (localizedPanelLabel(\"Model Panel5\")) -mbv $menusOkayInPanels  $panelName;\n\t\t$editorName = $panelName;\n        modelEditor -e \n            -camera \"persp\" \n            -useInteractiveMode 0\n"
		+ "            -displayLights \"default\" \n            -displayAppearance \"smoothShaded\" \n            -activeOnly 0\n            -ignorePanZoom 0\n            -wireframeOnShaded 0\n            -headsUpDisplay 1\n            -selectionHiliteDisplay 1\n            -useDefaultMaterial 0\n            -bufferMode \"double\" \n            -twoSidedLighting 1\n            -backfaceCulling 0\n            -xray 0\n            -jointXray 0\n            -activeComponentsXray 0\n            -displayTextures 0\n            -smoothWireframe 0\n            -lineWidth 1\n            -textureAnisotropic 0\n            -textureHilight 1\n            -textureSampling 2\n            -textureDisplay \"modulate\" \n            -textureMaxSize 16384\n            -fogging 0\n            -fogSource \"fragment\" \n            -fogMode \"linear\" \n            -fogStart 0\n            -fogEnd 100\n            -fogDensity 0.1\n            -fogColor 0.5 0.5 0.5 1 \n            -maxConstantTransparency 1\n            -rendererName \"base_OpenGL_Renderer\" \n            -objectFilterShowInHUD 1\n"
		+ "            -isFiltered 0\n            -colorResolution 256 256 \n            -bumpResolution 512 512 \n            -textureCompression 0\n            -transparencyAlgorithm \"frontAndBackCull\" \n            -transpInShadows 0\n            -cullingOverride \"none\" \n            -lowQualityLighting 0\n            -maximumNumHardwareLights 1\n            -occlusionCulling 0\n            -shadingModel 0\n            -useBaseRenderer 0\n            -useReducedRenderer 0\n            -smallObjectCulling 0\n            -smallObjectThreshold -1 \n            -interactiveDisableShadows 0\n            -interactiveBackFaceCull 0\n            -sortTransparent 1\n            -nurbsCurves 1\n            -nurbsSurfaces 1\n            -polymeshes 1\n            -subdivSurfaces 1\n            -planes 1\n            -lights 1\n            -cameras 1\n            -controlVertices 1\n            -hulls 1\n            -grid 1\n            -joints 1\n            -ikHandles 1\n            -deformers 1\n            -dynamics 1\n            -fluids 1\n            -hairSystems 1\n"
		+ "            -follicles 1\n            -nCloths 1\n            -nParticles 1\n            -nRigids 1\n            -dynamicConstraints 1\n            -locators 1\n            -manipulators 1\n            -dimensions 1\n            -handles 1\n            -pivots 1\n            -textures 1\n            -strokes 1\n            -motionTrails 1\n            -shadows 0\n            $editorName;\nmodelEditor -e -viewSelected 0 $editorName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\tif ($useSceneConfig) {\n\t\tmodelPanel -e -to $panelName;\n\t}\n\n\n\tif ($useSceneConfig) {\n        string $configName = `getPanel -cwl (localizedPanelLabel(\"Current Layout\"))`;\n        if (\"\" != $configName) {\n\t\t\tpanelConfiguration -edit -label (localizedPanelLabel(\"Current Layout\")) \n\t\t\t\t-defaultImage \"\"\n\t\t\t\t-image \"\"\n\t\t\t\t-sc false\n\t\t\t\t-configString \"global string $gMainPane; paneLayout -e -cn \\\"vertical2\\\" -ps 1 53 100 -ps 2 47 100 $gMainPane;\"\n\t\t\t\t-removeAllPanels\n\t\t\t\t-ap false\n\t\t\t\t\t(localizedPanelLabel(\"Hypergraph Hierarchy\")) \n\t\t\t\t\t\"scriptedPanel\"\n"
		+ "\t\t\t\t\t\"$panelName = `scriptedPanel -unParent  -type \\\"hyperGraphPanel\\\" -l (localizedPanelLabel(\\\"Hypergraph Hierarchy\\\")) -mbv $menusOkayInPanels `;\\n\\n\\t\\t\\t$editorName = ($panelName+\\\"HyperGraphEd\\\");\\n            hyperGraph -e \\n                -graphLayoutStyle \\\"hierarchicalLayout\\\" \\n                -orientation \\\"horiz\\\" \\n                -mergeConnections 0\\n                -zoom 0.84729\\n                -animateTransition 0\\n                -showRelationships 1\\n                -showShapes 0\\n                -showDeformers 0\\n                -showExpressions 0\\n                -showConstraints 0\\n                -showUnderworld 0\\n                -showInvisible 1\\n                -transitionFrames 5\\n                -currentNode \\\"placement_tmpCtrl\\\" \\n                -opaqueContainers 0\\n                -freeform 0\\n                -imagePosition 0 0 \\n                -imageScale 1\\n                -imageEnabled 0\\n                -graphType \\\"DAG\\\" \\n                -heatMapDisplay 0\\n                -updateSelection 1\\n                -updateNodeAdded 1\\n                -useDrawOverrideColor 0\\n                -limitGraphTraversal -1\\n                -range 0 0 \\n                -iconSize \\\"largeIcons\\\" \\n                -showCachedConnections 0\\n                $editorName\"\n"
		+ "\t\t\t\t\t\"scriptedPanel -edit -l (localizedPanelLabel(\\\"Hypergraph Hierarchy\\\")) -mbv $menusOkayInPanels  $panelName;\\n\\n\\t\\t\\t$editorName = ($panelName+\\\"HyperGraphEd\\\");\\n            hyperGraph -e \\n                -graphLayoutStyle \\\"hierarchicalLayout\\\" \\n                -orientation \\\"horiz\\\" \\n                -mergeConnections 0\\n                -zoom 0.84729\\n                -animateTransition 0\\n                -showRelationships 1\\n                -showShapes 0\\n                -showDeformers 0\\n                -showExpressions 0\\n                -showConstraints 0\\n                -showUnderworld 0\\n                -showInvisible 1\\n                -transitionFrames 5\\n                -currentNode \\\"placement_tmpCtrl\\\" \\n                -opaqueContainers 0\\n                -freeform 0\\n                -imagePosition 0 0 \\n                -imageScale 1\\n                -imageEnabled 0\\n                -graphType \\\"DAG\\\" \\n                -heatMapDisplay 0\\n                -updateSelection 1\\n                -updateNodeAdded 1\\n                -useDrawOverrideColor 0\\n                -limitGraphTraversal -1\\n                -range 0 0 \\n                -iconSize \\\"largeIcons\\\" \\n                -showCachedConnections 0\\n                $editorName\"\n"
		+ "\t\t\t\t-ap false\n\t\t\t\t\t(localizedPanelLabel(\"Persp View\")) \n\t\t\t\t\t\"modelPanel\"\n"
		+ "\t\t\t\t\t\"$panelName = `modelPanel -unParent -l (localizedPanelLabel(\\\"Persp View\\\")) -mbv $menusOkayInPanels `;\\n$editorName = $panelName;\\nmodelEditor -e \\n    -camera \\\"front\\\" \\n    -useInteractiveMode 0\\n    -displayLights \\\"default\\\" \\n    -displayAppearance \\\"smoothShaded\\\" \\n    -activeOnly 0\\n    -ignorePanZoom 0\\n    -wireframeOnShaded 0\\n    -headsUpDisplay 1\\n    -selectionHiliteDisplay 1\\n    -useDefaultMaterial 0\\n    -bufferMode \\\"double\\\" \\n    -twoSidedLighting 1\\n    -backfaceCulling 0\\n    -xray 0\\n    -jointXray 0\\n    -activeComponentsXray 0\\n    -displayTextures 0\\n    -smoothWireframe 0\\n    -lineWidth 1\\n    -textureAnisotropic 0\\n    -textureHilight 1\\n    -textureSampling 2\\n    -textureDisplay \\\"modulate\\\" \\n    -textureMaxSize 16384\\n    -fogging 0\\n    -fogSource \\\"fragment\\\" \\n    -fogMode \\\"linear\\\" \\n    -fogStart 0\\n    -fogEnd 100\\n    -fogDensity 0.1\\n    -fogColor 0.5 0.5 0.5 1 \\n    -maxConstantTransparency 1\\n    -rendererName \\\"base_OpenGL_Renderer\\\" \\n    -objectFilterShowInHUD 1\\n    -isFiltered 0\\n    -colorResolution 256 256 \\n    -bumpResolution 512 512 \\n    -textureCompression 0\\n    -transparencyAlgorithm \\\"frontAndBackCull\\\" \\n    -transpInShadows 0\\n    -cullingOverride \\\"none\\\" \\n    -lowQualityLighting 0\\n    -maximumNumHardwareLights 1\\n    -occlusionCulling 0\\n    -shadingModel 0\\n    -useBaseRenderer 0\\n    -useReducedRenderer 0\\n    -smallObjectCulling 0\\n    -smallObjectThreshold -1 \\n    -interactiveDisableShadows 0\\n    -interactiveBackFaceCull 0\\n    -sortTransparent 1\\n    -nurbsCurves 1\\n    -nurbsSurfaces 1\\n    -polymeshes 1\\n    -subdivSurfaces 1\\n    -planes 1\\n    -lights 1\\n    -cameras 1\\n    -controlVertices 1\\n    -hulls 1\\n    -grid 1\\n    -joints 1\\n    -ikHandles 1\\n    -deformers 1\\n    -dynamics 1\\n    -fluids 1\\n    -hairSystems 1\\n    -follicles 1\\n    -nCloths 1\\n    -nParticles 1\\n    -nRigids 1\\n    -dynamicConstraints 1\\n    -locators 1\\n    -manipulators 1\\n    -dimensions 1\\n    -handles 1\\n    -pivots 1\\n    -textures 1\\n    -strokes 1\\n    -motionTrails 1\\n    -shadows 0\\n    $editorName;\\nmodelEditor -e -viewSelected 0 $editorName\"\n"
		+ "\t\t\t\t\t\"modelPanel -edit -l (localizedPanelLabel(\\\"Persp View\\\")) -mbv $menusOkayInPanels  $panelName;\\n$editorName = $panelName;\\nmodelEditor -e \\n    -camera \\\"front\\\" \\n    -useInteractiveMode 0\\n    -displayLights \\\"default\\\" \\n    -displayAppearance \\\"smoothShaded\\\" \\n    -activeOnly 0\\n    -ignorePanZoom 0\\n    -wireframeOnShaded 0\\n    -headsUpDisplay 1\\n    -selectionHiliteDisplay 1\\n    -useDefaultMaterial 0\\n    -bufferMode \\\"double\\\" \\n    -twoSidedLighting 1\\n    -backfaceCulling 0\\n    -xray 0\\n    -jointXray 0\\n    -activeComponentsXray 0\\n    -displayTextures 0\\n    -smoothWireframe 0\\n    -lineWidth 1\\n    -textureAnisotropic 0\\n    -textureHilight 1\\n    -textureSampling 2\\n    -textureDisplay \\\"modulate\\\" \\n    -textureMaxSize 16384\\n    -fogging 0\\n    -fogSource \\\"fragment\\\" \\n    -fogMode \\\"linear\\\" \\n    -fogStart 0\\n    -fogEnd 100\\n    -fogDensity 0.1\\n    -fogColor 0.5 0.5 0.5 1 \\n    -maxConstantTransparency 1\\n    -rendererName \\\"base_OpenGL_Renderer\\\" \\n    -objectFilterShowInHUD 1\\n    -isFiltered 0\\n    -colorResolution 256 256 \\n    -bumpResolution 512 512 \\n    -textureCompression 0\\n    -transparencyAlgorithm \\\"frontAndBackCull\\\" \\n    -transpInShadows 0\\n    -cullingOverride \\\"none\\\" \\n    -lowQualityLighting 0\\n    -maximumNumHardwareLights 1\\n    -occlusionCulling 0\\n    -shadingModel 0\\n    -useBaseRenderer 0\\n    -useReducedRenderer 0\\n    -smallObjectCulling 0\\n    -smallObjectThreshold -1 \\n    -interactiveDisableShadows 0\\n    -interactiveBackFaceCull 0\\n    -sortTransparent 1\\n    -nurbsCurves 1\\n    -nurbsSurfaces 1\\n    -polymeshes 1\\n    -subdivSurfaces 1\\n    -planes 1\\n    -lights 1\\n    -cameras 1\\n    -controlVertices 1\\n    -hulls 1\\n    -grid 1\\n    -joints 1\\n    -ikHandles 1\\n    -deformers 1\\n    -dynamics 1\\n    -fluids 1\\n    -hairSystems 1\\n    -follicles 1\\n    -nCloths 1\\n    -nParticles 1\\n    -nRigids 1\\n    -dynamicConstraints 1\\n    -locators 1\\n    -manipulators 1\\n    -dimensions 1\\n    -handles 1\\n    -pivots 1\\n    -textures 1\\n    -strokes 1\\n    -motionTrails 1\\n    -shadows 0\\n    $editorName;\\nmodelEditor -e -viewSelected 0 $editorName\"\n"
		+ "\t\t\t\t$configName;\n\n            setNamedPanelLayout (localizedPanelLabel(\"Current Layout\"));\n        }\n\n        panelHistory -e -clear mainPanelHistory;\n        setFocus `paneLayout -q -p1 $gMainPane`;\n        sceneUIReplacement -deleteRemaining;\n        sceneUIReplacement -clear;\n\t}\n\n\ngrid -spacing 5 -size 12 -divisions 5 -displayAxes yes -displayGridLines yes -displayDivisionLines yes -displayPerspectiveLabels no -displayOrthographicLabels no -displayAxesBold yes -perspectiveLabelPosition axis -orthographicLabelPosition edge;\nviewManip -drawCompass 0 -compassAngle 0 -frontParameters \"\" -homeParameters \"\" -selectionLockParameters \"\";\n}\n");
	setAttr ".st" 3;
select -ne :time1;
	setAttr -av -k on ".cch";
	setAttr -cb on ".ihi";
	setAttr -k on ".nds";
	setAttr -cb on ".bnm";
	setAttr -k on ".o" 1;
	setAttr ".unw" 1;
select -ne :renderPartition;
	setAttr -k on ".cch";
	setAttr -cb on ".ihi";
	setAttr -k on ".nds";
	setAttr -cb on ".bnm";
	setAttr -s 8 ".st";
	setAttr -cb on ".an";
	setAttr -cb on ".pt";
select -ne :initialShadingGroup;
	setAttr -k on ".cch";
	setAttr -cb on ".ihi";
	setAttr -av -k on ".nds";
	setAttr -cb on ".bnm";
	setAttr -k on ".mwc";
	setAttr -cb on ".an";
	setAttr -cb on ".il";
	setAttr -cb on ".vo";
	setAttr -cb on ".eo";
	setAttr -cb on ".fo";
	setAttr -cb on ".epo";
	setAttr -k on ".ro" yes;
	setAttr -s 3 ".gn";
lockNode -l 1 ;
select -ne :initialParticleSE;
	setAttr -k on ".cch";
	setAttr -cb on ".ihi";
	setAttr -av -k on ".nds";
	setAttr -cb on ".bnm";
	setAttr -k on ".mwc";
	setAttr -cb on ".an";
	setAttr -cb on ".il";
	setAttr -cb on ".vo";
	setAttr -cb on ".eo";
	setAttr -cb on ".fo";
	setAttr -cb on ".epo";
	setAttr -k on ".ro" yes;
select -ne :defaultShaderList1;
	setAttr -k on ".cch";
	setAttr -cb on ".ihi";
	setAttr -k on ".nds";
	setAttr -cb on ".bnm";
	setAttr -s 2 ".s";
select -ne :postProcessList1;
	setAttr -k on ".cch";
	setAttr -cb on ".ihi";
	setAttr -k on ".nds";
	setAttr -cb on ".bnm";
	setAttr -s 2 ".p";
select -ne :defaultRenderingList1;
select -ne :renderGlobalsList1;
	setAttr -k on ".cch";
	setAttr -cb on ".ihi";
	setAttr -k on ".nds";
	setAttr -cb on ".bnm";
select -ne :defaultLightSet;
	setAttr -k on ".cch";
	setAttr -k on ".ihi";
	setAttr -k on ".nds";
	setAttr -k on ".bnm";
	setAttr -k on ".mwc";
	setAttr -k on ".an";
	setAttr -k on ".il";
	setAttr -k on ".vo";
	setAttr -k on ".eo";
	setAttr -k on ".fo";
	setAttr -k on ".epo";
	setAttr -k on ".ro" yes;
select -ne :defaultObjectSet;
	setAttr -k on ".cch";
	setAttr -k on ".ihi";
	setAttr -k on ".nds";
	setAttr -k on ".bnm";
	setAttr -k on ".mwc";
	setAttr -k on ".an";
	setAttr -k on ".il";
	setAttr -k on ".vo";
	setAttr -k on ".eo";
	setAttr -k on ".fo";
	setAttr -k on ".epo";
	setAttr ".ro" yes;
select -ne :hardwareRenderGlobals;
	setAttr -k on ".cch";
	setAttr -cb on ".ihi";
	setAttr -k on ".nds";
	setAttr -cb on ".bnm";
	setAttr ".ctrs" 256;
	setAttr ".btrs" 512;
	setAttr -k off ".fbfm";
	setAttr -k off -cb on ".ehql";
	setAttr -k off -cb on ".eams";
	setAttr -k off -cb on ".eeaa";
	setAttr -k off -cb on ".engm";
	setAttr -k off -cb on ".mes";
	setAttr -k off -cb on ".emb";
	setAttr -av -k off -cb on ".mbbf";
	setAttr -k off -cb on ".mbs";
	setAttr -k off -cb on ".trm";
	setAttr -k off -cb on ".tshc";
	setAttr -k off ".enpt";
	setAttr -k off -cb on ".clmt";
	setAttr -k off -cb on ".tcov";
	setAttr -k off -cb on ".lith";
	setAttr -k off -cb on ".sobc";
	setAttr -k off -cb on ".cuth";
	setAttr -k off -cb on ".hgcd";
	setAttr -k off -cb on ".hgci";
	setAttr -k off -cb on ".mgcs";
	setAttr -k off -cb on ".twa";
	setAttr -k off -cb on ".twz";
	setAttr -cb on ".hwcc";
	setAttr -cb on ".hwdp";
	setAttr -cb on ".hwql";
	setAttr -k on ".hwfr";
select -ne :defaultHardwareRenderGlobals;
	setAttr -k on ".cch";
	setAttr -cb on ".ihi";
	setAttr -k on ".nds";
	setAttr -cb on ".bnm";
	setAttr -k on ".rp";
	setAttr -k on ".cai";
	setAttr -k on ".coi";
	setAttr -cb on ".bc";
	setAttr -av -k on ".bcb";
	setAttr -av -k on ".bcg";
	setAttr -av -k on ".bcr";
	setAttr -k on ".ei";
	setAttr -k on ".ex";
	setAttr -av -k on ".es";
	setAttr -av -k on ".ef";
	setAttr -av -k on ".bf";
	setAttr -k on ".fii";
	setAttr -av -k on ".sf";
	setAttr -k on ".gr";
	setAttr -k on ".li";
	setAttr -k on ".ls";
	setAttr -k on ".mb";
	setAttr -k on ".ti";
	setAttr -k on ".txt";
	setAttr -k on ".mpr";
	setAttr -k on ".wzd";
	setAttr -k on ".fn" -type "string" "im";
	setAttr -k on ".if";
	setAttr -k on ".res" -type "string" "ntsc_4d 646 485 1.333";
	setAttr -k on ".as";
	setAttr -k on ".ds";
	setAttr -k on ".lm";
	setAttr -k on ".fir";
	setAttr -k on ".aap";
	setAttr -k on ".gh";
	setAttr -cb on ".sd";
select -ne :ikSystem;
	setAttr -s 4 ".sol";
select -ne :hyperGraphLayout;
	setAttr -s 8 ".hyp";
	setAttr ".hyp[1].isc" yes;
	setAttr ".hyp[3].isc" yes;
	setAttr ".hyp[4].isc" yes;
	setAttr ".hyp[5].isc" yes;
	setAttr ".hyp[6].isc" yes;
	setAttr ".hyp[7].isc" yes;
connectAttr "root_tmpJnt.s" "spine1_tmpJnt.is";
connectAttr "spine1_tmpJnt.s" "spine2_tmpJnt.is";
connectAttr "spine3_tmpJnt.s" "spine4_tmpJnt.is";
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
connectAttr "spine4_tmpJnt.s" "clavLFT_tmpJnt.is";
connectAttr "clavLFT_tmpJnt.s" "upArmLFT_tmpJnt.is";
connectAttr "upArmLFT_tmpJnt.s" "forearmLFT_tmpJnt.is";
connectAttr "forearmLFT_tmpJnt.s" "wristLFT_tmpJnt.is";
connectAttr "wristLFT_tmpJnt.s" "handLFT_tmpJnt.is";
connectAttr "handLFT_tmpJnt.s" "thumb1LFT_tmpJnt.is";
connectAttr "thumb1LFT_tmpJnt.s" "thumb2LFT_tmpJnt.is";
connectAttr "thumb2LFT_tmpJnt.s" "thumb3LFT_tmpJnt.is";
connectAttr "thumb3LFT_tmpJnt.s" "thumb4LFT_tmpJnt.is";
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
connectAttr "spine4_tmpJnt.s" "clavRGT_tmpJnt.is";
connectAttr "clavRGT_tmpJnt.s" "upArmRGT_tmpJnt.is";
connectAttr "upArmRGT_tmpJnt.s" "forearmRGT_tmpJnt.is";
connectAttr "forearmRGT_tmpJnt.s" "wristRGT_tmpJnt.is";
connectAttr "wristRGT_tmpJnt.s" "handRGT_tmpJnt.is";
connectAttr "handRGT_tmpJnt.s" "thumb1RGT_tmpJnt.is";
connectAttr "thumb1RGT_tmpJnt.s" "thumb2RGT_tmpJnt.is";
connectAttr "thumb2RGT_tmpJnt.s" "thumb3RGT_tmpJnt.is";
connectAttr "thumb3RGT_tmpJnt.s" "thumb4RGT_tmpJnt.is";
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
connectAttr "root_tmpJnt.s" "pelvis_tmpJnt.is";
connectAttr "pelvis_tmpJnt.s" "upLegLFT_tmpJnt.is";
connectAttr "upLegLFT_tmpJnt.s" "lowLegLFT_tmpJnt.is";
connectAttr "lowLegLFT_tmpJnt.s" "kneeIkLFT_tmpJnt.is";
connectAttr "lowLegLFT_tmpJnt.s" "ankleLFT_tmpJnt.is";
connectAttr "ballLFT_tmpJnt.s" "toeLFT_tmpJnt.is";
connectAttr "ankleLFT_tmpJnt.s" "footInLFT_tmpJnt.is";
connectAttr "ankleLFT_tmpJnt.s" "footOutLFT_tmpJnt.is";
connectAttr "ankleLFT_tmpJnt.s" "heelLFT_tmpJnt.is";
connectAttr "pelvis_tmpJnt.s" "upLegRGT_tmpJnt.is";
connectAttr "upLegRGT_tmpJnt.s" "lowLegRGT_tmpJnt.is";
connectAttr "lowLegRGT_tmpJnt.s" "kneeIkRGT_tmpJnt.is";
connectAttr "lowLegRGT_tmpJnt.s" "ankleRGT_tmpJnt.is";
connectAttr "ballRGT_tmpJnt.s" "toeRGT_tmpJnt.is";
connectAttr "ankleRGT_tmpJnt.s" "footInRGT_tmpJnt.is";
connectAttr "ankleRGT_tmpJnt.s" "footOutRGT_tmpJnt.is";
connectAttr "ankleRGT_tmpJnt.s" "heelRGT_tmpJnt.is";
connectAttr "placement_tmpCtrl.s" "addJnt_grp.s";
connectAttr "placement_tmpCtrl.r" "addJnt_grp.r";
connectAttr "placement_tmpCtrl.t" "addJnt_grp.t";
connectAttr "tongue1_jnt.s" "tongue2_jnt.is";
connectAttr "tongue2_jnt.s" "tongue3_jnt.is";
connectAttr "tongue3_jnt.s" "tongue4_jnt.is";
connectAttr "tongue4_jnt.s" "tongue5_jnt.is";
connectAttr "tongue5_jnt.s" "tongue6_jnt.is";
connectAttr "thumbToe1LFT_jnt.s" "thumbToe2LFT_jnt.is";
connectAttr "indexToe1LFT_jnt.s" "indexToe2LFT_jnt.is";
connectAttr "middleToe1LFT_jnt.s" "middleToe2LFT_jnt.is";
connectAttr "ringToe1LFT_jnt.s" "ringToe2LFT_jnt.is";
connectAttr "pinkyToe1LFT_jnt.s" "pinkyToe2LFT_jnt.is";
connectAttr "thumbToe1RGT_jnt.s" "thumbToe2RGT_jnt.is";
connectAttr "indexToe1RGT_jnt.s" "indexToe2RGT_jnt.is";
connectAttr "middleToe1RGT_jnt.s" "middleToe2RGT_jnt.is";
connectAttr "ringToe1RGT_jnt.s" "ringToe2RGT_jnt.is";
connectAttr "pinkyToe1RGT_jnt.s" "pinkyToe2RGT_jnt.is";
relationship "link" ":lightLinker1" ":initialShadingGroup.message" ":defaultLightSet.message";
relationship "link" ":lightLinker1" ":initialParticleSE.message" ":defaultLightSet.message";
relationship "link" ":lightLinker1" "eyeSpecMat_sg.message" ":defaultLightSet.message";
relationship "link" ":lightLinker1" "eyeMat_sg.message" ":defaultLightSet.message";
relationship "link" ":lightLinker1" "corneaMat_sg.message" ":defaultLightSet.message";
relationship "link" ":lightLinker1" "eyeSpecMat_sg1.message" ":defaultLightSet.message";
relationship "link" ":lightLinker1" "eyeMat_sg1.message" ":defaultLightSet.message";
relationship "link" ":lightLinker1" "corneaMat_sg1.message" ":defaultLightSet.message";
relationship "shadowLink" ":lightLinker1" ":initialShadingGroup.message" ":defaultLightSet.message";
relationship "shadowLink" ":lightLinker1" ":initialParticleSE.message" ":defaultLightSet.message";
relationship "shadowLink" ":lightLinker1" "eyeSpecMat_sg.message" ":defaultLightSet.message";
relationship "shadowLink" ":lightLinker1" "eyeMat_sg.message" ":defaultLightSet.message";
relationship "shadowLink" ":lightLinker1" "corneaMat_sg.message" ":defaultLightSet.message";
relationship "shadowLink" ":lightLinker1" "eyeSpecMat_sg1.message" ":defaultLightSet.message";
relationship "shadowLink" ":lightLinker1" "eyeMat_sg1.message" ":defaultLightSet.message";
relationship "shadowLink" ":lightLinker1" "corneaMat_sg1.message" ":defaultLightSet.message";
connectAttr "layerManager.dli[0]" "defaultLayer.id";
connectAttr "renderLayerManager.rlmi[0]" "defaultRenderLayer.rlid";
connectAttr "eyeSpecMat_sg.pa" ":renderPartition.st" -na;
connectAttr "eyeMat_sg.pa" ":renderPartition.st" -na;
connectAttr "corneaMat_sg.pa" ":renderPartition.st" -na;
connectAttr "eyeSpecMat_sg1.pa" ":renderPartition.st" -na;
connectAttr "eyeMat_sg1.pa" ":renderPartition.st" -na;
connectAttr "corneaMat_sg1.pa" ":renderPartition.st" -na;
connectAttr "groupId463.msg" ":initialShadingGroup.gn" -na;
connectAttr "groupId19.msg" ":initialShadingGroup.gn" -na;
connectAttr "groupId492.msg" ":initialShadingGroup.gn" -na;
connectAttr "defaultRenderLayer.msg" ":defaultRenderingList1.r" -na;
connectAttr "handLFT_tmpJnt.msg" ":hyperGraphLayout.hyp[1].dn";
connectAttr "thumb1LFT_tmpJnt.msg" ":hyperGraphLayout.hyp[3].dn";
connectAttr "index1LFT_tmpJnt.msg" ":hyperGraphLayout.hyp[4].dn";
connectAttr "middle1LFT_tmpJnt.msg" ":hyperGraphLayout.hyp[5].dn";
connectAttr "ring1LFT_tmpJnt.msg" ":hyperGraphLayout.hyp[6].dn";
connectAttr "pinky1LFT_tmpJnt.msg" ":hyperGraphLayout.hyp[7].dn";
// End of tmpJnt_3.ma
