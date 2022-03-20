#!/usr/bin/env python

from CRABClient.UserUtilities import config
from CRABAPI.RawCommand import crabCommand
from CRABClient.ClientExceptions import ClientException
from httplib import HTTPException

from datetime import date

def submit(config):
    try:
        crabCommand('submit', config = config)
    except HTTPException as hte:
        print "Failed submitting task: %s" % (hte.headers)
    except ClientException as cle:
        print "Failed submitting task: %s" % (cle)


workarea='/afs/hep.wisc.edu/user/wadud/private/sf_and_prefiring_fix/CMSSW_10_6_24/src/ggAnalysis/ggNtuplizer/test/crab_submit//jobs//jobsUL2016PreVFP_MC_scaleFix_v1//aNTGCZNuNuGamma6002016PreVFPGEN/'

mainOutputDir = '/store/user/mwadud/aNTGCmet/ntuples/UL2016PreVFP/jobsUL2016PreVFP_MC_scaleFix_v1'

config                                = config()

config.General.requestName = 'aNTGCZNuNuGamma6002016PreVFPGEN'
# config.General.transferLogs = True
# config.General.transferOutputs = True
config.General.workArea = '%s' % workarea


config.Site.storageSite = 'T2_US_Wisconsin'
config.Site.whitelist = ['T3_US_UCR','T3_US_FNALLPC','T3_US_Rice','T3_US_Rutgers','T3_US_FIT','T3_US_PSC','T3_US_OSU','T3_US_TAMU','T3_US_UMD','T3_US_VC3_NotreDame','T3_US_SDSC','T3_US_Colorado','T3_US_OSG','T3_US_Princeton_ICSE','T3_US_NERSC','T3_US_Baylor','T2_US_Nebraska','T2_US_UCSD','T2_US_Wisconsin','T2_US_MIT','T3_US_TACC','T3_US_UMiss','T2_US_Caltech','T2_US_Florida','T2_US_Vanderbilt']
config.Site.blacklist = ['T2_US_Purdue']


config.JobType.psetName  = '/afs/hep.wisc.edu/user/wadud/private/sf_and_prefiring_fix/CMSSW_10_6_24/src/ggAnalysis/ggNtuplizer/test/crab_submit//jobs//jobsUL2016PreVFP_MC_scaleFix_v1//aNTGCZNuNuGamma6002016PreVFPGEN//run_mc2016preVFP_106X.py'
config.JobType.pluginName  = 'Analysis'
config.JobType.maxMemoryMB             = 2600
config.JobType.maxJobRuntimeMin        = 3000
# config.JobType.maxMemoryMB             = 2600
# config.JobType.maxJobRuntimeMin        = 5000
# config.JobType.maxMemoryMB             = 1500
# config.JobType.maxJobRuntimeMin        = 1000
# config.JobType.inputFiles  =    ['/afs/hep.wisc.edu/user/wadud/private/CMSSW_10_6_24/src/ggAnalysis/ggNtuplizer/test/EcalTimeCalibConstants_2018_RunD_UL_Corr_v2.db']

config.Data.inputDBS = 'phys03'
config.Data.inputDataset = '/aNTGC_ZNuNuGamma_600_2016PreVFP_GEN/mwadud-aNTGC_ZNuNuGamma_600_2016PreVFP_MINIAODSIM-890b564db4d193927f08e22fd05ac87a/USER'
config.Data.publication = False
config.Data.allowNonValidInputDataset = True
config.Data.outLFNDirBase = '%s' % mainOutputDir
config.Data.splitting     = 'FileBased'
config.Data.unitsPerJob   = 5
config.Data.ignoreLocality = True
config.Data.totalUnits = 50000000000
#config.Data.lumiMask = '#lumiMaskFile'

submit(config)
