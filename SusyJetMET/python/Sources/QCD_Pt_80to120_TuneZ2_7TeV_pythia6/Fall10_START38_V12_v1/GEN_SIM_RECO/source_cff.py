
import FWCore.ParameterSet.Config as cms

source = cms.Source(
	"PoolSource",

	noEventSort = cms.untracked.bool(True),
	duplicateCheckMode = cms.untracked.string("noDuplicateCheck"),
	fileNames = cms.untracked.vstring()
)
source.fileNames.extend([
		'/store/cmst3/user/cbern/RA2SusyJetMET/QCD_Pt_80to120_TuneZ2_7TeV_pythia6/Fall10-START38_V12-v1/GEN-SIM-RECO/susypat_RA2_10_2_fkV.root',
		'/store/cmst3/user/cbern/RA2SusyJetMET/QCD_Pt_80to120_TuneZ2_7TeV_pythia6/Fall10-START38_V12-v1/GEN-SIM-RECO/susypat_RA2_11_2_teQ.root',
		'/store/cmst3/user/cbern/RA2SusyJetMET/QCD_Pt_80to120_TuneZ2_7TeV_pythia6/Fall10-START38_V12-v1/GEN-SIM-RECO/susypat_RA2_12_1_7Be.root',
		'/store/cmst3/user/cbern/RA2SusyJetMET/QCD_Pt_80to120_TuneZ2_7TeV_pythia6/Fall10-START38_V12-v1/GEN-SIM-RECO/susypat_RA2_13_2_FeE.root',
		'/store/cmst3/user/cbern/RA2SusyJetMET/QCD_Pt_80to120_TuneZ2_7TeV_pythia6/Fall10-START38_V12-v1/GEN-SIM-RECO/susypat_RA2_14_1_EVw.root',
		'/store/cmst3/user/cbern/RA2SusyJetMET/QCD_Pt_80to120_TuneZ2_7TeV_pythia6/Fall10-START38_V12-v1/GEN-SIM-RECO/susypat_RA2_15_1_h9c.root',
		'/store/cmst3/user/cbern/RA2SusyJetMET/QCD_Pt_80to120_TuneZ2_7TeV_pythia6/Fall10-START38_V12-v1/GEN-SIM-RECO/susypat_RA2_16_2_vDP.root',
		'/store/cmst3/user/cbern/RA2SusyJetMET/QCD_Pt_80to120_TuneZ2_7TeV_pythia6/Fall10-START38_V12-v1/GEN-SIM-RECO/susypat_RA2_17_2_lEV.root',
		'/store/cmst3/user/cbern/RA2SusyJetMET/QCD_Pt_80to120_TuneZ2_7TeV_pythia6/Fall10-START38_V12-v1/GEN-SIM-RECO/susypat_RA2_18_2_6fw.root',
		'/store/cmst3/user/cbern/RA2SusyJetMET/QCD_Pt_80to120_TuneZ2_7TeV_pythia6/Fall10-START38_V12-v1/GEN-SIM-RECO/susypat_RA2_19_1_N6S.root',
		'/store/cmst3/user/cbern/RA2SusyJetMET/QCD_Pt_80to120_TuneZ2_7TeV_pythia6/Fall10-START38_V12-v1/GEN-SIM-RECO/susypat_RA2_1_2_s3o.root',
		'/store/cmst3/user/cbern/RA2SusyJetMET/QCD_Pt_80to120_TuneZ2_7TeV_pythia6/Fall10-START38_V12-v1/GEN-SIM-RECO/susypat_RA2_20_2_2pd.root',
		'/store/cmst3/user/cbern/RA2SusyJetMET/QCD_Pt_80to120_TuneZ2_7TeV_pythia6/Fall10-START38_V12-v1/GEN-SIM-RECO/susypat_RA2_21_1_urb.root',
		'/store/cmst3/user/cbern/RA2SusyJetMET/QCD_Pt_80to120_TuneZ2_7TeV_pythia6/Fall10-START38_V12-v1/GEN-SIM-RECO/susypat_RA2_22_1_XaJ.root',
		'/store/cmst3/user/cbern/RA2SusyJetMET/QCD_Pt_80to120_TuneZ2_7TeV_pythia6/Fall10-START38_V12-v1/GEN-SIM-RECO/susypat_RA2_23_2_vVe.root',
		'/store/cmst3/user/cbern/RA2SusyJetMET/QCD_Pt_80to120_TuneZ2_7TeV_pythia6/Fall10-START38_V12-v1/GEN-SIM-RECO/susypat_RA2_24_1_mbB.root',
		'/store/cmst3/user/cbern/RA2SusyJetMET/QCD_Pt_80to120_TuneZ2_7TeV_pythia6/Fall10-START38_V12-v1/GEN-SIM-RECO/susypat_RA2_25_1_egt.root',
		'/store/cmst3/user/cbern/RA2SusyJetMET/QCD_Pt_80to120_TuneZ2_7TeV_pythia6/Fall10-START38_V12-v1/GEN-SIM-RECO/susypat_RA2_26_1_dpk.root',
		'/store/cmst3/user/cbern/RA2SusyJetMET/QCD_Pt_80to120_TuneZ2_7TeV_pythia6/Fall10-START38_V12-v1/GEN-SIM-RECO/susypat_RA2_27_2_WC8.root',
		'/store/cmst3/user/cbern/RA2SusyJetMET/QCD_Pt_80to120_TuneZ2_7TeV_pythia6/Fall10-START38_V12-v1/GEN-SIM-RECO/susypat_RA2_28_1_CfS.root',
		'/store/cmst3/user/cbern/RA2SusyJetMET/QCD_Pt_80to120_TuneZ2_7TeV_pythia6/Fall10-START38_V12-v1/GEN-SIM-RECO/susypat_RA2_29_1_P1o.root',
		'/store/cmst3/user/cbern/RA2SusyJetMET/QCD_Pt_80to120_TuneZ2_7TeV_pythia6/Fall10-START38_V12-v1/GEN-SIM-RECO/susypat_RA2_2_1_MSs.root',
		'/store/cmst3/user/cbern/RA2SusyJetMET/QCD_Pt_80to120_TuneZ2_7TeV_pythia6/Fall10-START38_V12-v1/GEN-SIM-RECO/susypat_RA2_30_2_SMG.root',
		'/store/cmst3/user/cbern/RA2SusyJetMET/QCD_Pt_80to120_TuneZ2_7TeV_pythia6/Fall10-START38_V12-v1/GEN-SIM-RECO/susypat_RA2_31_1_hSy.root',
		'/store/cmst3/user/cbern/RA2SusyJetMET/QCD_Pt_80to120_TuneZ2_7TeV_pythia6/Fall10-START38_V12-v1/GEN-SIM-RECO/susypat_RA2_32_1_Dm6.root',
		'/store/cmst3/user/cbern/RA2SusyJetMET/QCD_Pt_80to120_TuneZ2_7TeV_pythia6/Fall10-START38_V12-v1/GEN-SIM-RECO/susypat_RA2_33_2_dPr.root',
		'/store/cmst3/user/cbern/RA2SusyJetMET/QCD_Pt_80to120_TuneZ2_7TeV_pythia6/Fall10-START38_V12-v1/GEN-SIM-RECO/susypat_RA2_34_1_BLs.root',
		'/store/cmst3/user/cbern/RA2SusyJetMET/QCD_Pt_80to120_TuneZ2_7TeV_pythia6/Fall10-START38_V12-v1/GEN-SIM-RECO/susypat_RA2_35_1_rry.root',
		'/store/cmst3/user/cbern/RA2SusyJetMET/QCD_Pt_80to120_TuneZ2_7TeV_pythia6/Fall10-START38_V12-v1/GEN-SIM-RECO/susypat_RA2_36_1_ZTY.root',
		'/store/cmst3/user/cbern/RA2SusyJetMET/QCD_Pt_80to120_TuneZ2_7TeV_pythia6/Fall10-START38_V12-v1/GEN-SIM-RECO/susypat_RA2_37_1_J1I.root',
		'/store/cmst3/user/cbern/RA2SusyJetMET/QCD_Pt_80to120_TuneZ2_7TeV_pythia6/Fall10-START38_V12-v1/GEN-SIM-RECO/susypat_RA2_38_2_E86.root',
		'/store/cmst3/user/cbern/RA2SusyJetMET/QCD_Pt_80to120_TuneZ2_7TeV_pythia6/Fall10-START38_V12-v1/GEN-SIM-RECO/susypat_RA2_39_2_TKR.root',
		'/store/cmst3/user/cbern/RA2SusyJetMET/QCD_Pt_80to120_TuneZ2_7TeV_pythia6/Fall10-START38_V12-v1/GEN-SIM-RECO/susypat_RA2_3_1_tqD.root',
		'/store/cmst3/user/cbern/RA2SusyJetMET/QCD_Pt_80to120_TuneZ2_7TeV_pythia6/Fall10-START38_V12-v1/GEN-SIM-RECO/susypat_RA2_40_1_M9k.root',
		'/store/cmst3/user/cbern/RA2SusyJetMET/QCD_Pt_80to120_TuneZ2_7TeV_pythia6/Fall10-START38_V12-v1/GEN-SIM-RECO/susypat_RA2_41_2_0Ak.root',
		'/store/cmst3/user/cbern/RA2SusyJetMET/QCD_Pt_80to120_TuneZ2_7TeV_pythia6/Fall10-START38_V12-v1/GEN-SIM-RECO/susypat_RA2_42_2_d5D.root',
		'/store/cmst3/user/cbern/RA2SusyJetMET/QCD_Pt_80to120_TuneZ2_7TeV_pythia6/Fall10-START38_V12-v1/GEN-SIM-RECO/susypat_RA2_43_1_TqA.root',
		'/store/cmst3/user/cbern/RA2SusyJetMET/QCD_Pt_80to120_TuneZ2_7TeV_pythia6/Fall10-START38_V12-v1/GEN-SIM-RECO/susypat_RA2_44_2_tGH.root',
		'/store/cmst3/user/cbern/RA2SusyJetMET/QCD_Pt_80to120_TuneZ2_7TeV_pythia6/Fall10-START38_V12-v1/GEN-SIM-RECO/susypat_RA2_45_2_BVd.root',
		'/store/cmst3/user/cbern/RA2SusyJetMET/QCD_Pt_80to120_TuneZ2_7TeV_pythia6/Fall10-START38_V12-v1/GEN-SIM-RECO/susypat_RA2_46_1_tK4.root',
		'/store/cmst3/user/cbern/RA2SusyJetMET/QCD_Pt_80to120_TuneZ2_7TeV_pythia6/Fall10-START38_V12-v1/GEN-SIM-RECO/susypat_RA2_47_2_wSu.root',
		'/store/cmst3/user/cbern/RA2SusyJetMET/QCD_Pt_80to120_TuneZ2_7TeV_pythia6/Fall10-START38_V12-v1/GEN-SIM-RECO/susypat_RA2_48_1_afo.root',
		'/store/cmst3/user/cbern/RA2SusyJetMET/QCD_Pt_80to120_TuneZ2_7TeV_pythia6/Fall10-START38_V12-v1/GEN-SIM-RECO/susypat_RA2_49_2_rIn.root',
		'/store/cmst3/user/cbern/RA2SusyJetMET/QCD_Pt_80to120_TuneZ2_7TeV_pythia6/Fall10-START38_V12-v1/GEN-SIM-RECO/susypat_RA2_4_1_Nyu.root',
		'/store/cmst3/user/cbern/RA2SusyJetMET/QCD_Pt_80to120_TuneZ2_7TeV_pythia6/Fall10-START38_V12-v1/GEN-SIM-RECO/susypat_RA2_50_1_To4.root',
		'/store/cmst3/user/cbern/RA2SusyJetMET/QCD_Pt_80to120_TuneZ2_7TeV_pythia6/Fall10-START38_V12-v1/GEN-SIM-RECO/susypat_RA2_51_1_Nn1.root',
		'/store/cmst3/user/cbern/RA2SusyJetMET/QCD_Pt_80to120_TuneZ2_7TeV_pythia6/Fall10-START38_V12-v1/GEN-SIM-RECO/susypat_RA2_52_2_7bu.root',
		'/store/cmst3/user/cbern/RA2SusyJetMET/QCD_Pt_80to120_TuneZ2_7TeV_pythia6/Fall10-START38_V12-v1/GEN-SIM-RECO/susypat_RA2_53_2_OoI.root',
		'/store/cmst3/user/cbern/RA2SusyJetMET/QCD_Pt_80to120_TuneZ2_7TeV_pythia6/Fall10-START38_V12-v1/GEN-SIM-RECO/susypat_RA2_54_2_JyV.root',
		'/store/cmst3/user/cbern/RA2SusyJetMET/QCD_Pt_80to120_TuneZ2_7TeV_pythia6/Fall10-START38_V12-v1/GEN-SIM-RECO/susypat_RA2_55_2_2I9.root',
		'/store/cmst3/user/cbern/RA2SusyJetMET/QCD_Pt_80to120_TuneZ2_7TeV_pythia6/Fall10-START38_V12-v1/GEN-SIM-RECO/susypat_RA2_56_1_xKN.root',
		'/store/cmst3/user/cbern/RA2SusyJetMET/QCD_Pt_80to120_TuneZ2_7TeV_pythia6/Fall10-START38_V12-v1/GEN-SIM-RECO/susypat_RA2_57_2_9Y0.root',
		'/store/cmst3/user/cbern/RA2SusyJetMET/QCD_Pt_80to120_TuneZ2_7TeV_pythia6/Fall10-START38_V12-v1/GEN-SIM-RECO/susypat_RA2_58_2_aDe.root',
		'/store/cmst3/user/cbern/RA2SusyJetMET/QCD_Pt_80to120_TuneZ2_7TeV_pythia6/Fall10-START38_V12-v1/GEN-SIM-RECO/susypat_RA2_59_1_ZNe.root',
		'/store/cmst3/user/cbern/RA2SusyJetMET/QCD_Pt_80to120_TuneZ2_7TeV_pythia6/Fall10-START38_V12-v1/GEN-SIM-RECO/susypat_RA2_5_2_cRB.root',
		'/store/cmst3/user/cbern/RA2SusyJetMET/QCD_Pt_80to120_TuneZ2_7TeV_pythia6/Fall10-START38_V12-v1/GEN-SIM-RECO/susypat_RA2_60_2_GY6.root',
		'/store/cmst3/user/cbern/RA2SusyJetMET/QCD_Pt_80to120_TuneZ2_7TeV_pythia6/Fall10-START38_V12-v1/GEN-SIM-RECO/susypat_RA2_61_1_VRP.root',
		'/store/cmst3/user/cbern/RA2SusyJetMET/QCD_Pt_80to120_TuneZ2_7TeV_pythia6/Fall10-START38_V12-v1/GEN-SIM-RECO/susypat_RA2_62_2_fSq.root',
		'/store/cmst3/user/cbern/RA2SusyJetMET/QCD_Pt_80to120_TuneZ2_7TeV_pythia6/Fall10-START38_V12-v1/GEN-SIM-RECO/susypat_RA2_63_2_Mae.root',
		'/store/cmst3/user/cbern/RA2SusyJetMET/QCD_Pt_80to120_TuneZ2_7TeV_pythia6/Fall10-START38_V12-v1/GEN-SIM-RECO/susypat_RA2_64_1_HTz.root',
		'/store/cmst3/user/cbern/RA2SusyJetMET/QCD_Pt_80to120_TuneZ2_7TeV_pythia6/Fall10-START38_V12-v1/GEN-SIM-RECO/susypat_RA2_65_2_f9N.root',
		'/store/cmst3/user/cbern/RA2SusyJetMET/QCD_Pt_80to120_TuneZ2_7TeV_pythia6/Fall10-START38_V12-v1/GEN-SIM-RECO/susypat_RA2_66_1_RJ5.root',
		'/store/cmst3/user/cbern/RA2SusyJetMET/QCD_Pt_80to120_TuneZ2_7TeV_pythia6/Fall10-START38_V12-v1/GEN-SIM-RECO/susypat_RA2_67_2_yee.root',
		'/store/cmst3/user/cbern/RA2SusyJetMET/QCD_Pt_80to120_TuneZ2_7TeV_pythia6/Fall10-START38_V12-v1/GEN-SIM-RECO/susypat_RA2_68_2_AhL.root',
		'/store/cmst3/user/cbern/RA2SusyJetMET/QCD_Pt_80to120_TuneZ2_7TeV_pythia6/Fall10-START38_V12-v1/GEN-SIM-RECO/susypat_RA2_69_1_VhK.root',
		'/store/cmst3/user/cbern/RA2SusyJetMET/QCD_Pt_80to120_TuneZ2_7TeV_pythia6/Fall10-START38_V12-v1/GEN-SIM-RECO/susypat_RA2_6_2_PvJ.root',
		'/store/cmst3/user/cbern/RA2SusyJetMET/QCD_Pt_80to120_TuneZ2_7TeV_pythia6/Fall10-START38_V12-v1/GEN-SIM-RECO/susypat_RA2_70_2_m1r.root',
		'/store/cmst3/user/cbern/RA2SusyJetMET/QCD_Pt_80to120_TuneZ2_7TeV_pythia6/Fall10-START38_V12-v1/GEN-SIM-RECO/susypat_RA2_71_2_jSB.root',
		'/store/cmst3/user/cbern/RA2SusyJetMET/QCD_Pt_80to120_TuneZ2_7TeV_pythia6/Fall10-START38_V12-v1/GEN-SIM-RECO/susypat_RA2_72_1_oDo.root',
		'/store/cmst3/user/cbern/RA2SusyJetMET/QCD_Pt_80to120_TuneZ2_7TeV_pythia6/Fall10-START38_V12-v1/GEN-SIM-RECO/susypat_RA2_73_2_3kW.root',
		'/store/cmst3/user/cbern/RA2SusyJetMET/QCD_Pt_80to120_TuneZ2_7TeV_pythia6/Fall10-START38_V12-v1/GEN-SIM-RECO/susypat_RA2_74_2_zY3.root',
		'/store/cmst3/user/cbern/RA2SusyJetMET/QCD_Pt_80to120_TuneZ2_7TeV_pythia6/Fall10-START38_V12-v1/GEN-SIM-RECO/susypat_RA2_75_2_rBU.root',
		'/store/cmst3/user/cbern/RA2SusyJetMET/QCD_Pt_80to120_TuneZ2_7TeV_pythia6/Fall10-START38_V12-v1/GEN-SIM-RECO/susypat_RA2_76_1_dtc.root',
		'/store/cmst3/user/cbern/RA2SusyJetMET/QCD_Pt_80to120_TuneZ2_7TeV_pythia6/Fall10-START38_V12-v1/GEN-SIM-RECO/susypat_RA2_77_1_zfC.root',
		'/store/cmst3/user/cbern/RA2SusyJetMET/QCD_Pt_80to120_TuneZ2_7TeV_pythia6/Fall10-START38_V12-v1/GEN-SIM-RECO/susypat_RA2_78_1_Ju7.root',
		'/store/cmst3/user/cbern/RA2SusyJetMET/QCD_Pt_80to120_TuneZ2_7TeV_pythia6/Fall10-START38_V12-v1/GEN-SIM-RECO/susypat_RA2_79_2_7YJ.root',
		'/store/cmst3/user/cbern/RA2SusyJetMET/QCD_Pt_80to120_TuneZ2_7TeV_pythia6/Fall10-START38_V12-v1/GEN-SIM-RECO/susypat_RA2_7_1_WOJ.root',
		'/store/cmst3/user/cbern/RA2SusyJetMET/QCD_Pt_80to120_TuneZ2_7TeV_pythia6/Fall10-START38_V12-v1/GEN-SIM-RECO/susypat_RA2_80_1_Hh8.root',
		'/store/cmst3/user/cbern/RA2SusyJetMET/QCD_Pt_80to120_TuneZ2_7TeV_pythia6/Fall10-START38_V12-v1/GEN-SIM-RECO/susypat_RA2_8_1_O4a.root',
		'/store/cmst3/user/cbern/RA2SusyJetMET/QCD_Pt_80to120_TuneZ2_7TeV_pythia6/Fall10-START38_V12-v1/GEN-SIM-RECO/susypat_RA2_9_1_CUm.root',
])
