#!/usr/bin/env python

from CRABClient.UserUtilities import config
# from CRABClient.ClientUtilities import getUsernameFromSiteDB
import sys

config = config()


#**************************submit function***********************
from CRABAPI.RawCommand import crabCommand
from CRABClient.ClientExceptions import ClientException
from httplib import HTTPException
def submit(config):
	try:
		crabCommand('submit', config = config)
	except HTTPException as hte:
		print "Failed submitting task: %s" % (hte.headers)
	except ClientException as cle:
		print "Failed submitting task: %s" % (cle)
#****************************************************************


workarea='/afs/cern.ch/work/m/mwadud/private/naTGC/CMSSW_9_4_13/src/ggAnalysis/ggNtuplizer/test/crab_submit/jobsMETv4//ZLLGJetsMonoPhotonPtG40to130TuneCP513TeVmadgraphpythia8/'

mainOutputDir = '/store/user/mwadud/aNTGCmet/ggNtuplizerMETv4/'


config.General.requestName = 'ZLLGJetsMonoPhotonPtG40to130TuneCP513TeVmadgraphpythia8'
config.General.transferLogs = True
config.General.workArea = '%s' % workarea


config.Site.storageSite = 'T2_US_Wisconsin'
config.Site.whitelist = ['T3_US_UCR','T3_US_FNALLPC','T2_US_Purdue','T3_US_Rice','T3_US_Rutgers','T3_US_FIT','T3_US_PSC','T3_US_OSU','T3_US_TAMU','T3_US_UMD','T3_US_VC3_NotreDame','T3_US_SDSC','T3_US_Colorado','T3_US_OSG','T3_US_Princeton_ICSE','T3_US_NERSC','T3_US_Baylor','T2_US_Nebraska','T2_US_UCSD','T2_US_Wisconsin','T2_US_MIT','T3_US_TACC','T3_US_TTU','T3_US_UMiss','T2_US_Caltech']
config.Site.blacklist = ['T2_US_Florida','T2_US_Vanderbilt','T3_US_PuertoRico']


config.JobType.psetName  = '/afs/cern.ch/work/m/mwadud/private/naTGC/CMSSW_9_4_13/src/ggAnalysis/ggNtuplizer/test/run_mc2017_94X.py'
config.JobType.pluginName  = 'Analysis'


config.Data.inputDBS = 'global'
config.Data.inputDataset = '/ZLLGJets_MonoPhoton_PtG-40to130_TuneCP5_13TeV-madgraph-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM'
config.Data.publication = False
config.Data.allowNonValidInputDataset = True
config.Data.outLFNDirBase = '%s' % mainOutputDir
config.Data.splitting     = 'FileBased'
config.Data.unitsPerJob   = 5
config.Data.ignoreLocality = True
config.Data.totalUnits = 5000
#config.Data.lumiMask = '#lumiMaskFile'
submit(config)
