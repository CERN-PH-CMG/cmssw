import random
from CMGTools.H2TauTau.proto.framework.Analyzer import Analyzer
from CMGTools.H2TauTau.proto.framework.AutoHandle import AutoHandle
from CMGTools.H2TauTau.proto.physicsobjects.PhysicsObjects import Jet
from CMGTools.H2TauTau.proto.physicsobjects.DeltaR import cleanObjectCollection
from CMGTools.H2TauTau.proto.physicsobjects.VBF import VBF
from CMGTools.H2TauTau.proto.statistics.Counter import Counter, Counters

class VBFAnalyzer( Analyzer ):
    '''Analyze jets, and in particular VBF.'''

    def declareHandles(self):
        super(VBFAnalyzer, self).declareHandles()

        self.handles['jets'] = AutoHandle( 'cmgPFJetSel',
                                           'std::vector<cmg::PFJet>' )

    def beginLoop(self):
        super(VBFAnalyzer,self).beginLoop()
        self.counters.addCounter('VBF')
        
    def process(self, iEvent, event):
        self.readCollections( iEvent )
        cmgJets = self.handles['jets'].product()
        event.jets = []
        event.cleanJets = []
        for cmgJet in cmgJets:
            jet = Jet( cmgJet )
            if self.cfg_comp.isMC:
                scale = random.gauss( self.cfg_comp.jetScale,
                                      self.cfg_comp.jetSmear )
                jet.scaleEnergy( scale )
            if not self.testJet( cmgJet ):
                continue
            event.jets.append(jet)
        self.counters.counter('VBF').inc('all events')
        if len( event.jets )<2:
            return True
        self.counters.counter('VBF').inc('at least 2 good jets')
       
        event.cleanJets = cleanObjectCollection( event.jets,
                                                 masks = [event.diLepton.leg1(),
                                                          event.diLepton.leg2() ],
                                                 deltaRMin = 0.5 )
        
        if len( event.cleanJets )<2:
            return True
        self.counters.counter('VBF').inc('at least 2 clean jets')

        event.vbf = VBF( event.cleanJets )
        if event.vbf.mjj > self.cfg_ana.Mjj:
            self.counters.counter('VBF').inc('M_jj > {cut:3.1f}'.format(cut=self.cfg_ana.Mjj) )
        else:
            return True 
        if abs(event.vbf.deta) > self.cfg_ana.deltaEta:
            self.counters.counter('VBF').inc('delta Eta > {cut:3.1f}'.format(cut=self.cfg_ana.deltaEta) )
        else:
            return True 
        if len(event.vbf.centralJets)==0:
            self.counters.counter('VBF').inc('no central jets')
        else:
            return True
        
        return True
        
        
    def testJet( self, jet ):
        if jet.pt() > self.cfg_ana.jetPt and \
               abs( jet.eta() ) < self.cfg_ana.jetEta:
            return True
        else:
            return False

