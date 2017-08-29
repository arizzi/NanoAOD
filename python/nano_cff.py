import FWCore.ParameterSet.Config as cms
from PhysicsTools.NanoAOD.jets_cff import *
from PhysicsTools.NanoAOD.muons_cff import *
from PhysicsTools.NanoAOD.taus_cff import *
from PhysicsTools.NanoAOD.electrons_cff import *
from PhysicsTools.NanoAOD.photons_cff import *


linkedObjects = cms.EDProducer("PATObjectCrossLinker",
   jets=cms.InputTag("finalJets"),
   muons=cms.InputTag("finalMuons"),
   electrons=cms.InputTag("finalElectrons"),
   taus=cms.InputTag("finalTaus"),
   photons=cms.InputTag("finalPhotons"),
)

nanoSequence = cms.Sequence(muonSequence + jetSequence + tauSequence + electronSequence+photonSequence+
	 linkedObjects +
	 jetTables + muonTables + tauTables + electronTables + photonTables)

