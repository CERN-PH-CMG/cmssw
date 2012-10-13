import FWCore.ParameterSet.Config as cms

from CMGTools.Common.Tools.cmsswRelease import isNewerThan


runOnMC      = False
runOld5XGT = False
runOnFastSim = False

process = cms.Process("CMG")

from CMGTools.Production.datasetToSource import *
process.source = datasetToSource(
    'cmgtools',
    '/DoubleMu/Run2011A-16Jan2012-v1/AOD/V5/PAT_CMG_V5_9_0'
   )

#process.source.fileNames = cms.untracked.vstring('file:cmgTuplePreskim.root')

## Maximal Number of Events
process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(10000) )

print 'loading the main CMG sequence'

process.load('CMGTools.Common.PAT.PATCMG_cff')

process.skim=cms.EDFilter('HZZCMGSkim',
                          nLeptons = cms.int32(3)
                          )


process.correctedMuons = cms.EDProducer('RochesterPATMuonCorrector',
             src = cms.InputTag("patMuonsWithTrigger"))

process.cleanedMuons = cms.EDProducer('PATMuonCleanerBySegments',
             src = cms.InputTag("correctedMuons"),
             preselection = cms.string("track.isNonnull"),
             passthrough = cms.string("isGlobalMuon && numberOfMatches >= 2"),
             fractionOfSharedSegments = cms.double(0.499))


process.cmgMuon.cfg.inputCollection = 'cleanedMuons'


process.patElectronsWithRegression = cms.EDProducer("RegressionEnergyPatElectronProducer",
                         debug = cms.untracked.bool(False),
                         inputPatElectronsTag = cms.InputTag('patElectronsWithTrigger'),
                         regressionInputFile = cms.string("EGamma/EGammaAnalysisTools/data/eleEnergyRegWeights_V1.root"),
                         energyRegressionType = cms.uint32(1),
                         rhoCollection = cms.InputTag('kt6PFJets:rho'),
                         vertexCollection = cms.InputTag('offlinePrimaryVertices')
)

process.calibratedPatElectrons = cms.EDProducer("CalibratedPatElectronProducer",
                                            inputPatElectronsTag = cms.InputTag("patElectronsWithRegression"),
                                            isMC = cms.bool(False),
                                            updateEnergyError = cms.bool(True),
                                            isAOD = cms.bool(False),
                                            debug = cms.bool(False),
                                            applyCorrections = cms.int32(1),
                                            inputDataset = cms.string("Jan16ReReco"),
                                            )

process.cmgElectron.cfg.inputCollection = 'calibratedPatElectrons'

process.p = cms.Path(process.correctedMuons+process.cleanedMuons+process.cmgMuon+process.skim)

########################################################
## CMG output definition
########################################################

process.outcmg = cms.OutputModule(
    "PoolOutputModule",
    fileName = cms.untracked.string('cmgTuple.root'),
    SelectEvents   = cms.untracked.PSet( SelectEvents = cms.vstring('p') ),
    outputCommands = cms.untracked.vstring(
    'keep *_*_*_*',
    'drop *_cmgPFBaseJetLeadCHS_*_*',
    'drop *_cmgDiElectronSel_*_*',
    'drop *_cmgDiMuonSel_*_*',
    'drop *_cmgPFJetLooseJetIdFailed_*_*',
    'drop *_cmgPFJetMediumJetIdFailed_*_*',
    'drop *_cmgPFJetSelCHS_*_*',
    "drop *_cmgPFJetTightJetIdFailed_*_*" , 
    "drop *_cmgPFJetVeryLooseJetId95Failed_*_*", 
    "drop *_cmgPFJetVeryLooseJetId95gammaFailed_*_*", 
    "drop *_cmgPFJetVeryLooseJetId95h0Failed_*_*",  
    "drop *_cmgPFJetVeryLooseJetId99Failed_*_*",  
    "drop *_cmgStructuredPFJetSel_*_*",         
    "drop *_cmgTauSel_*_*",                     
    "drop *_cmgMuonSel_*_PAT",                     
    "drop *_patMuonsWithTrigger_*_PAT",                     
    "drop *_cmgMuon_*_CMG",                     
    "drop *_correctedMuons_*_CMG",                     
    "drop *_tauGenJetsSelectorAllHadrons_*_*"
    ),
    dropMetaData = cms.untracked.string('PRIOR')
    )

process.outpath = cms.EndPath(process.outcmg)




########################################################
## Conditions 
########################################################

process.load("Configuration.StandardSequences.GeometryDB_cff")
process.load("Configuration.StandardSequences.FrontierConditions_GlobalTag_cff")
process.load("Configuration.StandardSequences.MagneticField_38T_cff")

from CMGTools.Common.Tools.getGlobalTag import getGlobalTag

process.GlobalTag.globaltag = getGlobalTag( runOnMC,runOld5XGT)
print 'Global tag       : ', process.GlobalTag.globaltag

########################################################
## Below, stuff that you probably don't want to modify
########################################################

## MessageLogger
process.load("FWCore.MessageLogger.MessageLogger_cfi")
process.MessageLogger.cerr.FwkReport.reportEvery = 10

## Options and Output Report
process.options   = cms.untracked.PSet( wantSummary = cms.untracked.bool(True) )

print 'starting CMSSW'

