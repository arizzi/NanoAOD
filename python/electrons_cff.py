import FWCore.ParameterSet.Config as cms
from PhysicsTools.NanoAOD.common_cff import *

finalElectrons = cms.EDFilter("PATElectronRefSelector",
    src = cms.InputTag("slimmedElectrons"),
    cut = cms.string("pt > 5 ")
)

electronTable = cms.EDProducer("SimpleCandidateFlatTableProducer",
    src = cms.InputTag("linkedObjects","electrons"),
    cut = cms.string("1"), #we should not filter on cross linked collections
    name= cms.string("Electron"),
    floats = cms.PSet(P4Floats, dxy = cms.string("dB"), jetPt = cms.string("?hasUserCand('jet')?userCand('jet').pt():-1")),
    ints = cms.PSet(CandInts,  jet = cms.string("?hasUserCand('jet')?userCand('jet').key():-1")),
    bools = cms.PSet()
)

electronSequence = cms.Sequence(finalElectrons)
electronTables = cms.Sequence ( electronTable)

