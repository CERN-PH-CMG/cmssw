#ifndef _CMGTools_Common_RunInfoAccounting_h_
#define _CMGTools_Common_RunInfoAccounting_h_

#include "CommonTools/Utils/interface/TFileDirectory.h"
#include "FWCore/Framework/interface/Run.h"

#include "TTree.h"

#include <string>

namespace cmg {

  class RunInfoAccounting
  {
  public:
    RunInfoAccounting(TFileDirectory& myDir, const std::string& name);
    void processRunInfo(const edm::Run& aRun);
  
    double getPreSelectionWeight(){
      return preselectionWeight_;
    }
  
    double getEventWeight(){
      return eventWeight_;
    }
  
  private:
    double initialEvents_;
    double finalEvents_;
    double preselectionWeight_;
    double genCrossSection_;
    double genFilterEfficiency_;
    double eventWeight_;
  
    TTree* tree_;
  };

}

#endif
