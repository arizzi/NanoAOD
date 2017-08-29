import FWCore.ParameterSet.Config as cms
from  PhysicsTools.NanoAOD.common_cff import *



##################### User floats producers, selectors ##########################


finalTaus = cms.EDFilter("PATTauRefSelector",
    src = cms.InputTag("slimmedTaus"),
    cut = cms.string("pt > 15")
)

##################### Tables for final output and docs ##########################
tauTable = cms.EDProducer("SimpleCandidateFlatTableProducer",
    src = cms.InputTag("linkedObjects","taus"),
    cut = cms.string("1"), #we should not filter on cross linked collections
    name= cms.string("Tau"),
    floats = cms.PSet(
                P4Floats, #common P4: pt,eta,phi,mass
		jetArea = cms.string("?hasUserCand('jet')?userCand('jet').jetArea:-1")
    ),
    ints = cms.PSet(
	 jet = cms.string("?hasUserCand('jet')?userCand('jet').key():-1")
    ),
)

tauSequence = cms.Sequence(finalTaus)
tauTables = cms.Sequence( tauTable )

