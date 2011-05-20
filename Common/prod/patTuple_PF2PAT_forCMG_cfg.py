## import skeleton process
from PhysicsTools.PatAlgos.patTemplate_cfg import *


# process.source.fileNames = cms.untracked.vstring(['/store/relval/CMSSW_4_2_3/RelValZTT/GEN-SIM-RECO/START42_V12-v2/0062/4CEA9C47-287B-E011-BAB7-00261894396B.root'])
process.source.fileNames = cms.untracked.vstring(['file:PFAOD.root'])

runOnMC = True
hpsTaus = True

# process.load("CommonTools.ParticleFlow.Sources.source_ZtoMus_DBS_cfi")
process.options   = cms.untracked.PSet( wantSummary = cms.untracked.bool(False))

process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(100) )
process.out.fileName = cms.untracked.string('patTuple_PF2PAT.root')

# load the PAT config
process.load("PhysicsTools.PatAlgos.patSequences_cff")

# Configure PAT to use PF2PAT instead of AOD sources
# this function will modify the PAT sequences. It is currently 
# not possible to run PF2PAT+PAT and standart PAT at the same time
from PhysicsTools.PatAlgos.tools.pfTools import *

### DEFINITION OF THE PF2PAT+PAT SEQUENCES #############################################

# ---------------- Sequence AK5 ----------------------

# PF2PAT+PAT sequence 1:
# no lepton cleaning, AK5PFJets

postfixAK5 = "AK5"
jetAlgoAK5="AK5"
usePF2PAT(process,runPF2PAT=True, jetAlgo=jetAlgoAK5, runOnMC=runOnMC, postfix=postfixAK5,
          jetCorrections=('AK5PFchs', ['L1FastJet','L2Relative','L3Absolute']))


from CommonTools.ParticleFlow.Tools.enablePileUpCorrection import enablePileUpCorrection
enablePileUpCorrection( process, postfix=postfixAK5)

from CMGTools.Common.PAT.embedPFCandidatesInTaus import embedPFCandidatesInTaus
embedPFCandidatesInTaus( process, postfix=postfixAK5, enable=True )

if hpsTaus:
    adaptPFTaus(process,"hpsPFTau",postfix=postfixAK5)

# curing a weird bug in PAT..
from CMGTools.Common.PAT.removePhotonMatching import removePhotonMatching
removePhotonMatching( process, postfixAK5 )

getattr(process,"pfNoMuon"+postfixAK5).enable = False 
getattr(process,"pfNoElectron"+postfixAK5).enable = False 
getattr(process,"pfNoTau"+postfixAK5).enable = False 
getattr(process,"pfNoJet"+postfixAK5).enable = True


# ---------------- Sequence AK5, lepton x-cleaning ---------------

# PF2PAT+PAT sequence 2:
# lepton cleaning, AK5PFJets. This sequence is a clone of the AK5 sequence defined previously.
# just modifying the x-cleaning parameters, and the isolation cut for x-cleaning

from PhysicsTools.PatAlgos.tools.helpers import cloneProcessingSnippet
postfixLC = 'LC'
# just cloning the first sequence, and enabling lepton cleaning 
cloneProcessingSnippet(process, getattr(process, 'patPF2PATSequence'+postfixAK5), postfixLC)

postfixAK5LC = postfixAK5+postfixLC
getattr(process,"pfNoMuon"+postfixAK5LC).enable = True
getattr(process,"pfNoElectron"+postfixAK5LC).enable = True 
getattr(process,"pfIsolatedMuons"+postfixAK5LC).combinedIsolationCut = 0.2
getattr(process,"pfIsolatedElectrons"+postfixAK5LC).combinedIsolationCut = 0.2

#COLIN : need to add the VBTF e and mu id


# ---------------- Sequence AK7, lepton x-cleaning ---------------

# PF2PAT+PAT sequence 3
# no lepton cleaning, AK7PFJets

postfixAK7 = "AK7"
jetAlgoAK7="AK7"

#COLIN : argh! AK7PFchs does not seem to exist yet...
# Maxime should maybe contact the JEC group if he wants them 
usePF2PAT(process,runPF2PAT=True, jetAlgo=jetAlgoAK7, runOnMC=runOnMC, postfix=postfixAK7,
          jetCorrections=('AK7PF', ['L1FastJet','L2Relative','L3Absolute']))

enablePileUpCorrection( process, postfix=postfixAK7)

# no need for taus in AK7 sequence. could remove the whole tau sequence to gain time?
# if hpsTaus:
#    adaptPFTaus(process,"hpsPFTau",postfix=postfixAK7)

getattr(process,"pfNoMuon"+postfixAK7).enable = False 
getattr(process,"pfNoElectron"+postfixAK7).enable = False 
getattr(process,"pfNoTau"+postfixAK7).enable = False 
getattr(process,"pfNoJet"+postfixAK7).enable = True

removePhotonMatching( process, postfixAK7 )


# ---------------- Common stuff ---------------

process.load('CMGTools.Common.gen_cff')


### PATH DEFINITION #############################################


if runOnMC:
    process.p = cms.Path( process.genSequence )

process.p += getattr(process,"patPF2PATSequence"+postfixAK5)
process.p += getattr(process,"patPF2PATSequence"+postfixAK5LC) 
process.p += getattr(process,"patPF2PATSequence"+postfixAK7) 


# Add PF2PAT output to the created file
from PhysicsTools.PatAlgos.patEventContent_cff import patEventContentNoCleaning
process.out.outputCommands = cms.untracked.vstring('drop *',
                                                   *patEventContentNoCleaning
                                                   )
# add gen event content to the pat-tuple (e.g. status 3 GenParticles)
from CMGTools.Common.eventContent.gen_cff import gen 
process.out.outputCommands.extend( gen )


# stuff kept by PAT, but that we don't need:
process.out.outputCommands.extend(
    [ 'drop *_selectedPatMuonsAK7_*_*',
      'drop *_selectedPatElectronsAK7_*_*',
      'drop *_selectedPatTausAK7_*_*',
      'drop CaloTowers_*_*_*',
      'drop patMETs_*_*_*',
      'keep patMETs_patMETsAK5_*_*',
      'drop patPFParticles_*_*_*'
    ] )



process.MessageLogger.cerr.FwkReport.reportEvery = 10

# process.Timing = cms.Service("Timing")
