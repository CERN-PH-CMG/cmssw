
 #include "CMGTools/H2TauTau/plugins/TauEleFlatNtp.h"
 #include "TauAnalysis/SVFitStandAlone/interface/NSVfitStandaloneAlgorithm2011.h"
 #include "TauAnalysis/CandidateTools/interface/NSVfitStandaloneAlgorithm.h"


TauEleFlatNtp::TauEleFlatNtp(const edm::ParameterSet & iConfig):
   BaseFlatNtp(iConfig)
{
}


TauEleFlatNtp::~TauEleFlatNtp(){

}


void TauEleFlatNtp::beginJob(){

  BaseFlatNtp::beginJob();
  //  tree_->Branch("",&_,"/F");

  tree_->Branch("mumvaid",&mumvaid_,"mumvaid/F");
  tree_->Branch("tauantiemva",&tauantiemva_,"tauantiemva/F");


  //counters
  counterev_=0;
  counterveto_=0;
  counterpresel_=0;
  countermuvtx_=0;
  countermuid_=0;
  countermuiso_=0;
  countermumatch_=0;
  countertaueop_=0;
  countertauvtx_=0;
  countertaumuveto_=0;
  countertaueveto_=0;
  countertauiso_=0;
  countertaumatch_=0;
  countertruth_=0;
}



 bool TauEleFlatNtp::fillVariables(const edm::Event & iEvent, const edm::EventSetup & iSetup){

   if(!BaseFlatNtp::fillVariables(iEvent,iSetup)) return 0;


   ///get the TauEle cands 
   iEvent.getByLabel(diTauTag_,diTauList_);

   return 1;
 }

 bool TauEleFlatNtp::applySelections(){
 

   //if none are selected returns 0
   diTauSel_=NULL;

   //trigger, n-vertex selection
   if(!BaseFlatNtp::applySelections()){
     if(printSelectionPass_)cout<<runnumber_<<":"<<eventid_<<" fail counterev"<<endl;
     return 0;
   }
   counterev_++;

   ////
   if(vetoDiLepton()){
     if(printSelectionPass_)cout<<runnumber_<<":"<<eventid_<<" fail counterveto"<<endl;
     return 0;
   }
   counterveto_++;


   std::vector<cmg::TauEle> tmpditaulist=*diTauList_;
   diTauSelList_.clear();

//    ///basic skims which should have been applied in H2TAUTAU step  
//    for(std::vector<cmg::TauEle>::const_iterator cand=tmpditaulist.begin(); cand!=tmpditaulist.end(); ++cand){    
//      if(cand->mass()>10.0
// 	&& cand->leg1().pt() > tauPtCut_
// 	&& fabs(cand->leg1().eta()) < tauEtaCut_
// 	&& cand->leg1().tauID("decayModeFinding") > 0.5
// 	&& cand->leg2().pt() > muPtCut_
// 	&& fabs(cand->leg2().eta()) < muEtaCut_
// 	)     
//        diTauSelList_.push_back(*cand);
     
//    }
//    if(diTauSelList_.size()==0) return 0;
//    counterpresel_++;
//    if(printSelectionPass_)cout<<runnumber_<<":"<<eventid_<<" fail counterpresel"<<endl;


   //muon vtx 
   //   tmpditaulist=diTauSelList_;
   //   diTauSelList_.clear();
   for(std::vector<cmg::TauEle>::const_iterator cand=tmpditaulist.begin(); cand!=tmpditaulist.end(); ++cand){    
//      if( fabs(cand->leg2().dxy())>0.045)continue;
//      if( fabs(cand->leg2().dz())>0.1 )continue;

     if(!((*(cand->leg2().sourcePtr()))->gsfTrack().isNonnull()))continue;
     if(!((*(cand->leg2().sourcePtr()))->gsfTrack().isAvailable()))continue;     
     if(fabs((*(cand->leg2().sourcePtr()))->gsfTrack()->dxy(PV_->position())) > 0.045 ) continue;
     if(fabs((*(cand->leg2().sourcePtr()))->gsfTrack()->dz(PV_->position()))  > 0.2 ) continue;


     diTauSelList_.push_back(*cand);
   }
   if(diTauSelList_.size()==0){
     if(printSelectionPass_)cout<<runnumber_<<":"<<eventid_<<" fail countermuvtx"<<endl;
     return 0;
   }
   countermuvtx_++;



   //ele id cuts
   tmpditaulist=diTauSelList_;
   diTauSelList_.clear();
   for(std::vector<cmg::TauEle>::const_iterator cand=tmpditaulist.begin(); cand!=tmpditaulist.end(); ++cand){    
     if(cand->leg2().numberOfHits()!=0) continue;
     diTauSelList_.push_back(*cand);
   }
   if(diTauSelList_.size()==0 && printSelectionPass_)cout<<runnumber_<<":"<<eventid_<<" fail cand->leg2().numberOfHits()"<<endl;

   tmpditaulist=diTauSelList_;
   diTauSelList_.clear();
   for(std::vector<cmg::TauEle>::const_iterator cand=tmpditaulist.begin(); cand!=tmpditaulist.end(); ++cand){    
     if(cand->leg2().passConversionVeto()!=1) continue; 
     diTauSelList_.push_back(*cand);
   }
   if(diTauSelList_.size()==0 && printSelectionPass_)cout<<runnumber_<<":"<<eventid_<<" fail cand->leg2().passConversionVeto()"<<endl;

//    tmpditaulist=diTauSelList_;
//    diTauSelList_.clear();
//    for(std::vector<cmg::TauEle>::const_iterator cand=tmpditaulist.begin(); cand!=tmpditaulist.end(); ++cand){    
//      if(!electronIDWP95(&(cand->leg2())))continue;     
//      diTauSelList_.push_back(*cand);
//    }
//    if(diTauSelList_.size()==0 && printSelectionPass_)cout<<runnumber_<<":"<<eventid_<<" fail electronIDWP95"<<endl;

   tmpditaulist=diTauSelList_;
   diTauSelList_.clear();
   for(std::vector<cmg::TauEle>::const_iterator cand=tmpditaulist.begin(); cand!=tmpditaulist.end(); ++cand){    
     //look here https://twiki.cern.ch/twiki/bin/view/CMS/MultivariateElectronIdentification
     float mvaid=cand->leg2().mvaNonTrigV0();
     float eta=(*(cand->leg2().sourcePtr()))->superCluster()->eta();
     //cout<<eta<<" "<<mvaid<<endl;
     if(fabs(eta)<0.8)
       if(mvaid<0.925)continue; 
     if(0.8<=fabs(eta)&&fabs(eta)<1.479)
       if(mvaid<0.975)continue;
     if(1.479<=fabs(eta))
       if(mvaid<0.985)continue; 
     
     diTauSelList_.push_back(*cand);
   }
   if(diTauSelList_.size()==0){
     if(printSelectionPass_)cout<<runnumber_<<":"<<eventid_<<" fail countermuid"<<endl;
     return 0;
   }
   countermuid_++;

//   /////////electron iso
//   tmpditaulist=diTauSelList_;
//   diTauSelList_.clear();
//   for(std::vector<cmg::TauEle>::const_iterator cand=tmpditaulist.begin(); cand!=tmpditaulist.end(); ++cand){    
//     if( electronRelIsoDBCorr( &(cand->leg2()) ) < 0.1){
//       diTauSelList_.push_back(*cand);
//     }
//   }
//   if(diTauSelList_.size()==0){
//     if(printSelectionPass_)cout<<runnumber_<<":"<<eventid_<<" fail countermuiso"<<endl;
//     return 0;
//   }
//   countermuiso_++;


   //muon trig-match
   tmpditaulist=diTauSelList_;
   diTauSelList_.clear();
   for(std::vector<cmg::TauEle>::const_iterator cand=tmpditaulist.begin(); cand!=tmpditaulist.end(); ++cand){    
     bool matchmu=0;
     if(trigPaths_.size()==0) matchmu=1;//no match requirement
     for(std::vector<edm::InputTag*>::const_iterator path=trigPaths_.begin(); path!=trigPaths_.end(); path++){
       if(trigObjMatch(cand->leg2().eta(),cand->leg2().phi(),(*path)->label(),(*path)->process()),11)
 	  matchmu=1;
     }
  
     if(matchmu) 
       diTauSelList_.push_back(*cand);
   }
   if(diTauSelList_.size()==0){
     if(printSelectionPass_)cout<<runnumber_<<":"<<eventid_<<" fail countermumatch"<<endl;
     return 0;
   }
   countermumatch_++;


//    //Tau E/P cut  ---> This is not needed for this channel as Z->mumu is not a problem
//    tmpditaulist=diTauSelList_;
//    diTauSelList_.clear();
//    for(std::vector<cmg::TauEle>::const_iterator cand=tmpditaulist.begin(); cand!=tmpditaulist.end(); ++cand){    
//      if(cand->leg1().decayMode()==0&&cand->leg1().p()>0.)
//        if(cand->leg1().eOverP()<0.2)
//  	continue;
  
//      diTauSelList_.push_back(*cand);
//    }
   if(diTauSelList_.size()==0){
     if(printSelectionPass_)cout<<runnumber_<<":"<<eventid_<<" fail countertaueop"<<endl;
     return 0;
   }
   countertaueop_++;


   //tau vtx
   tmpditaulist=diTauSelList_;
   diTauSelList_.clear();
   for(std::vector<cmg::TauEle>::const_iterator cand=tmpditaulist.begin(); cand!=tmpditaulist.end(); ++cand){    
     //if(fabs(cand->leg1().dxy())>0.045) continue;
     //if(fabs(cand->leg1().dz())>0.2 ) continue;
      
    if(fabs(computeDxy(cand->leg1().leadChargedHadrVertex(),cand->leg1().p4()))>0.045)continue;
    if(fabs(computeDz(cand->leg1().leadChargedHadrVertex(),cand->leg1().p4()))>0.2)continue;

    
     diTauSelList_.push_back(*cand);
   }
   if(diTauSelList_.size()==0){
     if(printSelectionPass_)cout<<runnumber_<<":"<<eventid_<<" fail countertauvtx"<<endl;
     return 0;
   }
   countertauvtx_++;


   //Tau anti-mu cut
   tmpditaulist=diTauSelList_;
   diTauSelList_.clear();
   for(std::vector<cmg::TauEle>::const_iterator cand=tmpditaulist.begin(); cand!=tmpditaulist.end(); ++cand){    
     if(cand->leg1().tauID("againstMuonLoose")<0.5)continue;
     diTauSelList_.push_back(*cand);
   }
   if(diTauSelList_.size()==0){
     if(printSelectionPass_)cout<<runnumber_<<":"<<eventid_<<" fail countertaumuveto"<<endl;
     return 0;
   }
   countertaumuveto_++;


   //Tau anti-e cut
   tmpditaulist=diTauSelList_;
   diTauSelList_.clear();
   for(std::vector<cmg::TauEle>::const_iterator cand=tmpditaulist.begin(); cand!=tmpditaulist.end(); ++cand){    
     if(cand->leg1().tauID("againstElectronMedium")<0.5)continue;
     if(cand->leg1().tauID("againstElectronMVA")<0.5)continue;
     if(cand->leg1().tauID("againstElectronTightMVA2")<0.5)continue; 
     diTauSelList_.push_back(*cand);
   }
   if(diTauSelList_.size()==0){
     if(printSelectionPass_)cout<<runnumber_<<":"<<eventid_<<" fail countertaueveto"<<endl;
     return 0;
   }
   countertaueveto_++;


//   /////////Tau Isolation
//   tmpditaulist=diTauSelList_;
//   diTauSelList_.clear();
//   for(std::vector<cmg::TauEle>::const_iterator cand=tmpditaulist.begin(); cand!=tmpditaulist.end(); ++cand){    
//     if(cand->leg1().tauID("byLooseIsoMVA")>0.5){
//       diTauSelList_.push_back(*cand);
//     }
//   }
//   if(diTauSelList_.size()==0){
//     if(printSelectionPass_)cout<<runnumber_<<":"<<eventid_<<" fail countertauiso"<<endl;
//     return 0;
//   }
//   countertauiso_++;

   //Tau Trig-Match
   tmpditaulist=diTauSelList_;
   diTauSelList_.clear();
   for(std::vector<cmg::TauEle>::const_iterator cand=tmpditaulist.begin(); cand!=tmpditaulist.end(); ++cand){    
     bool matchtau=0;
     if(trigPaths_.size()==0)matchtau=1;//no match requirement
     for(std::vector<edm::InputTag*>::const_iterator path=trigPaths_.begin(); path!=trigPaths_.end(); path++){
       if(trigObjMatch(cand->leg1().eta(),cand->leg1().phi(),(*path)->label(),(*path)->instance(),15)
	  || trigObjMatch(cand->leg1().eta(),cand->leg1().phi(),(*path)->label(),(*path)->instance(),0))
 	  matchtau=1;
     }
  
     if(matchtau)
       diTauSelList_.push_back(*cand);
   }
   if(diTauSelList_.size()==0){
     if(printSelectionPass_)cout<<runnumber_<<":"<<eventid_<<" fail countertaumatch"<<endl;
     return 0;
   }
   countertaumatch_++;


   /////////Isolation cuts
   tmpditaulist=diTauSelList_;
   diTauSelList_.clear();
   for(std::vector<cmg::TauEle>::const_iterator cand=tmpditaulist.begin(); cand!=tmpditaulist.end(); ++cand){    

     if(
        //-------iso cut here
	//cand->leg2().relIso(0.5) < 0.1
	electronRelIsoDBCorr( &(cand->leg2()) ) < 0.1
	
        //-------tau iso cut here
        // && cand->leg1().tauID("byLooseCombinedIsolationDeltaBetaCorr") > 0.5
	&& cand->leg1().tauID("byLooseIsoMVA")>0.5

        ){
       diTauSelList_.push_back(*cand);
     }
   }

   categoryIso_=1;//category gets set to "signal" by default
   nditau_=diTauSelList_.size();
   if(diTauSelList_.size()==0){//no isolated candidates were found, see if there are any anti-isolated ones
     categoryIso_=2;//category gets set to "sideband" if there was no candidate in the signal box
     for(std::vector<cmg::TauEle>::const_iterator cand = tmpditaulist.begin(); cand != tmpditaulist.end(); ++cand)
       diTauSelList_.push_back(*cand);
   }


   //choose the best candidate
   nditau_=diTauSelList_.size();//keep track of the number of candidates per event
   diTauSel_=&(*diTauSelList_.begin());
   double highsumpt=diTauSel_->leg1().pt()+diTauSel_->leg2().pt();
   for(std::vector<cmg::TauEle>::const_iterator cand=diTauSelList_.begin(); cand!=diTauSelList_.end(); ++cand)
     if(cand->leg1().pt()+cand->leg2().pt()>highsumpt){
       diTauSel_=&(*cand);
       highsumpt=diTauSel_->leg1().pt()+diTauSel_->leg2().pt();
     }



   //truth match 
   truthEventType_=0;
   if(genBoson_)
     fillTruthEventType(diTauSel_->leg1().eta(),diTauSel_->leg1().phi(),diTauSel_->leg2().eta(),diTauSel_->leg2().phi());
   if(sampleTruthEventType_>0)
     if(sampleTruthEventType_!=truthEventType_){
       if(printSelectionPass_)cout<<runnumber_<<":"<<eventid_<<" fail countertruth"<<endl;
       return 0;
     }
   countertruth_++;

   
   return 1;
 }

bool TauEleFlatNtp::fill(){

  BaseFlatNtp::fill();

  /////mu and tau trigger efficiency weight
  eventweight_=1.;
  triggerEffWeight_=1.;
  triggerEffWeightMu_=1.;
  triggerEffWeightTau_=1.;
  selectionEffWeight_=1.;
  selectionEffWeightId_=1.;
  selectionEffWeightIso_=1.;

  for(long i=0;i<5;i++){
    triggerEffWeightsMu_[i]=1.;
    triggerEffWeightsTau_[i]=1.;
    selectionEffWeightsId_[i]=1.;
    selectionEffWeightsIso_[i]=1.;
  }

  if(dataType_==0 || dataType_==2){
  
    ///trigger corrections
    if(dataPeriodFlag_==2011){
      if(trigPaths_.size()>0){//trigger applied--> apply a correction factor
	if(triggerEff_.effMediumIsoTau20MC(diTauSel_->leg1().pt(),diTauSel_->leg1().eta())>0.)
	  triggerEffWeight_ *= triggerEff_.effTau2011AB_TauEle(diTauSel_->leg1().pt(),diTauSel_->leg1().eta())
	    /triggerEff_.effMediumIsoTau20MC(diTauSel_->leg1().pt(),diTauSel_->leg1().eta());
	if(triggerEff_.effEle18MC(diTauSel_->leg2().pt(),diTauSel_->leg2().eta())>0.)
	  triggerEffWeight_ *= triggerEff_.effEle2011AB(diTauSel_->leg2().pt(),diTauSel_->leg2().eta())
	    /triggerEff_.effEle18MC(diTauSel_->leg2().pt(),diTauSel_->leg2().eta());
      }else{//no trigger applied --> apply efficiency
	triggerEffWeight_ *= triggerEff_.effTau2011AB_TauEle(diTauSel_->leg1().pt(),diTauSel_->leg1().eta());
	triggerEffWeight_ *= triggerEff_.effEle2011AB(diTauSel_->leg2().pt(),diTauSel_->leg2().eta());
      }
      //id+isolation corrections
      selectionEffWeight_ *= selectionEff_.effCorrEle2011AB(diTauSel_->leg2().pt(),diTauSel_->leg2().eta());
    }

    if(dataPeriodFlag_==2012){
       
      if(trigPaths_.size()>0){

	if(triggerEff_.eff2012Tau20MC53X_TauEle(diTauSel_->leg1().pt(),diTauSel_->leg1().eta())>0.)
	  triggerEffWeightsTau_[0] = triggerEff_.effTau2012AB_TauEle(diTauSel_->leg1().pt(),diTauSel_->leg1().eta())
	    /triggerEff_.eff2012Tau20MC53X_TauEle(diTauSel_->leg1().pt(),diTauSel_->leg1().eta()); 
	if(triggerEff_.eff_2012_Rebecca_TauEle_Ele2253XMC(diTauSel_->leg2().pt(),diTauSel_->leg2().eta())>0.)
	  triggerEffWeightsMu_[0] =  triggerEff_.effEle2012AB(diTauSel_->leg2().pt(),diTauSel_->leg2().eta())
	    /triggerEff_.eff_2012_Rebecca_TauEle_Ele2253XMC(diTauSel_->leg2().pt(),diTauSel_->leg2().eta());
	if(triggerEff_.eff2012Tau20MC53X_TauEle(diTauSel_->leg1().pt(),diTauSel_->leg1().eta())>0.)
	  triggerEffWeightsTau_[1] = triggerEff_.effTau2012ABC_TauEle(diTauSel_->leg1().pt(),diTauSel_->leg1().eta())
	    /triggerEff_.eff2012Tau20MC53X_TauEle(diTauSel_->leg1().pt(),diTauSel_->leg1().eta());
	if(triggerEff_.eff_2012_Rebecca_TauEle_Ele2253XMC(diTauSel_->leg2().pt(),diTauSel_->leg2().eta())>0.)
	  triggerEffWeightsMu_[1] = triggerEff_.effEle2012_Rebecca_TauEle_ABC(diTauSel_->leg2().pt(),diTauSel_->leg2().eta())
	    /triggerEff_.eff_2012_Rebecca_TauEle_Ele2253XMC(diTauSel_->leg2().pt(),diTauSel_->leg2().eta());
	if(triggerEff_.effTau_eTau_MC_2012D(diTauSel_->leg1().pt(),diTauSel_->leg1().eta())>0.)
	  triggerEffWeightsTau_[2] = triggerEff_.effTau_eTau_Data_2012D(diTauSel_->leg1().pt(),diTauSel_->leg1().eta())
	    /triggerEff_.effTau_eTau_MC_2012D(diTauSel_->leg1().pt(),diTauSel_->leg1().eta());
	if(triggerEff_.eff_2012_Rebecca_TauEle_Ele2253XMC(diTauSel_->leg2().pt(),diTauSel_->leg2().eta())>0.)
	  triggerEffWeightsMu_[2] = triggerEff_.effEle_eTau_Data_2012D(diTauSel_->leg2().pt(),diTauSel_->leg2().eta())
	    /triggerEff_.eff_2012_Rebecca_TauEle_Ele2253XMC(diTauSel_->leg2().pt(),diTauSel_->leg2().eta());
	if(triggerEff_.effTau_eTau_MC_2012ABCD(diTauSel_->leg1().pt(),diTauSel_->leg1().eta())>0.)
	  triggerEffWeightsTau_[3] = triggerEff_.effTau_eTau_Data_2012ABCD(diTauSel_->leg1().pt(),diTauSel_->leg1().eta())
	    /triggerEff_.effTau_eTau_MC_2012ABCD(diTauSel_->leg1().pt(),diTauSel_->leg1().eta());
	if(triggerEff_.effEle_eTau_MC_2012ABCD(diTauSel_->leg2().pt(),diTauSel_->leg2().eta())>0.)
	  triggerEffWeightsMu_[3] = triggerEff_.effEle_eTau_Data_2012ABCD(diTauSel_->leg2().pt(),diTauSel_->leg2().eta())
	    /triggerEff_.effEle_eTau_MC_2012ABCD(diTauSel_->leg2().pt(),diTauSel_->leg2().eta());


	 
      }else{//no trigger applied --> apply Data efficiency
	triggerEffWeightsTau_[0] = triggerEff_.effTau2012AB_TauEle(diTauSel_->leg1().pt(),diTauSel_->leg1().eta());
	triggerEffWeightsMu_[0] =   triggerEff_.effEle2012AB(diTauSel_->leg2().pt(),diTauSel_->leg2().eta());
	triggerEffWeightsTau_[1] = triggerEff_.effTau2012ABC_TauEle(diTauSel_->leg1().pt(),diTauSel_->leg1().eta());
	triggerEffWeightsMu_[1] = triggerEff_.effEle2012_Rebecca_TauEle_ABC(diTauSel_->leg2().pt(),diTauSel_->leg2().eta());
	triggerEffWeightsTau_[2] =  triggerEff_.effTau_eTau_Data_2012D(diTauSel_->leg1().pt(),diTauSel_->leg1().eta());
	triggerEffWeightsMu_[2] = triggerEff_.effEle_eTau_Data_2012D(diTauSel_->leg2().pt(),diTauSel_->leg2().eta());
	triggerEffWeightsTau_[3] =  triggerEff_.effTau_eTau_Data_2012ABCD(diTauSel_->leg1().pt(),diTauSel_->leg1().eta());
	triggerEffWeightsMu_[3] = triggerEff_.effEle_eTau_Data_2012ABCD(diTauSel_->leg2().pt(),diTauSel_->leg2().eta());
	 
      }

      //id
      selectionEffWeightsId_[0] = selectionEff_.effCorrEle2012AB(diTauSel_->leg2().pt(),diTauSel_->leg2().eta());
      selectionEffWeightsId_[1] = selectionEff_.effCorrEleID2012ABC(diTauSel_->leg2().pt(),diTauSel_->leg2().eta());
      selectionEffWeightsId_[2] = selectionEff_.effCorrEleID2012D(diTauSel_->leg2().pt(),diTauSel_->leg2().eta());
      selectionEffWeightsId_[3] = selectionEff_.effCorrEleID2012ABCD(diTauSel_->leg2().pt(),diTauSel_->leg2().eta());

      //isolation
      if(dataType_==0){
	selectionEffWeightsIso_[0] = 1.;//need to separate
	selectionEffWeightsIso_[1] = selectionEff_.effCorrEleIso2012ABC(diTauSel_->leg2().pt(),diTauSel_->leg2().eta());
	selectionEffWeightsIso_[2] = selectionEff_.effCorrEleIso2012D(diTauSel_->leg2().pt(),diTauSel_->leg2().eta());
	selectionEffWeightsIso_[3] = selectionEff_.effCorrEleIso2012ABCD(diTauSel_->leg2().pt(),diTauSel_->leg2().eta());
      }
    }
     
  }

   
  ///////////////check some filter paths
  for(long p=0;p<10;p++){  trigPath_[p]=0;  trigTest_[p]=0;}
  int i=0;
  for(std::vector<edm::InputTag *>::const_iterator path=trigPaths_.begin(); path!=trigPaths_.end(); path++){//cmg ObjetSel
    if(trig_->begin()->hasSelection((*path)->label())){
      if(trig_->begin()->getSelection((*path)->label())){
	//trigPath_[i]=1;

	if(trigObjMatch(diTauSel_->leg2().eta(),diTauSel_->leg2().phi(),(*path)->label(),(*path)->process(),11)
	   &&
	   (trigObjMatch(diTauSel_->leg1().eta(),diTauSel_->leg1().phi(),(*path)->label(),(*path)->instance(),15)
	    ||trigObjMatch(diTauSel_->leg1().eta(),diTauSel_->leg1().phi(),(*path)->label(),(*path)->instance(),0)
	    )
	   )trigPath_[i]=1;
	
      }
    }
    i++;
  }
  int j=0;
  for(std::vector<edm::InputTag *>::const_iterator path=trigPathsTest_.begin(); path!=trigPathsTest_.end(); path++){//cmg ObjetSel
    if(trig_->begin()->hasSelection((*path)->label())){
      if(trig_->begin()->getSelection((*path)->label())){
	
	//trigTest_[j]=1;
	if(trigObjMatch(diTauSel_->leg2().eta(),diTauSel_->leg2().phi(),(*path)->label(),(*path)->process(),11)
	   &&
	   (trigObjMatch(diTauSel_->leg1().eta(),diTauSel_->leg1().phi(),(*path)->label(),(*path)->instance(),15)
	    ||trigObjMatch(diTauSel_->leg1().eta(),diTauSel_->leg1().phi(),(*path)->label(),(*path)->instance(),0)
	    )
	   )trigTest_[i]=1;
	
      }
    }
    j++;
  }
  ///////////////



   mupt_=diTauSel_->leg2().pt();
   mueta_=diTauSel_->leg2().eta();
   muphi_=diTauSel_->leg2().phi();
   muiso_= electronRelIsoDBCorr( &(diTauSel_->leg2()) ); //diTauSel_->leg2().relIso(0.5);
   muisomva_=(*(diTauSel_->leg2().sourcePtr()))->userFloat("mvaIsoRings");
   mudz_=diTauSel_->leg2().dz();
   mudxy_=diTauSel_->leg2().dxy();
   mux_=diTauSel_->leg2().vertex().x();
   muy_=diTauSel_->leg2().vertex().y();
   muz_=diTauSel_->leg2().vertex().z();
   mutruth_=truthMatchLeg(diTauSel_->leg2().eta(),diTauSel_->leg2().phi(),mutruthpt_,mutrutheta_,mutruthstatus_);
   mumvaid_=diTauSel_->leg2().mvaNonTrigV0();
   mucharge_=diTauSel_->leg2().charge();

   taumass_=diTauSel_->leg1().p4().M();
   taupt_=diTauSel_->leg1().pt();
   taueta_=diTauSel_->leg1().eta();
   tauphi_=diTauSel_->leg1().phi();
   taudz_=diTauSel_->leg1().dz();
   taudxy_=diTauSel_->leg1().dxy();
   tautruth_=truthMatchLeg(diTauSel_->leg1().eta(),diTauSel_->leg1().phi(),tautruthpt_,tautrutheta_,tautruthstatus_);
   tauehop_=diTauSel_->leg1().eOverP();
   taueop_=diTauSel_->leg1().leadChargedHadrEcalEnergy()/diTauSel_->leg1().p();
   tauhoe_=diTauSel_->leg1().leadChargedHadrHcalEnergy()/diTauSel_->leg1().leadChargedHadrEcalEnergy();
   taudecaymode_=diTauSel_->leg1().decayMode();
   taux_=diTauSel_->leg1().leadChargedHadrVertex().x();
   tauy_=diTauSel_->leg1().leadChargedHadrVertex().y();
   tauz_=diTauSel_->leg1().leadChargedHadrVertex().z();
   tauiso_=diTauSel_->leg1().relIso(0.5);
   tauisomva_=diTauSel_->leg1().tauID("byRawIsoMVA");
   taucharge_=diTauSel_->leg1().charge();

   tauleadpt_=diTauSel_->leg1().leadChargedHadrPt();  
   tauleadhcal_=diTauSel_->leg1().leadChargedHadrHcalEnergy();
   tauleadecal_=diTauSel_->leg1().leadChargedHadrEcalEnergy();

   tauantie_=0;
   if(diTauSel_->leg1().tauID("againstElectronLoose")>0.5)tauantie_=1;
   if(diTauSel_->leg1().tauID("againstElectronMedium")>0.5)tauantie_=2;
   if(diTauSel_->leg1().tauID("againstElectronTight")>0.5)tauantie_=3;
   tauantiemva_=0;
   if(diTauSel_->leg1().tauID("againstElectronMVA")>0.5)tauantiemva_=1;
   tauantimu_=0;
   if(diTauSel_->leg1().tauID("againstMuonLoose")>0.5)tauantimu_=1;
   if(diTauSel_->leg1().tauID("againstMuonMedium")>0.5)tauantimu_=2;
   if(diTauSel_->leg1().tauID("againstMuonTight")>0.5)tauantimu_=3;
   tauisodisc_=0;
   if(diTauSel_->leg1().tauID("byVLooseCombinedIsolationDeltaBetaCorr")>0.5)tauisodisc_=1;
   if(diTauSel_->leg1().tauID("byLooseCombinedIsolationDeltaBetaCorr")>0.5)tauisodisc_=2;
   if(diTauSel_->leg1().tauID("byMediumCombinedIsolationDeltaBetaCorr")>0.5)tauisodisc_=3;
   if(diTauSel_->leg1().tauID("byTightCombinedIsolationDeltaBetaCorr")>0.5)tauisodisc_=4;
   tauisodiscmva_=0;
   if(diTauSel_->leg1().tauID("byLooseIsoMVA")>0.5)tauisodiscmva_=1;
   if(diTauSel_->leg1().tauID("byMediumIsoMVA")>0.5)tauisodiscmva_=2;
   if(diTauSel_->leg1().tauID("byTightIsoMVA")>0.5)tauisodiscmva_=3;


   ditaumass_=diTauSel_->mass();
   ditaucharge_=diTauSel_->charge();
   ditaueta_=diTauSel_->eta();
   ditaupt_=diTauSel_->pt();
   ditauphi_=diTauSel_->phi();
   svfitmass_=0.;//diTauSel_->massSVFit();
   ditaudeltaR_= reco::deltaR(diTauSel_->leg1().p4().eta(),diTauSel_->leg1().p4().phi(),
			      diTauSel_->leg2().p4().eta(),diTauSel_->leg2().p4().phi()
			      ); 
   ditaudeltaEta_=diTauSel_->leg2().p4().eta()-diTauSel_->leg1().p4().eta();;
   ditaudeltaPhi_=diTauSel_->leg2().p4().phi()-diTauSel_->leg1().p4().phi();;
   
   
   ///get the jets //need the jets here because of randomization of mT
   edm::Handle< std::vector<cmg::PFJet> > eventJetList;
   iEvent_->getByLabel(pfJetListTag_,eventJetList);
   fullJetList_.clear();
   for(std::vector<cmg::PFJet>::const_iterator jet=eventJetList->begin(); jet!=eventJetList->end(); ++jet)
     fullJetList_.push_back(&(*jet));

   //apply pt and eta cuts on jets
   fillPFJetList(&fullJetList_,&pfJetList_);
   fillPFJetListLC(diTauSel_->leg1().eta(),diTauSel_->leg1().phi(),diTauSel_->leg2().eta(),diTauSel_->leg2().phi(),&pfJetList_,&pfJetListLC_);
   fillPFJetListLepLC(diTauSel_->leg2().eta(),diTauSel_->leg2().phi(),&pfJetList_,&pfJetListLepLC_);
   fillJetVariables();

   //jets of pt>20
   fillPFJetList20(&fullJetList_,&pfJetList20_);
   fillPFJetListLC(diTauSel_->leg1().eta(),diTauSel_->leg1().phi(),diTauSel_->leg2().eta(),diTauSel_->leg2().phi(),&pfJetList20_,&pfJetList20LC_);
   fillJetVariables20();
   //fillBTagWeight();

   //B-jets
   fillPFJetListBTag(&pfJetList20LC_,&pfJetListBTagLC_);
   fillPFJetListBTagLoose(&pfJetList20LC_,&pfJetListBTagLCLoose_);
   fillBJetVariables();

 //   ///---- b-jets
//    fillPFJetListB(&fullJetList_,&pfJetListB_);
//    fillPFJetListLC(diTauSel_->leg1().eta(),diTauSel_->leg1().phi(),diTauSel_->leg2().eta(),diTauSel_->leg2().phi(),&pfJetListB_,&pfJetListBLC_);
//    fillPFJetListBTag(&pfJetListBLC_,&pfJetListBTagLC_);
//    fillBJetVariables();
//    fillBTagWeight();


   //find the jet matching to the tau
   taujetpt_=0.;
   taujeteta_=0.;
   const cmg::PFJet * taujet = findJet(&fullJetList_,diTauSel_->leg1().eta(),diTauSel_->leg1().phi());
   if(taujet) taujetpt_=taujet->pt();
   if(taujet) taujeteta_=taujet->eta();
   //find the jet matching to the mu
   mujetpt_=0.;
   mujeteta_=0.;
   const cmg::PFJet * mujet = findJet(&fullJetList_,diTauSel_->leg2().eta(),diTauSel_->leg2().phi());
   if(mujet) mujetpt_=mujet->pt();
   if(mujet) mujeteta_=mujet->eta();
  


   //////////////MET/////////////////
   metSig_=0;
   metpt_=0.;
   metphi_=0.;
   //needed for mva MET
   diobjectmet_=diTauSel_->met();
   diobjectindex_=0;
   for(std::vector<cmg::TauEle>::const_iterator cand=diTauList_->begin(); cand!=diTauList_->end(); ++cand){
     if(cand->mass()==diTauSel_->mass()) break;
     diobjectindex_++;
   }
   fillMET();
  
   //
   pftransversemass_=sqrt(2*mupt_*pfmetpt_*(1-cos(muphi_-pfmetphi_)));
   transversemass_=sqrt(2*mupt_*metP4_.pt()*(1-cos(muphi_-metP4_.phi())));
   compZeta(diTauSel_->leg2().p4(),diTauSel_->leg1().p4(),metP4_.px(),metP4_.py(),&pZeta_,&pZetaVis_);

   ///----SVFit
   taup4_=diTauSel_->leg1().p4();
   mup4_=diTauSel_->leg2().p4();
   runSVFit();



   //VBF 
   vbfmva_=0.;
   if(njet20_>=2) fillVBFMVA();
   vbfmva2012_=0.;
   if(njet20_>=2) fillVBFMVA2012();


   return 1;
 }

 void TauEleFlatNtp::analyze(const edm::Event & iEvent, const edm::EventSetup & iSetup){

   fillVariables(iEvent,iSetup);
   if(!applySelections()) return;
   fill();
   tree_->Fill();
 }



 bool TauEleFlatNtp::vetoDiLepton(){

   bool muminus=0;
   bool muplus=0;
   for(std::vector<cmg::Electron>::const_iterator m=leptonVetoListElectron_->begin(); m!=leptonVetoListElectron_->end(); ++m){  
     if(m->pt()<=15.0)continue;
     if(fabs(m->eta())>=2.5)continue;
     if(fabs((*(m->sourcePtr()))->gsfTrack()->dz(PV_->position()))  > 0.2 ) continue;     
     if(!electronIDWP95(&(*m)))continue;
     if( electronRelIsoDBCorr( &(*m) )>=0.3 ) continue; 

     if(m->charge()==-1)muminus=1;
     if(m->charge()==1)muplus=1;
   }
   if(muminus&&muplus) return 1;

   //3rd lepton veto
   int nleptons=0;
   for(std::vector<cmg::Muon>::const_iterator m=leptonVetoListMuon_->begin(); m!=leptonVetoListMuon_->end(); ++m){  
     if(m->pt()<=10.0)continue;
     if(fabs(m->eta())>=2.4)continue;
     if(!(m->isTracker()))continue; 
     if(!(m->isGlobal()))continue; 
     if((*(m->sourcePtr()))->userFloat("isPFMuon")<0.5) continue;
     if(!(m->normalizedChi2() < 10))continue;
     if(!(m->numberOfValidMuonHits() > 0))continue; 
     if(!(m->numberOfMatches() > 1))continue; //cout<<"pass"<<endl;
     if(!(m->trackerLayersWithMeasurement() > 5))continue; 
   
     ///this is crashing saying track is not there , so must check 
     if(!((*(m->sourcePtr()))->innerTrack().isNonnull()))continue;
     if(!((*(m->sourcePtr()))->innerTrack().isAvailable()))continue;
     if(!((*(m->sourcePtr()))->innerTrack()->hitPattern().numberOfValidPixelHits() > 0))continue;
     if(fabs((*(m->sourcePtr()))->innerTrack()->dz(PV_->position()))  > 0.2 ) continue;
     if(fabs((*(m->sourcePtr()))->innerTrack()->dxy(PV_->position())) > 0.045 ) continue;
    
     if(m->relIso(0.5,1)>=0.3)continue;        
     nleptons++;
   }
   for(std::vector<cmg::Electron>::const_iterator m=leptonVetoListElectron_->begin(); m!=leptonVetoListElectron_->end(); ++m){  
     if(m->pt()<=10.0)continue;
     if(fabs(m->eta())>=2.5)continue;
     if(m->numberOfHits()!=0) continue;
     if(m->passConversionVeto()!=1) continue;

     if(!((*(m->sourcePtr()))->gsfTrack().isNonnull()))continue;
     if(!((*(m->sourcePtr()))->gsfTrack().isAvailable()))continue;     
     if(fabs((*(m->sourcePtr()))->gsfTrack()->dxy(PV_->position())) > 0.045 ) continue;
     if(fabs((*(m->sourcePtr()))->gsfTrack()->dz(PV_->position()))  > 0.2 ) continue;

     float mvaid=m->mvaNonTrigV0();
     float eta=(*(m->sourcePtr()))->superCluster()->eta();
     if(m->pt()<20){
       if(fabs(eta)<0.8)                  if(mvaid<0.925)continue; 
       if(0.8<=fabs(eta)&&fabs(eta)<1.479)if(mvaid<0.915)continue;
       if(1.479<=fabs(eta))               if(mvaid<0.965)continue; 
     }
     if(m->pt()>=20){
       if(fabs(eta)<0.8)                  if(mvaid<0.905)continue; 
       if(0.8<=fabs(eta)&&fabs(eta)<1.479)if(mvaid<0.955)continue;
       if(1.479<=fabs(eta))               if(mvaid<0.975)continue; 
     }

     if( electronRelIsoDBCorr( &(*m) )>=0.3 ) continue; 
     nleptons++;
   }

   if(nleptons>=2)return 1;
   
   return 0;
 }


 void TauEleFlatNtp::endJob(){
   BaseFlatNtp::endJob();
   cout<<"counterev = "<<counterev_<<endl;
   cout<<"counterveto = "<<counterveto_<<endl;
   cout<<"counterpresel = "<<counterpresel_<<endl;
   cout<<"countermuvtx = "<<countermuvtx_<<endl;
   cout<<"countermuid = "<<countermuid_<<endl;
   cout<<"countermuiso = "<<countermuiso_<<endl;
   cout<<"countermumatch = "<<countermumatch_<<endl;
   cout<<"countertaueop = "<<countertaueop_<<endl;
   cout<<"countertauvtx = "<<countertauvtx_<<endl;
   cout<<"countertaumuveto = "<<countertaumuveto_<<endl;
   cout<<"countertaueveto = "<<countertaueveto_<<endl;
   cout<<"countertauiso = "<<countertauiso_<<endl;
   cout<<"countertaumatch = "<<countertaumatch_<<endl;
   cout<<"countertruth = "<<countertruth_<<endl;

 }

 #include "FWCore/Framework/interface/MakerMacros.h"

 DEFINE_FWK_MODULE(TauEleFlatNtp);


