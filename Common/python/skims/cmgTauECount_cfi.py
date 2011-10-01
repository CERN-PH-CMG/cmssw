import FWCore.ParameterSet.Config as cms

# do not rely on the default cuts implemented here,
# as they are subject to change. 
# you should override these cuts in your analysis.

cmgTauECount = cms.EDFilter(
    "CandViewCountFilter",
    src = cms.InputTag("cmgTauESel"),
    minNumber = cms.uint32(0),
    )


