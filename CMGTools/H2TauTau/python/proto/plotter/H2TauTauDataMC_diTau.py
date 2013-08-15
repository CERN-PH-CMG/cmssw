import os
from fnmatch import fnmatch
import copy

from ROOT import TFile, TH1F, TPaveText

from CMGTools.RootTools.DataMC.AnalysisDataMCPlot import AnalysisDataMC
from CMGTools.RootTools.fwlite.Weight import Weight
from CMGTools.RootTools.fwlite.Weight import printWeights
from CMGTools.RootTools.Style import *

class H2TauTauDataMC( AnalysisDataMC ):

    def __init__(self, varName, directory, selComps, weights,
                 bins = None, xmin = None, xmax=None, cut = '',
                 weight='weight', embed = False, photon = False, electron = True,  shift=None, treeName=None):
        '''Data/MC plotter adapted to the H->tau tau analysis.
        The plotter takes a collection of trees in input. The trees are found according
        to the dictionary of selected components selComps.
        The global weighting information for each component is read from the weights dictionary.
        The weight parameter is the name of an event weight variable that can be found in the tree.
        The default is "weight" (full event weight computed at python analysis stage),
        but you can build up the weight string you want before calling this constructor.
        To do an unweighted plot, choose weight="1" (the string, not the number).        
        '''
        if treeName is None:
            treeName = 'H2TauTauTreeProducerTauTau'
        self.treeName = treeName
        self.selComps = selComps
        self.varName = varName
        self.cut = cut
        self.eventWeight = weight
        # import pdb; pdb.set_trace()
        self.bins = bins
        self.xmin = xmin
        self.xmax = xmax
	self.photon = photon
	self.electron = electron
        self.keeper = []
        
        super(H2TauTauDataMC, self).__init__(varName, directory, weights)
        self.legendBorders = 0.55,0.65,0.85,0.88

        self.dataComponents = [ key for key, value in selComps.iteritems() \
                                if value.isData is True ]
        groupDataName = 'Data'

        self.groupDataComponents( self.dataComponents, groupDataName)
        
        if embed: 
            self.setupEmbedding( embed )
        else:
            self.removeEmbeddedSamples()

    def _BuildHistogram(self, tree, comp, compName, varName, cut, layer ):
        '''Build one histogram, for a given component'''
        histName = '_'.join( [compName, self.varName] )
        hist = None
        if self.xmin is not None and self.xmax is not None:
            hist = TH1F( histName, '', self.bins, self.xmin, self.xmax )
        else:
            hist = TH1F( histName, '', len(self.bins)-1, self.bins )
        hist.Sumw2()
	if varName=="tau1Mass":
	    varName="sqrt(l1E*l1E-l1Px*l1Px-l1Py*l1Py-l1Pz*l1Pz)"
	if varName=="tau2Mass":
	    varName="sqrt(l2E*l2E-l2Px*l2Px-l2Py*l2Py-l2Pz*l2Pz)"
        tree.Project( histName, varName, '{weight}*({cut})'.format(cut=cut,weight=self.eventWeight) )
        hist.GetXaxis().SetTitle(varName)
        hist.SetTitle("")
        hist.SetStats(0)
        componentName = compName
        legendLine = compName
        self.AddHistogram( componentName, hist, layer, legendLine)
        if comp.isData:
            self.Hist(componentName).stack = False
        self.Hist(componentName).tree = tree

    def _ReadHistograms(self, directory):
        '''Build histograms for all components.'''
        for layer, (compName, comp) in enumerate( self.selComps.iteritems() ) : 
            fileName = '/'.join([ directory,
                                  compName,
                                  'H2TauTauTreeProducerTauTau',
                                  'H2TauTauTreeProducerTauTau_tree.root'])
            file = TFile(fileName)
            self.keeper.append( file )
            tree = file.Get('H2TauTauTreeProducerTauTau')
	    #print fileName, tree
            
            if compName == 'DYJets':
	        if self.photon:
		    phot="&& isPhoton==0"
	        elif self.electron:
		    phot="&& isElectron==0"
                else:
		    phot=""
                self._BuildHistogram(tree, comp, compName, self.varName,
                                     self.cut + ' && isFake==0'+phot, layer)
                fakeCompName = 'DYJets_Fakes'
                self._BuildHistogram(tree, comp, fakeCompName, self.varName,
                                     self.cut + ' && isFake'+phot, layer)
                self.weights[fakeCompName] = self.weights[compName]
		if self.photon:
                    photonCompName = 'DYJets_Photon'
                    self._BuildHistogram(tree, comp, photonCompName, self.varName,
                                         self.cut + ' && isPhoton', layer)
                    self.weights[photonCompName] = self.weights[compName]
		if self.electron:
                    electronCompName = 'DYJets_Electron'
                    self._BuildHistogram(tree, comp, electronCompName, self.varName,
                                         self.cut + ' && isElectron', layer)
                    self.weights[electronCompName] = self.weights[compName]
            else:
                self._BuildHistogram(tree, comp, compName, self.varName,
                                     self.cut, layer )     

        self._ApplyWeights()
        self._ApplyPrefs()
        

    def removeEmbeddedSamples(self):
        for compname in self.selComps:
            if compname.startswith('embed_'):
                hist = self.Hist(compname)
                hist.stack = False
                hist.on = False
                

    def setupEmbedding(self, doEmbedding ):
        name = 'DYJets'
        try:
            dyHist = self.Hist(name)
        except KeyError:
            return 
        newName = name
        embed = None
        embedFactor = None
        for comp in self.selComps.values():
            if not comp.isEmbed:
                continue
            embedHistName = comp.name
            if embedFactor is None:
                embedFactor = comp.embedFactor
            elif embedFactor != comp.embedFactor:
                raise ValueError('All embedded samples should have the same scale factor')
            embedHist = self.Hist( embedHistName )
            embedHist.stack = False
            embedHist.on = False
            if doEmbedding:
                if embed is None:
                    embed = copy.deepcopy( embedHist )
                    embed.name = 'DYJets (emb)'
                    embed.on = True
                    # self.AddHistogram(newName, embed.weighted, 3.5)
                    self.Replace('DYJets', embed)
                    self.Hist(newName).stack = True
                else:
                    self.Hist(newName).Add(embedHist)
        if doEmbedding:
            #         embedYield = self.Hist(newName).Yield()
            print 'EMBEDDING: scale factor = ', embedFactor
            # import pdb; pdb.set_trace()
            self.Hist(newName).Scale( embedFactor ) 
            self._ApplyPrefs()
            # self.Hist(name).on = False


    def groupDataComponents( self, dataComponents, name ):
        '''Groups all data components into a single component with name <name>.

        The resulting histogram is the sum of all data histograms.
        The resulting integrated luminosity is used to scale all the
        MC components.
        '''
        
        self.intLumi = 0
        # self.dataComponents = dataComponents
        data = None
        for component in dataComponents:
            # print component
            hist = self.Hist(component)
            hist.stack = False
            hist.on = False
            self.intLumi += self.weights[component].intLumi
            if data is None:
                # keep first histogram
                data = copy.deepcopy( hist )
                self.AddHistogram(name, data.weighted, 10000, 'Observed')
                self.Hist(name).stack = False
                continue
            # other data histograms added to the first one...
            # ... and removed from the stack
            self.Hist(name).Add( hist )
            # compute integrated luminosity for all data samples
        # print intLumi
        # set lumi for all MC samples:
        for component, weight in self.weights.iteritems():
            if component not in dataComponents:
                self.weights[component].intLumi = self.intLumi
        self._ApplyWeights()
        self._ApplyPrefs()
        

    def _InitPrefs(self):
        '''Define preferences for each component'''
        self.histPref = {}
        
        self.histPref['Data']             = {'style':sData      , 'layer':2999 , 'legend':'Observed'             }
        self.histPref['data_*']           = {'style':sBlack     , 'layer':2002 , 'legend':None                   }
        self.histPref['DY*Jets']          = {'style':sHTT_DYJets, 'layer':4    , 'legend':'Z#rightarrow#tau#tau' }
        self.histPref['embed_*']          = {'style':sViolet    , 'layer':4.1  , 'legend':None                   }
        self.histPref['TTJets*']          = {'style':sHTT_TTJets, 'layer':1    , 'legend':'t#bar{t}'             } 
        self.histPref['T*tW*']            = {'style':sHTT_TTJets, 'layer':1    , 'legend':'t#bar{t}'             } 
        self.histPref['WW*']              = {'style':sBlue      , 'layer':0.9  , 'legend':None                   } 
        self.histPref['WZ*']              = {'style':sRed       , 'layer':0.8  , 'legend':None                   } 
        self.histPref['ZZ*']              = {'style':sGreen     , 'layer':0.7  , 'legend':None                   } 
        self.histPref['QCD']              = {'style':sHTT_QCD   , 'layer':2    , 'legend':None                   }
        self.histPref['WJets*']           = {'style':sHTT_WJets , 'layer':3    , 'legend':None                   }  
        self.histPref['DYJets_Fakes']     = {'style':sHTT_ZL    , 'layer':3.1  , 'legend':None                   }
        self.histPref['DYJets_Electron']  = {'style':sHTT_ZL    , 'layer':3.2  , 'legend':None                   }
        self.histPref['Higgs*']           = {'style':sHTT_Higgs , 'layer':1001 , 'legend':None                   }
