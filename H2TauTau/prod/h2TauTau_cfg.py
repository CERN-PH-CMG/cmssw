import FWCore.ParameterSet.Config as cms

# from PhysicsTools.PatAlgos.patTemplate_cfg import *

sep_line = '-'*70
########## CONTROL CARDS

process = cms.Process("H2TAUTAU")


process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(1000) )

process.maxLuminosityBlocks = cms.untracked.PSet(
    input = cms.untracked.int32(-1)
    )

# -1 : process all files
numberOfFilesToProcess = 5

debugEventContent = False

#1=mu-tau, 2=e-tau, 3=e-mu, 4=tau-tau, -1=all
channel = -1
##########



# Input  & JSON             -------------------------------------------------


# process.setName_('H2TAUTAU')

dataset_user = 'cmgtools' 
dataset_name = '/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/Fall11-PU_S6_START42_V14B-v1/AODSIM/V5/PAT_CMG_V5_1_0'
# dataset_name = '/TauPlusX/Run2011A-PromptReco-v4/AOD/V5/PAT_CMG_V5_1_0'

dataset_files = 'cmgTuple.*root'

# creating the source
from CMGTools.Production.datasetToSource import *
process.source = datasetToSource(
    dataset_user,
    dataset_name,
    dataset_files,
    )


#process.source = cms.Source(
#    "PoolSource",
#    fileNames = cms.untracked.vstring(
#    #'/store/cmst3/user/cmgtools/CMG/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/Summer11-PU_S4_START42_V11-v1/AODSIM/V2/PAT_CMG_V2_5_0/tree_CMG_1.root'
#    #'/store/cmst3/user/cmgtools/CMG/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/Summer11-PU_S4_START42_V11-v1/AODSIM/V2/PAT_CMG_V2_5_0/tree_CMG_1.root'
#    'file:../../../Common/prod/TEST/cmgTuple_HToTauTau.root'
#    )
#    )

process.source.fileNames = ['file:DYJets.root']

# restricting the number of files to process to a given number
if numberOfFilesToProcess>0:
    process.source.fileNames = process.source.fileNames[:numberOfFilesToProcess]


###ProductionTaskHook$$$
    
runOnMC = process.source.fileNames[0].find('Run201')==-1 and process.source.fileNames[0].find('embedded')==-1


# Sequence & path definition -------------------------------------------------


# set up JSON ---------------------------------------------------------------
if runOnMC==False:
    from CMGTools.H2TauTau.tools.setupJSON import setupJSON
    json = setupJSON(process)


# generator ----------------------------------------------
process.generatorPath = cms.Path()
if runOnMC:
    # setting up vertex weighting 
    process.load('CMGTools.Common.generator.vertexWeight.vertexWeight_cff')
    process.generatorPath += process.vertexWeightSequence 

    # input needed for all recoil corrections 
    process.load('CMGTools.Common.generator.metRecoilCorrection.metRecoilCorrection_cff')
    process.generatorPath += process.cmgPFJetForRecoil 
    process.generatorPath += process.genWorZ


# load the channel paths -------------------------------------------
process.load('CMGTools.H2TauTau.h2TauTau_cff')

# setting up the recoil correction according to the input file ---------------
print sep_line
from CMGTools.H2TauTau.tools.setupRecoilCorrection import setupRecoilCorrection
setupRecoilCorrection( process )


# OUTPUT definition ----------------------------------------------------------
process.outpath = cms.EndPath()


#Jose: process.schedule doesn't have a += operator?
if channel==-1:
    process.schedule = cms.Schedule(
        process.generatorPath,
        process.tauMuFullSelPath,
        process.tauEleFullSelPath,
        process.muEleFullSelPath,    
        process.diTauFullSelPath,
        process.outpath
        )
elif channel==1:
    process.schedule = cms.Schedule(
        process.generatorPath,
        process.tauMuFullSelPath,
        process.outpath
        )
elif channel==2:
    process.schedule = cms.Schedule(
        process.generatorPath,
        process.tauEleFullSelPath,
        process.outpath
        )
elif channel==3:
    process.schedule = cms.Schedule(
        process.generatorPath,
        process.muEleFullSelPath,
        process.outpath
        )
elif channel==4:
    process.schedule = cms.Schedule(
        process.generatorPath,
        process.diTauFullSelPath,
        process.outpath
        )
else:
    raise ValueError('unrecognized channel')    




# process.tauMuFullSelPath += process.mvaMETSequence
# process.mvaMETTauMu.verbose = True

print sep_line
print 'INPUT:'
print sep_line
print process.source.fileNames
print
if runOnMC==False:
    print 'json:', json
print
print sep_line
print 'PROCESSING'
print sep_line
print 'runOnMC:', runOnMC
print 
print sep_line
print 'OUPUT:'
print sep_line
justn = 30 
# print 'baseline selection EDM output'.ljust(justn), baselineName
# print 'basic selection EDM output'.ljust(justn), basicName
# print 'histograms output'.ljust(justn), histName 
# print 'Debug event content'.ljust(justn), debugEventContent

# you can enable printouts of most modules like this:
# process.cmgTauMuCorPreSelSVFit.verbose = True

# systematic shift on tau energy scale 
# process.cmgTauScaler.cfg.nSigma = -1

from CMGTools.H2TauTau.tools.setupOutput import *
if channel==1 or channel==-1:
    addTauMuOutput( process, debugEventContent, addPreSel=False)
if channel==2 or channel==-1:
    addTauEleOutput( process, debugEventContent, addPreSel=False)
if channel==3 or channel==-1:
    addMuEleOutput( process, debugEventContent, addPreSel=False)
if channel==4 or channel==-1:
    addDiTauOutput( process, debugEventContent, addPreSel=False)




# Message logger setup.
process.load("FWCore.MessageLogger.MessageLogger_cfi")
process.MessageLogger.cerr.FwkReport.reportEvery = 100
process.options = cms.untracked.PSet( wantSummary = cms.untracked.bool(False) )

