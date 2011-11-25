from PhysicsTools.PatAlgos.patTemplate_cfg import *

sep_line = '-'*70
########## CONTROL CARDS


process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )

process.maxLuminosityBlocks = cms.untracked.PSet(
    input = cms.untracked.int32(-1)
    )

# -1 : process all files
numberOfFilesToProcess = 5

debugEventContent = False

dataset_user = 'cmgtools' 
# dataset_name = '/WJetsToLNu_TuneZ2_7TeV-madgraph-tauola/Summer11-PU_S4_START42_V11-v1/AODSIM/V2/PAT_CMG_V2_3_0'
# dataset_name = '/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/Summer11-PU_S4_START42_V11-v1/AODSIM/V2/PAT_CMG_V2_3_0'
# dataset_name = '/TauPlusX/Run2011A-PromptReco-v4/AOD/V2/PAT_CMG_V2_4_0'
dataset_name = '/TauPlusX/Run2011A-May10ReReco-v1/AOD/V2/PAT_CMG_V2_4_0'
# JSON: will be applied if dataset_name contains the string 'Run201' (data)


##########



# Input  & JSON             -------------------------------------------------


process.setName_('H2TAUTAU')

# creating the source
from CMGTools.Production.datasetToSource import *
process.source = datasetToSource(
    dataset_user,
    dataset_name,
    'tree.*root') 

# restricting the number of files to process to a given number
if numberOfFilesToProcess>0:
    process.source.fileNames = process.source.fileNames[:numberOfFilesToProcess]


###ProductionTaskHook$$$
    

# Sequence & path definition -------------------------------------------------

process.load('CMGTools.H2TauTau.h2TauTau_cff')


process.schedule = cms.Schedule(
    # this path corresponds to the basic preselection:
    process.tauMuPreSelPath,
    # and this one to the full baseline selection
    process.tauMuFullSelPath,    
    process.outpath
    )


json = None
if dataset_name.find('Run201')>-1:
    #DATA
    # attach JSON mask to the source if reading a data file
    from CMGTools.Common.Tools.applyJSON_cff import *
    from CMGTools.H2TauTau.tools.jsonPick import *
    # json = '/afs/cern.ch/cms/CAF/CMSCOMM/COMM_DQM/certification/Collisions11/7TeV/Prompt/Cert_160404-178078_7TeV_PromptReco_Collisions11_JSON.txt'
    json = jsonPick( dataset_name )
    applyJSON(process, json )
else:
    #SIMULATION
    process.load('CMGTools.Common.generator.vertexWeight.vertexWeight_cff')
    process.objectSequence += process.vertexWeightSequence

# setting up the recoil correction according to the input file ---------------

print sep_line
from CMGTools.H2TauTau.tools.setupRecoilCorrection import setupRecoilCorrection
setupRecoilCorrection( process )

# OUTPUT definition ----------------------------------------------------------


# skim (basic selection)     ------

outFileNameExt = 'CMG'
basicName = 'h2TauTau_presel_tree_%s.root' %  outFileNameExt
process.out.fileName = cms.untracked.string( basicName )
from CMGTools.H2TauTau.eventContent.tauMu_cff import tauMu as tauMuEventContent
from CMGTools.H2TauTau.eventContent.tauMu_cff import tauMuDebug as tauMuDebugEventContent
if debugEventContent:
    process.out.outputCommands.extend( tauMuDebugEventContent )
else:
    process.out.outputCommands.extend( tauMuEventContent )
process.out.SelectEvents = cms.untracked.PSet( SelectEvents = cms.vstring('tauMuPreSelPath') )


# full baseline selection    ------

process.outBaseline = process.out.clone()
process.outBaseline.SelectEvents = cms.untracked.PSet( SelectEvents = cms.vstring('tauMuFullSelPath') )
baselineName = 'h2TauTau_fullsel_tree_%s.root' % outFileNameExt
process.outBaseline.fileName = baselineName

process.outpath += process.outBaseline

# Message logger setup.
process.MessageLogger.cerr.FwkReport.reportEvery = 100
process.options = cms.untracked.PSet( wantSummary = cms.untracked.bool(True) )




# histograms                 ------

histName = "h2TauTau_histograms_%s.root" %  outFileNameExt
process.TFileService = cms.Service(
    "TFileService",
    fileName = cms.string( histName )
    )


print sep_line
print 'INPUT:'
print sep_line
print process.source.fileNames
if json != None:
    print 'JSON:', json
print
print sep_line
print 'OUPUT:'
print sep_line
justn = 30 
print 'baseline selection EDM output'.ljust(justn), baselineName
print 'basic selection EDM output'.ljust(justn), basicName
print 'histograms output'.ljust(justn), histName 
print 'Debug event content'.ljust(justn), debugEventContent

# you can enable printouts of most modules like this:
# process.cmgTauMuCorPreSelSVFit.verbose = True

# process.cmgTauScaler.cfg.nSigma = -1
