
import FWCore.ParameterSet.Config as cms

source = cms.Source(
	"PoolSource",

	noEventSort = cms.untracked.bool(True),
	duplicateCheckMode = cms.untracked.string("noDuplicateCheck"),
	fileNames = cms.untracked.vstring()
)
source.fileNames.extend([
		'/store/cmst3/user/cbern/CMG/HT/Run2011A-May10ReReco-v1/AOD/PAT_CMG_NewJEC/RA2/susy_tree_CMG_0.root',
		'/store/cmst3/user/cbern/CMG/HT/Run2011A-May10ReReco-v1/AOD/PAT_CMG_NewJEC/RA2/susy_tree_CMG_1.root',
		'/store/cmst3/user/cbern/CMG/HT/Run2011A-May10ReReco-v1/AOD/PAT_CMG_NewJEC/RA2/susy_tree_CMG_10.root',
		'/store/cmst3/user/cbern/CMG/HT/Run2011A-May10ReReco-v1/AOD/PAT_CMG_NewJEC/RA2/susy_tree_CMG_100.root',
		'/store/cmst3/user/cbern/CMG/HT/Run2011A-May10ReReco-v1/AOD/PAT_CMG_NewJEC/RA2/susy_tree_CMG_101.root',
		'/store/cmst3/user/cbern/CMG/HT/Run2011A-May10ReReco-v1/AOD/PAT_CMG_NewJEC/RA2/susy_tree_CMG_102.root',
		'/store/cmst3/user/cbern/CMG/HT/Run2011A-May10ReReco-v1/AOD/PAT_CMG_NewJEC/RA2/susy_tree_CMG_103.root',
		'/store/cmst3/user/cbern/CMG/HT/Run2011A-May10ReReco-v1/AOD/PAT_CMG_NewJEC/RA2/susy_tree_CMG_104.root',
		'/store/cmst3/user/cbern/CMG/HT/Run2011A-May10ReReco-v1/AOD/PAT_CMG_NewJEC/RA2/susy_tree_CMG_105.root',
		'/store/cmst3/user/cbern/CMG/HT/Run2011A-May10ReReco-v1/AOD/PAT_CMG_NewJEC/RA2/susy_tree_CMG_106.root',
		'/store/cmst3/user/cbern/CMG/HT/Run2011A-May10ReReco-v1/AOD/PAT_CMG_NewJEC/RA2/susy_tree_CMG_107.root',
		'/store/cmst3/user/cbern/CMG/HT/Run2011A-May10ReReco-v1/AOD/PAT_CMG_NewJEC/RA2/susy_tree_CMG_108.root',
		'/store/cmst3/user/cbern/CMG/HT/Run2011A-May10ReReco-v1/AOD/PAT_CMG_NewJEC/RA2/susy_tree_CMG_109.root',
		'/store/cmst3/user/cbern/CMG/HT/Run2011A-May10ReReco-v1/AOD/PAT_CMG_NewJEC/RA2/susy_tree_CMG_11.root',
		'/store/cmst3/user/cbern/CMG/HT/Run2011A-May10ReReco-v1/AOD/PAT_CMG_NewJEC/RA2/susy_tree_CMG_110.root',
		'/store/cmst3/user/cbern/CMG/HT/Run2011A-May10ReReco-v1/AOD/PAT_CMG_NewJEC/RA2/susy_tree_CMG_111.root',
		'/store/cmst3/user/cbern/CMG/HT/Run2011A-May10ReReco-v1/AOD/PAT_CMG_NewJEC/RA2/susy_tree_CMG_112.root',
		'/store/cmst3/user/cbern/CMG/HT/Run2011A-May10ReReco-v1/AOD/PAT_CMG_NewJEC/RA2/susy_tree_CMG_113.root',
		'/store/cmst3/user/cbern/CMG/HT/Run2011A-May10ReReco-v1/AOD/PAT_CMG_NewJEC/RA2/susy_tree_CMG_114.root',
		'/store/cmst3/user/cbern/CMG/HT/Run2011A-May10ReReco-v1/AOD/PAT_CMG_NewJEC/RA2/susy_tree_CMG_115.root',
		'/store/cmst3/user/cbern/CMG/HT/Run2011A-May10ReReco-v1/AOD/PAT_CMG_NewJEC/RA2/susy_tree_CMG_116.root',
		'/store/cmst3/user/cbern/CMG/HT/Run2011A-May10ReReco-v1/AOD/PAT_CMG_NewJEC/RA2/susy_tree_CMG_117.root',
		'/store/cmst3/user/cbern/CMG/HT/Run2011A-May10ReReco-v1/AOD/PAT_CMG_NewJEC/RA2/susy_tree_CMG_118.root',
		'/store/cmst3/user/cbern/CMG/HT/Run2011A-May10ReReco-v1/AOD/PAT_CMG_NewJEC/RA2/susy_tree_CMG_119.root',
		'/store/cmst3/user/cbern/CMG/HT/Run2011A-May10ReReco-v1/AOD/PAT_CMG_NewJEC/RA2/susy_tree_CMG_12.root',
		'/store/cmst3/user/cbern/CMG/HT/Run2011A-May10ReReco-v1/AOD/PAT_CMG_NewJEC/RA2/susy_tree_CMG_120.root',
		'/store/cmst3/user/cbern/CMG/HT/Run2011A-May10ReReco-v1/AOD/PAT_CMG_NewJEC/RA2/susy_tree_CMG_121.root',
		'/store/cmst3/user/cbern/CMG/HT/Run2011A-May10ReReco-v1/AOD/PAT_CMG_NewJEC/RA2/susy_tree_CMG_122.root',
		'/store/cmst3/user/cbern/CMG/HT/Run2011A-May10ReReco-v1/AOD/PAT_CMG_NewJEC/RA2/susy_tree_CMG_123.root',
		'/store/cmst3/user/cbern/CMG/HT/Run2011A-May10ReReco-v1/AOD/PAT_CMG_NewJEC/RA2/susy_tree_CMG_124.root',
		'/store/cmst3/user/cbern/CMG/HT/Run2011A-May10ReReco-v1/AOD/PAT_CMG_NewJEC/RA2/susy_tree_CMG_125.root',
		'/store/cmst3/user/cbern/CMG/HT/Run2011A-May10ReReco-v1/AOD/PAT_CMG_NewJEC/RA2/susy_tree_CMG_126.root',
		'/store/cmst3/user/cbern/CMG/HT/Run2011A-May10ReReco-v1/AOD/PAT_CMG_NewJEC/RA2/susy_tree_CMG_127.root',
		'/store/cmst3/user/cbern/CMG/HT/Run2011A-May10ReReco-v1/AOD/PAT_CMG_NewJEC/RA2/susy_tree_CMG_128.root',
		'/store/cmst3/user/cbern/CMG/HT/Run2011A-May10ReReco-v1/AOD/PAT_CMG_NewJEC/RA2/susy_tree_CMG_129.root',
		'/store/cmst3/user/cbern/CMG/HT/Run2011A-May10ReReco-v1/AOD/PAT_CMG_NewJEC/RA2/susy_tree_CMG_13.root',
		'/store/cmst3/user/cbern/CMG/HT/Run2011A-May10ReReco-v1/AOD/PAT_CMG_NewJEC/RA2/susy_tree_CMG_130.root',
		'/store/cmst3/user/cbern/CMG/HT/Run2011A-May10ReReco-v1/AOD/PAT_CMG_NewJEC/RA2/susy_tree_CMG_131.root',
		'/store/cmst3/user/cbern/CMG/HT/Run2011A-May10ReReco-v1/AOD/PAT_CMG_NewJEC/RA2/susy_tree_CMG_132.root',
		'/store/cmst3/user/cbern/CMG/HT/Run2011A-May10ReReco-v1/AOD/PAT_CMG_NewJEC/RA2/susy_tree_CMG_133.root',
		'/store/cmst3/user/cbern/CMG/HT/Run2011A-May10ReReco-v1/AOD/PAT_CMG_NewJEC/RA2/susy_tree_CMG_134.root',
		'/store/cmst3/user/cbern/CMG/HT/Run2011A-May10ReReco-v1/AOD/PAT_CMG_NewJEC/RA2/susy_tree_CMG_135.root',
		'/store/cmst3/user/cbern/CMG/HT/Run2011A-May10ReReco-v1/AOD/PAT_CMG_NewJEC/RA2/susy_tree_CMG_136.root',
		'/store/cmst3/user/cbern/CMG/HT/Run2011A-May10ReReco-v1/AOD/PAT_CMG_NewJEC/RA2/susy_tree_CMG_137.root',
		'/store/cmst3/user/cbern/CMG/HT/Run2011A-May10ReReco-v1/AOD/PAT_CMG_NewJEC/RA2/susy_tree_CMG_138.root',
		'/store/cmst3/user/cbern/CMG/HT/Run2011A-May10ReReco-v1/AOD/PAT_CMG_NewJEC/RA2/susy_tree_CMG_139.root',
		'/store/cmst3/user/cbern/CMG/HT/Run2011A-May10ReReco-v1/AOD/PAT_CMG_NewJEC/RA2/susy_tree_CMG_14.root',
		'/store/cmst3/user/cbern/CMG/HT/Run2011A-May10ReReco-v1/AOD/PAT_CMG_NewJEC/RA2/susy_tree_CMG_140.root',
		'/store/cmst3/user/cbern/CMG/HT/Run2011A-May10ReReco-v1/AOD/PAT_CMG_NewJEC/RA2/susy_tree_CMG_141.root',
		'/store/cmst3/user/cbern/CMG/HT/Run2011A-May10ReReco-v1/AOD/PAT_CMG_NewJEC/RA2/susy_tree_CMG_142.root',
		'/store/cmst3/user/cbern/CMG/HT/Run2011A-May10ReReco-v1/AOD/PAT_CMG_NewJEC/RA2/susy_tree_CMG_143.root',
		'/store/cmst3/user/cbern/CMG/HT/Run2011A-May10ReReco-v1/AOD/PAT_CMG_NewJEC/RA2/susy_tree_CMG_144.root',
		'/store/cmst3/user/cbern/CMG/HT/Run2011A-May10ReReco-v1/AOD/PAT_CMG_NewJEC/RA2/susy_tree_CMG_145.root',
		'/store/cmst3/user/cbern/CMG/HT/Run2011A-May10ReReco-v1/AOD/PAT_CMG_NewJEC/RA2/susy_tree_CMG_146.root',
		'/store/cmst3/user/cbern/CMG/HT/Run2011A-May10ReReco-v1/AOD/PAT_CMG_NewJEC/RA2/susy_tree_CMG_147.root',
		'/store/cmst3/user/cbern/CMG/HT/Run2011A-May10ReReco-v1/AOD/PAT_CMG_NewJEC/RA2/susy_tree_CMG_148.root',
		'/store/cmst3/user/cbern/CMG/HT/Run2011A-May10ReReco-v1/AOD/PAT_CMG_NewJEC/RA2/susy_tree_CMG_149.root',
		'/store/cmst3/user/cbern/CMG/HT/Run2011A-May10ReReco-v1/AOD/PAT_CMG_NewJEC/RA2/susy_tree_CMG_15.root',
		'/store/cmst3/user/cbern/CMG/HT/Run2011A-May10ReReco-v1/AOD/PAT_CMG_NewJEC/RA2/susy_tree_CMG_150.root',
		'/store/cmst3/user/cbern/CMG/HT/Run2011A-May10ReReco-v1/AOD/PAT_CMG_NewJEC/RA2/susy_tree_CMG_151.root',
		'/store/cmst3/user/cbern/CMG/HT/Run2011A-May10ReReco-v1/AOD/PAT_CMG_NewJEC/RA2/susy_tree_CMG_152.root',
		'/store/cmst3/user/cbern/CMG/HT/Run2011A-May10ReReco-v1/AOD/PAT_CMG_NewJEC/RA2/susy_tree_CMG_153.root',
		'/store/cmst3/user/cbern/CMG/HT/Run2011A-May10ReReco-v1/AOD/PAT_CMG_NewJEC/RA2/susy_tree_CMG_154.root',
		'/store/cmst3/user/cbern/CMG/HT/Run2011A-May10ReReco-v1/AOD/PAT_CMG_NewJEC/RA2/susy_tree_CMG_155.root',
		'/store/cmst3/user/cbern/CMG/HT/Run2011A-May10ReReco-v1/AOD/PAT_CMG_NewJEC/RA2/susy_tree_CMG_156.root',
		'/store/cmst3/user/cbern/CMG/HT/Run2011A-May10ReReco-v1/AOD/PAT_CMG_NewJEC/RA2/susy_tree_CMG_157.root',
		'/store/cmst3/user/cbern/CMG/HT/Run2011A-May10ReReco-v1/AOD/PAT_CMG_NewJEC/RA2/susy_tree_CMG_158.root',
		'/store/cmst3/user/cbern/CMG/HT/Run2011A-May10ReReco-v1/AOD/PAT_CMG_NewJEC/RA2/susy_tree_CMG_159.root',
		'/store/cmst3/user/cbern/CMG/HT/Run2011A-May10ReReco-v1/AOD/PAT_CMG_NewJEC/RA2/susy_tree_CMG_16.root',
		'/store/cmst3/user/cbern/CMG/HT/Run2011A-May10ReReco-v1/AOD/PAT_CMG_NewJEC/RA2/susy_tree_CMG_160.root',
		'/store/cmst3/user/cbern/CMG/HT/Run2011A-May10ReReco-v1/AOD/PAT_CMG_NewJEC/RA2/susy_tree_CMG_161.root',
		'/store/cmst3/user/cbern/CMG/HT/Run2011A-May10ReReco-v1/AOD/PAT_CMG_NewJEC/RA2/susy_tree_CMG_162.root',
		'/store/cmst3/user/cbern/CMG/HT/Run2011A-May10ReReco-v1/AOD/PAT_CMG_NewJEC/RA2/susy_tree_CMG_163.root',
		'/store/cmst3/user/cbern/CMG/HT/Run2011A-May10ReReco-v1/AOD/PAT_CMG_NewJEC/RA2/susy_tree_CMG_164.root',
		'/store/cmst3/user/cbern/CMG/HT/Run2011A-May10ReReco-v1/AOD/PAT_CMG_NewJEC/RA2/susy_tree_CMG_165.root',
		'/store/cmst3/user/cbern/CMG/HT/Run2011A-May10ReReco-v1/AOD/PAT_CMG_NewJEC/RA2/susy_tree_CMG_166.root',
		'/store/cmst3/user/cbern/CMG/HT/Run2011A-May10ReReco-v1/AOD/PAT_CMG_NewJEC/RA2/susy_tree_CMG_167.root',
		'/store/cmst3/user/cbern/CMG/HT/Run2011A-May10ReReco-v1/AOD/PAT_CMG_NewJEC/RA2/susy_tree_CMG_168.root',
		'/store/cmst3/user/cbern/CMG/HT/Run2011A-May10ReReco-v1/AOD/PAT_CMG_NewJEC/RA2/susy_tree_CMG_169.root',
		'/store/cmst3/user/cbern/CMG/HT/Run2011A-May10ReReco-v1/AOD/PAT_CMG_NewJEC/RA2/susy_tree_CMG_17.root',
		'/store/cmst3/user/cbern/CMG/HT/Run2011A-May10ReReco-v1/AOD/PAT_CMG_NewJEC/RA2/susy_tree_CMG_170.root',
		'/store/cmst3/user/cbern/CMG/HT/Run2011A-May10ReReco-v1/AOD/PAT_CMG_NewJEC/RA2/susy_tree_CMG_171.root',
		'/store/cmst3/user/cbern/CMG/HT/Run2011A-May10ReReco-v1/AOD/PAT_CMG_NewJEC/RA2/susy_tree_CMG_18.root',
		'/store/cmst3/user/cbern/CMG/HT/Run2011A-May10ReReco-v1/AOD/PAT_CMG_NewJEC/RA2/susy_tree_CMG_19.root',
		'/store/cmst3/user/cbern/CMG/HT/Run2011A-May10ReReco-v1/AOD/PAT_CMG_NewJEC/RA2/susy_tree_CMG_2.root',
		'/store/cmst3/user/cbern/CMG/HT/Run2011A-May10ReReco-v1/AOD/PAT_CMG_NewJEC/RA2/susy_tree_CMG_20.root',
		'/store/cmst3/user/cbern/CMG/HT/Run2011A-May10ReReco-v1/AOD/PAT_CMG_NewJEC/RA2/susy_tree_CMG_21.root',
		'/store/cmst3/user/cbern/CMG/HT/Run2011A-May10ReReco-v1/AOD/PAT_CMG_NewJEC/RA2/susy_tree_CMG_22.root',
		'/store/cmst3/user/cbern/CMG/HT/Run2011A-May10ReReco-v1/AOD/PAT_CMG_NewJEC/RA2/susy_tree_CMG_23.root',
		'/store/cmst3/user/cbern/CMG/HT/Run2011A-May10ReReco-v1/AOD/PAT_CMG_NewJEC/RA2/susy_tree_CMG_24.root',
		'/store/cmst3/user/cbern/CMG/HT/Run2011A-May10ReReco-v1/AOD/PAT_CMG_NewJEC/RA2/susy_tree_CMG_25.root',
		'/store/cmst3/user/cbern/CMG/HT/Run2011A-May10ReReco-v1/AOD/PAT_CMG_NewJEC/RA2/susy_tree_CMG_26.root',
		'/store/cmst3/user/cbern/CMG/HT/Run2011A-May10ReReco-v1/AOD/PAT_CMG_NewJEC/RA2/susy_tree_CMG_27.root',
		'/store/cmst3/user/cbern/CMG/HT/Run2011A-May10ReReco-v1/AOD/PAT_CMG_NewJEC/RA2/susy_tree_CMG_28.root',
		'/store/cmst3/user/cbern/CMG/HT/Run2011A-May10ReReco-v1/AOD/PAT_CMG_NewJEC/RA2/susy_tree_CMG_29.root',
		'/store/cmst3/user/cbern/CMG/HT/Run2011A-May10ReReco-v1/AOD/PAT_CMG_NewJEC/RA2/susy_tree_CMG_3.root',
		'/store/cmst3/user/cbern/CMG/HT/Run2011A-May10ReReco-v1/AOD/PAT_CMG_NewJEC/RA2/susy_tree_CMG_30.root',
		'/store/cmst3/user/cbern/CMG/HT/Run2011A-May10ReReco-v1/AOD/PAT_CMG_NewJEC/RA2/susy_tree_CMG_31.root',
		'/store/cmst3/user/cbern/CMG/HT/Run2011A-May10ReReco-v1/AOD/PAT_CMG_NewJEC/RA2/susy_tree_CMG_32.root',
		'/store/cmst3/user/cbern/CMG/HT/Run2011A-May10ReReco-v1/AOD/PAT_CMG_NewJEC/RA2/susy_tree_CMG_33.root',
		'/store/cmst3/user/cbern/CMG/HT/Run2011A-May10ReReco-v1/AOD/PAT_CMG_NewJEC/RA2/susy_tree_CMG_34.root',
		'/store/cmst3/user/cbern/CMG/HT/Run2011A-May10ReReco-v1/AOD/PAT_CMG_NewJEC/RA2/susy_tree_CMG_35.root',
		'/store/cmst3/user/cbern/CMG/HT/Run2011A-May10ReReco-v1/AOD/PAT_CMG_NewJEC/RA2/susy_tree_CMG_36.root',
		'/store/cmst3/user/cbern/CMG/HT/Run2011A-May10ReReco-v1/AOD/PAT_CMG_NewJEC/RA2/susy_tree_CMG_37.root',
		'/store/cmst3/user/cbern/CMG/HT/Run2011A-May10ReReco-v1/AOD/PAT_CMG_NewJEC/RA2/susy_tree_CMG_38.root',
		'/store/cmst3/user/cbern/CMG/HT/Run2011A-May10ReReco-v1/AOD/PAT_CMG_NewJEC/RA2/susy_tree_CMG_39.root',
		'/store/cmst3/user/cbern/CMG/HT/Run2011A-May10ReReco-v1/AOD/PAT_CMG_NewJEC/RA2/susy_tree_CMG_4.root',
		'/store/cmst3/user/cbern/CMG/HT/Run2011A-May10ReReco-v1/AOD/PAT_CMG_NewJEC/RA2/susy_tree_CMG_40.root',
		'/store/cmst3/user/cbern/CMG/HT/Run2011A-May10ReReco-v1/AOD/PAT_CMG_NewJEC/RA2/susy_tree_CMG_41.root',
		'/store/cmst3/user/cbern/CMG/HT/Run2011A-May10ReReco-v1/AOD/PAT_CMG_NewJEC/RA2/susy_tree_CMG_42.root',
		'/store/cmst3/user/cbern/CMG/HT/Run2011A-May10ReReco-v1/AOD/PAT_CMG_NewJEC/RA2/susy_tree_CMG_43.root',
		'/store/cmst3/user/cbern/CMG/HT/Run2011A-May10ReReco-v1/AOD/PAT_CMG_NewJEC/RA2/susy_tree_CMG_44.root',
		'/store/cmst3/user/cbern/CMG/HT/Run2011A-May10ReReco-v1/AOD/PAT_CMG_NewJEC/RA2/susy_tree_CMG_45.root',
		'/store/cmst3/user/cbern/CMG/HT/Run2011A-May10ReReco-v1/AOD/PAT_CMG_NewJEC/RA2/susy_tree_CMG_46.root',
		'/store/cmst3/user/cbern/CMG/HT/Run2011A-May10ReReco-v1/AOD/PAT_CMG_NewJEC/RA2/susy_tree_CMG_47.root',
		'/store/cmst3/user/cbern/CMG/HT/Run2011A-May10ReReco-v1/AOD/PAT_CMG_NewJEC/RA2/susy_tree_CMG_48.root',
		'/store/cmst3/user/cbern/CMG/HT/Run2011A-May10ReReco-v1/AOD/PAT_CMG_NewJEC/RA2/susy_tree_CMG_49.root',
		'/store/cmst3/user/cbern/CMG/HT/Run2011A-May10ReReco-v1/AOD/PAT_CMG_NewJEC/RA2/susy_tree_CMG_5.root',
		'/store/cmst3/user/cbern/CMG/HT/Run2011A-May10ReReco-v1/AOD/PAT_CMG_NewJEC/RA2/susy_tree_CMG_50.root',
		'/store/cmst3/user/cbern/CMG/HT/Run2011A-May10ReReco-v1/AOD/PAT_CMG_NewJEC/RA2/susy_tree_CMG_51.root',
		'/store/cmst3/user/cbern/CMG/HT/Run2011A-May10ReReco-v1/AOD/PAT_CMG_NewJEC/RA2/susy_tree_CMG_52.root',
		'/store/cmst3/user/cbern/CMG/HT/Run2011A-May10ReReco-v1/AOD/PAT_CMG_NewJEC/RA2/susy_tree_CMG_53.root',
		'/store/cmst3/user/cbern/CMG/HT/Run2011A-May10ReReco-v1/AOD/PAT_CMG_NewJEC/RA2/susy_tree_CMG_54.root',
		'/store/cmst3/user/cbern/CMG/HT/Run2011A-May10ReReco-v1/AOD/PAT_CMG_NewJEC/RA2/susy_tree_CMG_55.root',
		'/store/cmst3/user/cbern/CMG/HT/Run2011A-May10ReReco-v1/AOD/PAT_CMG_NewJEC/RA2/susy_tree_CMG_56.root',
		'/store/cmst3/user/cbern/CMG/HT/Run2011A-May10ReReco-v1/AOD/PAT_CMG_NewJEC/RA2/susy_tree_CMG_57.root',
		'/store/cmst3/user/cbern/CMG/HT/Run2011A-May10ReReco-v1/AOD/PAT_CMG_NewJEC/RA2/susy_tree_CMG_58.root',
		'/store/cmst3/user/cbern/CMG/HT/Run2011A-May10ReReco-v1/AOD/PAT_CMG_NewJEC/RA2/susy_tree_CMG_59.root',
		'/store/cmst3/user/cbern/CMG/HT/Run2011A-May10ReReco-v1/AOD/PAT_CMG_NewJEC/RA2/susy_tree_CMG_6.root',
		'/store/cmst3/user/cbern/CMG/HT/Run2011A-May10ReReco-v1/AOD/PAT_CMG_NewJEC/RA2/susy_tree_CMG_60.root',
		'/store/cmst3/user/cbern/CMG/HT/Run2011A-May10ReReco-v1/AOD/PAT_CMG_NewJEC/RA2/susy_tree_CMG_61.root',
		'/store/cmst3/user/cbern/CMG/HT/Run2011A-May10ReReco-v1/AOD/PAT_CMG_NewJEC/RA2/susy_tree_CMG_62.root',
		'/store/cmst3/user/cbern/CMG/HT/Run2011A-May10ReReco-v1/AOD/PAT_CMG_NewJEC/RA2/susy_tree_CMG_63.root',
		'/store/cmst3/user/cbern/CMG/HT/Run2011A-May10ReReco-v1/AOD/PAT_CMG_NewJEC/RA2/susy_tree_CMG_64.root',
		'/store/cmst3/user/cbern/CMG/HT/Run2011A-May10ReReco-v1/AOD/PAT_CMG_NewJEC/RA2/susy_tree_CMG_65.root',
		'/store/cmst3/user/cbern/CMG/HT/Run2011A-May10ReReco-v1/AOD/PAT_CMG_NewJEC/RA2/susy_tree_CMG_66.root',
		'/store/cmst3/user/cbern/CMG/HT/Run2011A-May10ReReco-v1/AOD/PAT_CMG_NewJEC/RA2/susy_tree_CMG_67.root',
		'/store/cmst3/user/cbern/CMG/HT/Run2011A-May10ReReco-v1/AOD/PAT_CMG_NewJEC/RA2/susy_tree_CMG_68.root',
		'/store/cmst3/user/cbern/CMG/HT/Run2011A-May10ReReco-v1/AOD/PAT_CMG_NewJEC/RA2/susy_tree_CMG_69.root',
		'/store/cmst3/user/cbern/CMG/HT/Run2011A-May10ReReco-v1/AOD/PAT_CMG_NewJEC/RA2/susy_tree_CMG_7.root',
		'/store/cmst3/user/cbern/CMG/HT/Run2011A-May10ReReco-v1/AOD/PAT_CMG_NewJEC/RA2/susy_tree_CMG_70.root',
		'/store/cmst3/user/cbern/CMG/HT/Run2011A-May10ReReco-v1/AOD/PAT_CMG_NewJEC/RA2/susy_tree_CMG_71.root',
		'/store/cmst3/user/cbern/CMG/HT/Run2011A-May10ReReco-v1/AOD/PAT_CMG_NewJEC/RA2/susy_tree_CMG_72.root',
		'/store/cmst3/user/cbern/CMG/HT/Run2011A-May10ReReco-v1/AOD/PAT_CMG_NewJEC/RA2/susy_tree_CMG_73.root',
		'/store/cmst3/user/cbern/CMG/HT/Run2011A-May10ReReco-v1/AOD/PAT_CMG_NewJEC/RA2/susy_tree_CMG_74.root',
		'/store/cmst3/user/cbern/CMG/HT/Run2011A-May10ReReco-v1/AOD/PAT_CMG_NewJEC/RA2/susy_tree_CMG_75.root',
		'/store/cmst3/user/cbern/CMG/HT/Run2011A-May10ReReco-v1/AOD/PAT_CMG_NewJEC/RA2/susy_tree_CMG_76.root',
		'/store/cmst3/user/cbern/CMG/HT/Run2011A-May10ReReco-v1/AOD/PAT_CMG_NewJEC/RA2/susy_tree_CMG_77.root',
		'/store/cmst3/user/cbern/CMG/HT/Run2011A-May10ReReco-v1/AOD/PAT_CMG_NewJEC/RA2/susy_tree_CMG_78.root',
		'/store/cmst3/user/cbern/CMG/HT/Run2011A-May10ReReco-v1/AOD/PAT_CMG_NewJEC/RA2/susy_tree_CMG_79.root',
		'/store/cmst3/user/cbern/CMG/HT/Run2011A-May10ReReco-v1/AOD/PAT_CMG_NewJEC/RA2/susy_tree_CMG_8.root',
		'/store/cmst3/user/cbern/CMG/HT/Run2011A-May10ReReco-v1/AOD/PAT_CMG_NewJEC/RA2/susy_tree_CMG_80.root',
		'/store/cmst3/user/cbern/CMG/HT/Run2011A-May10ReReco-v1/AOD/PAT_CMG_NewJEC/RA2/susy_tree_CMG_81.root',
		'/store/cmst3/user/cbern/CMG/HT/Run2011A-May10ReReco-v1/AOD/PAT_CMG_NewJEC/RA2/susy_tree_CMG_82.root',
		'/store/cmst3/user/cbern/CMG/HT/Run2011A-May10ReReco-v1/AOD/PAT_CMG_NewJEC/RA2/susy_tree_CMG_83.root',
		'/store/cmst3/user/cbern/CMG/HT/Run2011A-May10ReReco-v1/AOD/PAT_CMG_NewJEC/RA2/susy_tree_CMG_84.root',
		'/store/cmst3/user/cbern/CMG/HT/Run2011A-May10ReReco-v1/AOD/PAT_CMG_NewJEC/RA2/susy_tree_CMG_85.root',
		'/store/cmst3/user/cbern/CMG/HT/Run2011A-May10ReReco-v1/AOD/PAT_CMG_NewJEC/RA2/susy_tree_CMG_86.root',
		'/store/cmst3/user/cbern/CMG/HT/Run2011A-May10ReReco-v1/AOD/PAT_CMG_NewJEC/RA2/susy_tree_CMG_87.root',
		'/store/cmst3/user/cbern/CMG/HT/Run2011A-May10ReReco-v1/AOD/PAT_CMG_NewJEC/RA2/susy_tree_CMG_88.root',
		'/store/cmst3/user/cbern/CMG/HT/Run2011A-May10ReReco-v1/AOD/PAT_CMG_NewJEC/RA2/susy_tree_CMG_89.root',
		'/store/cmst3/user/cbern/CMG/HT/Run2011A-May10ReReco-v1/AOD/PAT_CMG_NewJEC/RA2/susy_tree_CMG_9.root',
		'/store/cmst3/user/cbern/CMG/HT/Run2011A-May10ReReco-v1/AOD/PAT_CMG_NewJEC/RA2/susy_tree_CMG_90.root',
		'/store/cmst3/user/cbern/CMG/HT/Run2011A-May10ReReco-v1/AOD/PAT_CMG_NewJEC/RA2/susy_tree_CMG_91.root',
		'/store/cmst3/user/cbern/CMG/HT/Run2011A-May10ReReco-v1/AOD/PAT_CMG_NewJEC/RA2/susy_tree_CMG_92.root',
		'/store/cmst3/user/cbern/CMG/HT/Run2011A-May10ReReco-v1/AOD/PAT_CMG_NewJEC/RA2/susy_tree_CMG_93.root',
		'/store/cmst3/user/cbern/CMG/HT/Run2011A-May10ReReco-v1/AOD/PAT_CMG_NewJEC/RA2/susy_tree_CMG_94.root',
		'/store/cmst3/user/cbern/CMG/HT/Run2011A-May10ReReco-v1/AOD/PAT_CMG_NewJEC/RA2/susy_tree_CMG_95.root',
		'/store/cmst3/user/cbern/CMG/HT/Run2011A-May10ReReco-v1/AOD/PAT_CMG_NewJEC/RA2/susy_tree_CMG_96.root',
		'/store/cmst3/user/cbern/CMG/HT/Run2011A-May10ReReco-v1/AOD/PAT_CMG_NewJEC/RA2/susy_tree_CMG_97.root',
		'/store/cmst3/user/cbern/CMG/HT/Run2011A-May10ReReco-v1/AOD/PAT_CMG_NewJEC/RA2/susy_tree_CMG_98.root',
		'/store/cmst3/user/cbern/CMG/HT/Run2011A-May10ReReco-v1/AOD/PAT_CMG_NewJEC/RA2/susy_tree_CMG_99.root',
])
