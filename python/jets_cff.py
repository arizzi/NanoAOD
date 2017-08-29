import FWCore.ParameterSet.Config as cms
from  PhysicsTools.NanoAOD.common_cff import *



##################### User floats producers, selectors ##########################


finalJets = cms.EDFilter("PATJetRefSelector",
    src = cms.InputTag("slimmedJets"),
    cut = cms.string("pt > 15")
)

##################### Tables for final output and docs ##########################
jetTable = cms.EDProducer("SimpleCandidateFlatTableProducer",
    src = cms.InputTag("linkedObjects","jets"),
    cut = cms.string("1"), #we should not filter on cross linked collections
    name= cms.string("Jet"),
    floats = cms.PSet(
                P4Floats, #common P4: pt,eta,phi,mass
		area = cms.string("jetArea()")
    ),
    ints = cms.PSet(
		nMuonsInJet = cms.string("?hasOverlaps('muons')?overlaps('muons').size():0")
    ),
)

jetSequence = cms.Sequence(finalJets)
jetTables = cms.Sequence( jetTable )

