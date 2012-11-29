#include <iostream>
#include <boost/shared_ptr.hpp>

#include "EGamma/EGammaAnalysisTools/interface/EGammaCutBasedEleId.h"

#include "CMGTools/HtoZZ2l2nu/interface/ZZ2l2nuSummaryHandler.h"
#include "CMGTools/HtoZZ2l2nu/interface/ZZ2l2nuPhysicsEvent.h"
#include "CMGTools/HtoZZ2l2nu/interface/METUtils.h"
#include "CMGTools/HtoZZ2l2nu/interface/GammaEventHandler.h"
#include "CMGTools/HtoZZ2l2nu/interface/setStyle.h"
#include "CMGTools/HtoZZ2l2nu/interface/plotter.h"
#include "CMGTools/HtoZZ2l2nu/interface/ObjectFilters.h"
#include "CMGTools/HtoZZ2l2nu/interface/SmartSelectionMonitor.h"
#include "CMGTools/HtoZZ2l2nu/interface/TMVAUtils.h"
#include "CMGTools/HtoZZ2l2nu/interface/MacroUtils.h"
#include "CMGTools/HtoZZ2l2nu/interface/EventCategory.h"
#include "CMGTools/HtoZZ2l2nu/interface/EfficiencyMap.h"
#include "CMGTools/HtoZZ2l2nu/interface/LeptonEfficiencySF.h"

#include "CondFormats/JetMETObjects/interface/JetResolution.h"
#include "CondFormats/JetMETObjects/interface/JetCorrectionUncertainty.h"

#include "FWCore/FWLite/interface/AutoLibraryLoader.h"
#include "FWCore/PythonParameterSet/interface/MakeParameterSets.h"
#include "FWCore/ParameterSet/interface/ParameterSet.h"
#include "PhysicsTools/Utilities/interface/LumiReWeighting.h"

#include "TSystem.h"
#include "TFile.h"
#include "TTree.h"
#include "TCanvas.h"
#include "TH1F.h"
#include "TH2F.h"
#include "TProfile.h"
#include "TEventList.h"
#include "TROOT.h"
 
using namespace std;



int main(int argc, char* argv[])
{
  //##############################################
  //########    GLOBAL INITIALIZATION     ########
  //##############################################

  // check arguments
  if(argc<2){ std::cout << "Usage : " << argv[0] << " parameters_cfg.py" << std::endl; exit(0); }
  
  // load framework libraries
  gSystem->Load( "libFWCoreFWLite" );
  AutoLibraryLoader::enable();
  
  // configure the process
  const edm::ParameterSet &runProcess = edm::readPSetsFrom(argv[1])->getParameter<edm::ParameterSet>("runProcess");

  bool use2011Id = runProcess.getParameter<bool>("is2011");
  cout << "Note: will apply " << (use2011Id ? 2011 : 2012) << " version of the id's" << endl;

  bool isMC = runProcess.getParameter<bool>("isMC");
  int mctruthmode=runProcess.getParameter<int>("mctruthmode");

  TString url=runProcess.getParameter<std::string>("input");
  TString outFileUrl(gSystem->BaseName(url));
  outFileUrl.ReplaceAll(".root","");
  if(mctruthmode!=0) { outFileUrl += "_filt"; outFileUrl += mctruthmode; }
  TString outdir=runProcess.getParameter<std::string>("outdir");
  TString outUrl( outdir );
  gSystem->Exec("mkdir -p " + outUrl);
  int fType(0);
  if(url.Contains("DoubleEle")) fType=EE;
  if(url.Contains("DoubleMu"))  fType=MUMU;
  if(url.Contains("MuEG"))      fType=EMU;
  if(url.Contains("SingleMu"))  fType=MUMU;
  bool isSingleMuPD(!isMC && url.Contains("SingleMu"));  
  bool isV0JetsMC(isMC && url.Contains("0Jets"));  

  TString outTxtUrl= outUrl + "/" + outFileUrl + ".txt";
  FILE* outTxtFile = NULL;
  if(!isMC)outTxtFile = fopen(outTxtUrl.Data(), "w");
  printf("TextFile URL = %s\n",outTxtUrl.Data());

  //tree info
  int evStart=runProcess.getParameter<int>("evStart");
  int evEnd=runProcess.getParameter<int>("evEnd");
  TString dirname = runProcess.getParameter<std::string>("dirName");

  //lepton efficiencies
  LeptonEfficiencySF lepEff2012;

  //jet energy scale uncertainties
  TString uncFile =  runProcess.getParameter<std::string>("jesUncFileName"); gSystem->ExpandPathName(uncFile);
  JetCorrectionUncertainty jecUnc(uncFile.Data());

  //systematics
  bool runSystematics                        = runProcess.getParameter<bool>("runSystematics");
  TString varNames[]={"",
		      "_jerup","_jerdown",
		      "_jesup","_jesdown",
		      "_umetup","_umetdown",
		      "_lesup","_lesdown",
		      "_puup","_pudown",
		      "_btagup","_btagdown"};
  size_t nvarsToInclude(1);
  if(runSystematics)
    {
      cout << "Systematics will be computed for this analysis" << endl;
      nvarsToInclude=sizeof(varNames)/sizeof(TString);
    }

  //##############################################
  //########    INITIATING HISTOGRAMS     ########
  //##############################################
  SmartSelectionMonitor mon;

  TH1F* Hcutflow  = (TH1F*) mon.addHistogram(  new TH1F ("cutflow"    , "cutflow"    ,6,0,6) ) ;
  TH1 *h=mon.addHistogram( new TH1F ("eventflow", ";;Events", 6,0,6) );
  h->GetXaxis()->SetBinLabel(1,"Trigger");
  h->GetXaxis()->SetBinLabel(2,"#geq 2 leptons");
  h->GetXaxis()->SetBinLabel(3,"|M-M_{Z}|<15");
  h->GetXaxis()->SetBinLabel(4,"p_{T}^{ll}>50, #eta^{ll}<1.44");
  h->GetXaxis()->SetBinLabel(5,"3^{rd}-lepton veto"); 
  h->GetXaxis()->SetBinLabel(6,"#geq 2 jets"); 

  //pileup control
  mon.addHistogram( new TH1F( "nvtx",";Vertices;Events",50,0,50) ); 
  mon.addHistogram( new TH1F( "nvtxraw",";Vertices;Events",50,0,50) ); 
  mon.addHistogram( new TH1F( "rho",";#rho;Events",50,0,25) ); 
  mon.addHistogram( new TH1F( "rho25",";#rho(#eta<2.5);Events",50,0,25) ); 

  //lepton control
  mon.addHistogram( new TH1F("ereliso",           ";RelIso;Leptons",50,0,2) );
  mon.addHistogram( new TH1F("mureliso",           ";RelIso;Leptons",50,0,2) );
  mon.addHistogram( new TH1F( "leadpt", ";p_{T}^{l};Events", 50,0,500) );
  mon.addHistogram( new TH1F( "leadeta", ";#eta^{l};Events", 50,-2.6,2.6) );
  mon.addHistogram( new TH1F( "trailerpt", ";p_{T}^{l};Events", 50,0,500) );
  mon.addHistogram( new TH1F( "trailereta", ";#eta^{l};Events", 50,-2.6,2.6) );

  Float_t qtaxis[100];
  for(size_t i=0; i<40; i++)  qtaxis[i]=2.5*i;       //0-97.5                                                                                                                                   
  for(size_t i=0; i<20; i++)  qtaxis[40+i]=100+5*i;  //100-195                                                                                                                                   
  for(size_t i=0; i<15; i++)  qtaxis[60+i]=200+10*i; //200-340                                                                                                                                    
  for(size_t i=0; i<25; i++)  qtaxis[75+i]=350+25*i; //350-976                                        
  mon.addHistogram( new TH1D( "qt",        ";p_{T}^{#gamma} [GeV/c];Events / (2.5 GeV/c)",99,qtaxis));
  mon.addHistogram( new TH1F( "zpt", ";p_{T}^{ll};Events", 50,0,500) );
  mon.addHistogram( new TH1F( "zptNM1", ";p_{T}^{ll};Events", 50,0,500) );
  mon.addHistogram( new TH1F( "zeta", ";#eta^{ll};Events", 50,-10,10) );
  mon.addHistogram( new TH1F( "zetaNM1", ";#eta^{ll};Events", 50,-10,10) );
  mon.addHistogram( new TH1F( "zmass", ";M^{ll};Events", 100,40,250) );

  //jet control
  mon.addHistogram( new TH1F("jetpt"       , ";p_{T} [GeV/c];Events",50,0,250) );
  mon.addHistogram( new TH1F("jeteta"       , ";|#eta|;Events",25,0,5) );
  mon.addHistogram( new TH1F("btags", ";CSV;Events",50,-0.5,1.2) );
  h=mon.addHistogram( new TH1F("njets",  ";Jet multiplicity (p_{T}>30 GeV/c);Events",5,0,5) );
  TH1 *hb=mon.addHistogram( new TH1F("nbtags",   ";b-tag multiplicity (CSV);Events",5,0,5) );
  for(int ibin=1; ibin<=h->GetXaxis()->GetNbins(); ibin++)
    {
      TString label("");
      if(ibin==h->GetXaxis()->GetNbins()) label +="#geq";
      else                                label +="=";
      label += (ibin-1);
      h->GetXaxis()->SetBinLabel(ibin,label);
      hb->GetXaxis()->SetBinLabel(ibin,label);
    } 

  //vbf control
  int jetIdToApply=JETID_OPT_LOOSE;
  mon.addHistogram( new TH2F("njetsvsavginstlumi",  ";;Jet multiplicity (p_{T}>30 GeV/c);Events",5,0,5,10,0,5000) );
  mon.addHistogram( new TH1F("vbfcandjeteta"     , ";#eta;Jets",                                 50,0,5) );
  mon.addHistogram( new TH1F("vbfcandjetpt"      , ";p_{T} [GeV/c];Jets",                        50,0,500) );
  mon.addHistogram( new TH1F("vbfcandjet1eta"    , ";#eta;Jets",                                 50,0,5) );
  mon.addHistogram( new TH1F("vbfcandjet1pt"     , ";p_{T} [GeV/c];Jets",                        50,0,500) );
  mon.addHistogram( new TH1F("vbfcandjet2eta"    , ";#eta;Jets",                                 50,0,5) );
  mon.addHistogram( new TH1F("vbfcandjet2pt"     , ";p_{T} [GeV/c];Jets",                        50,0,500) );
  mon.addHistogram( new TH1F("vbfcandjetdeta"    , ";|#Delta #eta|;Jets",                        50,0,10) );
  mon.addHistogram( new TH1F("vbfcandjetetaNM1"  , ";#eta;Jets",                                 50,0,5) );
  mon.addHistogram( new TH1F("vbfcandjetptNM1"   , ";p_{T} [GeV/c];Jets",                        50,0,500) );
  mon.addHistogram( new TH1F("vbfcandjet1etaNM1" , ";#eta;Jets",                                 50,0,5) );
  mon.addHistogram( new TH1F("vbfcandjet1ptNM1"  , ";p_{T} [GeV/c];Jets",                        50,0,500) );
  mon.addHistogram( new TH1F("vbfcandjet2etaNM1" , ";#eta;Jets",                                 50,0,5) );
  mon.addHistogram( new TH1F("vbfcandjet2ptNM1"  , ";p_{T} [GeV/c];Jets",                        50,0,500) );
  mon.addHistogram( new TH1F("vbfcandjetdetaNM1" , ";|#Delta #eta|;Jets",                        50,0,10) );
  mon.addHistogram( new TH1F("vbfhardpt"       , ";Hard p_{T} [GeV/c];Events",                   25,0,250) );
  mon.addHistogram( new TH1F("vbfhardpt50"       , ";Hard p_{T} [GeV/c];Events",                 25,0,250) );
  h=mon.addHistogram( new TH1F("vbfcjv"       , ";Central jet count;Events",                     3,0,3) );
  h->GetXaxis()->SetBinLabel(1,"=0 jets");
  h->GetXaxis()->SetBinLabel(2,"=1 jets");
  h->GetXaxis()->SetBinLabel(3,"#geq 2 jets");
  mon.addHistogram( new TH1F("vbfhtcjv"          , ";Central jet H_{T} [GeV/c];Events",50,0,250) );
  mon.addHistogram( new TH1F("vbfhtcjvall"       , ";Central jet H_{T} [GeV/c];Events",50,0,250) );
  mon.addHistogram( new TH1F("vbfpremjj"         , ";M(jet_{1},jet_{2}) [GeV/c^{2}];Events",60,0,3000) );
  mon.addHistogram( new TH1F("vbfmjj"            , ";M(jet_{1},jet_{2}) [GeV/c^{2}];Events",60,0,3000) );
  mon.addHistogram( new TH1F("vbfmjjNM1"         , ";M(jet_{1},jet_{2}) [GeV/c^{2}];Events",60,0,3000) );
  mon.addHistogram( new TH1F("vbfdphijj"         , ";#Delta#phi;Events",20,0,3.5) );


  //statistical analysis
  std::vector<double> optim_Cuts2_z_pt;
  std::vector<double> optim_Cuts2_jet_pt; 
  std::vector<double> optim_Cuts2_eta_gap;
  std::vector<double> optim_Cuts2_dijet_mass;
  for(double z_pt=50;z_pt<=100;z_pt+=10)
    {
      for(double jet_pt=30;jet_pt<=100;jet_pt+=10)
	{
	  for(double eta_gap=3.5;eta_gap<=5.0;eta_gap+=0.5)
	    {
	      for(double dijet_mass=400; dijet_mass<=1000; dijet_mass+=50)
		{
		  optim_Cuts2_z_pt.push_back(z_pt);
		  optim_Cuts2_jet_pt.push_back(jet_pt);
		  optim_Cuts2_eta_gap.push_back(eta_gap);
		  optim_Cuts2_dijet_mass.push_back(dijet_mass);
		}
            }
	}
    } 
  TH1F* Hoptim_cuts2_z_pt      =(TH1F*)mon.addHistogram(new TProfile("optim_cut2_z_pt",      ";cut index;z_pt",       optim_Cuts2_z_pt.size(),0,optim_Cuts2_z_pt.size())) ;
  TH1F* Hoptim_cuts2_jet_pt    =(TH1F*)mon.addHistogram(new TProfile("optim_cut2_jet_pt",    ";cut index;jet_pt",     optim_Cuts2_jet_pt.size(),0,optim_Cuts2_jet_pt.size())) ;
  TH1F* Hoptim_cuts2_eta_gap   =(TH1F*)mon.addHistogram(new TProfile("optim_cut2_eta_gap",   ";cut index;eta_gap",    optim_Cuts2_eta_gap.size(),0,optim_Cuts2_eta_gap.size())) ;
  TH1F* Hoptim_cuts2_dijet_mass=(TH1F*)mon.addHistogram(new TProfile("optim_cut2_dijet_mass",";cut index;dijet_mass", optim_Cuts2_dijet_mass.size(),0,optim_Cuts2_dijet_mass.size()));
  for(unsigned int index=0;index<optim_Cuts2_z_pt.size();index++){
    Hoptim_cuts2_z_pt->Fill(index,optim_Cuts2_z_pt[index]);   
    Hoptim_cuts2_jet_pt->Fill(index,optim_Cuts2_jet_pt[index]); 
    Hoptim_cuts2_eta_gap->Fill(index,optim_Cuts2_eta_gap[index]);
    Hoptim_cuts2_dijet_mass->Fill(index,optim_Cuts2_dijet_mass[index]);
  }
 
  TH1F* Hoptim_systs     =  (TH1F*) mon.addHistogram( new TH1F ("optim_systs"    , ";syst;", nvarsToInclude,0,nvarsToInclude) ) ;
  for(size_t ivar=0; ivar<nvarsToInclude; ivar++)
  {
    Hoptim_systs->GetXaxis()->SetBinLabel(ivar+1, varNames[ivar]);
    mon.addHistogram( new TH2F (TString("dijet_mass_shapes")+varNames[ivar],";cut index;M_Z [GeV];#events (/1GeV)",optim_Cuts2_dijet_mass.size(),0,optim_Cuts2_dijet_mass.size(),120,0,3000) );
  }
  
  //##############################################
  //######## GET READY FOR THE EVENT LOOP ########
  //##############################################

  //open the file and get events tree
  ZZ2l2nuSummaryHandler evSummaryHandler;
  TFile *file = TFile::Open(url);
  printf("Looping on %s\n",url.Data());
  if(file==0) return -1;
  if(file->IsZombie()) return -1;
  if( !evSummaryHandler.attachToTree( (TTree *)file->Get(dirname) ) ){
      file->Close();
      return -1;
  }


  //check run range to compute scale factor (if not all entries are used)
  const Int_t totalEntries= evSummaryHandler.getEntries();
  float rescaleFactor( evEnd>0 ?  float(totalEntries)/float(evEnd-evStart) : -1 );
  if(evEnd<0 || evEnd>evSummaryHandler.getEntries() ) evEnd=totalEntries;
  if(evStart > evEnd ){
      file->Close();
      return -1;
  }

  //MC normalization (to 1/pb)
  float cnorm=1.0;
  if(isMC){
      TH1F* cutflowH = (TH1F *) file->Get("evAnalyzer/h2zz/cutflow");
      if(cutflowH) cnorm=cutflowH->GetBinContent(1);
      if(rescaleFactor>0) cnorm /= rescaleFactor;
      printf("cnorm = %f\n",cnorm);
  }
  Hcutflow->SetBinContent(1,cnorm);


  //pileup weighting: based on vtx for now...
  std::vector<double> dataPileupDistributionDouble = runProcess.getParameter< std::vector<double> >("datapileup");
  std::vector<float> dataPileupDistribution; for(unsigned int i=0;i<dataPileupDistributionDouble.size();i++){dataPileupDistribution.push_back(dataPileupDistributionDouble[i]);}
  std::vector<float> mcPileupDistribution;
  bool useObservedPU(true);
  if(isMC){
    TString puDist("evAnalyzer/h2zz/pileuptrue");
    if(useObservedPU) puDist="evAnalyzer/h2zz/pileup";
    TH1F* histo = (TH1F *) file->Get(puDist);
    if(!histo)std::cout<<"pileup histogram is null!!!\n";
    for(int i=1;i<=histo->GetNbinsX();i++){mcPileupDistribution.push_back(histo->GetBinContent(i));}
    delete histo;
    if(dataPileupDistribution.size()==0) dataPileupDistribution=mcPileupDistribution;
  }
  while(mcPileupDistribution.size()<dataPileupDistribution.size())  mcPileupDistribution.push_back(0.0);
  while(mcPileupDistribution.size()>dataPileupDistribution.size())dataPileupDistribution.push_back(0.0);

  gROOT->cd();  //THIS LINE IS NEEDED TO MAKE SURE THAT HISTOGRAM INTERNALLY PRODUCED IN LumiReWeighting ARE NOT DESTROYED WHEN CLOSING THE FILE
  edm::LumiReWeighting *LumiWeights=0;
  PuShifter_t PuShifters;
  //  reweight::PoissonMeanShifter *PShiftUp=0, *PShiftDown=0;
  if(isMC){
      LumiWeights= new edm::LumiReWeighting(mcPileupDistribution,dataPileupDistribution);
      PuShifters=getPUshifters(dataPileupDistribution,0.05);
  }

  //event Categorizer
  EventCategory eventCategoryInst(4); //0,>=1jet, VBF


  //##############################################
  //########           EVENT LOOP         ########
  //##############################################
  //loop on all the events
  printf("Progressing Bar     :0%%       20%%       40%%       60%%       80%%       100%%\n");
  printf("Scanning the ntuple :");
  int treeStep = (evEnd-evStart)/50;if(treeStep==0)treeStep=1;
  DuplicatesChecker duplicatesChecker;
  int nDuplicates(0);
  for( int iev=evStart; iev<evEnd; iev++){
      if((iev-evStart)%treeStep==0){printf(".");fflush(stdout);}

      //##############################################   EVENT LOOP STARTS   ##############################################
      //load the event content from tree
      evSummaryHandler.getEntry(iev);
      ZZ2l2nuSummary_t &ev=evSummaryHandler.getEvent();
      if(!isMC && duplicatesChecker.isDuplicate( ev.run, ev.lumi, ev.event) ) { nDuplicates++; continue; }
      PhysicsEvent_t phys=getPhysicsEventFrom(ev);
      
      //event category
      bool isSameFlavor(ev.cat==MUMU || ev.cat==EE);
      TString tag_cat;
      switch(ev.cat){
         case MUMU : tag_cat = "mumu";  break;
         case EE   : tag_cat = "ee";    break;
         case EMU  : tag_cat = "emu";   break;
         default   : continue;
      }
      //      if(isMC && mctruthmode==1 && !isDYToLL(ev.mccat) && !isZZ2l2nu(ev.mccat) ) continue;
      if(isMC && mctruthmode==1 && !isDYToLL(ev.mccat) ) continue;
      if(isMC && mctruthmode==2 && !isDYToTauTau(ev.mccat) ) continue;
      if(isV0JetsMC && ev.mc_nup>5)                          continue; 

//require compatibilitiy of the event with the PD
      bool hasTrigger(false);
      bool hasEEtrigger = ev.triggerType & 0x1;
      bool hasMMtrigger = (ev.triggerType >> 1 ) & 0x1;
      bool hasEMtrigger = (ev.triggerType >> 2 ) & 0x1;
      bool hasMtrigger  = (ev.triggerType >> 3 ) & 0x1;
      if(!isMC){
	  if(ev.cat!=fType) continue;

	  if(ev.cat==EE   && !hasEEtrigger) continue;
	  if(ev.cat==MUMU && !(hasMMtrigger||hasMtrigger) ) continue;
	  if(ev.cat==EMU  && !hasEMtrigger) continue;

	  //this is a safety veto for the single mu PD
	  if(isSingleMuPD) {
	    if(!hasMtrigger) continue;
	    if(hasMtrigger && hasMMtrigger) continue;
	  }

	  hasTrigger=true;
      }
      else 
	{
	  if(ev.cat==EE   && hasEEtrigger)                   hasTrigger=true;
	  if(ev.cat==MUMU && (hasMMtrigger || hasMtrigger) ) hasTrigger=true;
	  if(ev.cat==EMU  && hasEMtrigger)                   hasTrigger=true;
	}
      
      
      //prepare the tag's vectors for histo filling
      std::vector<TString> tags(1,"all");
      
      //pileup weight
      float weight = 1.0;
      double TotalWeight_plus = 1.0;
      double TotalWeight_minus = 1.0;
      if(isMC){
        weight            = LumiWeights->weight(useObservedPU ? ev.ngenITpu : ev.ngenTruepu);
        TotalWeight_plus  = PuShifters[PUUP]->Eval(useObservedPU ? ev.ngenITpu : ev.ngenTruepu);
        TotalWeight_minus = PuShifters[PUDOWN]->Eval(useObservedPU ? ev.ngenITpu : ev.ngenTruepu);
      }
      Hcutflow->Fill(1,1);
      Hcutflow->Fill(2,weight);
      Hcutflow->Fill(3,weight*TotalWeight_minus);
      Hcutflow->Fill(4,weight*TotalWeight_plus);
      Hcutflow->Fill(5,weight);

      //
      //
      // BELOW FOLLOWS THE ANALYSIS OF THE MAIN SELECTION WITH N-1 PLOTS
      //
      //
      
      //
      // LEPTON ANALYSIS
      //
      LorentzVector lep1=phys.leptons[0];
      LorentzVector lep2=phys.leptons[1];
      LorentzVector zll(lep1+lep2);
      bool passIdAndIso(true);
      bool passZmass(fabs(zll.mass()-91)<15);
      bool passZpt(zll.pt()>50 && fabs(zll.eta())<1.4442);
      double llScaleFactor(1.0),llTriggerEfficiency(1.0);
      for(int ilep=0; ilep<2; ilep++)
	{
	  TString lepStr( fabs(phys.leptons[ilep].id)==13 ? "mu" : "e");
	  
	  //generator level matching
	  int matchid(0);
	  LorentzVector genP4(0,0,0,0);
	  for(size_t igl=0;igl<phys.genleptons.size(); igl++) 
	    {
	      if(deltaR(phys.genleptons[igl],phys.leptons[ilep])>0.1) continue;
	      genP4=phys.genleptons[igl];
	      matchid=phys.genleptons[igl].id;
	    }
	  
	  //id and isolation
	  int lpid=phys.leptons[ilep].pid;
	  float relIso2011    = phys.leptons[ilep].relIsoRho(ev.rho);
	  float relIso = (lepStr=="mu") ? 
	    phys.leptons[ilep].pfRelIsoDbeta(): 
	    phys.leptons[ilep].ePFRelIsoCorrected2012(ev.rho);
	  
	  bool hasGoodId(false), isIso(false);
	  if(fabs(phys.leptons[ilep].id)==13)
	    {
	      if(!use2011Id)
		{
		  hasGoodId=hasObjectId(ev.mn_idbits[lpid], MID_TIGHT);
		  isIso=(relIso<0.2);
		  llScaleFactor *= lepEff2012.getLeptonEfficiency(phys.leptons[ilep].pt(),fabs(phys.leptons[ilep].eta()),13).first;
		  llTriggerEfficiency *= muonTriggerEfficiency(phys.leptons[ilep].pt(),fabs(phys.leptons[ilep].eta()),2012);
		}
	      else
		{
		  hasGoodId=hasObjectId(ev.mn_idbits[lpid], MID_VBTF2011);
		  isIso=relIso2011<0.15;
		  llScaleFactor *= muonScaleFactor(phys.leptons[ilep].pt(),fabs(phys.leptons[ilep].eta()));
		  llTriggerEfficiency *= muonTriggerEfficiency(phys.leptons[ilep].pt(),fabs(phys.leptons[ilep].eta()));
		}
	    }
	  else
	    {
	      if(!use2011Id)
		{
		  hasGoodId = EgammaCutBasedEleId::PassWP(EgammaCutBasedEleId::MEDIUM,
						       (fabs(phys.leptons[ilep].eta())<1.4442),
						       phys.leptons[ilep].pt(), phys.leptons[ilep].eta(),
						       ev.en_detain[lpid],  ev.en_dphiin[lpid], ev.en_sihih[lpid], ev.en_hoe[lpid],
						       ev.en_ooemoop[lpid], phys.leptons[ilep].d0, phys.leptons[ilep].dZ,
						       0., 0., 0.,
						       !hasObjectId(ev.en_idbits[lpid], EID_CONVERSIONVETO),0,ev.rho);
		  isIso=(relIso<0.15);
		  llScaleFactor *= lepEff2012.getLeptonEfficiency(phys.leptons[ilep].pt(),fabs(phys.leptons[ilep].eta()),11).first;
		  llTriggerEfficiency *= electronTriggerEfficiency(phys.leptons[ilep].pt(),fabs(phys.leptons[ilep].eta()),2012);
		}
	      else
		{
		  hasGoodId=hasObjectId(ev.en_idbits[lpid], EID_VBTF2011);
		  isIso=relIso2011<0.1;
		  llScaleFactor *= muonScaleFactor(phys.leptons[ilep].pt(),fabs(phys.leptons[ilep].eta()));
		  llTriggerEfficiency *= muonTriggerEfficiency(phys.leptons[ilep].pt(),fabs(phys.leptons[ilep].eta()));
		}
	    }
	  if(!hasGoodId)  passIdAndIso=false;
	  else if(!isIso) passIdAndIso=false;     
	  
	  if(hasGoodId)	    mon.fillHisto(lepStr+"reliso",     tags, relIso,   weight);
	}
      if(isMC) weight *= llScaleFactor*llTriggerEfficiency;

      //
      // 3rd LEPTON ANALYSIS
      //
      int nextraleptons(0);
      std::vector<LorentzVector> extraLeptonsP4;
      for(size_t ilep=2; ilep<phys.leptons.size(); ilep++){
	//lepton type
	bool isGood(false);
	int lpid=phys.leptons[ilep].pid;
	if(fabs(phys.leptons[ilep].id)==13){
	  if(!use2011Id){
	    isGood = (hasObjectId(ev.mn_idbits[lpid], MID_LOOSE) && phys.leptons[ilep].pfRelIsoDbeta()<0.2);
	  }else{
	    isGood = (hasObjectId(ev.mn_idbits[lpid], MID_VBTF2011) && phys.leptons[ilep].relIsoRho(ev.rho)<0.15 && phys.leptons[ilep].pt()>10);
	  }
	}else{
	  if(!use2011Id){
	    isGood = ( hasObjectId(ev.en_idbits[lpid],EID_LOOSE) && phys.leptons[ilep].ePFRelIsoCorrected2012(ev.rho)<0.15 && phys.leptons[ilep].pt()>10);
	  }else{
	    isGood = ( hasObjectId(ev.en_idbits[lpid],EID_VBTF2011) && phys.leptons[ilep].relIsoRho(ev.rho)<0.1 && phys.leptons[ilep].pt()>10);
	  }
	    }
	nextraleptons += isGood;
	
	if(!isGood) continue;
	extraLeptonsP4.push_back( phys.leptons[ilep] );
      }
      bool pass3dLeptonVeto(nextraleptons==0);
      
      //
      //JET/MET ANALYSIS
      //
      std::vector<PhysicsObjectJetCollection> variedAJets;
      LorentzVectorCollection zvvs;
      METUtils::computeVariation(phys.ajets, phys.leptons, phys.met[0], variedAJets, zvvs, &jecUnc);
      PhysicsObjectJetCollection aJets= variedAJets[0];
      PhysicsObjectJetCollection aGoodIdJets;
      int nAJetsLoose(0), nABtags(0);
      for(size_t ijet=0; ijet<aJets.size(); ijet++) 
	{
	  if(aJets[ijet].pt()<15 || fabs(aJets[ijet].eta())>4.7 ) continue;
	  
	  bool isGoodJet = hasObjectId(aJets[ijet].pid,JETID_LOOSE);
	  isGoodJet     &= hasObjectId(aJets[ijet].pid,jetIdToApply);
	  if(!isGoodJet) continue;
	  aGoodIdJets.push_back(aJets[ijet]);
	  if(aJets[ijet].pt()>30 ) nAJetsLoose++;
	  if(aJets[ijet].pt()>30 && fabs(aJets[ijet].eta())<2.5) nABtags += (aJets[ijet].btag2>0.244);
	}
      bool passBveto(nABtags==0);
      bool passJetPt(false), passDetajj(false),passMjj(false);
      float hardpt, dphijj, maxPt, minPt, maxEta, minEta, detajj, mjj;
      int ncjv, htcjv, htcjvall;

      tags.push_back(tag_cat);

      if(hasTrigger) mon.fillHisto("eventflow",tags,0,weight);
      else           continue;

      if(passIdAndIso) mon.fillHisto("eventflow",tags,1,weight);
      else             continue;
      mon.fillHisto("zmass",    tags, zll.mass(), weight);  
      if(passZmass){

	//pu control
	mon.fillHisto("nvtx"     ,   tags, ev.nvtx,      weight);
	mon.fillHisto("nvtxraw"  ,   tags, ev.nvtx,      1);
	mon.fillHisto("rho"      ,   tags, ev.rho,       weight);
	mon.fillHisto("rho25"    ,   tags, ev.rho25Neut, weight);

	//basic Z and pu control
	mon.fillHisto("eventflow",   tags, 2,            weight);
	mon.fillHisto("zpt"      ,   tags, zll.pt(),     weight);      
	mon.fillHisto("zeta"     ,   tags, zll.eta(),    weight);
	
	if(passZpt){
	  mon.fillHisto  ("eventflow",tags,3,weight);
	  
	  //analyze dilepton kinematics
	  LorentzVector leadingLep(phys.leptons[0].pt()>phys.leptons[1].pt() ? phys.leptons[0]: phys.leptons[1]);
	  LorentzVector trailerLep(phys.leptons[0].pt()>phys.leptons[1].pt() ? phys.leptons[1]: phys.leptons[0]);
	  mon.fillHisto("leadeta"     ,   tags, leadingLep.eta()   ,weight);
	  mon.fillHisto("leadpt"      ,   tags, leadingLep.pt()    ,weight);
	  mon.fillHisto("trailereta"  ,   tags, trailerLep.eta()   ,weight);
	  mon.fillHisto("trailerpt"   ,   tags, trailerLep.pt()    ,weight);

	  //analyze also 3 lepton category
	  mon.fillHisto("nleptons",tags,2+nextraleptons,weight);
	  if(nextraleptons==1) 
	    {
	      mon.fillHisto("thirdleptoneta",   tags,fabs(extraLeptonsP4[0].eta())   ,weight);
	      mon.fillHisto("thirdleptonpt" ,   tags,extraLeptonsP4[0].pt()     ,weight);
	      mon.fillHisto("mt3",tags,METUtils::transverseMass(extraLeptonsP4[0],zvvs[0],false),weight);
	    }
	  
	  mon.fillHisto("eventflow",tags,4,weight);
	  mon.fillHisto("njets",    tags, nAJetsLoose,weight);
	  mon.fillHisto("nbtags",  tags, nABtags,weight);
	  int evcat=eventCategoryInst.Get(phys,&aGoodIdJets);
	  TString tag_subcat=eventCategoryInst.GetLabel(evcat);
	  if(tag_subcat=="geq1jets" || tag_subcat=="vbf")
	    {
	      if(nAJetsLoose==1)      tag_subcat="eq1jets";
	      else if(nAJetsLoose==2) tag_subcat="eq2jets";
	      else                    tag_subcat="geq3jets";
	    }
	  tags.push_back(tag_cat+tag_subcat);

	  mon.fillHisto("qt"          ,   tags, zll.pt()           ,weight,true);
	  if(nAJetsLoose>=2)
	    {
	      mon.fillHisto("eventflow",tags,5,weight);
	      
              //VBF region
	      mon.fillHisto("njetsvsavginstlumi", tags, nAJetsLoose,ev.curAvgInstLumi,weight);
	
	      if(!hasObjectId(aGoodIdJets[0].pid,jetIdToApply) || !hasObjectId(aGoodIdJets[1].pid,jetIdToApply)) continue; 
		
    	      LorentzVector vbfSyst=aGoodIdJets[0]+aGoodIdJets[1];
	      LorentzVector hardSyst=vbfSyst+zll; //+zvvs[0]
	      hardpt=hardSyst.pt();
	      mjj=vbfSyst.mass();
	      dphijj=deltaPhi(aGoodIdJets[0].phi(),aGoodIdJets[1].phi());
	      maxPt=max(aGoodIdJets[0].pt(),aGoodIdJets[1].pt());
	      minPt=min(aGoodIdJets[0].pt(),aGoodIdJets[1].pt());
	      maxEta=max(aGoodIdJets[0].eta(),aGoodIdJets[1].eta());
	      minEta=min(aGoodIdJets[0].eta(),aGoodIdJets[1].eta());
	      detajj=maxEta-minEta;
	      ncjv=0;
	      htcjv=0;
	      htcjvall=0;
	     
	      mon.fillHisto("vbfcandjetpt",  tags, maxPt,weight);
	      mon.fillHisto("vbfcandjetpt",  tags, minPt,weight);
	      mon.fillHisto("vbfcandjet1pt", tags, maxPt,weight);
	      mon.fillHisto("vbfcandjet2pt", tags, minPt,weight);
	      if(aGoodIdJets[0].pt()>30 && aGoodIdJets[1].pt()>30){
		
		passJetPt=true;
		for(size_t iotherjet=2; iotherjet<aGoodIdJets.size(); iotherjet++){
		  if(aGoodIdJets[iotherjet].eta()<minEta || aGoodIdJets[iotherjet].eta()>maxEta) continue;
		  if(!hasObjectId(aGoodIdJets[iotherjet].pid,jetIdToApply)) continue;
		  htcjvall +=aGoodIdJets[iotherjet].pt();
		  if(aGoodIdJets[iotherjet].pt()<30)continue;
		  htcjv    +=aGoodIdJets[iotherjet].pt();
		  ncjv++;
		}
		mon.fillHisto("vbfcandjet1eta",     tags, max(fabs(maxEta),fabs(minEta)),weight);
		mon.fillHisto("vbfcandjet2eta",     tags, min(fabs(maxEta),fabs(minEta)),weight);
		mon.fillHisto("vbfcandjeteta",      tags, fabs(maxEta),weight);
		mon.fillHisto("vbfcandjeteta",      tags, fabs(minEta),weight);
		mon.fillHisto("vbfcandjetdeta",     tags, fabs(detajj),weight);
		mon.fillHisto("vbfpremjj",          tags, mjj,weight);
		if(fabs(detajj)>4.5){
		  passDetajj=true;
		  mon.fillHisto("vbfmjj",          tags, mjj,weight);
		  
		  if(vbfSyst.mass()>450){
		    passMjj=true;
		    mon.fillHisto("vbfhardpt",     tags, hardpt,weight);
		    mon.fillHisto("vbfdphijj",     tags, fabs(dphijj),weight);
		    mon.fillHisto("vbfcjv",             tags, ncjv,weight);
		    mon.fillHisto("vbfhtcjv",           tags, htcjv,weight);
		    mon.fillHisto("vbfhtcjvall",        tags, htcjvall,weight);
		  }
		}
	      }
	      
	    }//end nAJetsLoose
  
	  //STATISTICAL ANALYSIS
	  for(size_t ivar=0; ivar<nvarsToInclude; ivar++){
	    float iweight = weight;                                               //nominal
	    if(ivar==9)                         iweight *=TotalWeight_plus;        //pu up
	    if(ivar==10)                        iweight *=TotalWeight_minus;       //pu down

	    int localNAJetsLoose(0),localNABtags(0);
	    PhysicsObjectJetCollection &varJets=variedAJets[ivar>4 ? 0  : ivar];
	    PhysicsObjectJetCollection tightVarJets;
	    for(size_t ijet=0; ijet<varJets.size(); ijet++){
	      if(varJets[ijet].pt()<30) continue;
	      if(!hasObjectId(varJets[ijet].pid,JETID_LOOSE)) continue;
	      if(!hasObjectId(varJets[ijet].pid,jetIdToApply)) continue;
	      tightVarJets.push_back( varJets[ijet] );
	      localNAJetsLoose++;
	      if(fabs(varJets[ijet].eta())<2.5)continue;
	      if(ivar==11)      localNABtags += (varJets[ijet].btag2>0.250);
	      else if(ivar==12) localNABtags += (varJets[ijet].btag2>0.240);
	      else              localNABtags += (varJets[ijet].btag2>0.244);
	    }
	    if(localNAJetsLoose<2) continue;
	    
	    //re-assign the event category;
	    int evcat=eventCategoryInst.Get(phys,&varJets);
	    tags.clear();
	    tags.push_back(tag_cat);
	    tags.push_back(tag_cat+eventCategoryInst.GetLabel(evcat));
	    for(unsigned int index=0; index<optim_Cuts2_z_pt.size();index++){
	      
	     float minZPt=optim_Cuts2_z_pt[index];
	     float minJetPt=optim_Cuts2_jet_pt[index];
       	     float minEtaGap=optim_Cuts2_eta_gap[index];
	     float minDijetMass=optim_Cuts2_dijet_mass[index];
	     LorentzVector vbfSyst=tightVarJets[0]+tightVarJets[1];
	     
	     bool passLocalZmass(fabs(zll.mass()-91)<15);
	     bool passLocalZpt(zll.pt()>minZPt && fabs(zll.eta())<1.4442); 
	     bool passLocalJet1Pt(varJets[0].pt()>minJetPt);
	     bool passLocalJet2Pt(varJets[1].pt()>minJetPt);
	     bool passLocalEtaGap(fabs(varJets[0].eta()-varJets[1].eta())>minEtaGap);	     
	     bool passLocalDijetMass(vbfSyst.M()>minDijetMass);
	     if(passLocalJet1Pt && passLocalJet2Pt && passLocalEtaGap && passLocalDijetMass && passLocalZmass && passLocalZpt /*&& pass3dLeptonVeto*/){
	       mon.fillHisto(TString("dijet_mass_shapes")+varNames[ivar],tags,index,vbfSyst.M(),iweight);
	     }
	    }
	  }
	}//end passZpt

	//
	//N-1 CONTROL
	//
	if(           (nAJetsLoose>=2) && passJetPt && passDetajj && passMjj)
	  {
	    mon.fillHisto("zptNM1"      ,   tags, zll.pt(),     weight);      
	    mon.fillHisto("zetaNM1"     ,   tags, zll.eta(),    weight);
	  } 
	if(passZpt && (nAJetsLoose>=2)              && passDetajj && passMjj)
	  {
	    mon.fillHisto("vbfcandjetptNM1",  tags, maxPt,weight);
	    mon.fillHisto("vbfcandjetptNM1",  tags, minPt,weight);
	    mon.fillHisto("vbfcandjet1ptNM1", tags, maxPt,weight);
	    mon.fillHisto("vbfcandjet2ptNM1", tags, minPt,weight);

	  } 
	if(passZpt && (nAJetsLoose>=2) && passJetPt               && passMjj)
	  {
	    mon.fillHisto("vbfcandjet1etaNM1",     tags, max(fabs(maxEta),fabs(minEta)),weight);
	    mon.fillHisto("vbfcandjet2etaNM1",     tags, min(fabs(maxEta),fabs(minEta)),weight);
	    mon.fillHisto("vbfcandjetetaNM1",      tags, fabs(maxEta),weight);
	    mon.fillHisto("vbfcandjetetaNM1",      tags, fabs(minEta),weight);
	    mon.fillHisto("vbfcandjetdetaNM1",     tags, fabs(detajj),weight);
	  } 
	if(passZpt && (nAJetsLoose>=2) && passJetPt && passDetajj           )
	  {
	    mon.fillHisto("vbfmjjNM1",          tags, mjj,weight);
	  } 

      }//end passZmass



      
  }
  
  printf("\n"); 
  file->Close();
  
  //##############################################
  //########     SAVING HISTO TO FILE     ########
  //##############################################
  //save control plots to file
  outUrl += "/";
  outUrl += outFileUrl + ".root";
  printf("Results save in %s\n", outUrl.Data());

  //save all to the file
  TFile *ofile=TFile::Open(outUrl, "recreate");
  mon.Write();
  ofile->Close();

  if(outTxtFile)fclose(outTxtFile);
}  





