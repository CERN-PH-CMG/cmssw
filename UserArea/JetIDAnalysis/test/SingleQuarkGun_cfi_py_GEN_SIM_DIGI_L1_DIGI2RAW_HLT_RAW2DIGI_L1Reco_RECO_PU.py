# Auto generated configuration fileimport FWCore.Parame
# using: 
# Revision: 1.341 
# Source: /cvs/CMSSW/CMSSW/Configuration/PyReleaseValidation/python/ConfigBuilder.py,v 
# with command line options: SingleQuarkGun_cfi.py --step GEN,SIM,DIGI,L1,DIGI2RAW,HLT:GRun,RAW2DIGI,L1Reco,RECO --conditions START44_V10::All --pileup mix_E7TeV_Chamonix2012_50ns_PoissonOOT --datamix NODATAMIXER --eventcontent AODSIM --datatier AODSIM -n 25
import FWCore.ParameterSet.Config as cms

process = cms.Process('HLT')

# import of standard configurations
process.load('Configuration.StandardSequences.Services_cff')
process.load('SimGeneral.HepPDTESSource.pythiapdt_cfi')
process.load('FWCore.MessageService.MessageLogger_cfi')
process.load('Configuration.EventContent.EventContent_cff')
process.load('SimGeneral.MixingModule.mix_E7TeV_Chamonix2012_50ns_PoissonOOT_cfi')
process.load('Configuration.StandardSequences.GeometryDB_cff')
process.load('Configuration.StandardSequences.MagneticField_38T_cff')
process.load('Configuration.StandardSequences.Generator_cff')
process.load('IOMC.EventVertexGenerators.VtxSmearedRealistic7TeV2011Collision_cfi')
process.load('GeneratorInterface.Core.genFilterSummary_cff')
process.load('Configuration.StandardSequences.SimIdeal_cff')
process.load('Configuration.StandardSequences.Digi_cff')
process.load('Configuration.StandardSequences.SimL1Emulator_cff')
process.load('Configuration.StandardSequences.DigiToRaw_cff')
process.load('HLTrigger.Configuration.HLT_GRun_cff')
process.load('Configuration.StandardSequences.RawToDigi_cff')
process.load('Configuration.StandardSequences.L1Reco_cff')
process.load('Configuration.StandardSequences.Reconstruction_cff')
process.load('Configuration.StandardSequences.EndOfProcess_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')

from CMG.JetIDAnalysis.minBiasSource_cfg import FileNames as FullMinBiasFileNames
process.mix.input.fileNames = FullMinBiasFileNames
process.mix.input.fileNames = cms.untracked.vstring('/store/relval/CMSSW_4_4_2_patch7/RelValMinBias/GEN-SIM-DIGI-RAW-HLTDEBUG/START44_V9_special_111126-v1/0072/269DF920-8118-E111-945D-003048FFD76E.root',
						    '/store/relval/CMSSW_4_4_2_patch7/RelValMinBias/GEN-SIM-DIGI-RAW-HLTDEBUG/START44_V9_special_111126-v1/0072/2E28D79F-8218-E111-9E38-003048679084.root',
						    '/store/relval/CMSSW_4_4_2_patch7/RelValMinBias/GEN-SIM-DIGI-RAW-HLTDEBUG/START44_V9_special_111126-v1/0072/5C4758B3-C818-E111-92FC-003048678FFA.root',
						    '/store/relval/CMSSW_4_4_2_patch7/RelValMinBias/GEN-SIM-DIGI-RAW-HLTDEBUG/START44_V9_special_111126-v1/0071/4466B2D8-6518-E111-A761-0026189438FD.root')
#print "Hey: random seed is", process.RandomNumberGeneratorService.generator.initialSeed
import random
random.seed(process.RandomNumberGeneratorService.generator.initialSeed.value())
random.shuffle(process.mix.input.fileNames)
flist=open('list_of_pu.txt','w+')
print >> flist, process.mix.input.fileNames
flist.close()

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(25)
)

# Input source
process.source = cms.Source("EmptySource")

process.options = cms.untracked.PSet(

)

# Production Info
process.configurationMetadata = cms.untracked.PSet(
    version = cms.untracked.string('$Revision: 1.3 $'),
    annotation = cms.untracked.string('SingleQuarkGun_cfi.py nevts:25'),
    name = cms.untracked.string('PyReleaseValidation')
)

# Output definition

process.AODSIMoutput = cms.OutputModule("PoolOutputModule",
    eventAutoFlushCompressedSize = cms.untracked.int32(15728640),
    outputCommands = process.AODSIMEventContent.outputCommands,
    fileName = cms.untracked.string('SingleQuarkGun_cfi_py_GEN_SIM_DIGI_L1_DIGI2RAW_HLT_RAW2DIGI_L1Reco_RECO_PU.root'),
    dataset = cms.untracked.PSet(
        filterName = cms.untracked.string(''),
        dataTier = cms.untracked.string('AODSIM')
    ),
    SelectEvents = cms.untracked.PSet(
        SelectEvents = cms.vstring('generation_step')
    )
)

PFAOD = ['drop recoCaloTau*_*_*_*',
	'drop recoPFTau*_*_*_*',
	'drop recoCaloJet*_*_*_*',
	'drop recoPFJet*_*_*_*',
	'drop recoJPTJets_*_*_*',
	'drop recoTrackJets_*_*_*',
	'drop recoJetIDedmValueMap_*_*_*',
	'drop recoConversions_*_*_*',
	'drop recoJetedmRefToBaseProdTofloatsAssociationVector_*_*_*',
	'drop recoPreshowerClusters_*_*_*',
	'drop recoMETs_*_*_*',
	'drop recoPFMETs_*_*_*',
	'drop recoCaloMETs_*_*_*',
	# caloMET can always be useful for understanding fake MET
	'keep recoCaloMETs_corMetGlobalMuons_*_*',
	'drop *_genMetCalo_*_*',
	'drop *_genMetCaloAndNonPrompt_*_*',
	'drop *_tevMuons_*_*',
	'drop *_generalV0Candidates_*_*',
	'drop *_*TracksFromConversions_*_*',
	'drop recoPhoton*_*_*_*',
	'drop *_muIsoDeposit*_*_*',
	'drop recoMuonMETCorrectionDataedmValueMap_*_*_*',
	'drop *_*JetTracksAssociator*_*_*',
	'drop *_*JetExtender_*_*',
	'drop recoSoftLeptonTagInfos_*_*_*',
	'drop *_impactParameterTagInfos_*_*',
	'drop *_towerMaker_*_*',
	'drop *_sisCone*_*_*',
	'drop *_PhotonIDProd_*_*',
	'drop recoHFEMClusterShapes_*_*_*',
	'drop recoCaloClustersToOnereco*_*_*_*',
	'drop EcalRecHitsSorted_*_*_*',
	# the next 2 are needed for fake MET event cleaning (RA2 filters)
	'keep EcalRecHitsSorted_reducedEcalRecHitsEB_*_*',
	'keep EcalRecHitsSorted_reducedEcalRecHitsEE_*_*',
	# 'keep EcalTriggerPrimitiveDigisSorted_ecalTPSkim_*_*',
	'drop recoCaloClusters_*_*_*',
	# needed somewhere in PAT. and could be useful in the future.
	#        'drop *_softPFElectrons_*_*',
	'drop *_particleFlow_electrons_*',
	'drop recoPreshowerClusterShapes_*_*_*',
	# needed in PAT by allLayer1Electrons - dunno why:
	#        'drop *_gsfElectronCores_*_*',
	'drop *_hfRecoEcalCandidate_*_*',
	'drop recoSuperClusters_*_*_*',
	'keep *_pfElectronTranslator_*_*',
	'keep recoSuperClusters_corrected*_*_*',
	'keep *_TriggerResults_*_*',
	'keep *_hltTriggerSummaryAOD_*_*',
	'keep *_lumiProducer_*_*'
	]
PFAOD.extend( [ 'drop *Castor*_*_*_*',
		'keep recoCaloClusters_hybridSuperClusters_hybridBarrelBasicClusters_*',
		'keep recoCaloClusters_multi5x5BasicClusters_multi5x5EndcapBasicClusters_*',
		'keep recoCaloClusters_hybridSuperClusters_uncleanOnlyHybridBarrelBasicClusters_*',
		'keep recoSuperClusters_hybridSuperClusters_uncleanOnlyHybridSuperClusters_*',
		'keep recoCaloClusters_pfPhotonTranslator_pfphot_*',
		'keep recoTracks_tevMuons_default_*',
		'keep recoTracks_tevMuons_dyt_*',
		'keep recoTracks_tevMuons_firstHit_*',
		'keep recoTracks_tevMuons_picky_*',
		'keep recoTrackExtras_tevMuons_default_*',
		'keep recoTrackExtras_tevMuons_dyt_*',
		'keep recoTrackExtras_tevMuons_firstHit_*',
		'keep recoTrackExtras_tevMuons_picky_*',
		'keep recoTracksToOnerecoTracksAssociation_tevMuons_default_*',
		'keep recoTracksToOnerecoTracksAssociation_tevMuons_dyt_*',
		'keep recoTracksToOnerecoTracksAssociation_tevMuons_firstHit_*',
		'keep recoTracksToOnerecoTracksAssociation_tevMuons_picky_*',
		'keep *_ak7CaloJets_*_*',
		'keep recoPhotonCores_photonCore__*',
		'keep recoPhotons_pfPhotonTranslator_pfphot_*',
		'keep recoPhotons_photons__*',
		'keep booledmValueMap_PhotonIDProd_PhotonCutBasedIDLoose_*',
		'keep booledmValueMap_PhotonIDProd_PhotonCutBasedIDLooseEM_*',
		'keep booledmValueMap_PhotonIDProd_PhotonCutBasedIDTight_*',
		'keep recoPreshowerClusters_pfPhotonTranslator_pfphot_*',
		'keep recoSuperClusters_pfPhotonTranslator_pfphot_*',
		]
	      )
process.AODSIMoutput.outputCommands.extend(PFAOD)


# Additional output definition

# Other statements
process.GlobalTag.globaltag = 'START44_V10::All'

process.generator = cms.EDProducer("Pythia6PtGun",
    PGunParameters = cms.PSet(
        MinPhi = cms.double(-3.14159265359),
        MinPt = cms.double(5.0),
        ParticleID = cms.vint32(1),
        MaxEta = cms.double(5),
        MaxPhi = cms.double(3.14159265359),
        MinEta = cms.double(-5),
        AddAntiParticle = cms.bool(False),
        MaxPt = cms.double(300)
    ),
    Verbosity = cms.untracked.int32(0),
    psethack = cms.string('single quark pt 15-300'),
    firstRun = cms.untracked.uint32(1),
    PythiaParameters = cms.PSet(
        pythiaUESettings = cms.vstring('MSTU(21)=1     ! Check on possible errors during program execution', 
            'MSTJ(22)=2     ! Decay those unstable particles', 
            'PARJ(71)=10 .  ! for which ctau  10 mm', 
            'MSTP(33)=0     ! no K factors in hard cross sections', 
            'MSTP(2)=1      ! which order running alphaS', 
            'MSTP(51)=10042 ! structure function chosen (external PDF CTEQ6L1)', 
            'MSTP(52)=2     ! work with LHAPDF', 
            'PARP(82)=1.832 ! pt cutoff for multiparton interactions', 
            'PARP(89)=1800. ! sqrts for which PARP82 is set', 
            'PARP(90)=0.275 ! Multiple interactions: rescaling power', 
            'MSTP(95)=6     ! CR (color reconnection parameters)', 
            'PARP(77)=1.016 ! CR', 
            'PARP(78)=0.538 ! CR', 
            'PARP(80)=0.1   ! Prob. colored parton from BBR', 
            'PARP(83)=0.356 ! Multiple interactions: matter distribution parameter', 
            'PARP(84)=0.651 ! Multiple interactions: matter distribution parameter', 
            'PARP(62)=1.025 ! ISR cutoff', 
            'MSTP(91)=1     ! Gaussian primordial kT', 
            'PARP(93)=10.0  ! primordial kT-max', 
            'MSTP(81)=21    ! multiple parton interactions 1 is Pythia default', 
            'MSTP(82)=4     ! Defines the multi-parton model'),
        parameterSets = cms.vstring('pythiaUESettings')
    )
)


# Path and EndPath definitions
process.generation_step = cms.Path(process.pgen)
process.simulation_step = cms.Path(process.psim)
process.digitisation_step = cms.Path(process.pdigi)
process.L1simulation_step = cms.Path(process.SimL1Emulator)
process.digi2raw_step = cms.Path(process.DigiToRaw)
process.raw2digi_step = cms.Path(process.RawToDigi)
process.L1Reco_step = cms.Path(process.L1Reco)
process.reconstruction_step = cms.Path(process.reconstruction)
process.genfiltersummary_step = cms.EndPath(process.genFilterSummary)
process.endjob_step = cms.EndPath(process.endOfProcess)
process.AODSIMoutput_step = cms.EndPath(process.AODSIMoutput)

# Schedule definition
process.schedule = cms.Schedule(process.generation_step,process.genfiltersummary_step,process.simulation_step,process.digitisation_step,process.L1simulation_step,process.digi2raw_step)
process.schedule.extend(process.HLTSchedule)
process.schedule.extend([process.raw2digi_step,process.L1Reco_step,process.reconstruction_step,process.endjob_step,process.AODSIMoutput_step])
# filter all path with the production filter sequence
for path in process.paths:
	getattr(process,path)._seq = process.generator * getattr(process,path)._seq 

