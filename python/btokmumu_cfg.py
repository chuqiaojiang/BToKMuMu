import FWCore.ParameterSet.Config as cms
from btokmumu_cfi import process 


process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )

process.source = cms.Source("PoolSource",
                            fileNames = cms.untracked.vstring(
                              '/store/mc/RunIIFall17MiniAODv2/BdToKstarMuMu_BMuonFilter_SoftQCDnonD_TuneCP5_13TeV-pythia8-evtgen/MINIAODSIM/PU2017_12Apr2018_N1_94X_mc2017_realistic_v14-v1/90000/8AE50B00-3F42-E811-A6D5-842B2B76653D.root'
                              #'/store/data/Run2017B/DoubleMuonLowMass/MINIAOD/22Jun2017-v1/00000/D6F6E300-7658-E711-8D1A-002590791D6A.root'                                
                                                              )
                            )

process.GlobalTag.globaltag = cms.string('94X_mc2017_realistic_v14'
                                        #'94X_dataRun2_ReReco_EOY17_v6'
                                        )



# do trigger matching for muons
triggerProcessName = 'HLT'




#  comment 20191103
'''
process.cleanMuonTriggerMatchHLT0 = cms.EDProducer(
        # match by DeltaR only (best match by DeltaR)
        'PATTriggerMatcherDRLessByR',
            src                   = cms.InputTag('cleanPatMuons'),
            # default producer label as defined in
            # PhysicsTools/PatAlgos/python/triggerLayer1/triggerProducer_cfi.py
            matched               = cms.InputTag('patTrigger'),
            matchedCuts           = cms.string('path("HLT_DoubleMu3p5_LowMass_Displaced*",0,0)'),
            maxDeltaR             = cms.double(0.1),
            # only one match per trigger object
            resolveAmbiguities    = cms.bool(True),
            # take best match found per reco object (by DeltaR here, see above)
            resolveByMatchQuality = cms.bool(False))
'''



from PhysicsTools.PatAlgos.tools.trigTools import *
switchOnTriggerMatchEmbedding(process, triggerMatchers = ['cleanMuonTriggerMatchHLT0'],
                               hltProcess = triggerProcessName, outputModule = '')

g_TriggerNames_LastFilterNames = [
        ('HLT_DoubleMu3p5_LowMass_Displaced',  'hltDisplacedmumuFilterDoubleMu3p5LowMass')
        ]




g_TriggerNames = [i[0] for i in g_TriggerNames_LastFilterNames]
g_LastFilterNames = [i[1] for i in g_TriggerNames_LastFilterNames]

process.ntuple.TriggerNames = cms.vstring(g_TriggerNames)
process.ntuple.LastFilterNames = cms.vstring(g_LastFilterNames)
