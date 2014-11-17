//Maya ASCII 2012 scene
//Name: proxySkinJoint_1.ma
//Last modified: Tue, Oct 08, 2013 02:39:29 PM
//Codeset: 1252
requires maya "2012";
currentUnit -l centimeter -a degree -t film;
fileInfo "application" "maya";
fileInfo "product" "Maya 2012";
fileInfo "version" "2012 x64";
fileInfo "cutIdentifier" "201201172029-821146";
fileInfo "osv" "Microsoft Windows 7 Business Edition, 64-bit Windows 7 Service Pack 1 (Build 7601)\n";
createNode transform -s -n "persp";
	setAttr ".v" no;
	setAttr ".t" -type "double3" 77.051683137378461 214.60129104416652 416.62190359921766 ;
	setAttr ".r" -type "double3" -16.471881498418316 10.600000000000685 -6.0670725016694353e-016 ;
createNode camera -s -n "perspShape" -p "persp";
	setAttr -k off ".v" no;
	setAttr ".fl" 34.999999999999986;
	setAttr ".coi" 436.79671146146012;
	setAttr ".imn" -type "string" "persp";
	setAttr ".den" -type "string" "persp_depth";
	setAttr ".man" -type "string" "persp_mask";
	setAttr ".tp" -type "double3" -4.4642734039257448e-005 90.749872440971416 4.8996373812953333 ;
	setAttr ".hc" -type "string" "viewSet -p %camera";
createNode transform -s -n "top";
	setAttr ".v" no;
	setAttr ".t" -type "double3" 0 100.1 0 ;
	setAttr ".r" -type "double3" -89.999999999999986 0 0 ;
createNode camera -s -n "topShape" -p "top";
	setAttr -k off ".v" no;
	setAttr ".rnd" no;
	setAttr ".coi" 100.1;
	setAttr ".ow" 30;
	setAttr ".imn" -type "string" "top";
	setAttr ".den" -type "string" "top_depth";
	setAttr ".man" -type "string" "top_mask";
	setAttr ".hc" -type "string" "viewSet -t %camera";
	setAttr ".o" yes;
createNode transform -s -n "front";
	setAttr ".v" no;
	setAttr ".t" -type "double3" 1.2423097593816803 92.768698344408364 150.49367992070955 ;
createNode camera -s -n "frontShape" -p "front";
	setAttr -k off ".v" no;
	setAttr ".rnd" no;
	setAttr ".coi" 100.1;
	setAttr ".ow" 192.875520928361;
	setAttr ".imn" -type "string" "front";
	setAttr ".den" -type "string" "front_depth";
	setAttr ".man" -type "string" "front_mask";
	setAttr ".hc" -type "string" "viewSet -f %camera";
	setAttr ".o" yes;
createNode transform -s -n "side";
	setAttr ".v" no;
	setAttr ".t" -type "double3" 186.80628625299431 119.5764700023019 2.9841875661882282 ;
	setAttr ".r" -type "double3" 0 89.999999999999986 0 ;
createNode camera -s -n "sideShape" -p "side";
	setAttr -k off ".v" no;
	setAttr ".rnd" no;
	setAttr ".coi" 100.1;
	setAttr ".ow" 37.299894129947496;
	setAttr ".imn" -type "string" "side";
	setAttr ".den" -type "string" "side_depth";
	setAttr ".man" -type "string" "side_mask";
	setAttr ".hc" -type "string" "viewSet -s %camera";
	setAttr ".o" yes;
createNode transform -n "proxySkin_grp";
createNode joint -n "rootProxySkin_jnt" -p "proxySkin_grp";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".t" -type "double3" 0 102.759605213703 0.42218038887933029 ;
	setAttr ".bps" -type "matrix" 1 0 0 0 0 1 0 0 0 0 1 0 0 102.759605213703 0.42218038887933029 1;
createNode joint -n "pelvisProxySkin_jnt" -p "rootProxySkin_jnt";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".t" -type "double3" 0 -2.7783041166882043 -1.1102230246251565e-016 ;
	setAttr ".bps" -type "matrix" 1 0 0 0 0 1 0 0 0 0 1 0 0 99.981301097014793 0.42218038887933018 1;
createNode joint -n "pelvisScaProxySkin_jnt" -p "pelvisProxySkin_jnt";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".uoc" yes;
	setAttr ".bps" -type "matrix" 1 0 0 0 0 1 0 0 0 0 1 0 0 99.981301097014793 0.42218038887933018 1;
	setAttr ".radi" 2;
createNode joint -n "upLegProxySkinLFT_jnt" -p "pelvisProxySkin_jnt";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".t" -type "double3" 9.6001712238537511 -1.9988478509214076 0.11211344323189609 ;
	setAttr ".ro" 1;
	setAttr ".jo" -type "double3" 0 0 180 ;
	setAttr ".bps" -type "matrix" -1 1.2246467991473532e-016 0 0 -1.2246467991473532e-016 -1 0 0
		 0 0 1 0 9.6001712238537511 97.982453246093385 0.53429383211122627 1;
createNode joint -n "lowLegProxySkinLFT_jnt" -p "upLegProxySkinLFT_jnt";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".t" -type "double3" -3.5527136788005009e-015 41.975826323438497 -0.39642730167556284 ;
	setAttr ".ro" 1;
	setAttr ".bps" -type "matrix" -1 1.2246467991473532e-016 0 0 -1.2246467991473532e-016 -1 0 0
		 0 0 1 0 9.6001712238537493 56.006626922654888 0.13786653043566344 1;
createNode joint -n "ankleProxySkinLFT_jnt" -p "lowLegProxySkinLFT_jnt";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".t" -type "double3" -3.5527136788005009e-015 48.28298789576597 -4.6230424143192819 ;
	setAttr ".ro" 1;
	setAttr ".bps" -type "matrix" -1 1.2246467991473532e-016 0 0 -1.2246467991473532e-016 -1 0 0
		 0 0 1 0 9.6001712238537475 7.7236390268889181 -4.4851758838836187 1;
createNode joint -n "ballProxySkinLFT_jnt" -p "ankleProxySkinLFT_jnt";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".t" -type "double3" -1.7763568394002505e-015 7.7236390268889634 13.056435631577738 ;
	setAttr ".ro" 1;
	setAttr ".jo" -type "double3" 89.999999999999986 0 0 ;
	setAttr ".ssc" no;
	setAttr ".bps" -type "matrix" -1 1.2246467991473532e-016 0 0 -2.7192621468937821e-032 -2.2204460492503131e-016 1.0000000000000002 0
		 1.2246467991473535e-016 1.0000000000000002 2.2204460492503131e-016 0 9.6001712238537475 -4.5297099404706387e-014 8.5712597476941195 1;
createNode joint -n "toeProxySkinLFT_jnt" -p "ballProxySkinLFT_jnt";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".t" -type "double3" 0 9.9989462759571452 6.7470860954405359e-015 ;
	setAttr ".ro" 1;
	setAttr ".bps" -type "matrix" -1 1.2246467991473532e-016 0 0 -2.7192621468937821e-032 -2.2204460492503131e-016 1.0000000000000002 0
		 1.2246467991473535e-016 1.0000000000000002 2.2204460492503131e-016 0 9.6001712238537475 -4.0770225384777367e-014 18.570206023651266 1;
createNode joint -n "lowLegRbnDtl1ProxySkinLFT_jnt" -p "lowLegProxySkinLFT_jnt";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".t" -type "double3" 0 4.8282987895765856 -0.46230424143192844 ;
	setAttr ".jo" -type "double3" 5.4693338486754461 0 -180 ;
	setAttr ".bps" -type "matrix" 1 0 0 0 0 0.99544735486364322 0.095312977579005309 0
		 0 -0.095312977579005309 0.99544735486364322 0 9.6001712238537493 51.178328133078303 -0.32443771099626501 1;
	setAttr ".radi" 2;
createNode joint -n "lowLegRbnDtl2ProxySkinLFT_jnt" -p "lowLegProxySkinLFT_jnt";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".t" -type "double3" -1.7763568394002505e-015 14.484896368729792 -1.386912724295789 ;
	setAttr ".jo" -type "double3" 5.4693338486754461 0 -180 ;
	setAttr ".bps" -type "matrix" 1 0 0 0 0 0.99544735486364322 0.095312977579005309 0
		 0 -0.095312977579005309 0.99544735486364322 0 9.6001712238537493 41.521730553925096 -1.2490461938601256 1;
	setAttr ".radi" 2;
createNode joint -n "lowLegRbnDtl3ProxySkinLFT_jnt" -p "lowLegProxySkinLFT_jnt";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".t" -type "double3" 0 24.141493947882999 -2.3115212071596423 ;
	setAttr ".jo" -type "double3" 5.4693338486754461 0 -180 ;
	setAttr ".bps" -type "matrix" 1 0 0 0 0 0.99544735486364322 0.095312977579005309 0
		 0 -0.095312977579005309 0.99544735486364322 0 9.6001712238537458 31.865132974771889 -2.1736546767239791 1;
	setAttr ".radi" 2;
createNode joint -n "lowLegRbnDtl4ProxySkinLFT_jnt" -p "lowLegProxySkinLFT_jnt";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".t" -type "double3" 0 33.798091527036185 -3.2361296900234953 ;
	setAttr ".jo" -type "double3" 5.4693338486754461 0 -180 ;
	setAttr ".bps" -type "matrix" 1 0 0 0 0 0.99544735486364322 0.095312977579005309 0
		 0 -0.095312977579005309 0.99544735486364322 0 9.6001712238537458 22.208535395618703 -3.098263159587832 1;
	setAttr ".radi" 2;
createNode joint -n "lowLegRbnDtl5ProxySkinLFT_jnt" -p "lowLegProxySkinLFT_jnt";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".t" -type "double3" 0 43.454689106189385 -4.1607381728873536 ;
	setAttr ".jo" -type "double3" 5.4693338486754461 0 -180 ;
	setAttr ".bps" -type "matrix" 1 0 0 0 0 0.99544735486364322 0.095312977579005309 0
		 0 -0.095312977579005309 0.99544735486364322 0 9.600171223853744 12.551937816465504 -4.0228716424516904 1;
	setAttr ".radi" 2;
createNode joint -n "upLegRbnDtl1ProxySkinLFT_jnt" -p "upLegProxySkinLFT_jnt";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".t" -type "double3" -1.7763568394002505e-015 4.1975826323438383 -0.039642730167570472 ;
	setAttr ".jo" -type "double3" 0.5410956257505023 0 -180 ;
	setAttr ".bps" -type "matrix" 1 0 0 0 0 0.99995540670558314 0.0094437598588600329 0
		 0 -0.0094437598588600329 0.99995540670558314 0 9.6001712238537511 93.784870613749547 0.4946511019436558 1;
	setAttr ".radi" 2;
createNode joint -n "upLegRbnDtl2ProxySkinLFT_jnt" -p "upLegProxySkinLFT_jnt";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".t" -type "double3" 0 12.592747897031558 -0.11892819050268866 ;
	setAttr ".jo" -type "double3" 0.5410956257505023 0 -180 ;
	setAttr ".bps" -type "matrix" 1 0 0 0 0 0.99995540670558314 0.0094437598588600329 0
		 0 -0.0094437598588600329 0.99995540670558314 0 9.6001712238537493 85.389705349061828 0.41536564160853762 1;
	setAttr ".radi" 2;
createNode joint -n "upLegRbnDtl3ProxySkinLFT_jnt" -p "upLegProxySkinLFT_jnt";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".t" -type "double3" 1.7763568394002505e-015 20.987913161719263 -0.19821365083778164 ;
	setAttr ".jo" -type "double3" 0.5410956257505023 0 -180 ;
	setAttr ".bps" -type "matrix" 1 0 0 0 0 0.99995540670558314 0.0094437598588600329 0
		 0 -0.0094437598588600329 0.99995540670558314 0 9.6001712238537458 76.994540084374123 0.33608018127344463 1;
	setAttr ".radi" 2;
createNode joint -n "upLegRbnDtl4ProxySkinLFT_jnt" -p "upLegProxySkinLFT_jnt";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".t" -type "double3" 1.7763568394002505e-015 29.383078426406954 -0.27749911117287457 ;
	setAttr ".jo" -type "double3" 0.5410956257505023 0 -180 ;
	setAttr ".bps" -type "matrix" 1 0 0 0 0 0.99995540670558314 0.0094437598588600329 0
		 0 -0.0094437598588600329 0.99995540670558314 0 9.6001712238537458 68.599374819686432 0.25679472093835171 1;
	setAttr ".radi" 2;
createNode joint -n "upLegRbnDtl5ProxySkinLFT_jnt" -p "upLegProxySkinLFT_jnt";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".t" -type "double3" 0 37.778243691094659 -0.35678457150799259 ;
	setAttr ".jo" -type "double3" 0.5410956257505023 0 -180 ;
	setAttr ".bps" -type "matrix" 1 0 0 0 0 0.99995540670558314 0.0094437598588600329 0
		 0 -0.0094437598588600329 0.99995540670558314 0 9.6001712238537458 60.204209554998727 0.17750926060323369 1;
	setAttr ".radi" 2;
createNode joint -n "upLegProxySkinRGT_jnt" -p "pelvisProxySkin_jnt";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".t" -type "double3" -9.60017 -1.9988010970147911 0.11211361112066986 ;
	setAttr ".ro" 1;
	setAttr ".jo" -type "double3" 0 180 0 ;
	setAttr ".bps" -type "matrix" -1 0 -1.2246467991473532e-016 0 0 1 0 0 1.2246467991473532e-016 0 -1 0
		 -9.6001700000000003 97.982500000000002 0.53429400000000005 1;
createNode joint -n "lowLegProxySkinRGT_jnt" -p "upLegProxySkinRGT_jnt";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".t" -type "double3" 0 -41.9759 0.39642700000000031 ;
	setAttr ".ro" 1;
	setAttr ".bps" -type "matrix" -1 0 -1.2246467991473532e-016 0 0 1 0 0 1.2246467991473532e-016 0 -1 0
		 -9.6001700000000003 56.006599999999999 0.13786699999999974 1;
createNode joint -n "ankleProxySkinRGT_jnt" -p "lowLegProxySkinRGT_jnt";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".t" -type "double3" 0 -48.28296 4.623047 ;
	setAttr ".ro" 1;
	setAttr ".bps" -type "matrix" -1 0 -1.2246467991473532e-016 0 0 1 0 0 1.2246467991473532e-016 0 -1 0
		 -9.6001700000000003 7.7236399999999961 -4.4851799999999997 1;
createNode joint -n "ballProxySkinRGT_jnt" -p "ankleProxySkinRGT_jnt";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".t" -type "double3" -1.7763568394002505e-015 -7.7236400000000414 -13.056440000000002 ;
	setAttr ".ro" 1;
	setAttr ".jo" -type "double3" 89.999999999999972 0 0 ;
	setAttr ".ssc" no;
	setAttr ".bps" -type "matrix" -1 0 -1.2246467991473532e-016 0 1.2246467991473532e-016 4.4408920985006262e-016 -1 0
		 5.4385242937875642e-032 -1 -4.4408920985006262e-016 0 -9.6001700000000003 -4.5297099404706387e-014 8.5712600000000023 1;
createNode joint -n "toeProxySkinRGT_jnt" -p "ballProxySkinRGT_jnt";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".t" -type "double3" 7.1054273576010019e-015 -9.9989399999999957 -4.5269207686445899e-015 ;
	setAttr ".ro" 1;
	setAttr ".bps" -type "matrix" -1 0 -1.2246467991473532e-016 0 1.2246467991473532e-016 4.4408920985006262e-016 -1 0
		 5.4385242937875642e-032 -1 -4.4408920985006262e-016 0 -9.6001700000000092 -4.5210599999999978e-014 18.5702 1;
createNode joint -n "lowLegRbnDtl1ProxySkinRGT_jnt" -p "lowLegProxySkinRGT_jnt";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".t" -type "double3" 1.7763568394002505e-015 -4.8282959999999875 0.46230469999999951 ;
	setAttr ".jo" -type "double3" 5.4693423816935427 180 0 ;
	setAttr ".bps" -type "matrix" 1 0 0 0 0 0.99544734066874085 0.095313125830243137 0
		 0 -0.095313125830243137 0.99544734066874085 0 -9.6001700000000021 51.178304000000011 -0.32443769999999977 1;
	setAttr ".radi" 2;
createNode joint -n "lowLegRbnDtl2ProxySkinRGT_jnt" -p "lowLegProxySkinRGT_jnt";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".t" -type "double3" 1.7763568394002505e-015 -14.484887999999984 1.3869140999999987 ;
	setAttr ".jo" -type "double3" 5.4693423816935427 180 0 ;
	setAttr ".bps" -type "matrix" 1 0 0 0 0 0.99544734066874085 0.095313125830243137 0
		 0 -0.095313125830243137 0.99544734066874085 0 -9.6001700000000021 41.521712000000015 -1.249047099999999 1;
	setAttr ".radi" 2;
createNode joint -n "lowLegRbnDtl3ProxySkinRGT_jnt" -p "lowLegProxySkinRGT_jnt";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".t" -type "double3" 1.7763568394002505e-015 -24.141479999999994 2.311523499999999 ;
	setAttr ".jo" -type "double3" 5.4693423816935427 180 0 ;
	setAttr ".bps" -type "matrix" 1 0 0 0 0 0.99544734066874085 0.095313125830243137 0
		 0 -0.095313125830243137 0.99544734066874085 0 -9.6001700000000021 31.865120000000005 -2.1736564999999994 1;
	setAttr ".radi" 2;
createNode joint -n "lowLegRbnDtl4ProxySkinRGT_jnt" -p "lowLegProxySkinRGT_jnt";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".t" -type "double3" 5.3290705182007514e-015 -33.798071999999983 3.236132899999999 ;
	setAttr ".jo" -type "double3" 5.4693423816935427 180 0 ;
	setAttr ".bps" -type "matrix" 1 0 0 0 0 0.99544734066874085 0.095313125830243137 0
		 0 -0.095313125830243137 0.99544734066874085 0 -9.6001700000000056 22.208528000000015 -3.0982658999999995 1;
	setAttr ".radi" 2;
createNode joint -n "lowLegRbnDtl5ProxySkinRGT_jnt" -p "lowLegProxySkinRGT_jnt";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".t" -type "double3" 5.3290705182007514e-015 -43.454663999999994 4.1607422999999999 ;
	setAttr ".jo" -type "double3" 5.4693423816935427 180 0 ;
	setAttr ".bps" -type "matrix" 1 0 0 0 0 0.99544734066874085 0.095313125830243137 0
		 0 -0.095313125830243137 0.99544734066874085 0 -9.6001700000000056 12.551936000000005 -4.0228752999999999 1;
	setAttr ".radi" 2;
createNode joint -n "upLegRbnDtl1ProxySkinRGT_jnt" -p "upLegProxySkinRGT_jnt";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".t" -type "double3" 1.7763568394002505e-015 -4.1975900000000337 0.039642699999999642 ;
	setAttr ".jo" -type "double3" 0.54109426432965768 180 0 ;
	setAttr ".bps" -type "matrix" 1 0 0 0 0 0.99995540692997864 0.0094437360986433863 0
		 0 -0.0094437360986433863 0.99995540692997864 0 -9.6001700000000021 93.784909999999968 0.49465130000000046 1;
	setAttr ".radi" 2;
createNode joint -n "upLegRbnDtl2ProxySkinRGT_jnt" -p "upLegProxySkinRGT_jnt";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".t" -type "double3" 1.7763568394002505e-015 -12.59277000000003 0.11892809999999954 ;
	setAttr ".jo" -type "double3" 0.54109426432965768 180 0 ;
	setAttr ".bps" -type "matrix" 1 0 0 0 0 0.99995540692997864 0.0094437360986433863 0
		 0 -0.0094437360986433863 0.99995540692997864 0 -9.6001700000000021 85.389729999999972 0.41536590000000057 1;
	setAttr ".radi" 2;
createNode joint -n "upLegRbnDtl3ProxySkinRGT_jnt" -p "upLegProxySkinRGT_jnt";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".t" -type "double3" 1.7763568394002505e-015 -20.987949999999998 0.19821349999999999 ;
	setAttr ".jo" -type "double3" 0.54109426432965768 180 0 ;
	setAttr ".bps" -type "matrix" 1 0 0 0 0 0.99995540692997864 0.0094437360986433863 0
		 0 -0.0094437360986433863 0.99995540692997864 0 -9.6001700000000021 76.994550000000004 0.33608050000000012 1;
	setAttr ".radi" 2;
createNode joint -n "upLegRbnDtl4ProxySkinRGT_jnt" -p "upLegProxySkinRGT_jnt";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".t" -type "double3" 1.7763568394002505e-015 -29.383130000000008 0.27749890000000083 ;
	setAttr ".jo" -type "double3" 0.54109426432965768 180 0 ;
	setAttr ".bps" -type "matrix" 1 0 0 0 0 0.99995540692997864 0.0094437360986433863 0
		 0 -0.0094437360986433863 0.99995540692997864 0 -9.6001700000000021 68.599369999999993 0.25679509999999928 1;
	setAttr ".radi" 2;
createNode joint -n "upLegRbnDtl5ProxySkinRGT_jnt" -p "upLegProxySkinRGT_jnt";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".t" -type "double3" 5.3290705182007514e-015 -37.778310000000019 0.35678430000000078 ;
	setAttr ".jo" -type "double3" 0.54109426432965768 180 0 ;
	setAttr ".bps" -type "matrix" 1 0 0 0 0 0.99995540692997864 0.0094437360986433863 0
		 0 -0.0094437360986433863 0.99995540692997864 0 -9.6001700000000056 60.204189999999983 0.17750969999999933 1;
	setAttr ".radi" 2;
createNode joint -n "spine1ProxySkin_jnt" -p "rootProxySkin_jnt";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".t" -type "double3" 0 6.8170281074114598 -2.5730567954467762 ;
	setAttr ".ro" 1;
	setAttr ".bps" -type "matrix" 1 0 0 0 0 1 0 0 0 0 1 0 0 109.57663332111446 -2.1508764065674457 1;
createNode joint -n "spine2ProxySkin_jnt" -p "spine1ProxySkin_jnt";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".t" -type "double3" 0 7.3045949691374972 1.9929576368999264 ;
	setAttr ".ro" 1;
	setAttr ".bps" -type "matrix" 1 0 0 0 0 1 0 0 0 0 1 0 0 116.88122829025195 -0.15791876966751928 1;
createNode joint -n "spine3ProxySkin_jnt" -p "spine2ProxySkin_jnt";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".t" -type "double3" 0 10.288851658927555 1.1102230246251565e-016 ;
	setAttr ".ro" 1;
	setAttr ".bps" -type "matrix" 1 0 0 0 0 1 0 0 0 0 1 0 0 127.17007994917951 -0.15791876966751917 1;
createNode joint -n "spine4ProxySkin_jnt" -p "spine3ProxySkin_jnt";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".t" -type "double3" 0 16.765651099258591 -0.60884067450085566 ;
	setAttr ".ro" 1;
	setAttr ".bps" -type "matrix" 1 0 0 0 0 1 0 0 0 0 1 0 0 143.9357310484381 -0.76675944416837483 1;
createNode joint -n "spine5ProxySkin_jnt" -p "spine4ProxySkin_jnt";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".t" -type "double3" 0 11.877696630834862 -0.33969709515650381 ;
	setAttr ".ro" 1;
	setAttr ".bps" -type "matrix" 1 0 0 0 0 1 0 0 0 0 1 0 0 155.81342767927296 -1.1064565393248786 1;
createNode joint -n "neck1ProxySkin_jnt" -p "spine5ProxySkin_jnt";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".bps" -type "matrix" 1 0 0 0 0 1 0 0 0 0 1 0 0 155.81342767927296 -1.1064565393248786 1;
createNode joint -n "neck2ProxySkin_jnt" -p "neck1ProxySkin_jnt";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".t" -type "double3" 0 12.434707792332631 1.6828000537817809 ;
	setAttr ".bps" -type "matrix" 1 0 0 0 0 1 0 0 0 0 1 0 0 168.24813547160559 0.57634351445690224 1;
createNode joint -n "head1ProxySkin_jnt" -p "neck2ProxySkin_jnt";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".bps" -type "matrix" 1 0 0 0 0 1 0 0 0 0 1 0 0 168.24813547160559 0.57634351445690224 1;
createNode joint -n "head2ProxySkin_jnt" -p "head1ProxySkin_jnt";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".t" -type "double3" 0 13.251609410337295 0 ;
	setAttr ".ssc" no;
	setAttr ".bps" -type "matrix" 1 0 0 0 0 1 0 0 0 0 1 0 0 181.49974488194289 0.57634351445690224 1;
createNode joint -n "jaw1LWRProxySkin_jnt" -p "head1ProxySkin_jnt";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".t" -type "double3" 0 -1.6417330834029826 2.8399032789149734 ;
	setAttr ".ssc" no;
	setAttr ".bps" -type "matrix" 1 0 0 0 0 1 0 0 0 0 1 0 0 166.60640238820261 3.4162467933718759 1;
createNode joint -n "jaw2LWRProxySkin_jnt" -p "jaw1LWRProxySkin_jnt";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".t" -type "double3" 0 -4.6896081030582764 5.7025109252335575 ;
	setAttr ".bps" -type "matrix" 1 0 0 0 0 1 0 0 0 0 1 0 0 161.91679428514433 9.1187577186054334 1;
createNode joint -n "jaw3LWRProxySkin_jnt" -p "jaw2LWRProxySkin_jnt";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".t" -type "double3" 0 0 2.0860059131040902 ;
	setAttr ".bps" -type "matrix" 1 0 0 0 0 1 0 0 0 0 1 0 0 161.91679428514433 11.204763631709524 1;
createNode joint -n "jaw1UPRProxySkin_jnt" -p "head1ProxySkin_jnt";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".t" -type "double3" -4.0430028438967361e-017 -5.2589442567452522 8.7641425339278314 ;
	setAttr ".jo" -type "double3" 0 0 180 ;
	setAttr ".ssc" no;
	setAttr ".bps" -type "matrix" -1 1.2246467991473532e-016 0 0 -1.2246467991473532e-016 -1 0 0
		 0 0 1 0 -4.0430028438967361e-017 162.98919121486034 9.340486048384733 1;
createNode joint -n "jaw2UPRProxySkin_jnt" -p "jaw1UPRProxySkin_jnt";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".t" -type "double3" 0 0 2.1407412644068913 ;
	setAttr ".ssc" no;
	setAttr ".bps" -type "matrix" -1 1.2246467991473532e-016 0 0 -1.2246467991473532e-016 -1 0 0
		 0 0 1 0 -4.0430028438967361e-017 162.98919121486034 11.481227312791624 1;
createNode joint -n "eyeProxySkinLFT_jnt" -p "head1ProxySkin_jnt";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".t" -type "double3" 2.7862998843193054 1.350413417554563 8.3938067178581619 ;
	setAttr ".ssc" no;
	setAttr ".bps" -type "matrix" 1 0 0 0 0 1 0 0 0 0 1 0 2.7862998843193054 169.59854888916016 8.9701502323150635 1;
createNode joint -n "eyeProxySkinRGT_jnt" -p "head1ProxySkin_jnt";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".t" -type "double3" -2.781099945306778 1.350810146070188 8.3938067178581619 ;
	setAttr ".ssc" no;
	setAttr ".bps" -type "matrix" 1 0 0 0 0 1 0 0 0 0 1 0 -2.781099945306778 169.59894561767578 8.9701502323150635 1;
createNode joint -n "neckRbnProxySkin_jnt" -p "neck1ProxySkin_jnt";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".t" -type "double3" 0 6.2173538961662587 0.84140002689088988 ;
	setAttr ".jo" -type "double3" 7.7070661324706089 0 0 ;
	setAttr ".bps" -type "matrix" 1 0 0 0 0 0.9909666680272381 0.13410839965861079 0
		 0 -0.13410839965861079 0.9909666680272381 0 0 162.03078157543922 -0.26505651243398876 1;
createNode joint -n "spine4ScaProxySkin_jnt" -p "spine4ProxySkin_jnt";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".bps" -type "matrix" 1 0 0 0 0 1 0 0 0 0 1 0 0 143.9357310484381 -0.76675944416837483 1;
	setAttr ".radi" 2;
createNode joint -n "clav1ProxySkinLFT_jnt" -p "spine4ProxySkin_jnt";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".t" -type "double3" 1.9757774640097452 4.5838630458049181 6.9513118237347014 ;
	setAttr ".jo" -type "double3" 0 0 -89.999999999999986 ;
	setAttr ".bps" -type "matrix" 2.2204460492503131e-016 -1.0000000000000002 0 0 1.0000000000000002 2.2204460492503131e-016 0 0
		 0 0 1 0 1.9757774640097452 148.51959409424302 6.1845523795663269 1;
createNode joint -n "clav2ProxySkinLFT_jnt" -p "clav1ProxySkinLFT_jnt";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".t" -type "double3" 1.7181100256687216 15.856889833164324 -8.9449485347118056 ;
	setAttr ".jo" -type "double3" 0 0 -53.826918307873264 ;
	setAttr ".bps" -type "matrix" -0.80723769735614159 -0.59022648192634908 0 0 0.59022648192634908 -0.80723769735614159 0 0
		 0 0 1 0 17.832667297174073 146.8014840685743 -2.7603961551454788 1;
createNode joint -n "upArmProxySkinLFT_jnt" -p "clav2ProxySkinLFT_jnt";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".t" -type "double3" 0 -1.4210854715202004e-014 0 ;
	setAttr ".ro" 1;
	setAttr ".bps" -type "matrix" -0.80723769735614159 -0.59022648192634908 0 0 0.59022648192634908 -0.80723769735614159 0 0
		 0 0 1 0 17.832667297174066 146.8014840685743 -2.7603961551454788 1;
createNode joint -n "forearmProxySkinLFT_jnt" -p "upArmProxySkinLFT_jnt";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".t" -type "double3" -5.8989257922803517e-011 26.795944706572456 -0.58742491966385435 ;
	setAttr ".ro" 1;
	setAttr ".jo" -type "double3" -5.9496752756331688e-005 0 0 ;
	setAttr ".bps" -type "matrix" -0.80723769735614159 -0.59022648192634908 0 0 0.59022648192603089 -0.80723769735570639 -1.038414229842813e-006 0
		 6.1289957766238277e-007 -8.3824711180016352e-007 0.99999999999946088 0 33.64834347127492 125.17078736519306 -3.3478210748093331 1;
createNode joint -n "wristProxySkinLFT_jnt" -p "forearmProxySkinLFT_jnt";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".t" -type "double3" -1.8943069335364271e-010 25.838120664570951 -0.12356304365562742 ;
	setAttr ".ro" 1;
	setAttr ".jo" -type "double3" 5.9496752756331675e-005 0 0 ;
	setAttr ".bps" -type "matrix" -0.80723769735614159 -0.59022648192634908 0 0 0.59022648192634919 -0.80723769735614159 -2.1175823681357508e-022 0
		 1.0587911840678754e-022 -2.1175823681357508e-022 1 0 48.898686455126089 104.31328243961408 -3.4714109491370646 1;
createNode joint -n "handProxySkinLFT_jnt" -p "wristProxySkinLFT_jnt";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".t" -type "double3" -3.4816594052244909e-011 9.3880866852304194 -5.163805127939014e-006 ;
	setAttr ".ro" 1;
	setAttr ".ssc" no;
	setAttr ".bps" -type "matrix" -0.80723769735614159 -0.59022648192634908 0 0 0.59022648192634919 -0.80723769735614159 -2.1175823681357508e-022 0
		 1.0587911840678754e-022 -2.1175823681357508e-022 1 0 54.439783831397349 96.734864961269381 -3.4714161129421925 1;
createNode joint -n "index1ProxySkinLFT_jnt" -p "handProxySkinLFT_jnt";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".t" -type "double3" -0.41730921184299063 -6.2885619810649871 3.3206718290628436 ;
	setAttr ".r" -type "double3" -1.2563190991780891e-013 -5.7399072767036922e-015 -7.9513867036587298e-016 ;
	setAttr ".jo" -type "double3" 89.999999999947534 -84.769180512173094 -89.999999999947605 ;
	setAttr ".ssc" no;
	setAttr ".bps" -type "matrix" -0.05380991829891791 0.073594452083357242 0.99583550314056102 0
		 0.58776848559600547 -0.80387595850068383 0.091168254808270732 0 0.80723769735613982 0.59022648192635152 8.3488771451811772e-014 0
		 51.064975744191209 102.0575362025272 -0.15074428387934891 1;
createNode joint -n "index2ProxySkinLFT_jnt" -p "index1ProxySkinLFT_jnt";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".t" -type "double3" 1.1830536550405668e-012 7.9712898007461348 4.2632564145606011e-014 ;
	setAttr ".bps" -type "matrix" -0.05380991829891791 0.073594452083357242 0.99583550314056102 0
		 0.58776848559600547 -0.80387595850068383 0.091168254808270732 0 0.80723769735613982 0.59022648192635152 8.3488771451811772e-014 0
		 55.750248678622619 95.649607973465791 0.57598429582682253 1;
createNode joint -n "index3ProxySkinLFT_jnt" -p "index2ProxySkinLFT_jnt";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".t" -type "double3" 3.8191672047105385e-013 4.5012097358703613 0 ;
	setAttr ".bps" -type "matrix" -0.05380991829891791 0.073594452083357242 0.99583550314056102 0
		 0.58776848559600547 -0.80387595850068383 0.091168254808270732 0 0.80723769735613982 0.59022648192635152 8.3488771451811772e-014 0
		 58.395917908425119 92.031193682630416 0.98635173197250092 1;
createNode joint -n "index4ProxySkinLFT_jnt" -p "index3ProxySkinLFT_jnt";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".t" -type "double3" 2.2915003228263231e-013 2.7661755084991171 -2.8421709430404007e-014 ;
	setAttr ".bps" -type "matrix" -0.05380991829891791 0.073594452083357242 0.99583550314056102 0
		 0.58776848559600547 -0.80387595850068383 0.091168254808270732 0 0.80723769735613982 0.59022648192635152 8.3488771451811772e-014 0
		 60.021788697948367 89.807531694354566 1.2385391255759746 1;
createNode joint -n "index5ProxySkinLFT_jnt" -p "index4ProxySkinLFT_jnt";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".t" -type "double3" 2.6201263381153694e-013 3.0700502395629883 5.6843418860808015e-014 ;
	setAttr ".bps" -type "matrix" -0.05380991829891791 0.073594452083357242 0.99583550314056102 0
		 0.58776848559600547 -0.80387595850068383 0.091168254808270732 0 0.80723769735613982 0.59022648192635152 8.3488771451811772e-014 0
		 61.826267477959988 87.339592115380668 1.5184302480909067 1;
createNode joint -n "middle1ProxySkinLFT_jnt" -p "handProxySkinLFT_jnt";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".t" -type "double3" -0.38446972249563771 -6.2502803554177149 1.3734927967666297 ;
	setAttr ".jo" -type "double3" 0 -89.999999999989612 0 ;
	setAttr ".ssc" no;
	setAttr ".bps" -type "matrix" -1.4644134755118067e-013 -1.0707324731018576e-013 1 0
		 0.59022648192634919 -0.80723769735614159 -2.1175823681357508e-022 0 0.80723769735614159 0.59022648192634908 1.8141044222375058e-013 0
		 51.061061299656316 102.00725109492291 -2.0979233161755628 1;
createNode joint -n "middle2ProxySkinLFT_jnt" -p "middle1ProxySkinLFT_jnt";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".t" -type "double3" 1.1883827255587676e-012 8.2252219902964825 2.8421709430404007e-014 ;
	setAttr ".bps" -type "matrix" -1.4644134755118067e-013 -1.0707324731018576e-013 1 0
		 0.59022648192634919 -0.80723769735614159 -2.1175823681357508e-022 0 0.80723769735614159 0.59022648192634908 1.8141044222375058e-013 0
		 55.915805138052278 95.367541835232885 -2.0979233161743744 1;
createNode joint -n "middle3ProxySkinLFT_jnt" -p "middle2ProxySkinLFT_jnt";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".t" -type "double3" 4.0012437807490642e-013 4.7475261688232564 0 ;
	setAttr ".bps" -type "matrix" -1.4644134755118067e-013 -1.0707324731018576e-013 1 0
		 0.59022648192634919 -0.80723769735614159 -2.1175823681357508e-022 0 0.80723769735614159 0.59022648192634908 1.8141044222375058e-013 0
		 58.71792080653011 91.535159742573981 -2.0979233161739743 1;
createNode joint -n "middle4ProxySkinLFT_jnt" -p "middle3ProxySkinLFT_jnt";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".t" -type "double3" 2.6778579353958776e-013 3.1957211494445659 0 ;
	setAttr ".bps" -type "matrix" -1.4644134755118067e-013 -1.0707324731018576e-013 1 0
		 0.59022648192634919 -0.80723769735614159 -2.1175823681357508e-022 0 0.80723769735614159 0.59022648192634908 1.8141044222375058e-013 0
		 60.604120057784407 88.955453160504021 -2.0979233161737065 1;
createNode joint -n "middle5ProxySkinLFT_jnt" -p "middle4ProxySkinLFT_jnt";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".t" -type "double3" 2.9132252166164108e-013 3.4594769477844238 1.4210854715202004e-014 ;
	setAttr ".bps" -type "matrix" -1.4644134755118067e-013 -1.0707324731018576e-013 1 0
		 0.59022648192634919 -0.80723769735614159 -2.1175823681357508e-022 0 0.80723769735614159 0.59022648192634908 1.8141044222375058e-013 0
		 62.64599496598052 86.162832955117878 -2.0979233161734152 1;
createNode joint -n "ring1ProxySkinLFT_jnt" -p "handProxySkinLFT_jnt";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".t" -type "double3" -0.40463191178650959 -6.2544362113196073 -1.1422382643303641 ;
	setAttr ".r" -type "double3" 4.1367089325784854e-013 -1.0753008112526133e-014 1.8089404750823706e-014 ;
	setAttr ".jo" -type "double3" -89.999999999906919 -87.022763360209112 89.999999999906308 ;
	setAttr ".ssc" no;
	setAttr ".bps" -type "matrix" 0.030655891891000257 -0.041927281032542299 0.99865024878462116 0
		 0.58942982301501412 -0.80614812729303986 -0.05193920101825282 0 0.8072376973561487 0.59022648192633942 8.4376949871511897e-014 0
		 51.07488408270477 102.02250611652478 -4.6136543772725567 1;
createNode joint -n "ring2ProxySkinLFT_jnt" -p "ring1ProxySkinLFT_jnt";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".t" -type "double3" 1.2407852523210749e-012 8.2730924912224566 5.6843418860808015e-014 ;
	setAttr ".bps" -type "matrix" 0.030655891891000257 -0.041927281032542299 0.99865024878462116 0
		 0.58942982301501412 -0.80614812729303986 -0.05193920101825282 0 0.8072376973561487 0.59022648192633942 8.4376949871511897e-014 0
		 55.95129152559295 95.353168097803675 -5.0433521912155186 1;
createNode joint -n "ring3ProxySkinLFT_jnt" -p "ring2ProxySkinLFT_jnt";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".t" -type "double3" 3.6504133049675147e-013 4.3779153823852752 8.5265128291212022e-014 ;
	setAttr ".bps" -type "matrix" 0.030655891891000257 -0.041927281032542299 0.99865024878462116 0
		 0.58942982301501412 -0.80614812729303986 -0.05193920101825282 0 0.8072376973561487 0.59022648192633942 8.4376949871511897e-014 0
		 58.531765414607094 91.823919810846434 -5.270737618301764 1;
createNode joint -n "ring4ProxySkinLFT_jnt" -p "ring3ProxySkinLFT_jnt";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".t" -type "double3" 2.4336088699783431e-013 2.8819530010223247 -1.4210854715202004e-014 ;
	setAttr ".bps" -type "matrix" 0.030655891891000257 -0.041927281032542299 0.99865024878462116 0
		 0.58942982301501412 -0.80614812729303986 -0.05193920101825282 0 0.8072376973561487 0.59022648192633942 8.4376949871511897e-014 0
		 60.23047446193727 89.500638796125713 -5.4204239545467763 1;
createNode joint -n "ring5ProxySkinLFT_jnt" -p "ring4ProxySkinLFT_jnt";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".t" -type "double3" 2.7267077484793845e-013 3.2981657981872559 8.5265128291212022e-014 ;
	setAttr ".bps" -type "matrix" 0.030655891891000257 -0.041927281032542299 0.99865024878462116 0
		 0.58942982301501412 -0.80614812729303986 -0.05193920101825282 0 0.8072376973561487 0.59022648192633942 8.4376949871511897e-014 0
		 62.174511744637037 86.841828614415135 -5.5917280509300777 1;
createNode joint -n "pinky1ProxySkinLFT_jnt" -p "handProxySkinLFT_jnt";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".t" -type "double3" 0.031037366383927179 -6.1655452894430098 -3.5337675514816742 ;
	setAttr ".r" -type "double3" -8.0706575042136755e-014 4.174478019420866e-015 -2.940075398216848e-030 ;
	setAttr ".jo" -type "double3" -89.999999999899259 -84.088992492743301 89.999999999899742 ;
	setAttr ".ssc" no;
	setAttr ".bps" -type "matrix" 0.060783668259022761 -0.083132271941291982 0.99468305054165684 0
		 0.58708827755298587 -0.80294565531841888 -0.10298363445297434 0 0.80723769735614181 0.59022648192634874 1.8107737531636303e-013 0
		 50.775661193880069 101.69360646809531 -7.0051836644238668 1;
createNode joint -n "pinky2ProxySkinLFT_jnt" -p "pinky1ProxySkinLFT_jnt";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".t" -type "double3" 1.1652900866465643e-012 7.4065697414324632 2.8421709430404007e-014 ;
	setAttr ".bps" -type "matrix" 0.060783668259022761 -0.083132271941291982 0.99468305054165684 0
		 0.58708827755298587 -0.80294565531841888 -0.10298363445297434 0 0.80723769735614181 0.59022648192634874 1.8107737531636303e-013 0
		 55.123971465953815 95.746533473399168 -7.7679391352248492 1;
createNode joint -n "pinky3ProxySkinLFT_jnt" -p "pinky2ProxySkinLFT_jnt";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".t" -type "double3" 3.0375701953744283e-013 3.5743153095245361 1.4210854715202004e-014 ;
	setAttr ".bps" -type "matrix" 0.060783668259022761 -0.083132271941291982 0.99468305054165684 0
		 0.58708827755298587 -0.80294565531841888 -0.10298363445297434 0 0.80723769735614181 0.59022648192634874 1.8107737531636303e-013 0
		 57.22241008445387 92.876552524878321 -8.1360351164802918 1;
createNode joint -n "pinky4ProxySkinLFT_jnt" -p "pinky3ProxySkinLFT_jnt";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".t" -type "double3" 2.2026824808563106e-013 2.5687654018402242 -1.4210854715202004e-014 ;
	setAttr ".bps" -type "matrix" 0.060783668259022761 -0.083132271941291982 0.99468305054165684 0
		 0.58708827755298587 -0.80294565531841888 -0.10298363445297434 0 0.80723769735614181 0.59022648192634874 1.8107737531636303e-013 0
		 58.730502139657951 90.813973505938407 -8.4005759136186349 1;
createNode joint -n "pinky5ProxySkinLFT_jnt" -p "pinky4ProxySkinLFT_jnt";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".t" -type "double3" 2.3447910280083306e-013 2.773944616317749 -2.8421709430404007e-014 ;
	setAttr ".bps" -type "matrix" 0.060783668259022761 -0.083132271941291982 0.99468305054165684 0
		 0.58708827755298587 -0.80294565531841888 -0.10298363445297434 0 0.80723769735614181 0.59022648192634874 1.8107737531636303e-013 0
		 60.359052506479308 88.586646728172113 -8.686246811978064 1;
createNode joint -n "thumb1ProxySkinLFT_jnt" -p "handProxySkinLFT_jnt";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".t" -type "double3" 1.4165168608910932 -6.816302240489442 2.6100399637168659 ;
	setAttr ".r" -type "double3" -9.5416640443905503e-015 3.975693351829396e-015 7.951386703658788e-016 ;
	setAttr ".jo" -type "double3" 34.025117761710071 -23.440713848906285 -51.206437321755523 ;
	setAttr ".ssc" no;
	setAttr ".bps" -type "matrix" -0.88607168703326855 0.23797515539292663 0.397799938227409 0
		 -1.9984014388896878e-014 -0.85816298902846522 0.51337733126982776 0 0.46354823420871538 0.4548891180028854 0.76039392743796896 0
		 49.273155931194708 101.40117532297248 -0.86137614922532668 1;
createNode joint -n "thumb2ProxySkinLFT_jnt" -p "thumb1ProxySkinLFT_jnt";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".t" -type "double3" 0.013455738170272014 3.8389952476881604 0.83355343883231114 ;
	setAttr ".bps" -type "matrix" -0.88607168703326855 0.23797515539292663 0.397799938227409 0
		 -1.9984014388896878e-014 -0.85816298902846522 0.51337733126982776 0 0.46354823420871538 0.4548891180028854 0.76039392743796896 0
		 49.647625407263142 98.489068206331027 1.7486586506864366 1;
createNode joint -n "thumb3ProxySkinLFT_jnt" -p "thumb2ProxySkinLFT_jnt";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".t" -type "double3" 2.8776980798284058e-013 4.5514883995055868 2.4158453015843406e-013 ;
	setAttr ".bps" -type "matrix" -0.88607168703326855 0.23797515539292663 0.397799938227409 0
		 -1.9984014388896878e-014 -0.85816298902846522 0.51337733126982776 0 0.46354823420871538 0.4548891180028854 0.76039392743796896 0
		 49.647625407262908 94.583149316883109 4.085289618530493 1;
createNode joint -n "thumb4ProxySkinLFT_jnt" -p "thumb3ProxySkinLFT_jnt";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".t" -type "double3" 1.3500311979441904e-013 3.7794413566589355 1.1368683772161603e-013 ;
	setAttr ".bps" -type "matrix" -0.88607168703326855 0.23797515539292663 0.397799938227409 0
		 -1.9984014388896878e-014 -0.85816298902846522 0.51337733126982776 0 0.46354823420871538 0.4548891180028854 0.76039392743796896 0
		 49.647625407262765 91.339772625394957 6.025569135903015 1;
createNode joint -n "forearmRbnDtl1ProxySkinLFT_jnt" -p "forearmProxySkinLFT_jnt";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".t" -type "double3" -1.8928858480649069e-011 2.583812066457142 -0.012356304365563009 ;
	setAttr ".jo" -type "double3" -4.238114764090535e-016 0.27399775040866592 90.000000000420087 ;
	setAttr ".bps" -type "matrix" 0.59021973004496386 -0.80722846296784989 -0.0047831830627840842 0
		 0.80723769735181361 0.59022648193226734 2.1684043449710081e-019 0 0.0028231613115850588 -0.003861165681614021 0.99998856051446305 0
		 35.17337776966005 123.08503687263511 -3.3601800622421067 1;
	setAttr ".radi" 2;
createNode joint -n "forearmRbnDtl2ProxySkinLFT_jnt" -p "forearmProxySkinLFT_jnt";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".t" -type "double3" -5.6814997151377611e-011 7.7514361993713123 -0.037068913096688139 ;
	setAttr ".jo" -type "double3" -4.238114764090535e-016 0.27399775040866592 90.000000000420087 ;
	setAttr ".bps" -type "matrix" 0.59021973004496386 -0.80722846296784989 -0.0047831830627840842 0
		 0.80723769735181361 0.59022648193226734 2.1684043449710081e-019 0 0.0028231613115850588 -0.003861165681614021 0.99998856051446305 0
		 38.223446366430274 118.91353588751933 -3.3848980371076527 1;
	setAttr ".radi" 2;
createNode joint -n "forearmRbnDtl3ProxySkinLFT_jnt" -p "forearmProxySkinLFT_jnt";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".t" -type "double3" -9.4701135822106153e-011 12.919060332285497 -0.061781521827812824 ;
	setAttr ".jo" -type "double3" -4.238114764090535e-016 0.27399775040866592 90.000000000420087 ;
	setAttr ".bps" -type "matrix" 0.59021973004496386 -0.80722846296784989 -0.0047831830627840842 0
		 0.80723769735181361 0.59022648193226734 2.1684043449710081e-019 0 0.0028231613115850588 -0.003861165681614021 0.99998856051446305 0
		 41.273514963200505 114.74203490240355 -3.4096160119731982 1;
	setAttr ".radi" 2;
createNode joint -n "forearmRbnDtl4ProxySkinLFT_jnt" -p "forearmProxySkinLFT_jnt";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".t" -type "double3" -1.3258727449283469e-010 18.086684465199696 -0.086494130558938842 ;
	setAttr ".jo" -type "double3" -4.238114764090535e-016 0.27399775040866592 90.000000000420087 ;
	setAttr ".bps" -type "matrix" 0.59021973004496386 -0.80722846296784989 -0.0047831830627840842 0
		 0.80723769735181361 0.59022648193226734 2.1684043449710081e-019 0 0.0028231613115850588 -0.003861165681614021 0.99998856051446305 0
		 44.323583559970743 110.57053391728775 -3.434333986838745 1;
	setAttr ".radi" 2;
createNode joint -n "forearmRbnDtl5ProxySkinLFT_jnt" -p "forearmProxySkinLFT_jnt";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".t" -type "double3" -1.7048762401827844e-010 23.254308598113873 -0.11120673929006397 ;
	setAttr ".jo" -type "double3" -4.238114764090535e-016 0.27399775040866592 90.000000000420087 ;
	setAttr ".bps" -type "matrix" 0.59021973004496386 -0.80722846296784989 -0.0047831830627840842 0
		 0.80723769735181361 0.59022648193226734 2.1684043449710081e-019 0 0.0028231613115850588 -0.003861165681614021 0.99998856051446305 0
		 47.373652156740981 106.39903293217196 -3.459051961704291 1;
	setAttr ".radi" 2;
createNode joint -n "upArmRbnDtl1ProxySkinLFT_jnt" -p "upArmProxySkinLFT_jnt";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".t" -type "double3" -5.8548721426632255e-012 2.679594470657193 -0.058742491966384591 ;
	setAttr ".jo" -type "double3" 0 1.2558459485975768 90.000000000126192 ;
	setAttr ".bps" -type "matrix" 0.59008470721367889 -0.80704379569583795 -0.021916891691136926 0
		 0.80723769735484163 0.59022648192812632 0 0 0.012935929877659536 -0.017692141181928835 0.99975979608033783 0
		 19.414234914584082 144.63841439823619 -2.8191386471118633 1;
	setAttr ".radi" 2;
createNode joint -n "upArmRbnDtl2ProxySkinLFT_jnt" -p "upArmProxySkinLFT_jnt";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".t" -type "double3" -1.7649881556280889e-011 8.038783411971707 -0.17622747589915644 ;
	setAttr ".jo" -type "double3" 0 1.2558459485975768 90.000000000126192 ;
	setAttr ".bps" -type "matrix" 0.59008470721367889 -0.80704379569583795 -0.021916891691136926 0
		 0.80723769735484163 0.59022648192812632 0 0 0.012935929877659536 -0.017692141181928835 0.99975979608033783 0
		 22.577370149404253 140.31227505755993 -2.9366236310446352 1;
	setAttr ".radi" 2;
createNode joint -n "upArmRbnDtl3ProxySkinLFT_jnt" -p "upArmProxySkinLFT_jnt";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".t" -type "double3" -2.9459101824613754e-011 13.397972353286207 -0.29371245983192651 ;
	setAttr ".jo" -type "double3" 0 1.2558459485975768 90.000000000126192 ;
	setAttr ".bps" -type "matrix" 0.59008470721367889 -0.80704379569583795 -0.021916891691136926 0
		 0.80723769735484163 0.59022648192812632 0 0 0.012935929877659536 -0.017692141181928835 0.99975979608033783 0
		 25.740505384224441 135.98613571688367 -3.0541086149774053 1;
	setAttr ".radi" 2;
createNode joint -n "upArmRbnDtl4ProxySkinLFT_jnt" -p "upArmProxySkinLFT_jnt";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".t" -type "double3" -4.1211478674085811e-011 18.757161294600706 -0.41119744376469791 ;
	setAttr ".jo" -type "double3" 0 1.2558459485975768 90.000000000126192 ;
	setAttr ".bps" -type "matrix" 0.59008470721367889 -0.80704379569583795 -0.021916891691136926 0
		 0.80723769735484163 0.59022648192812632 0 0 0.012935929877659536 -0.017692141181928835 0.99975979608033783 0
		 28.903640619044594 131.6599963762074 -3.1715935989101767 1;
	setAttr ".radi" 2;
createNode joint -n "upArmRbnDtl5ProxySkinLFT_jnt" -p "upArmProxySkinLFT_jnt";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".t" -type "double3" -5.3020698942418676e-011 24.116350235915206 -0.52868242769746843 ;
	setAttr ".jo" -type "double3" 0 1.2558459485975768 90.000000000126192 ;
	setAttr ".bps" -type "matrix" 0.59008470721367889 -0.80704379569583795 -0.021916891691136926 0
		 0.80723769735484163 0.59022648192812632 0 0 0.012935929877659536 -0.017692141181928835 0.99975979608033783 0
		 32.066775853864769 127.33385703553117 -3.2890785828429472 1;
	setAttr ".radi" 2;
createNode joint -n "clav1ScaProxySkinLFT_jnt" -p "clav1ProxySkinLFT_jnt";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".t" -type "double3" 0 0 -8.8817841970012523e-016 ;
	setAttr ".bps" -type "matrix" 2.2204460492503131e-016 -1.0000000000000002 0 0 1.0000000000000002 2.2204460492503131e-016 0 0
		 0 0 1 0 1.9757774640097452 148.51959409424302 6.184552379566326 1;
	setAttr ".radi" 2;
createNode joint -n "clav1ProxySkinRGT_jnt" -p "spine4ProxySkin_jnt";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".t" -type "double3" -1.97578 4.5842689515619099 6.9513094441683743 ;
	setAttr ".jo" -type "double3" 180 0 89.999999999999972 ;
	setAttr ".bps" -type "matrix" 4.4408920985006262e-016 1 0 0 1 -4.4408920985006262e-016 1.224646799147353e-016 0
		 1.2246467991473532e-016 -6.1629758220391547e-032 -1 0 -1.9757800000000001 148.52000000000001 6.1845499999999998 1;
createNode joint -n "clav2ProxySkinRGT_jnt" -p "clav1ProxySkinRGT_jnt";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".t" -type "double3" -1.7190000000000225 -15.856919999999997 8.9449499999999986 ;
	setAttr ".jo" -type "double3" 0 0 -53.826918307873285 ;
	setAttr ".bps" -type "matrix" -0.80723769735614148 0.59022648192634886 -9.8858106221827856e-017 0
		 0.59022648192634886 0.80723769735614148 7.2281897186310574e-017 0 1.2246467991473532e-016 -6.1629758220391547e-032 -1 0
		 -17.832699999999996 146.80099999999999 -2.7604000000000006 1;
createNode joint -n "upArmProxySkinRGT_jnt" -p "clav2ProxySkinRGT_jnt";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".t" -type "double3" 0 0 -4.4408920985006262e-016 ;
	setAttr ".ro" 1;
	setAttr ".bps" -type "matrix" -0.80723769735614148 0.59022648192634886 -9.8858106221827856e-017 0
		 0.59022648192634886 0.80723769735614148 7.2281897186310574e-017 0 1.2246467991473532e-016 -6.1629758220391547e-032 -1 0
		 -17.832699999999996 146.80099999999999 -2.7604000000000002 1;
createNode joint -n "forearmProxySkinRGT_jnt" -p "upArmProxySkinRGT_jnt";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".t" -type "double3" 0.00034972223885176845 -26.795337341367741 0.58741999999999939 ;
	setAttr ".ro" 1;
	setAttr ".jo" -type "double3" 5.9476840593794676e-005 0 0 ;
	setAttr ".bps" -type "matrix" -0.80723769735614148 0.59022648192634886 -9.8858106221827856e-017 0
		 0.59022648192603089 0.8072376973557065 -1.038066696973068e-006 0 -6.1269445447951729e-007 -8.3796657022498363e-007 -0.99999999999946121 0
		 -33.648300000000006 125.17099999999995 -3.3478200000000014 1;
createNode joint -n "wristProxySkinRGT_jnt" -p "forearmProxySkinRGT_jnt";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".t" -type "double3" -0.00024618025960876366 -25.83855370311538 0.12361682214216829 ;
	setAttr ".ro" 1;
	setAttr ".jo" -type "double3" 5.945845423973661e-005 0 0 ;
	setAttr ".bps" -type "matrix" -0.80723769735614148 0.59022648192634886 -9.8858106221827856e-017 0
		 0.59022648192507721 0.80723769735440221 -2.0758124916015486e-006 0 -1.2251995039769489e-006 -1.6756740959218976e-006 -0.9999999999978455 0
		 -48.898700000000055 104.31300000000002 -3.4714100000000059 1;
createNode joint -n "handProxySkinRGT_jnt" -p "wristProxySkinRGT_jnt";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".t" -type "double3" 0.00018950213402035843 -9.3878319532956667 2.9487378840453715e-005 ;
	setAttr ".ro" 1;
	setAttr ".jo" -type "double3" 0.00011892303804445534 0 0 ;
	setAttr ".ssc" no;
	setAttr ".bps" -type "matrix" -0.80723769735614148 0.59022648192634886 -9.8858106221827856e-017 0
		 0.5902264819212627 0.80723769734918538 -4.1514110619413382e-006 0 -2.4502727460399623e-006 -3.3511755064786885e-006 -0.99999999999138289 0
		 -54.43980000000002 96.73490000000001 -3.4714200000000086 1;
createNode joint -n "index1ProxySkinRGT_jnt" -p "handProxySkinRGT_jnt";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".t" -type "double3" 0.41756880490460446 6.288889532456281 -3.3207021077941885 ;
	setAttr ".r" -type "double3" 3.975693351829396e-016 -1.2722218725854067e-014 -3.975693351829396e-016 ;
	setAttr ".jo" -type "double3" 89.99999999994759 -84.769418370501143 -89.999999999948088 ;
	setAttr ".ssc" no;
	setAttr ".bps" -type "matrix" -0.053809918298966607 -0.073594452083425549 -0.99583550314055314 0
		 0.58776848559599437 0.80387595850068194 -0.091168254808354665 0 0.80723769735614415 -0.59022648192634519 -8.316788755039658e-014 0
		 -51.064999999999969 102.05800000000002 -0.15074400000000754 1;
createNode joint -n "index2ProxySkinRGT_jnt" -p "index1ProxySkinRGT_jnt";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".t" -type "double3" 3.1372419434738674e-005 -7.97162612465047 0.00033732712374501261 ;
	setAttr ".bps" -type "matrix" -0.053809918298966607 -0.073594452083425549 -0.99583550314055314 0
		 0.58776848559599437 0.80387595850068194 -0.091168254808354665 0 0.80723769735614415 -0.59022648192634519 -8.316788755039658e-014 0
		 -55.750199999999943 95.649600000000021 0.57598399999997085 1;
createNode joint -n "index3ProxySkinRGT_jnt" -p "index2ProxySkinRGT_jnt";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".t" -type "double3" 4.2509459063921895e-008 -4.501216411590562 -3.3273692920943176e-005 ;
	setAttr ".bps" -type "matrix" -0.053809918298966607 -0.073594452083425549 -0.99583550314055314 0
		 0.58776848559599437 0.80387595850068194 -0.091168254808354665 0 0.80723769735614415 -0.59022648192634519 -8.316788755039658e-014 0
		 -58.395900015647051 92.031199978599915 0.98635200242697851 1;
createNode joint -n "index4ProxySkinRGT_jnt" -p "index3ProxySkinRGT_jnt";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".t" -type "double3" 3.7653941955539949e-006 -2.7662231922149729 -1.1442717067211561e-006 ;
	setAttr ".bps" -type "matrix" -0.053809918298966607 -0.073594452083425549 -0.99583550314055314 0
		 0.58776848559599437 0.80387595850068194 -0.091168254808354665 0 0.80723769735614415 -0.59022648192634519 -8.316788755039658e-014 0
		 -60.021799958470574 89.807500056798631 1.2385399935583901 1;
createNode joint -n "index5ProxySkinRGT_jnt" -p "index4ProxySkinRGT_jnt";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".t" -type "double3" -6.5310683794450597e-007 -3.070030689239502 -4.0490133173420872e-005 ;
	setAttr ".bps" -type "matrix" -0.053809918298966607 -0.073594452083425549 -0.99583550314055314 0
		 0.58776848559599437 0.80387595850068194 -0.091168254808354665 0 0.80723769735614415 -0.59022648192634519 -8.316788755039658e-014 0
		 -61.826299897436343 87.339600140273618 1.5184299840914222 1;
createNode joint -n "middle1ProxySkinRGT_jnt" -p "handProxySkinRGT_jnt";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".t" -type "double3" 0.3843190273066881 6.2500303766989447 -1.373525946457081 ;
	setAttr ".r" -type "double3" -1.5554342031205659e-009 3.228642142902349e-015 4.4979641526365485e-015 ;
	setAttr ".jo" -type "double3" -89.999526517399829 -89.999762141660383 90.000002230994426 ;
	setAttr ".ssc" no;
	setAttr ".bps" -type "matrix" 1.997380727272193e-013 -1.1375017206914813e-016 -0.99999999999999989 0
		 0.59023318417089854 0.80723279684579352 1.1780021606073131e-013 0 0.80723279684579341 -0.59023318417089854 1.6119291726964065e-013 0
		 -51.061099999999989 102.00700000000002 -2.0979200000000064 1;
createNode joint -n "middle2ProxySkinRGT_jnt" -p "middle1ProxySkinRGT_jnt";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".t" -type "double3" -9.6855856668298657e-013 -8.225027193852128 -1.9832544623454851e-005 ;
	setAttr ".r" -type "double3" 1.5902676344491611e-014 0 0 ;
	setAttr ".jo" -type "double3" -0.00047570747547553358 0 0 ;
	setAttr ".bps" -type "matrix" 1.997380727272193e-013 -1.1375017206914813e-016 -0.99999999999999989 0
		 0.59022648196971073 0.80723769732443662 1.1779887772640681e-013 0 0.80723769732443651 -0.59022648196971073 1.6119389531942968e-013 0
		 -55.915800000000026 95.367500000000021 -2.0979200000000069 1;
createNode joint -n "middle3ProxySkinRGT_jnt" -p "middle2ProxySkinRGT_jnt";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".t" -type "double3" -5.5777604757167865e-013 -4.7474508285522461 -3.5804820242901769e-005 ;
	setAttr ".bps" -type "matrix" 1.997380727272193e-013 -1.1375017206914813e-016 -0.99999999999999989 0
		 0.59022648196971073 0.80723769732443662 1.1779887772640681e-013 0 0.80723769732443651 -0.59022648196971073 1.6119389531942968e-013 0
		 -58.717900103861254 91.535199857951611 -2.0979200000000082 1;
createNode joint -n "middle4ProxySkinRGT_jnt" -p "middle3ProxySkinRGT_jnt";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".t" -type "double3" -3.7525538232330291e-013 -3.1957163810729909 -4.4891561543636271e-006 ;
	setAttr ".bps" -type "matrix" 1.997380727272193e-013 -1.1375017206914813e-016 -0.99999999999999989 0
		 0.59022648196971073 0.80723769732443662 1.1779887772640681e-013 0 0.80723769732443651 -0.59022648196971073 1.6119389531942968e-013 0
		 -60.604100164651015 88.955499774811116 -2.0979200000000096 1;
createNode joint -n "middle5ProxySkinRGT_jnt" -p "middle4ProxySkinRGT_jnt";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".t" -type "double3" -4.0811798385220754e-013 -3.4595561027526855 2.6842030024454289e-005 ;
	setAttr ".bps" -type "matrix" 1.997380727272193e-013 -1.1375017206914813e-016 -0.99999999999999989 0
		 0.59022648196971073 0.80723769732443662 1.1779887772640681e-013 0 0.80723769732443651 -0.59022648196971073 1.6119389531942968e-013 0
		 -62.646000124457068 86.162799829783381 -2.0979200000000091 1;
createNode joint -n "ring1ProxySkinRGT_jnt" -p "handProxySkinRGT_jnt";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".t" -type "double3" 0.40490253124100661 6.2548114982353411 1.1422040337162018 ;
	setAttr ".r" -type "double3" -1.3934805198162038e-013 -2.7395012002448946e-015 4.0750856856251317e-014 ;
	setAttr ".jo" -type "double3" -89.999999999905953 -87.022525501881034 89.999999999906436 ;
	setAttr ".ssc" no;
	setAttr ".bps" -type "matrix" 0.030655891890951088 0.041927281032474728 -0.99865024878462538 0
		 0.58942982301503133 0.80614812729303231 0.051939201018169269 0 0.80723769735613748 -0.5902264819263543 -8.5166242199031272e-014 0
		 -51.074899999999992 102.02299999999998 -4.6136500000000122 1;
createNode joint -n "ring2ProxySkinRGT_jnt" -p "ring1ProxySkinRGT_jnt";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".t" -type "double3" -1.6958344660089608e-005 -8.2734606430470023 0.00027868176488254903 ;
	setAttr ".bps" -type "matrix" 0.030655891890951088 0.041927281032474728 -0.99865024878462538 0
		 0.58942982301503133 0.80614812729303231 0.051939201018169269 0 0.80723769735613748 -0.5902264819263543 -8.5166242199031272e-014 0
		 -55.951300000000018 95.353200000000086 -5.0433500000000286 1;
createNode joint -n "ring3ProxySkinRGT_jnt" -p "ring2ProxySkinRGT_jnt";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".t" -type "double3" 1.5980986267649655e-006 -4.3779726028442454 9.4446351965871145e-006 ;
	setAttr ".bps" -type "matrix" 0.030655891890951088 0.041927281032474728 -0.99865024878462538 0
		 0.58942982301503133 0.80614812729303231 0.051939201018169269 0 0.80723769735613748 -0.5902264819263543 -8.5166242199031272e-014 0
		 -58.531799943402447 91.823900077407117 -5.2707399950127849 1;
createNode joint -n "ring4ProxySkinRGT_jnt" -p "ring3ProxySkinRGT_jnt";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".t" -type "double3" -6.8463398248397311e-006 -2.8819625377655029 1.8508960607732661e-005 ;
	setAttr ".bps" -type "matrix" 0.030655891890951088 0.041927281032474728 -0.99865024878462538 0
		 0.58942982301503133 0.80614812729303231 0.051939201018169269 0 0.80723769735613748 -0.5902264819263543 -8.5166242199031272e-014 0
		 -60.230499880723428 89.500600163131665 -5.420419989489651 1;
createNode joint -n "ring5ProxySkinRGT_jnt" -p "ring4ProxySkinRGT_jnt";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".t" -type "double3" 7.4654741437640837e-006 -3.2981359958648682 2.4086485510110833e-005 ;
	setAttr ".bps" -type "matrix" 0.030655891890951088 0.041927281032474728 -0.99865024878462538 0
		 0.58942982301503133 0.80614812729303231 0.051939201018169269 0 0.80723769735613748 -0.5902264819263543 -8.5166242199031272e-014 0
		 -62.174499924665696 86.841800103032895 -5.5917299933617475 1;
createNode joint -n "pinky1ProxySkinRGT_jnt" -p "handProxySkinRGT_jnt";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".t" -type "double3" -0.030807500361731854 6.1658359874224118 3.5337344031107287 ;
	setAttr ".r" -type "double3" -9.1440947092076072e-015 4.7211358552973996e-016 -9.1440947092076072e-015 ;
	setAttr ".jo" -type "double3" -89.999999999898833 -84.088754634415253 89.999999999899828 ;
	setAttr ".ssc" no;
	setAttr ".bps" -type "matrix" 0.060783668258973515 0.083132271941224314 -0.99468305054166561 0
		 0.58708827755299731 0.80294565531842077 0.10298363445289072 0 0.80723769735613671 -0.59022648192635541 -1.8175563988181248e-013 0
		 -50.775699999999972 101.69399999999999 -7.0051800000000108 1;
createNode joint -n "pinky2ProxySkinRGT_jnt" -p "pinky1ProxySkinRGT_jnt";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".t" -type "double3" -3.0368429754901172e-005 -7.4069070393052741 0.00026032184344160214 ;
	setAttr ".bps" -type "matrix" 0.060783668258973515 0.083132271941224314 -0.99468305054166561 0
		 0.58708827755299731 0.80294565531842077 0.10298363445289072 0 0.80723769735613671 -0.59022648192635541 -1.8175563988181248e-013 0
		 -55.123999999999967 95.746500000000012 -7.7679400000000189 1;
createNode joint -n "pinky3ProxySkinRGT_jnt" -p "pinky2ProxySkinRGT_jnt";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".t" -type "double3" 1.3074185629236013e-005 -3.5742280483246063 -1.6603651559421451e-005 ;
	setAttr ".bps" -type "matrix" 0.060783668258973515 0.083132271941224314 -0.99468305054166561 0
		 0.58708827755299731 0.80294565531842077 0.10298363445289072 0 0.80723769735613671 -0.59022648192635541 -1.8175563988181248e-013 0
		 -57.222399996868958 92.876600004282139 -8.1360399994507944 1;
createNode joint -n "pinky4ProxySkinRGT_jnt" -p "pinky3ProxySkinRGT_jnt";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".t" -type "double3" -3.0200170364480527e-006 -2.5687868595123149 5.9702384902493577e-006 ;
	setAttr ".bps" -type "matrix" 0.060783668258973515 0.083132271941224314 -0.99468305054166561 0
		 0.58708827755299731 0.80294565531842077 0.10298363445289072 0 0.80723769735613671 -0.59022648192635541 -1.8175563988181248e-013 0
		 -58.730500013786958 90.813999981143937 -8.400580002418442 1;
createNode joint -n "pinky5ProxySkinRGT_jnt" -p "pinky4ProxySkinRGT_jnt";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".t" -type "double3" -9.997600209032953e-006 -2.7740323543548584 3.1519285812464659e-006 ;
	setAttr ".bps" -type "matrix" 0.060783668258973515 0.083132271941224314 -0.99468305054166561 0
		 0.58708827755299731 0.80294565531842077 0.10298363445289072 0 0.80723769735613671 -0.59022648192635541 -1.8175563988181248e-013 0
		 -60.359099953916683 88.586600063027035 -8.6862499919163412 1;
createNode joint -n "thumb1ProxySkinRGT_jnt" -p "handProxySkinRGT_jnt";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".t" -type "double3" -1.4166184998437217 6.816105125729905 -2.6100722964767118 ;
	setAttr ".r" -type "double3" -1.4312496066585827e-014 2.385416011097636e-015 -1.1927080055488189e-014 ;
	setAttr ".jo" -type "double3" 34.024955334642861 -23.440899237591783 -51.206372708037129 ;
	setAttr ".ssc" no;
	setAttr ".bps" -type "matrix" -0.88607168703328809 -0.23797515539295319 -0.3977999382273491 0
		 -4.5975533831941508e-014 0.85816298902843124 -0.51337733126988438 0 0.46354823420867741 -0.45488911800293536 -0.76039392743796208 0
		 -49.273200000000024 101.40100000000001 -0.86137600000000702 1;
createNode joint -n "thumb2ProxySkinRGT_jnt" -p "thumb1ProxySkinRGT_jnt";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".t" -type "double3" -0.013567064957154429 -3.8388181239502188 -0.8336163609694438 ;
	setAttr ".bps" -type "matrix" -0.88607168703328809 -0.23797515539295319 -0.3977999382273491 0
		 -4.5975533831941508e-014 0.85816298902843124 -0.51337733126988438 0 0.46354823420867741 -0.45488911800293536 -0.76039392743796208 0
		 -49.647600000000018 98.489099999999993 1.7486600000000001 1;
createNode joint -n "thumb3ProxySkinRGT_jnt" -p "thumb2ProxySkinRGT_jnt";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".t" -type "double3" 1.9687304703808195e-005 -4.5515575408935547 3.7632250098340592e-005 ;
	setAttr ".bps" -type "matrix" -0.88607168703328809 -0.23797515539295319 -0.3977999382273491 0
		 -4.5975533831941508e-014 0.85816298902843124 -0.51337733126988438 0 0.46354823420867741 -0.45488911800293536 -0.76039392743796208 0
		 -49.647600000000018 94.583099972381433 4.0852900165222055 1;
createNode joint -n "thumb4ProxySkinRGT_jnt" -p "thumb3ProxySkinRGT_jnt";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".t" -type "double3" -1.8442657808037666e-005 -3.7793757915496826 -3.5253110411304078e-005 ;
	setAttr ".bps" -type "matrix" -0.88607168703328809 -0.23797515539295319 -0.3977999382273491 0
		 -4.5975533831941508e-014 0.85816298902843124 -0.51337733126988438 0 0.46354823420867741 -0.45488911800293536 -0.76039392743796208 0
		 -49.647600000000011 91.339799971594118 6.0255700169932052 1;
createNode joint -n "forearmRbnDtl1ProxySkinRGT_jnt" -p "forearmProxySkinRGT_jnt";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".t" -type "double3" -2.4618025975087221e-005 -2.5838553703116389 0.012361682214215186 ;
	setAttr ".jo" -type "double3" 179.99999999943333 0.27411240696987776 89.999454106834435 ;
	setAttr ".bps" -type "matrix" 0.59021203924837962 0.80723408662347429 0.0047831077172213908 0
		 -0.80724332078084238 0.59021879083499029 -2.452465314162211e-016 0 -0.0028230800532921176 -0.0038611317573021249 0.99998856087485599 0
		 -35.173340000000053 123.08519999999987 -3.3601790000000005 1;
	setAttr ".radi" 2;
createNode joint -n "forearmRbnDtl2ProxySkinRGT_jnt" -p "forearmProxySkinRGT_jnt";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".t" -type "double3" -7.3854077882629099e-005 -7.7515661109346752 0.037085046642648667 ;
	setAttr ".jo" -type "double3" 179.99999999943333 0.27411240696987776 89.999454106834435 ;
	setAttr ".bps" -type "matrix" 0.59021203924837962 0.80723408662347429 0.0047831077172213908 0
		 -0.80724332078084238 0.59021879083499029 -2.452465314162211e-016 0 -0.0028230800532921176 -0.0038611317573021249 0.99998856087485599 0
		 -38.223420000000061 118.91359999999992 -3.3848970000000014 1;
	setAttr ".radi" 2;
createNode joint -n "forearmRbnDtl3ProxySkinRGT_jnt" -p "forearmProxySkinRGT_jnt";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".t" -type "double3" -0.00012309012981859269 -12.919276851557782 0.061808411071082592 ;
	setAttr ".jo" -type "double3" 179.99999999943333 0.27411240696987776 89.999454106834435 ;
	setAttr ".bps" -type "matrix" 0.59021203924837962 0.80723408662347429 0.0047831077172213908 0
		 -0.80724332078084238 0.59021879083499029 -2.452465314162211e-016 0 -0.0028230800532921176 -0.0038611317573021249 0.99998856087485599 0
		 -41.27350000000007 114.7419999999999 -3.4096150000000027 1;
	setAttr ".radi" 2;
createNode joint -n "forearmRbnDtl4ProxySkinRGT_jnt" -p "forearmProxySkinRGT_jnt";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".t" -type "double3" -0.00017232618174034542 -18.086987592180868 0.086531775499516073 ;
	setAttr ".jo" -type "double3" 179.99999999943333 0.27411240696987776 89.999454106834435 ;
	setAttr ".bps" -type "matrix" 0.59021203924837962 0.80723408662347429 0.0047831077172213908 0
		 -0.80724332078084238 0.59021879083499029 -2.452465314162211e-016 0 -0.0028230800532921176 -0.0038611317573021249 0.99998856087485599 0
		 -44.323580000000085 110.57039999999991 -3.4343330000000032 1;
	setAttr ".radi" 2;
createNode joint -n "forearmRbnDtl5ProxySkinRGT_jnt" -p "forearmProxySkinRGT_jnt";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".t" -type "double3" -0.00022156223366209815 -23.254698332803926 0.11125513992795089 ;
	setAttr ".jo" -type "double3" 179.99999999943333 0.27411240696987776 89.999454106834435 ;
	setAttr ".bps" -type "matrix" 0.59021203924837962 0.80723408662347429 0.0047831077172213908 0
		 -0.80724332078084238 0.59021879083499029 -2.452465314162211e-016 0 -0.0028230800532921176 -0.0038611317573021249 0.99998856087485599 0
		 -47.373660000000086 106.39879999999994 -3.4590510000000054 1;
	setAttr ".radi" 2;
createNode joint -n "upArmRbnDtl1ProxySkinRGT_jnt" -p "upArmProxySkinRGT_jnt";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".t" -type "double3" 3.497222394344135e-005 -2.6795337341366832 0.05874199999999874 ;
	setAttr ".jo" -type "double3" -180 1.2558638908763025 90.00074780205351 ;
	setAttr ".bps" -type "matrix" 0.59009523632988103 0.80703608853380926 0.021917204767754699 0
		 -0.80722999388272187 0.59023701762605585 0 0 -0.01293634557681911 -0.017692225070600986 0.99975978921697406 0
		 -19.414259999999988 144.63800000000009 -2.8191419999999998 1;
	setAttr ".radi" 2;
createNode joint -n "upArmRbnDtl2ProxySkinRGT_jnt" -p "upArmProxySkinRGT_jnt";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".t" -type "double3" 0.00010491667170242636 -8.0386012024102911 0.17622599999999933 ;
	setAttr ".jo" -type "double3" -180 1.2558638908763025 90.00074780205351 ;
	setAttr ".bps" -type "matrix" 0.59009523632988103 0.80703608853380926 0.021917204767754699 0
		 -0.80722999388272187 0.59023701762605585 0 0 -0.01293634557681911 -0.017692225070600986 0.99975978921697406 0
		 -22.577380000000012 140.31200000000004 -2.9366260000000008 1;
	setAttr ".radi" 2;
createNode joint -n "upArmRbnDtl3ProxySkinRGT_jnt" -p "upArmProxySkinRGT_jnt";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".t" -type "double3" 0.00017486111944720051 -13.397668670683814 0.29370999999999681 ;
	setAttr ".jo" -type "double3" -180 1.2558638908763025 90.00074780205351 ;
	setAttr ".bps" -type "matrix" 0.59009523632988103 0.80703608853380926 0.021917204767754699 0
		 -0.80722999388272187 0.59023701762605585 0 0 -0.01293634557681911 -0.017692225070600986 0.99975978921697406 0
		 -25.740499999999983 135.98600000000005 -3.0541099999999988 1;
	setAttr ".radi" 2;
createNode joint -n "upArmRbnDtl4ProxySkinRGT_jnt" -p "upArmProxySkinRGT_jnt";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".t" -type "double3" 0.00024480556722039637 -18.756736138957365 0.41119399999999739 ;
	setAttr ".jo" -type "double3" -180 1.2558638908763025 90.00074780205351 ;
	setAttr ".bps" -type "matrix" 0.59009523632988103 0.80703608853380926 0.021917204767754699 0
		 -0.80722999388272187 0.59023701762605585 0 0 -0.01293634557681911 -0.017692225070600986 0.99975978921697406 0
		 -28.903619999999989 131.66000000000003 -3.1715939999999998 1;
	setAttr ".radi" 2;
createNode joint -n "upArmRbnDtl5ProxySkinRGT_jnt" -p "upArmProxySkinRGT_jnt";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".t" -type "double3" 0.00031475001499359223 -24.11580360723093 0.52867799999999709 ;
	setAttr ".jo" -type "double3" -180 1.2558638908763025 90.00074780205351 ;
	setAttr ".bps" -type "matrix" 0.59009523632988103 0.80703608853380926 0.021917204767754699 0
		 -0.80722999388272187 0.59023701762605585 0 0 -0.01293634557681911 -0.017692225070600986 0.99975978921697406 0
		 -32.06674000000001 127.33400000000002 -3.2890779999999999 1;
	setAttr ".radi" 2;
createNode joint -n "clav1ScaProxySkinRGT_jnt" -p "clav1ProxySkinRGT_jnt";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".bps" -type "matrix" 4.4408920985006262e-016 1 0 0 1 -4.4408920985006262e-016 1.224646799147353e-016 0
		 1.2246467991473532e-016 -6.1629758220391547e-032 -1 0 -1.9757800000000001 148.52000000000001 6.1845499999999998 1;
	setAttr ".radi" 2;
createNode joint -n "spine3ScaProxySkin_jnt" -p "spine3ProxySkin_jnt";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".bps" -type "matrix" 1 0 0 0 0 1 0 0 0 0 1 0 0 127.17007994917951 -0.15791876966751917 1;
	setAttr ".radi" 2;
createNode joint -n "spine2ScaProxySkin_jnt" -p "spine2ProxySkin_jnt";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".bps" -type "matrix" 1 0 0 0 0 1 0 0 0 0 1 0 0 116.88122829025195 -0.15791876966751928 1;
	setAttr ".radi" 2;
createNode joint -n "spine1ScaProxySkin_jnt" -p "spine1ProxySkin_jnt";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".bps" -type "matrix" 1 0 0 0 0 1 0 0 0 0 1 0 0 109.57663332111446 -2.1508764065674457 1;
	setAttr ".radi" 2;
createNode lightLinker -s -n "lightLinker1";
	setAttr -s 18 ".lnk";
	setAttr -s 18 ".slnk";
createNode displayLayerManager -n "layerManager";
createNode displayLayer -n "defaultLayer";
createNode renderLayerManager -n "renderLayerManager";
createNode renderLayer -n "defaultRenderLayer";
	setAttr ".g" yes;
createNode shadingEngine -n "clothMat_sg1";
	setAttr ".ihi" 0;
	setAttr ".ro" yes;
createNode materialInfo -n "materialInfo17";
createNode shadingEngine -n "skinMat_sg1";
	setAttr ".ihi" 0;
	setAttr ".ro" yes;
createNode materialInfo -n "pasted__pasted__pasted__materialInfo8";
createNode shadingEngine -n "whiteObjectMat_sg1";
	setAttr ".ihi" 0;
	setAttr ".ro" yes;
createNode materialInfo -n "materialInfo18";
createNode shadingEngine -n "pupilMat_sg1";
	setAttr ".ihi" 0;
	setAttr ".ro" yes;
createNode materialInfo -n "materialInfo19";
createNode shadingEngine -n "inmouthMat_sg1";
	setAttr ".ihi" 0;
	setAttr ".ro" yes;
createNode materialInfo -n "materialInfo20";
createNode shadingEngine -n "lambert2SG1";
	setAttr ".ihi" 0;
	setAttr ".ro" yes;
createNode materialInfo -n "materialInfo21";
createNode shadingEngine -n "lambert3SG1";
	setAttr ".ihi" 0;
	setAttr ".ro" yes;
createNode materialInfo -n "materialInfo22";
createNode shadingEngine -n "pant_bSG1";
	setAttr ".ihi" 0;
	setAttr ".ro" yes;
createNode materialInfo -n "materialInfo23";
createNode shadingEngine -n "clothMat_sg";
	setAttr ".ihi" 0;
	setAttr ".ro" yes;
createNode materialInfo -n "materialInfo5";
createNode shadingEngine -n "skinMat_sg";
	setAttr ".ihi" 0;
	setAttr ".ro" yes;
createNode materialInfo -n "pasted__pasted__pasted__materialInfo7";
createNode shadingEngine -n "whiteObjectMat_sg";
	setAttr ".ihi" 0;
	setAttr ".ro" yes;
createNode materialInfo -n "materialInfo8";
createNode shadingEngine -n "pupilMat_sg";
	setAttr ".ihi" 0;
	setAttr ".ro" yes;
createNode materialInfo -n "materialInfo9";
createNode shadingEngine -n "inmouthMat_sg";
	setAttr ".ihi" 0;
	setAttr ".ro" yes;
createNode materialInfo -n "materialInfo10";
createNode shadingEngine -n "lambert2SG";
	setAttr ".ihi" 0;
	setAttr ".ro" yes;
createNode materialInfo -n "materialInfo11";
createNode shadingEngine -n "lambert3SG";
	setAttr ".ihi" 0;
	setAttr ".ro" yes;
createNode materialInfo -n "materialInfo12";
createNode shadingEngine -n "pant_bSG";
	setAttr ".ihi" 0;
	setAttr ".ro" yes;
createNode materialInfo -n "materialInfo16";
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
		+ "\tif (\"\" == $panelName) {\n\t\tif ($useSceneConfig) {\n\t\t\t$panelName = `modelPanel -unParent -l (localizedPanelLabel(\"Persp View\")) -mbv $menusOkayInPanels `;\n\t\t\t$editorName = $panelName;\n            modelEditor -e \n                -camera \"persp\" \n                -useInteractiveMode 0\n                -displayLights \"default\" \n                -displayAppearance \"smoothShaded\" \n                -activeOnly 0\n                -ignorePanZoom 0\n                -wireframeOnShaded 0\n                -headsUpDisplay 1\n                -selectionHiliteDisplay 1\n                -useDefaultMaterial 0\n                -bufferMode \"double\" \n                -twoSidedLighting 1\n                -backfaceCulling 0\n                -xray 0\n                -jointXray 0\n                -activeComponentsXray 0\n                -displayTextures 0\n                -smoothWireframe 0\n                -lineWidth 1\n                -textureAnisotropic 0\n                -textureHilight 1\n                -textureSampling 2\n                -textureDisplay \"modulate\" \n"
		+ "                -textureMaxSize 16384\n                -fogging 0\n                -fogSource \"fragment\" \n                -fogMode \"linear\" \n                -fogStart 0\n                -fogEnd 100\n                -fogDensity 0.1\n                -fogColor 0.5 0.5 0.5 1 \n                -maxConstantTransparency 1\n                -rendererName \"base_OpenGL_Renderer\" \n                -objectFilterShowInHUD 1\n                -isFiltered 0\n                -colorResolution 256 256 \n                -bumpResolution 512 512 \n                -textureCompression 0\n                -transparencyAlgorithm \"frontAndBackCull\" \n                -transpInShadows 0\n                -cullingOverride \"none\" \n                -lowQualityLighting 0\n                -maximumNumHardwareLights 1\n                -occlusionCulling 0\n                -shadingModel 0\n                -useBaseRenderer 0\n                -useReducedRenderer 0\n                -smallObjectCulling 0\n                -smallObjectThreshold -1 \n                -interactiveDisableShadows 0\n"
		+ "                -interactiveBackFaceCull 0\n                -sortTransparent 1\n                -nurbsCurves 1\n                -nurbsSurfaces 1\n                -polymeshes 1\n                -subdivSurfaces 1\n                -planes 1\n                -lights 1\n                -cameras 1\n                -controlVertices 1\n                -hulls 1\n                -grid 1\n                -joints 1\n                -ikHandles 1\n                -deformers 1\n                -dynamics 1\n                -fluids 1\n                -hairSystems 1\n                -follicles 1\n                -nCloths 1\n                -nParticles 1\n                -nRigids 1\n                -dynamicConstraints 1\n                -locators 1\n                -manipulators 1\n                -dimensions 1\n                -handles 1\n                -pivots 1\n                -textures 1\n                -strokes 1\n                -motionTrails 1\n                -shadows 0\n                $editorName;\nmodelEditor -e -viewSelected 0 $editorName;\n\t\t}\n\t} else {\n"
		+ "\t\t$label = `panel -q -label $panelName`;\n\t\tmodelPanel -edit -l (localizedPanelLabel(\"Persp View\")) -mbv $menusOkayInPanels  $panelName;\n\t\t$editorName = $panelName;\n        modelEditor -e \n            -camera \"persp\" \n            -useInteractiveMode 0\n            -displayLights \"default\" \n            -displayAppearance \"smoothShaded\" \n            -activeOnly 0\n            -ignorePanZoom 0\n            -wireframeOnShaded 0\n            -headsUpDisplay 1\n            -selectionHiliteDisplay 1\n            -useDefaultMaterial 0\n            -bufferMode \"double\" \n            -twoSidedLighting 1\n            -backfaceCulling 0\n            -xray 0\n            -jointXray 0\n            -activeComponentsXray 0\n            -displayTextures 0\n            -smoothWireframe 0\n            -lineWidth 1\n            -textureAnisotropic 0\n            -textureHilight 1\n            -textureSampling 2\n            -textureDisplay \"modulate\" \n            -textureMaxSize 16384\n            -fogging 0\n            -fogSource \"fragment\" \n            -fogMode \"linear\" \n"
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
		+ "\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"hyperGraphPanel\" (localizedPanelLabel(\"Hypergraph Hierarchy\")) `;\n\tif (\"\" == $panelName) {\n\t\tif ($useSceneConfig) {\n\t\t\t$panelName = `scriptedPanel -unParent  -type \"hyperGraphPanel\" -l (localizedPanelLabel(\"Hypergraph Hierarchy\")) -mbv $menusOkayInPanels `;\n\n\t\t\t$editorName = ($panelName+\"HyperGraphEd\");\n            hyperGraph -e \n                -graphLayoutStyle \"hierarchicalLayout\" \n                -orientation \"horiz\" \n                -mergeConnections 0\n                -zoom 0.859645\n                -animateTransition 0\n                -showRelationships 1\n                -showShapes 0\n                -showDeformers 0\n                -showExpressions 0\n                -showConstraints 0\n                -showUnderworld 0\n                -showInvisible 1\n                -transitionFrames 5\n                -currentNode \"proxySkin_grp\" \n                -opaqueContainers 0\n                -freeform 0\n                -imagePosition 0 0 \n"
		+ "                -imageScale 1\n                -imageEnabled 0\n                -graphType \"DAG\" \n                -heatMapDisplay 0\n                -updateSelection 1\n                -updateNodeAdded 1\n                -useDrawOverrideColor 0\n                -limitGraphTraversal -1\n                -range 0 0 \n                -iconSize \"largeIcons\" \n                -showCachedConnections 0\n                $editorName;\n\t\t}\n\t} else {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Hypergraph Hierarchy\")) -mbv $menusOkayInPanels  $panelName;\n\n\t\t\t$editorName = ($panelName+\"HyperGraphEd\");\n            hyperGraph -e \n                -graphLayoutStyle \"hierarchicalLayout\" \n                -orientation \"horiz\" \n                -mergeConnections 0\n                -zoom 0.859645\n                -animateTransition 0\n                -showRelationships 1\n                -showShapes 0\n                -showDeformers 0\n                -showExpressions 0\n                -showConstraints 0\n                -showUnderworld 0\n"
		+ "                -showInvisible 1\n                -transitionFrames 5\n                -currentNode \"proxySkin_grp\" \n                -opaqueContainers 0\n                -freeform 0\n                -imagePosition 0 0 \n                -imageScale 1\n                -imageEnabled 0\n                -graphType \"DAG\" \n                -heatMapDisplay 0\n                -updateSelection 1\n                -updateNodeAdded 1\n                -useDrawOverrideColor 0\n                -limitGraphTraversal -1\n                -range 0 0 \n                -iconSize \"largeIcons\" \n                -showCachedConnections 0\n                $editorName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"hyperShadePanel\" (localizedPanelLabel(\"Hypershade\")) `;\n\tif (\"\" == $panelName) {\n\t\tif ($useSceneConfig) {\n\t\t\t$panelName = `scriptedPanel -unParent  -type \"hyperShadePanel\" -l (localizedPanelLabel(\"Hypershade\")) -mbv $menusOkayInPanels `;\n\t\t}\n\t} else {\n\t\t$label = `panel -q -label $panelName`;\n"
		+ "\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Hypershade\")) -mbv $menusOkayInPanels  $panelName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"visorPanel\" (localizedPanelLabel(\"Visor\")) `;\n\tif (\"\" == $panelName) {\n\t\tif ($useSceneConfig) {\n\t\t\t$panelName = `scriptedPanel -unParent  -type \"visorPanel\" -l (localizedPanelLabel(\"Visor\")) -mbv $menusOkayInPanels `;\n\t\t}\n\t} else {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Visor\")) -mbv $menusOkayInPanels  $panelName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"createNodePanel\" (localizedPanelLabel(\"Create Node\")) `;\n\tif (\"\" == $panelName) {\n\t\tif ($useSceneConfig) {\n\t\t\t$panelName = `scriptedPanel -unParent  -type \"createNodePanel\" -l (localizedPanelLabel(\"Create Node\")) -mbv $menusOkayInPanels `;\n\t\t}\n\t} else {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Create Node\")) -mbv $menusOkayInPanels  $panelName;\n"
		+ "\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"polyTexturePlacementPanel\" (localizedPanelLabel(\"UV Texture Editor\")) `;\n\tif (\"\" == $panelName) {\n\t\tif ($useSceneConfig) {\n\t\t\t$panelName = `scriptedPanel -unParent  -type \"polyTexturePlacementPanel\" -l (localizedPanelLabel(\"UV Texture Editor\")) -mbv $menusOkayInPanels `;\n\t\t}\n\t} else {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"UV Texture Editor\")) -mbv $menusOkayInPanels  $panelName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"renderWindowPanel\" (localizedPanelLabel(\"Render View\")) `;\n\tif (\"\" == $panelName) {\n\t\tif ($useSceneConfig) {\n\t\t\t$panelName = `scriptedPanel -unParent  -type \"renderWindowPanel\" -l (localizedPanelLabel(\"Render View\")) -mbv $menusOkayInPanels `;\n\t\t}\n\t} else {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Render View\")) -mbv $menusOkayInPanels  $panelName;\n"
		+ "\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextPanel \"blendShapePanel\" (localizedPanelLabel(\"Blend Shape\")) `;\n\tif (\"\" == $panelName) {\n\t\tif ($useSceneConfig) {\n\t\t\tblendShapePanel -unParent -l (localizedPanelLabel(\"Blend Shape\")) -mbv $menusOkayInPanels ;\n\t\t}\n\t} else {\n\t\t$label = `panel -q -label $panelName`;\n\t\tblendShapePanel -edit -l (localizedPanelLabel(\"Blend Shape\")) -mbv $menusOkayInPanels  $panelName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"dynRelEdPanel\" (localizedPanelLabel(\"Dynamic Relationships\")) `;\n\tif (\"\" == $panelName) {\n\t\tif ($useSceneConfig) {\n\t\t\t$panelName = `scriptedPanel -unParent  -type \"dynRelEdPanel\" -l (localizedPanelLabel(\"Dynamic Relationships\")) -mbv $menusOkayInPanels `;\n\t\t}\n\t} else {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Dynamic Relationships\")) -mbv $menusOkayInPanels  $panelName;\n\t\tif (!$useSceneConfig) {\n"
		+ "\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"relationshipPanel\" (localizedPanelLabel(\"Relationship Editor\")) `;\n\tif (\"\" == $panelName) {\n\t\tif ($useSceneConfig) {\n\t\t\t$panelName = `scriptedPanel -unParent  -type \"relationshipPanel\" -l (localizedPanelLabel(\"Relationship Editor\")) -mbv $menusOkayInPanels `;\n\t\t}\n\t} else {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Relationship Editor\")) -mbv $menusOkayInPanels  $panelName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"referenceEditorPanel\" (localizedPanelLabel(\"Reference Editor\")) `;\n\tif (\"\" == $panelName) {\n\t\tif ($useSceneConfig) {\n\t\t\t$panelName = `scriptedPanel -unParent  -type \"referenceEditorPanel\" -l (localizedPanelLabel(\"Reference Editor\")) -mbv $menusOkayInPanels `;\n\t\t}\n\t} else {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Reference Editor\")) -mbv $menusOkayInPanels  $panelName;\n"
		+ "\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"componentEditorPanel\" (localizedPanelLabel(\"Component Editor\")) `;\n\tif (\"\" == $panelName) {\n\t\tif ($useSceneConfig) {\n\t\t\t$panelName = `scriptedPanel -unParent  -type \"componentEditorPanel\" -l (localizedPanelLabel(\"Component Editor\")) -mbv $menusOkayInPanels `;\n\t\t}\n\t} else {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Component Editor\")) -mbv $menusOkayInPanels  $panelName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"dynPaintScriptedPanelType\" (localizedPanelLabel(\"Paint Effects\")) `;\n\tif (\"\" == $panelName) {\n\t\tif ($useSceneConfig) {\n\t\t\t$panelName = `scriptedPanel -unParent  -type \"dynPaintScriptedPanelType\" -l (localizedPanelLabel(\"Paint Effects\")) -mbv $menusOkayInPanels `;\n\t\t}\n\t} else {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Paint Effects\")) -mbv $menusOkayInPanels  $panelName;\n"
		+ "\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"scriptEditorPanel\" (localizedPanelLabel(\"Script Editor\")) `;\n\tif (\"\" == $panelName) {\n\t\tif ($useSceneConfig) {\n\t\t\t$panelName = `scriptedPanel -unParent  -type \"scriptEditorPanel\" -l (localizedPanelLabel(\"Script Editor\")) -mbv $menusOkayInPanels `;\n\t\t}\n\t} else {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Script Editor\")) -mbv $menusOkayInPanels  $panelName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\tif ($useSceneConfig) {\n        string $configName = `getPanel -cwl (localizedPanelLabel(\"Current Layout\"))`;\n        if (\"\" != $configName) {\n\t\t\tpanelConfiguration -edit -label (localizedPanelLabel(\"Current Layout\")) \n\t\t\t\t-defaultImage \"\"\n\t\t\t\t-image \"\"\n\t\t\t\t-sc false\n\t\t\t\t-configString \"global string $gMainPane; paneLayout -e -cn \\\"vertical2\\\" -ps 1 53 100 -ps 2 47 100 $gMainPane;\"\n\t\t\t\t-removeAllPanels\n\t\t\t\t-ap false\n\t\t\t\t\t(localizedPanelLabel(\"Hypergraph Hierarchy\")) \n"
		+ "\t\t\t\t\t\"scriptedPanel\"\n\t\t\t\t\t\"$panelName = `scriptedPanel -unParent  -type \\\"hyperGraphPanel\\\" -l (localizedPanelLabel(\\\"Hypergraph Hierarchy\\\")) -mbv $menusOkayInPanels `;\\n\\n\\t\\t\\t$editorName = ($panelName+\\\"HyperGraphEd\\\");\\n            hyperGraph -e \\n                -graphLayoutStyle \\\"hierarchicalLayout\\\" \\n                -orientation \\\"horiz\\\" \\n                -mergeConnections 0\\n                -zoom 0.859645\\n                -animateTransition 0\\n                -showRelationships 1\\n                -showShapes 0\\n                -showDeformers 0\\n                -showExpressions 0\\n                -showConstraints 0\\n                -showUnderworld 0\\n                -showInvisible 1\\n                -transitionFrames 5\\n                -currentNode \\\"proxySkin_grp\\\" \\n                -opaqueContainers 0\\n                -freeform 0\\n                -imagePosition 0 0 \\n                -imageScale 1\\n                -imageEnabled 0\\n                -graphType \\\"DAG\\\" \\n                -heatMapDisplay 0\\n                -updateSelection 1\\n                -updateNodeAdded 1\\n                -useDrawOverrideColor 0\\n                -limitGraphTraversal -1\\n                -range 0 0 \\n                -iconSize \\\"largeIcons\\\" \\n                -showCachedConnections 0\\n                $editorName\"\n"
		+ "\t\t\t\t\t\"scriptedPanel -edit -l (localizedPanelLabel(\\\"Hypergraph Hierarchy\\\")) -mbv $menusOkayInPanels  $panelName;\\n\\n\\t\\t\\t$editorName = ($panelName+\\\"HyperGraphEd\\\");\\n            hyperGraph -e \\n                -graphLayoutStyle \\\"hierarchicalLayout\\\" \\n                -orientation \\\"horiz\\\" \\n                -mergeConnections 0\\n                -zoom 0.859645\\n                -animateTransition 0\\n                -showRelationships 1\\n                -showShapes 0\\n                -showDeformers 0\\n                -showExpressions 0\\n                -showConstraints 0\\n                -showUnderworld 0\\n                -showInvisible 1\\n                -transitionFrames 5\\n                -currentNode \\\"proxySkin_grp\\\" \\n                -opaqueContainers 0\\n                -freeform 0\\n                -imagePosition 0 0 \\n                -imageScale 1\\n                -imageEnabled 0\\n                -graphType \\\"DAG\\\" \\n                -heatMapDisplay 0\\n                -updateSelection 1\\n                -updateNodeAdded 1\\n                -useDrawOverrideColor 0\\n                -limitGraphTraversal -1\\n                -range 0 0 \\n                -iconSize \\\"largeIcons\\\" \\n                -showCachedConnections 0\\n                $editorName\"\n"
		+ "\t\t\t\t-ap false\n\t\t\t\t\t(localizedPanelLabel(\"Persp View\")) \n\t\t\t\t\t\"modelPanel\"\n"
		+ "\t\t\t\t\t\"$panelName = `modelPanel -unParent -l (localizedPanelLabel(\\\"Persp View\\\")) -mbv $menusOkayInPanels `;\\n$editorName = $panelName;\\nmodelEditor -e \\n    -cam `findStartUpCamera persp` \\n    -useInteractiveMode 0\\n    -displayLights \\\"default\\\" \\n    -displayAppearance \\\"smoothShaded\\\" \\n    -activeOnly 0\\n    -ignorePanZoom 0\\n    -wireframeOnShaded 0\\n    -headsUpDisplay 1\\n    -selectionHiliteDisplay 1\\n    -useDefaultMaterial 0\\n    -bufferMode \\\"double\\\" \\n    -twoSidedLighting 1\\n    -backfaceCulling 0\\n    -xray 0\\n    -jointXray 0\\n    -activeComponentsXray 0\\n    -displayTextures 0\\n    -smoothWireframe 0\\n    -lineWidth 1\\n    -textureAnisotropic 0\\n    -textureHilight 1\\n    -textureSampling 2\\n    -textureDisplay \\\"modulate\\\" \\n    -textureMaxSize 16384\\n    -fogging 0\\n    -fogSource \\\"fragment\\\" \\n    -fogMode \\\"linear\\\" \\n    -fogStart 0\\n    -fogEnd 100\\n    -fogDensity 0.1\\n    -fogColor 0.5 0.5 0.5 1 \\n    -maxConstantTransparency 1\\n    -rendererName \\\"base_OpenGL_Renderer\\\" \\n    -objectFilterShowInHUD 1\\n    -isFiltered 0\\n    -colorResolution 256 256 \\n    -bumpResolution 512 512 \\n    -textureCompression 0\\n    -transparencyAlgorithm \\\"frontAndBackCull\\\" \\n    -transpInShadows 0\\n    -cullingOverride \\\"none\\\" \\n    -lowQualityLighting 0\\n    -maximumNumHardwareLights 1\\n    -occlusionCulling 0\\n    -shadingModel 0\\n    -useBaseRenderer 0\\n    -useReducedRenderer 0\\n    -smallObjectCulling 0\\n    -smallObjectThreshold -1 \\n    -interactiveDisableShadows 0\\n    -interactiveBackFaceCull 0\\n    -sortTransparent 1\\n    -nurbsCurves 1\\n    -nurbsSurfaces 1\\n    -polymeshes 1\\n    -subdivSurfaces 1\\n    -planes 1\\n    -lights 1\\n    -cameras 1\\n    -controlVertices 1\\n    -hulls 1\\n    -grid 1\\n    -joints 1\\n    -ikHandles 1\\n    -deformers 1\\n    -dynamics 1\\n    -fluids 1\\n    -hairSystems 1\\n    -follicles 1\\n    -nCloths 1\\n    -nParticles 1\\n    -nRigids 1\\n    -dynamicConstraints 1\\n    -locators 1\\n    -manipulators 1\\n    -dimensions 1\\n    -handles 1\\n    -pivots 1\\n    -textures 1\\n    -strokes 1\\n    -motionTrails 1\\n    -shadows 0\\n    $editorName;\\nmodelEditor -e -viewSelected 0 $editorName\"\n"
		+ "\t\t\t\t\t\"modelPanel -edit -l (localizedPanelLabel(\\\"Persp View\\\")) -mbv $menusOkayInPanels  $panelName;\\n$editorName = $panelName;\\nmodelEditor -e \\n    -cam `findStartUpCamera persp` \\n    -useInteractiveMode 0\\n    -displayLights \\\"default\\\" \\n    -displayAppearance \\\"smoothShaded\\\" \\n    -activeOnly 0\\n    -ignorePanZoom 0\\n    -wireframeOnShaded 0\\n    -headsUpDisplay 1\\n    -selectionHiliteDisplay 1\\n    -useDefaultMaterial 0\\n    -bufferMode \\\"double\\\" \\n    -twoSidedLighting 1\\n    -backfaceCulling 0\\n    -xray 0\\n    -jointXray 0\\n    -activeComponentsXray 0\\n    -displayTextures 0\\n    -smoothWireframe 0\\n    -lineWidth 1\\n    -textureAnisotropic 0\\n    -textureHilight 1\\n    -textureSampling 2\\n    -textureDisplay \\\"modulate\\\" \\n    -textureMaxSize 16384\\n    -fogging 0\\n    -fogSource \\\"fragment\\\" \\n    -fogMode \\\"linear\\\" \\n    -fogStart 0\\n    -fogEnd 100\\n    -fogDensity 0.1\\n    -fogColor 0.5 0.5 0.5 1 \\n    -maxConstantTransparency 1\\n    -rendererName \\\"base_OpenGL_Renderer\\\" \\n    -objectFilterShowInHUD 1\\n    -isFiltered 0\\n    -colorResolution 256 256 \\n    -bumpResolution 512 512 \\n    -textureCompression 0\\n    -transparencyAlgorithm \\\"frontAndBackCull\\\" \\n    -transpInShadows 0\\n    -cullingOverride \\\"none\\\" \\n    -lowQualityLighting 0\\n    -maximumNumHardwareLights 1\\n    -occlusionCulling 0\\n    -shadingModel 0\\n    -useBaseRenderer 0\\n    -useReducedRenderer 0\\n    -smallObjectCulling 0\\n    -smallObjectThreshold -1 \\n    -interactiveDisableShadows 0\\n    -interactiveBackFaceCull 0\\n    -sortTransparent 1\\n    -nurbsCurves 1\\n    -nurbsSurfaces 1\\n    -polymeshes 1\\n    -subdivSurfaces 1\\n    -planes 1\\n    -lights 1\\n    -cameras 1\\n    -controlVertices 1\\n    -hulls 1\\n    -grid 1\\n    -joints 1\\n    -ikHandles 1\\n    -deformers 1\\n    -dynamics 1\\n    -fluids 1\\n    -hairSystems 1\\n    -follicles 1\\n    -nCloths 1\\n    -nParticles 1\\n    -nRigids 1\\n    -dynamicConstraints 1\\n    -locators 1\\n    -manipulators 1\\n    -dimensions 1\\n    -handles 1\\n    -pivots 1\\n    -textures 1\\n    -strokes 1\\n    -motionTrails 1\\n    -shadows 0\\n    $editorName;\\nmodelEditor -e -viewSelected 0 $editorName\"\n"
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
	setAttr -s 18 ".st";
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
connectAttr "rootProxySkin_jnt.s" "pelvisProxySkin_jnt.is";
connectAttr "pelvisProxySkin_jnt.s" "pelvisScaProxySkin_jnt.is";
connectAttr "pelvisProxySkin_jnt.s" "upLegProxySkinLFT_jnt.is";
connectAttr "upLegProxySkinLFT_jnt.s" "lowLegProxySkinLFT_jnt.is";
connectAttr "lowLegProxySkinLFT_jnt.s" "ankleProxySkinLFT_jnt.is";
connectAttr "ankleProxySkinLFT_jnt.s" "ballProxySkinLFT_jnt.is";
connectAttr "ballProxySkinLFT_jnt.s" "toeProxySkinLFT_jnt.is";
connectAttr "lowLegProxySkinLFT_jnt.s" "lowLegRbnDtl1ProxySkinLFT_jnt.is";
connectAttr "lowLegProxySkinLFT_jnt.s" "lowLegRbnDtl2ProxySkinLFT_jnt.is";
connectAttr "lowLegProxySkinLFT_jnt.s" "lowLegRbnDtl3ProxySkinLFT_jnt.is";
connectAttr "lowLegProxySkinLFT_jnt.s" "lowLegRbnDtl4ProxySkinLFT_jnt.is";
connectAttr "lowLegProxySkinLFT_jnt.s" "lowLegRbnDtl5ProxySkinLFT_jnt.is";
connectAttr "upLegProxySkinLFT_jnt.s" "upLegRbnDtl1ProxySkinLFT_jnt.is";
connectAttr "upLegProxySkinLFT_jnt.s" "upLegRbnDtl2ProxySkinLFT_jnt.is";
connectAttr "upLegProxySkinLFT_jnt.s" "upLegRbnDtl3ProxySkinLFT_jnt.is";
connectAttr "upLegProxySkinLFT_jnt.s" "upLegRbnDtl4ProxySkinLFT_jnt.is";
connectAttr "upLegProxySkinLFT_jnt.s" "upLegRbnDtl5ProxySkinLFT_jnt.is";
connectAttr "pelvisProxySkin_jnt.s" "upLegProxySkinRGT_jnt.is";
connectAttr "upLegProxySkinRGT_jnt.s" "lowLegProxySkinRGT_jnt.is";
connectAttr "lowLegProxySkinRGT_jnt.s" "ankleProxySkinRGT_jnt.is";
connectAttr "ankleProxySkinRGT_jnt.s" "ballProxySkinRGT_jnt.is";
connectAttr "ballProxySkinRGT_jnt.s" "toeProxySkinRGT_jnt.is";
connectAttr "lowLegProxySkinRGT_jnt.s" "lowLegRbnDtl1ProxySkinRGT_jnt.is";
connectAttr "lowLegProxySkinRGT_jnt.s" "lowLegRbnDtl2ProxySkinRGT_jnt.is";
connectAttr "lowLegProxySkinRGT_jnt.s" "lowLegRbnDtl3ProxySkinRGT_jnt.is";
connectAttr "lowLegProxySkinRGT_jnt.s" "lowLegRbnDtl4ProxySkinRGT_jnt.is";
connectAttr "lowLegProxySkinRGT_jnt.s" "lowLegRbnDtl5ProxySkinRGT_jnt.is";
connectAttr "upLegProxySkinRGT_jnt.s" "upLegRbnDtl1ProxySkinRGT_jnt.is";
connectAttr "upLegProxySkinRGT_jnt.s" "upLegRbnDtl2ProxySkinRGT_jnt.is";
connectAttr "upLegProxySkinRGT_jnt.s" "upLegRbnDtl3ProxySkinRGT_jnt.is";
connectAttr "upLegProxySkinRGT_jnt.s" "upLegRbnDtl4ProxySkinRGT_jnt.is";
connectAttr "upLegProxySkinRGT_jnt.s" "upLegRbnDtl5ProxySkinRGT_jnt.is";
connectAttr "rootProxySkin_jnt.s" "spine1ProxySkin_jnt.is";
connectAttr "spine1ProxySkin_jnt.s" "spine2ProxySkin_jnt.is";
connectAttr "spine2ProxySkin_jnt.s" "spine3ProxySkin_jnt.is";
connectAttr "spine3ProxySkin_jnt.s" "spine4ProxySkin_jnt.is";
connectAttr "spine4ProxySkin_jnt.s" "spine5ProxySkin_jnt.is";
connectAttr "spine5ProxySkin_jnt.s" "neck1ProxySkin_jnt.is";
connectAttr "neck1ProxySkin_jnt.s" "neck2ProxySkin_jnt.is";
connectAttr "neck2ProxySkin_jnt.s" "head1ProxySkin_jnt.is";
connectAttr "head1ProxySkin_jnt.s" "head2ProxySkin_jnt.is";
connectAttr "head1ProxySkin_jnt.s" "jaw1LWRProxySkin_jnt.is";
connectAttr "jaw1LWRProxySkin_jnt.s" "jaw2LWRProxySkin_jnt.is";
connectAttr "jaw2LWRProxySkin_jnt.s" "jaw3LWRProxySkin_jnt.is";
connectAttr "head1ProxySkin_jnt.s" "jaw1UPRProxySkin_jnt.is";
connectAttr "jaw1UPRProxySkin_jnt.s" "jaw2UPRProxySkin_jnt.is";
connectAttr "head1ProxySkin_jnt.s" "eyeProxySkinLFT_jnt.is";
connectAttr "head1ProxySkin_jnt.s" "eyeProxySkinRGT_jnt.is";
connectAttr "neck1ProxySkin_jnt.s" "neckRbnProxySkin_jnt.is";
connectAttr "spine4ProxySkin_jnt.s" "spine4ScaProxySkin_jnt.is";
connectAttr "spine4ProxySkin_jnt.s" "clav1ProxySkinLFT_jnt.is";
connectAttr "clav1ProxySkinLFT_jnt.s" "clav2ProxySkinLFT_jnt.is";
connectAttr "clav2ProxySkinLFT_jnt.s" "upArmProxySkinLFT_jnt.is";
connectAttr "upArmProxySkinLFT_jnt.s" "forearmProxySkinLFT_jnt.is";
connectAttr "forearmProxySkinLFT_jnt.s" "wristProxySkinLFT_jnt.is";
connectAttr "wristProxySkinLFT_jnt.s" "handProxySkinLFT_jnt.is";
connectAttr "handProxySkinLFT_jnt.s" "index1ProxySkinLFT_jnt.is";
connectAttr "index1ProxySkinLFT_jnt.s" "index2ProxySkinLFT_jnt.is";
connectAttr "index2ProxySkinLFT_jnt.s" "index3ProxySkinLFT_jnt.is";
connectAttr "index3ProxySkinLFT_jnt.s" "index4ProxySkinLFT_jnt.is";
connectAttr "index4ProxySkinLFT_jnt.s" "index5ProxySkinLFT_jnt.is";
connectAttr "handProxySkinLFT_jnt.s" "middle1ProxySkinLFT_jnt.is";
connectAttr "middle1ProxySkinLFT_jnt.s" "middle2ProxySkinLFT_jnt.is";
connectAttr "middle2ProxySkinLFT_jnt.s" "middle3ProxySkinLFT_jnt.is";
connectAttr "middle3ProxySkinLFT_jnt.s" "middle4ProxySkinLFT_jnt.is";
connectAttr "middle4ProxySkinLFT_jnt.s" "middle5ProxySkinLFT_jnt.is";
connectAttr "handProxySkinLFT_jnt.s" "ring1ProxySkinLFT_jnt.is";
connectAttr "ring1ProxySkinLFT_jnt.s" "ring2ProxySkinLFT_jnt.is";
connectAttr "ring2ProxySkinLFT_jnt.s" "ring3ProxySkinLFT_jnt.is";
connectAttr "ring3ProxySkinLFT_jnt.s" "ring4ProxySkinLFT_jnt.is";
connectAttr "ring4ProxySkinLFT_jnt.s" "ring5ProxySkinLFT_jnt.is";
connectAttr "handProxySkinLFT_jnt.s" "pinky1ProxySkinLFT_jnt.is";
connectAttr "pinky1ProxySkinLFT_jnt.s" "pinky2ProxySkinLFT_jnt.is";
connectAttr "pinky2ProxySkinLFT_jnt.s" "pinky3ProxySkinLFT_jnt.is";
connectAttr "pinky3ProxySkinLFT_jnt.s" "pinky4ProxySkinLFT_jnt.is";
connectAttr "pinky4ProxySkinLFT_jnt.s" "pinky5ProxySkinLFT_jnt.is";
connectAttr "thumb1ProxySkinLFT_jnt.s" "thumb2ProxySkinLFT_jnt.is";
connectAttr "thumb2ProxySkinLFT_jnt.s" "thumb3ProxySkinLFT_jnt.is";
connectAttr "thumb3ProxySkinLFT_jnt.s" "thumb4ProxySkinLFT_jnt.is";
connectAttr "forearmProxySkinLFT_jnt.s" "forearmRbnDtl1ProxySkinLFT_jnt.is";
connectAttr "forearmProxySkinLFT_jnt.s" "forearmRbnDtl2ProxySkinLFT_jnt.is";
connectAttr "forearmProxySkinLFT_jnt.s" "forearmRbnDtl3ProxySkinLFT_jnt.is";
connectAttr "forearmProxySkinLFT_jnt.s" "forearmRbnDtl4ProxySkinLFT_jnt.is";
connectAttr "forearmProxySkinLFT_jnt.s" "forearmRbnDtl5ProxySkinLFT_jnt.is";
connectAttr "upArmProxySkinLFT_jnt.s" "upArmRbnDtl1ProxySkinLFT_jnt.is";
connectAttr "upArmProxySkinLFT_jnt.s" "upArmRbnDtl2ProxySkinLFT_jnt.is";
connectAttr "upArmProxySkinLFT_jnt.s" "upArmRbnDtl3ProxySkinLFT_jnt.is";
connectAttr "upArmProxySkinLFT_jnt.s" "upArmRbnDtl4ProxySkinLFT_jnt.is";
connectAttr "upArmProxySkinLFT_jnt.s" "upArmRbnDtl5ProxySkinLFT_jnt.is";
connectAttr "clav1ProxySkinLFT_jnt.s" "clav1ScaProxySkinLFT_jnt.is";
connectAttr "spine4ProxySkin_jnt.s" "clav1ProxySkinRGT_jnt.is";
connectAttr "clav1ProxySkinRGT_jnt.s" "clav2ProxySkinRGT_jnt.is";
connectAttr "clav2ProxySkinRGT_jnt.s" "upArmProxySkinRGT_jnt.is";
connectAttr "upArmProxySkinRGT_jnt.s" "forearmProxySkinRGT_jnt.is";
connectAttr "forearmProxySkinRGT_jnt.s" "wristProxySkinRGT_jnt.is";
connectAttr "wristProxySkinRGT_jnt.s" "handProxySkinRGT_jnt.is";
connectAttr "handProxySkinRGT_jnt.s" "index1ProxySkinRGT_jnt.is";
connectAttr "index1ProxySkinRGT_jnt.s" "index2ProxySkinRGT_jnt.is";
connectAttr "index2ProxySkinRGT_jnt.s" "index3ProxySkinRGT_jnt.is";
connectAttr "index3ProxySkinRGT_jnt.s" "index4ProxySkinRGT_jnt.is";
connectAttr "index4ProxySkinRGT_jnt.s" "index5ProxySkinRGT_jnt.is";
connectAttr "handProxySkinRGT_jnt.s" "middle1ProxySkinRGT_jnt.is";
connectAttr "middle1ProxySkinRGT_jnt.s" "middle2ProxySkinRGT_jnt.is";
connectAttr "middle2ProxySkinRGT_jnt.s" "middle3ProxySkinRGT_jnt.is";
connectAttr "middle3ProxySkinRGT_jnt.s" "middle4ProxySkinRGT_jnt.is";
connectAttr "middle4ProxySkinRGT_jnt.s" "middle5ProxySkinRGT_jnt.is";
connectAttr "handProxySkinRGT_jnt.s" "ring1ProxySkinRGT_jnt.is";
connectAttr "ring1ProxySkinRGT_jnt.s" "ring2ProxySkinRGT_jnt.is";
connectAttr "ring2ProxySkinRGT_jnt.s" "ring3ProxySkinRGT_jnt.is";
connectAttr "ring3ProxySkinRGT_jnt.s" "ring4ProxySkinRGT_jnt.is";
connectAttr "ring4ProxySkinRGT_jnt.s" "ring5ProxySkinRGT_jnt.is";
connectAttr "handProxySkinRGT_jnt.s" "pinky1ProxySkinRGT_jnt.is";
connectAttr "pinky1ProxySkinRGT_jnt.s" "pinky2ProxySkinRGT_jnt.is";
connectAttr "pinky2ProxySkinRGT_jnt.s" "pinky3ProxySkinRGT_jnt.is";
connectAttr "pinky3ProxySkinRGT_jnt.s" "pinky4ProxySkinRGT_jnt.is";
connectAttr "pinky4ProxySkinRGT_jnt.s" "pinky5ProxySkinRGT_jnt.is";
connectAttr "thumb1ProxySkinRGT_jnt.s" "thumb2ProxySkinRGT_jnt.is";
connectAttr "thumb2ProxySkinRGT_jnt.s" "thumb3ProxySkinRGT_jnt.is";
connectAttr "thumb3ProxySkinRGT_jnt.s" "thumb4ProxySkinRGT_jnt.is";
connectAttr "forearmProxySkinRGT_jnt.s" "forearmRbnDtl1ProxySkinRGT_jnt.is";
connectAttr "forearmProxySkinRGT_jnt.s" "forearmRbnDtl2ProxySkinRGT_jnt.is";
connectAttr "forearmProxySkinRGT_jnt.s" "forearmRbnDtl3ProxySkinRGT_jnt.is";
connectAttr "forearmProxySkinRGT_jnt.s" "forearmRbnDtl4ProxySkinRGT_jnt.is";
connectAttr "forearmProxySkinRGT_jnt.s" "forearmRbnDtl5ProxySkinRGT_jnt.is";
connectAttr "upArmProxySkinRGT_jnt.s" "upArmRbnDtl1ProxySkinRGT_jnt.is";
connectAttr "upArmProxySkinRGT_jnt.s" "upArmRbnDtl2ProxySkinRGT_jnt.is";
connectAttr "upArmProxySkinRGT_jnt.s" "upArmRbnDtl3ProxySkinRGT_jnt.is";
connectAttr "upArmProxySkinRGT_jnt.s" "upArmRbnDtl4ProxySkinRGT_jnt.is";
connectAttr "upArmProxySkinRGT_jnt.s" "upArmRbnDtl5ProxySkinRGT_jnt.is";
connectAttr "clav1ProxySkinRGT_jnt.s" "clav1ScaProxySkinRGT_jnt.is";
connectAttr "spine3ProxySkin_jnt.s" "spine3ScaProxySkin_jnt.is";
connectAttr "spine2ProxySkin_jnt.s" "spine2ScaProxySkin_jnt.is";
connectAttr "spine1ProxySkin_jnt.s" "spine1ScaProxySkin_jnt.is";
relationship "link" ":lightLinker1" ":initialShadingGroup.message" ":defaultLightSet.message";
relationship "link" ":lightLinker1" ":initialParticleSE.message" ":defaultLightSet.message";
relationship "link" ":lightLinker1" "clothMat_sg1.message" ":defaultLightSet.message";
relationship "link" ":lightLinker1" "skinMat_sg1.message" ":defaultLightSet.message";
relationship "link" ":lightLinker1" "whiteObjectMat_sg1.message" ":defaultLightSet.message";
relationship "link" ":lightLinker1" "pupilMat_sg1.message" ":defaultLightSet.message";
relationship "link" ":lightLinker1" "inmouthMat_sg1.message" ":defaultLightSet.message";
relationship "link" ":lightLinker1" "lambert2SG1.message" ":defaultLightSet.message";
relationship "link" ":lightLinker1" "lambert3SG1.message" ":defaultLightSet.message";
relationship "link" ":lightLinker1" "pant_bSG1.message" ":defaultLightSet.message";
relationship "link" ":lightLinker1" "clothMat_sg.message" ":defaultLightSet.message";
relationship "link" ":lightLinker1" "skinMat_sg.message" ":defaultLightSet.message";
relationship "link" ":lightLinker1" "whiteObjectMat_sg.message" ":defaultLightSet.message";
relationship "link" ":lightLinker1" "pupilMat_sg.message" ":defaultLightSet.message";
relationship "link" ":lightLinker1" "inmouthMat_sg.message" ":defaultLightSet.message";
relationship "link" ":lightLinker1" "lambert2SG.message" ":defaultLightSet.message";
relationship "link" ":lightLinker1" "lambert3SG.message" ":defaultLightSet.message";
relationship "link" ":lightLinker1" "pant_bSG.message" ":defaultLightSet.message";
relationship "shadowLink" ":lightLinker1" ":initialShadingGroup.message" ":defaultLightSet.message";
relationship "shadowLink" ":lightLinker1" ":initialParticleSE.message" ":defaultLightSet.message";
relationship "shadowLink" ":lightLinker1" "clothMat_sg1.message" ":defaultLightSet.message";
relationship "shadowLink" ":lightLinker1" "skinMat_sg1.message" ":defaultLightSet.message";
relationship "shadowLink" ":lightLinker1" "whiteObjectMat_sg1.message" ":defaultLightSet.message";
relationship "shadowLink" ":lightLinker1" "pupilMat_sg1.message" ":defaultLightSet.message";
relationship "shadowLink" ":lightLinker1" "inmouthMat_sg1.message" ":defaultLightSet.message";
relationship "shadowLink" ":lightLinker1" "lambert2SG1.message" ":defaultLightSet.message";
relationship "shadowLink" ":lightLinker1" "lambert3SG1.message" ":defaultLightSet.message";
relationship "shadowLink" ":lightLinker1" "pant_bSG1.message" ":defaultLightSet.message";
relationship "shadowLink" ":lightLinker1" "clothMat_sg.message" ":defaultLightSet.message";
relationship "shadowLink" ":lightLinker1" "skinMat_sg.message" ":defaultLightSet.message";
relationship "shadowLink" ":lightLinker1" "whiteObjectMat_sg.message" ":defaultLightSet.message";
relationship "shadowLink" ":lightLinker1" "pupilMat_sg.message" ":defaultLightSet.message";
relationship "shadowLink" ":lightLinker1" "inmouthMat_sg.message" ":defaultLightSet.message";
relationship "shadowLink" ":lightLinker1" "lambert2SG.message" ":defaultLightSet.message";
relationship "shadowLink" ":lightLinker1" "lambert3SG.message" ":defaultLightSet.message";
relationship "shadowLink" ":lightLinker1" "pant_bSG.message" ":defaultLightSet.message";
connectAttr "layerManager.dli[0]" "defaultLayer.id";
connectAttr "renderLayerManager.rlmi[0]" "defaultRenderLayer.rlid";
connectAttr "clothMat_sg1.msg" "materialInfo17.sg";
connectAttr "skinMat_sg1.msg" "pasted__pasted__pasted__materialInfo8.sg";
connectAttr "whiteObjectMat_sg1.msg" "materialInfo18.sg";
connectAttr "pupilMat_sg1.msg" "materialInfo19.sg";
connectAttr "inmouthMat_sg1.msg" "materialInfo20.sg";
connectAttr "lambert2SG1.msg" "materialInfo21.sg";
connectAttr "lambert3SG1.msg" "materialInfo22.sg";
connectAttr "pant_bSG1.msg" "materialInfo23.sg";
connectAttr "clothMat_sg.msg" "materialInfo5.sg";
connectAttr "skinMat_sg.msg" "pasted__pasted__pasted__materialInfo7.sg";
connectAttr "whiteObjectMat_sg.msg" "materialInfo8.sg";
connectAttr "pupilMat_sg.msg" "materialInfo9.sg";
connectAttr "inmouthMat_sg.msg" "materialInfo10.sg";
connectAttr "lambert2SG.msg" "materialInfo11.sg";
connectAttr "lambert3SG.msg" "materialInfo12.sg";
connectAttr "pant_bSG.msg" "materialInfo16.sg";
connectAttr "clothMat_sg1.pa" ":renderPartition.st" -na;
connectAttr "skinMat_sg1.pa" ":renderPartition.st" -na;
connectAttr "whiteObjectMat_sg1.pa" ":renderPartition.st" -na;
connectAttr "pupilMat_sg1.pa" ":renderPartition.st" -na;
connectAttr "inmouthMat_sg1.pa" ":renderPartition.st" -na;
connectAttr "lambert2SG1.pa" ":renderPartition.st" -na;
connectAttr "lambert3SG1.pa" ":renderPartition.st" -na;
connectAttr "pant_bSG1.pa" ":renderPartition.st" -na;
connectAttr "clothMat_sg.pa" ":renderPartition.st" -na;
connectAttr "skinMat_sg.pa" ":renderPartition.st" -na;
connectAttr "whiteObjectMat_sg.pa" ":renderPartition.st" -na;
connectAttr "pupilMat_sg.pa" ":renderPartition.st" -na;
connectAttr "inmouthMat_sg.pa" ":renderPartition.st" -na;
connectAttr "lambert2SG.pa" ":renderPartition.st" -na;
connectAttr "lambert3SG.pa" ":renderPartition.st" -na;
connectAttr "pant_bSG.pa" ":renderPartition.st" -na;
connectAttr "defaultRenderLayer.msg" ":defaultRenderingList1.r" -na;
// End of proxySkinJoint_1.ma
