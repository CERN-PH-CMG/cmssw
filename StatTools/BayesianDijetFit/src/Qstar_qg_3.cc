/***************************************************************************** 
 * Project: RooFit                                                           * 
 *                                                                           * 
 * This code was autogenerated by RooClassFactory                            * 
 *****************************************************************************/ 

// Your description goes here... 

#include "Riostream.h" 

#include "StatTools/BayesianDijetFit/interface/Qstar_qg_3.h" 
#include "RooAbsReal.h" 
#include "RooAbsCategory.h" 


#include <math.h> 
#include "TH1D.h"
#include "TFile.h"
#include "TMath.h" 
#include "TCanvas.h"

#include <string>

#include "StatTools/BayesianDijetFit/interface/LineShapeDensityPdf.h"


//--------------------------------------------------------------------
//  The main constructor.
//--------------------------------------------------------------------
Qstar_qg_3::Qstar_qg_3(const char *name, const char *title, 
                       RooAbsReal& _mjj,
		       RooAbsReal& _jes,
		       RooAbsReal& _jer,
                       RooAbsReal& _mass, RooAbsReal& iResonance) :
  RooAbsPdf(name,title), 
  mjj("mjj","Observable",this,_mjj),
  jes("jes","Jet Energy Scale",this,_jes),
  jer("jer","Jet Energy Resolution",this,_jer),
  mass("mass","Resonance Mass",this,_mass),
  M_CUT(890.0),
  INIT_MASS(1000.)
{ 
//  std::cout << "iResonance = " << iResonance << std::endl;


  

  int uR = TMath::Abs(iResonance.getVal());



  if ( (uR > 20 && uR < 29) ||(uR > 120 && uR < 129)) M_CUT = 526.0;
  if ( (uR > 20 && uR < 29) ||(uR > 120 && uR < 129)) INIT_MASS = 600.0;

  if ( uR > 200 && uR < 2010 ) M_CUT = 500.0;
  if ( uR > 200 && uR < 2010 ) INIT_MASS = 600.0;


  if ( uR > 1000 && uR < 2000 ) M_CUT = 890.0;
  if ( uR > 1000 && uR < 1020 ) INIT_MASS = 1000.0;
  if ( uR > 1100 && uR < 2000 ) {
    int nDim = (uR-1000)/100;
    int mD = (uR-1000) - nDim*100;
    INIT_MASS = mD*1000.0;

  }

  if ( uR > 2000 && uR < 3000 ) M_CUT = 890.0;
  if ( uR > 2000 && uR < 3000 ) INIT_MASS = 1000.0;

  if ( uR > 3000 && uR < 4000 ) M_CUT = 890.0;
  if ( uR > 3000 && uR < 4000 ) INIT_MASS = 1000.0;

  cout << "M_CUT = " << M_CUT << " INIT_MASS = " << INIT_MASS << endl;

  int bin_cut = TMath::Abs((M_CUT-SHAPE_BINS_MIN)/SHAPE_BINS_STEPS)+1;


  double m0[ N_MASS_POINTS ];
  for(int i=0; i<N_MASS_POINTS; i++) {
    m0[i]=INIT_MASS+i*MASS_STEPS;
  }


  string stitle("");

  switch (uR){

  case 11: 
    stitle = string("RSGraviton_ak5_GGtoGG_fat30");
     break;
  case 12:   
    stitle = string("RSGraviton_ak5_QQtoQQ_fat30");
     break;
  case 13:   
    stitle = string("Qstar_ak5_fat30"); 
     break;
  case 21: 
    stitle = string("RSGraviton_HLT_ak5_GGtoGG_fat30");
     break;
  case 22:   
    stitle = string("RSGraviton_HLT_ak5_QQtoQQ_fat30");
     break;
  case 23:   
    stitle = string("Qstar_HLT_ak5_fat30"); 
     break;
  case 121: 
    stitle = string("RSGraviton_HLT_ak5_GGtoGG_pf");
     break;
  case 122:   
    stitle = string("RSGraviton_HLT_ak5_QQtoQQ_pf");
     break;
  case 123:   
    stitle = string("Qstar_HLT_ak5_pf"); 
     break;
  case 201:
    stitle = string("ZprimeToTTbar");
     break;
  case 1005:
    stitle = string("QBH5_ak5_fat"); 
    break;
  case 1006:
    stitle = string("QBH6_ak5_fat"); 
    break;
  case 1007:
    stitle = string("QBH7_ak5_fat"); 
    break;
  case 1008:
    stitle = string("QBH8_ak5_fat"); 
    break;
  case 1009:
    stitle = string("QBH9_ak5_fat"); 
    break;
  case 1010:
    stitle = string("QBH10_ak5_fat"); 
    break;
  case 1502: 
    stitle = string("QBH52_ak5_fat");
    break;
  case 1503: 
    stitle = string("QBH53_ak5_fat");
    break;
  case 1504: 
    stitle = string("QBH54_ak5_fat");
    break;
  case 1505: 
    stitle = string("QBH55_ak5_fat");
    break;
  case 1602: 
    stitle = string("QBH62_ak5_fat");
    break;
  case 1603: 
    stitle = string("QBH63_ak5_fat");
    break;
  case 1604: 
    stitle = string("QBH64_ak5_fat");
    break;
  case 1605: 
    stitle = string("QBH65_ak5_fat");
    break;
  case 1702: 
    stitle = string("QBH72_ak5_fat");
    break;
  case 1703: 
    stitle = string("QBH73_ak5_fat");
    break;
  case 1704: 
    stitle = string("QBH74_ak5_fat");
    break;
  case 1705: 
    stitle = string("QBH75_ak5_fat");
    break;
  case 1802: 
    stitle = string("QBH82_ak5_fat");
    break;
  case 1803: 
    stitle = string("QBH83_ak5_fat");
    break;
  case 1804: 
    stitle = string("QBH84_ak5_fat");
    break;
  case 1805: 
    stitle = string("QBH85_ak5_fat");
    break;
  case 1902: 
    stitle = string("QBH92_ak5_fat");
    break;
  case 1903: 
    stitle = string("QBH93_ak5_fat");
    break;
  case 1904: 
    stitle = string("QBH94_ak5_fat");
    break;
  case 1905: 
    stitle = string("QBH95_ak5_fat");
    break;
  case 1102: 
    stitle = string("QBH102_ak5_fat");
    break;
  case 1103: 
    stitle = string("QBH103_ak5_fat");
    break;
  case 1104: 
    stitle = string("QBH104_ak5_fat");
    break;
  case 1105: 
    stitle = string("QBH105_ak5_fat");
    break;
  case 2001:
    stitle = string("Qstar_qW_ak5_fat"); 
    break;
  case 2002:
    stitle = string("Qstar_qZ_ak5_fat");
    break;
  case 2011:
    stitle = string("RSGraviton_WW_ak5_fat");
    break;
  case 2012:
    stitle = string("RSGraviton_WZ_ak5_fat");
    break;
  case 2013:
    stitle = string("RSGraviton_ZZ_ak5_fat");
    break;
  case 2014:
    stitle = string("RSGraviton_ZZ_01_ak5_fat");
    break;
  case 3111:
    stitle = string("RSGravitonGG_k0p1_fat30_ak5");
    break;
  case 3311:
    stitle = string("RSGravitonGG_k0p3_fat30_ak5");
    break;
  case 3511:
    stitle = string("RSGravitonGG_k0p5_fat30_ak5");
    break;
  case 3711:
    stitle = string("RSGravitonGG_k0p7_fat30_ak5");
    break;
  case 3911:
    stitle = string("RSGravitonGG_k0p9_fat30_ak5");
    break;
  case 3112:
    stitle = string("RSGravitonQQ_k0p1_fat30_ak5");
    break;
  case 3312:
    stitle = string("RSGravitonQQ_k0p3_fat30_ak5");
    break;
  case 3512:
    stitle = string("RSGravitonQQ_k0p5_fat30_ak5");
    break;
  case 3712:
    stitle = string("RSGravitonQQ_k0p7_fat30_ak5");
    break;
  case 3912:
    stitle = string("RSGravitonQQ_k0p9_fat30_ak5");
    break;
  default:
    std::cout << "Nothing would crash" << std::endl; 
    break;
  }
 
  string sout("Resonance_Shapes"); sout = sout + "_" + stitle + ".root";


  TFile * output = new TFile(sout.c_str(),"RECREATE");

  TH1D* eff = new TH1D("Efficiency", "cut efficiency", N_MASS_POINTS-1, INIT_MASS-MASS_STEPS/2, INIT_MASS+(N_MASS_POINTS-1)*MASS_STEPS-MASS_STEPS/2);

  for (int j = 0; j < N_MASS_POINTS; j++) {
    mass_points[j] = m0[j];
    double resmass = m0[j];
    std::cout << "Generating histogram for resonance mass = " << resmass << std::endl;
    char * histname = new char[100];
    sprintf (histname,"h_qstar_%d", (int)(resmass) );

    //--- Make the shape for this resonance mass.
    LineShapeDensity_pdf(resmass,  uR);

    // make the histograms
    hist[j]=new TH1D(histname, stitle.c_str(), N_SHAPE_BINS, SHAPE_BINS_MIN, SHAPE_BINS_MIN+N_SHAPE_BINS*SHAPE_BINS_STEPS);
    hist_cdf[j]=new TH1D(TString(histname)+"_cdf", stitle.c_str(), N_SHAPE_BINS, SHAPE_BINS_MIN, SHAPE_BINS_MIN+N_SHAPE_BINS*SHAPE_BINS_STEPS);


    for(int i=1; i<=N_SHAPE_BINS; i++) {
      double mss = hist[j]->GetBinCenter(i);
      double prob = FastQstarBinnedProb(mss);
      //      if (mss < 900 && mss > 880) cout << "mss = " << mss << " i = " << i << " prob = " << prob << endl; 
      hist[j]->SetBinContent(i, prob);
    }
    for(int i=1; i<=N_SHAPE_BINS; i++) {
      if (hist[j]->GetBinContent(i)<0.0) hist[j]->SetBinContent(i,0.0);
    }
    // re-normalize the histogram
    double integral=hist[j]->GetSumOfWeights()*SHAPE_BINS_STEPS;
    hist[j]->Scale(1/integral);

    // compute the cdf
    for(int i=1; i<=N_SHAPE_BINS; i++) {
      double prev=hist_cdf[j]->GetBinContent(i-1);
      double curr=hist[j]->GetBinContent(i)*SHAPE_BINS_STEPS;
      hist_cdf[j]->SetBinContent(i, prev+curr);
    }

    cout <<"bin_cut is = " << bin_cut << " min val at this bin is " << hist_cdf[j]->GetBinLowEdge(bin_cut) << " bin width is " << hist_cdf[j]->GetBinWidth(bin_cut) << " at mass " << resmass << " the efficiency is " << 1-hist_cdf[j]->GetBinContent(bin_cut) << endl;

    eff->SetBinContent(j+1, 1-hist_cdf[j]->GetBinContent(bin_cut));

    //--- Save all histograms, for backup.
    output->cd(); 

     hist[j]->Write();
    hist_cdf[j]->Write();
  }

  output->cd(); 
  eff->Write();
  // output->Close();
 

  return;
} 


//--------------------------------------------------------------------
// Copy constructor
//--------------------------------------------------------------------
Qstar_qg_3::Qstar_qg_3(const Qstar_qg_3& other, const char* name) :  
  RooAbsPdf(other,name), 
  mjj("mjj",this,other.mjj),
  jes("jes",this,other.jes),
  jer("jer",this,other.jer),
  mass("mass",this,other.mass),
  M_CUT(other.M_CUT),
  INIT_MASS(other.INIT_MASS)
{ 
  // Er, we should have something in there too...
  for (int j = 0; j < N_MASS_POINTS; j++) {
    mass_points[j] = other.mass_points[j];
    hist[j] = (TH1D*) other.hist[j]->Clone();
    hist_cdf[j] = (TH1D*) other.hist_cdf[j]->Clone();
  }
} 

Int_t Qstar_qg_3::findHistFast( double m ) const
{

  double val=(m-INIT_MASS)/MASS_STEPS+0.001;
  return static_cast<int>(val);
}

Double_t Qstar_qg_3::interpolate(Double_t mass, Double_t* histarray) const
{
  double binfloat=(mass-SHAPE_BINS_MIN)/SHAPE_BINS_STEPS;
  int binint=static_cast<int>(binfloat);
  int binlo, binhi;
  double frac;
  if(binfloat-binint<0.5) {
    binlo=binint-1;
    binhi=binint;
    frac=binfloat-binint+0.5;
  } else {
    binlo=binint;
    binhi=binint+1;
    frac=binfloat-binint-0.5;
  }
  if(binlo<0) return histarray[0];
  if(binhi>=N_SHAPE_BINS) return histarray[N_SHAPE_BINS-1];

  /*  
  if (mass < 900.) cout << "mass = " << mass << " density = " << histarray[binlo+1]*(1-frac)+histarray[binhi+1]*frac 
			 << " binlo = " << binlo << " binhi = " << binhi << " frac = "<< frac 
			 << " histarray[binlo] = " << histarray[binlo+1] << " histarray[binhi] = " << histarray[binhi+1] << endl;
  */

  return histarray[binlo+1]*(1-frac)+histarray[binhi+1]*frac;
}

Double_t Qstar_qg_3::evaluate() const 
{ 
  Int_t j = findHistFast( mass );
  Double_t* array = hist[j]->GetArray();
  return interpolate(jes*(jer*(mjj-mass)+mass), array);


}


Int_t Qstar_qg_3::getAnalyticalIntegral(RooArgSet& allVars, RooArgSet& analVars, const char* /*rangeName*/) const  
{ 
  //  if (matchArgs(allVars,analVars,mjj)) return 1 ; 
  return 0 ;
} 


Double_t Qstar_qg_3::analyticalIntegral(Int_t code, const char* rangeName) const
{
  assert(code==1);
  Double_t *histarray=hist_cdf[findHistFast(mass)]->GetArray();
  double xmin = mjj.min(rangeName);
  double xmax = mjj.max(rangeName);
  double xminprime = jes*(jer*(xmin-mass)+mass);
  double xmaxprime = jes*(jer*(xmax-mass)+mass);
  double lo = interpolate(xminprime, histarray);
  double hi = interpolate(xmaxprime, histarray);

  //  if(mjj.min(rangeName)<230 && mjj.max(rangeName)>3140) {
  //    hi=histarray[N_SHAPE_BINS-1];
  //    lo=histarray[0];
  //  }

  //  std::cout << "mjj.min=" << xmin << "; mjj.max=" << xmax
  //	    << "; jes=" << jes << "; jer=" << jer << "; mass=" << mass << std::endl;
  //  std::cout << "Computing integral from " << xminprime << " to " << xmaxprime << std::endl;
  //  std::cout << "hi=" << hi << "; lo=" << lo << "; integral=" << (hi-lo) << std::endl;
  //  std::cout << std::endl;
  
  return (hi-lo);
}



Int_t Qstar_qg_3::getGenerator(const RooArgSet& directVars, RooArgSet &generateVars, Bool_t /*staticInitOK*/) const 
{ 
  if (matchArgs(directVars,generateVars,mjj)) return 1 ;
  return 0 ; 
} 



void Qstar_qg_3::generateEvent(Int_t code) 
{ 
  assert(0) ; 
  return; 
} 

ClassImp(Qstar_qg_3)
