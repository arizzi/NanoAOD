import FWCore.ParameterSet.Config as cms
from PhysicsTools.NanoAOD.common_cff import *

finalMuons = cms.EDFilter("PATMuonRefSelector",
    src = cms.InputTag("slimmedMuons"),
    cut = cms.string("pt > 5 && track.isNonnull && (isGlobalMuon || isTrackerMuon) && isPFMuon")
)

muonTable = cms.EDProducer("SimpleCandidateFlatTableProducer",
    src = cms.InputTag("linkedObjects","muons"),
    cut = cms.string("1"), #we should not filter on cross linked collections
    name= cms.string("Muon"),
    floats = cms.PSet(P4Floats, dxy = cms.string("dB"), jetPt = cms.string("?hasUserCand('jet')?userCand('jet').pt():-1")),
    ints = cms.PSet(CandInts, nStations = cms.string("numberOfMatchedStations"), jet = cms.string("?hasUserCand('jet')?userCand('jet').key():-1")),
    bools = cms.PSet(mediumId = cms.string("isPFMuon && innerTrack.validFraction >= 0.49 && ( isGlobalMuon && globalTrack.normalizedChi2 < 3 && combinedQuality.chi2LocalPosition < 12 && combinedQuality.trkKink < 20 && segmentCompatibility >= 0.303 || segmentCompatibility >= 0.451 )")),
)

muonSequence = cms.Sequence(finalMuons)
muonTables = cms.Sequence ( muonTable)

