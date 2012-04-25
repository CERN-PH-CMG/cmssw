import FWCore.ParameterSet.Config as cms
from CMGTools.External.JetIdParams_cfi import *

####################################################################################################################  
full = cms.PSet(
 impactParTkThreshold = cms.double(1.) ,
 tmvaWeights = cms.string("CMGTools/External/data/TMVAClassification_PuJetIdOptMVA.weights.xml"),
 tmvaMethod  = cms.string("PuJetIdOptMVA"),
 version = cms.int32(-1),
 tmvaVariables = cms.vstring(
    "frac01",
    "frac02",
    "frac03",
    "frac04",
    "frac05",
    "nvtx",
    "nNeutrals",
    "beta",
    "betaStar",
    "dZ",
    "nCharged",
    ),
 tmvaSpectators = cms.vstring(
    "jetPt",
    "jetEta",
    ),
 JetIdParams = PuJetIdOptMVA_wp,
 label = cms.string("full")
 )

####################################################################################################################  
simple = cms.PSet( 
 impactParTkThreshold = cms.double(1.) ,
 tmvaWeights = cms.string("CMGTools/External/data/TMVAClassification_PuJetIdMinMVA.weights.xml"),
 tmvaMethod  = cms.string("PuJetIdMinMVA"),
 version = cms.int32(-1),
 tmvaVariables = cms.vstring(
    "frac01",
    "frac02",
    "frac03",
    "frac04",
    "frac05",
    "beta",
    "betaStar",
    ),
 tmvaSpectators = cms.vstring(
    "nvtx",
    "jetPt",
    "jetEta",
    ),
 JetIdParams = PuJetIdMinMVA_wp,
 label = cms.string("simple")
 )

####################################################################################################################  
PhilV0 = cms.PSet( 
 impactParTkThreshold = cms.double(1.) ,
 tmvaWeights = cms.string("CMGTools/External/data/mva_JetID.weights.xml"),
 tmvaMethod  = cms.string("JetID"),
 version = cms.int32(0),
 JetIdParams = EmptyJetIdParams
)


####################################################################################################################  
PhilV1 = cms.PSet(
 impactParTkThreshold = cms.double(1.) ,
 tmvaWeights = cms.string("CMGTools/External/data/mva_JetID_v1.weights.xml"),
 tmvaMethod  = cms.string("JetID"),
 version = cms.int32(-1),
 tmvaVariables = cms.vstring(
    "nvtx",
    "jetPt",
    "jetEta",
    "jetPhi",
    "dZ",
    "d0",
    "beta",
    "betaStar",
    "nCharged",
    "nNeutrals",
    "dRMean",
    "frac01",
    "frac02",
    "frac03",
    "frac04",
    "frac05",
    ),
 tmvaSpectators = cms.vstring(),
 JetIdParams = JetIdParams,
 label = cms.string("philv1")
 )

