import FWCore.ParameterSet.Config as cms
#from PhysicsTools.SelectorUtils.pfJetIDSelector_cfi import pfJetIDSelector
#from CMGTools.External.pujetidproducer_cfi import stdalgos, chsalgos

ggNtuplizer = cms.EDAnalyzer("ggNtuplizer",
                 doGenParticles            = cms.bool(True),
                 doGenJets                 = cms.bool(True),
                 runOnParticleGun          = cms.bool(False),
                 runOnSherpa               = cms.bool(False),
                 dumpPFPhotons             = cms.bool(False),
                 dumpJets                  = cms.bool(False),
                 dumpAK8Jets               = cms.bool(False),
                 dumpSoftDrop              = cms.bool(True),
                 dumpTaus                  = cms.bool(True),
                 dumpPDFSystWeight         = cms.bool(False),
                 dumpHFElectrons           = cms.bool(False),
                 development               = cms.bool(False),
                 addFilterInfoAOD          = cms.bool(True),
                 addFilterInfoMINIAOD      = cms.bool(True),
                 doNoHFMET                 = cms.bool(False),
                 getECALprefiringWeights   = cms.bool(False),

                 doTrks                    = cms.bool(True),
                 doOOTphotons              = cms.bool(True),

                 year                      = cms.int32(2017),

                 trgFilterDeltaPtCut       = cms.double(0.5),
                 trgFilterDeltaRCut        = cms.double(0.3),

                 beamHaloSummary           = cms.InputTag("BeamHaloSummary"),

                 triggerEvent              = cms.InputTag("slimmedPatTrigger", "", ""),
                 triggerResults            = cms.InputTag("TriggerResults", "", "HLT"),
                 patTriggerResults         = cms.InputTag("TriggerResults", "", "PAT"),
                 #patTriggerResults        = cms.InputTag("TriggerResults", "", "RECO"),
                 genParticleSrc            = cms.InputTag("prunedGenParticles"),
                 generatorLabel            = cms.InputTag("generator"),
                 LHEEventLabel             = cms.InputTag("externalLHEProducer"),
                 newParticles              = cms.vint32(1000006, 1000021, 1000022, 1000024, 1000025, 1000039, 3000001, 3000002, 35),
                 pileupCollection          = cms.InputTag("slimmedAddPileupInfo"),
                 VtxLabel                  = cms.InputTag("offlineSlimmedPrimaryVertices"),
                 VtxBSLabel                = cms.InputTag("offlinePrimaryVerticesWithBS"),
                 rhoLabel                  = cms.InputTag("fixedGridRhoFastjetAll"),
                 rhoCentralLabel           = cms.InputTag("fixedGridRhoFastjetCentralNeutral"),
                 pfMETLabel                = cms.InputTag("slimmedMETs"),
                 electronSrc               = cms.InputTag("slimmedElectrons"),
                 
                 calibelectronSrc          = cms.InputTag("slimmedElectrons"),
                 photonSrc                 = cms.InputTag("slimmedPhotons"),
                 photonOOTSrc              = cms.InputTag("slimmedOOTPhotons"),
                 
                 calibphotonSrc            = cms.InputTag("slimmedPhotons"),
                 muonSrc                   = cms.InputTag("slimmedMuons"),
                 gsfTrackSrc               = cms.InputTag("reducedEgamma", "reducedGsfTracks"),
                 ebReducedRecHitCollection = cms.InputTag("reducedEgamma", "reducedEBRecHits"),
                 eeReducedRecHitCollection = cms.InputTag("reducedEgamma", "reducedEERecHits"),
                 esReducedRecHitCollection = cms.InputTag("reducedEgamma", "reducedESRecHits"),
                 ecalSCcollection          = cms.InputTag("reducedEgamma", "reducedSuperClusters"),
                 ecalSCOOTcollection       = cms.InputTag("reducedEgamma", "reducedOOTSuperClusters"),
                 recoPhotonSrc             = cms.InputTag("reducedEgamma", "reducedGedPhotonCores"),
                 TrackLabel                = cms.InputTag("generalTracks"),
                 gsfElectronLabel          = cms.InputTag("gsfElectrons"),
                 PFAllCandidates           = cms.InputTag("particleFlow"),
                 
                 ak4PFJetsCHSSrc           = cms.InputTag("slimmedJets"),
                 ak4PFJetsPUPPISrc         = cms.InputTag("slimmedJetsPuppi"),
                 ak4PFJetsCHSGenJetLabel   = cms.InputTag("slimmedGenJets"),
                 ak8GenJetLabel            = cms.InputTag("slimmedGenJetsAK8"),
                 ak8JetsPUPPISrc           = cms.InputTag("slimmedJetsAK8"),
                 tauSrc                    = cms.InputTag("slimmedTaus"),
                 isoTrkSrc                 = cms.InputTag("isolatedTracks", "", "PAT"),
                 packedPFCands             = cms.InputTag("packedPFCandidates"),
                 elePFClusEcalIsoProducer  = cms.InputTag("electronEcalPFClusterIsolationProducer"),
                 elePFClusHcalIsoProducer  = cms.InputTag("electronHcalPFClusterIsolationProducer"),
                 BadChargedCandidateFilter = cms.InputTag("BadChargedCandidateFilter"),
                 BadPFMuonFilter           = cms.InputTag("BadPFMuonFilter"),

                 convPhotonTag             = cms.InputTag("reducedEgamma","reducedConversions"),
                 convPhotonTagSL           = cms.InputTag("reducedEgamma","reducedSingleLegConversions"),

                 offlineBeamSpot = cms.InputTag("offlineBeamSpot"),
                             #new reso: from here: https://github.com/cms-analysis/flashgg/blob/dev_legacy_runII/MicroAOD/python/flashggDiPhotons_cfi.py
                             sigma1Pix               = cms.double(0.0125255),
                             sigma1Tib               = cms.double(0.716301),
                             sigma1Tob               = cms.double(3.17615),
                             sigma1PixFwd            = cms.double(0.0581667),
                             sigma1Tid               = cms.double(0.38521),
                             sigma1Tec               = cms.double(1.67937),
                             sigma2Pix               = cms.double(0.0298574),
                             sigma2Tib               = cms.double(0.414393),
                             sigma2Tob               = cms.double(1.06805),
                             sigma2PixFwd            = cms.double(0.180419),
                             sigma2Tid               = cms.double(0.494722),
                             sigma2Tec               = cms.double(1.21941),
                             singlelegsigma1Pix      = cms.double(0.0178107),
                             singlelegsigma1Tib      = cms.double(1.3188),
                             singlelegsigma1Tob      = cms.double(2.23662),
                             singlelegsigma1PixFwd   = cms.double(0.152157),
                             singlelegsigma1Tid      = cms.double(0.702755),
                             singlelegsigma1Tec      = cms.double(2.46599),
                             singlelegsigma2Pix      = cms.double(0.0935307),
                             singlelegsigma2Tib      = cms.double(0.756568),
                             singlelegsigma2Tob      = cms.double(0.62143),
                             singlelegsigma2PixFwd   = cms.double(0.577081),
                             singlelegsigma2Tid      = cms.double(0.892751),
                             singlelegsigma2Tec      = cms.double(1.56638),


 )
