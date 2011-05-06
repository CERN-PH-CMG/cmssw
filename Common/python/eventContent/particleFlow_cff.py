import FWCore.ParameterSet.Config as cms


particleFlowJets = cms.untracked.vstring(
    'keep *_cmgPFJetSel_*_*',
    'keep *_cmgPFBaseJetSel_*_*',
    'keep cmgAbstractPhysicsObjects_*PF*Jet*_*_*'
    # here add all PF jet objects, even the base ones. 
    )

particleFlowMET = cms.untracked.vstring(
    'keep  *_cmgPFMET_*_*',                                    
    # 'keep  *_cmgMETPFCandidates*_*_*',
    # here add the other PF-based MET objects, even the base ones. 
    )

# to be added to the output module if needed
particleFlowMHT = cms.untracked.vstring(
    'keep  *_cmgMHTPFJet30_*_*'
    )

particleFlowMuons = cms.untracked.vstring(
    # does not look like PF?     
    'keep *_cmgMuonSel_*_*',
    'keep *_cmgDiMuonSel_*_*'
    )

particleFlowTaus = cms.untracked.vstring(
    # does not look like PF?     
    'keep *_cmgTauSel_*_*',
    'keep *_cmgDiTauSel_*_*'
    )

particleFlowElectrons = cms.untracked.vstring(
    # does not look like PF? 
    'keep *_cmgElectronSel_*_*',
    'keep *_cmgDiElectronSel_*_*'
    )

particleFlowPhotons = cms.untracked.vstring(
    # does not look like PF? 
    'keep *_cmgPhotonSel_*_*',
    'keep *_cmgDiPhotonSel_*_*'
    )

particleFlowW = cms.untracked.vstring(
    # does not look like PF? 
    'keep *_cmgWENuSel_*_*',
    'keep *_cmgWMuNuSel_*_*',
    'keep *_cmgWTauNu_*_*'                                  
    )

particleFlowVBF = cms.untracked.vstring(
    'keep *_vbfEventJetJetPF_*_*'                                 
    )

particleFlowHemispheres = cms.untracked.vstring(
    'keep *_cmgHemi_*_*',
    'keep *_cmgDiHemi_*_*',
    )

particleFlow = particleFlowJets + particleFlowMET + particleFlowMuons + particleFlowTaus + particleFlowElectrons + particleFlowPhotons + particleFlowW + particleFlowVBF + particleFlowHemispheres


particleFlowBase = cms.untracked.vstring(
    'keep *_cmgPFBaseJetSel_*_*',
    # here add the other generic PF objects
    )
