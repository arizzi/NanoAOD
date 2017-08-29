import FWCore.ParameterSet.Config as cms
from PhysicsTools.NanoAOD.common_cff import *

finalPhotons = cms.EDFilter("PATPhotonRefSelector",
    src = cms.InputTag("slimmedPhotons"),
    cut = cms.string("pt > 5 ")
)

photonTable = cms.EDProducer("SimpleCandidateFlatTableProducer",
    src = cms.InputTag("linkedObjects","photons"),
    cut = cms.string("1"), #we should not filter on cross linked collections
    name= cms.string("Photon"),
    floats = cms.PSet(P4Floats, jetPt = cms.string("?hasUserCand('jet')?userCand('jet').pt():-1")),
    ints = cms.PSet(CandInts,  jet = cms.string("?hasUserCand('jet')?userCand('jet').key():-1")),
    bools = cms.PSet()
)

photonSequence = cms.Sequence(finalPhotons)
photonTables = cms.Sequence ( photonTable)

