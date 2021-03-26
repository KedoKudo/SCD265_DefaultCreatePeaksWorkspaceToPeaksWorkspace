#!/usr/bin/env python
from mantid.simpleapi import *

#-- default, regular PeaksWorkspaces with an instrument specified
sampleWs = CreateSampleWorkspace()
pws_withInst = CreatePeaksWorkspace(
    InstrumentWorkspace=sampleWs,
    NumberOfPeaks=3,
    )

#-- defualt, regular Peaksworkspace without specifying an instrument
pws_withoutInst = CreatePeaksWorkspace(NumberOfPeaks=3)

#-- lean pws, Lean Elastic Peaksworkspace without specifying an instrument
lpws = CreatePeaksWorkspace(
    NumberOfPeaks=3,
    OutputType="Lean",
    )

#-- lean pws, Lean Elastic Peakworkspace with specifying an instrument, which is ignored
lpws_ignoreInst = CreatePeaksWorkspace(
    InstrumentWorkspace=sampleWs,
    NumberOfPeaks=3,
    OutputType="Lean",
    )
