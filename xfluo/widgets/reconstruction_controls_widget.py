# #########################################################################
# Copyright (c) 2018, UChicago Argonne, LLC. All rights reserved.         #
#                                                                         #
# Copyright 2018. UChicago Argonne, LLC. This software was produced       #
# under U.S. Government contract DE-AC02-06CH11357 for Argonne National   #
# Laboratory (ANL), which is operated by UChicago Argonne, LLC for the    #
# U.S. Department of Energy. The U.S. Government has rights to use,       #
# reproduce, and distribute this software.  NEITHER THE GOVERNMENT NOR    #
# UChicago Argonne, LLC MAKES ANY WARRANTY, EXPRESS OR IMPLIED, OR        #
# ASSUMES ANY LIABILITY FOR THE USE OF THIS SOFTWARE.  If software is     #
# modified to produce derivative works, such modified software should     #
# be clearly marked, so as not to confuse it with the version available   #
# from ANL.                                                               #
#                                                                         #
# Additionally, redistribution and use in source and binary forms, with   #
# or without modification, are permitted provided that the following      #
# conditions are met:                                                     #
#                                                                         #
#     * Redistributions of source code must retain the above copyright    #
#       notice, this list of conditions and the following disclaimer.     #
#                                                                         #
#     * Redistributions in binary form must reproduce the above copyright #
#       notice, this list of conditions and the following disclaimer in   #
#       the documentation and/or other materials provided with the        #
#       distribution.                                                     #
#                                                                         #
#     * Neither the name of UChicago Argonne, LLC, Argonne National       #
#       Laboratory, ANL, the U.S. Government, nor the names of its        #
#       contributors may be used to endorse or promote products derived   #
#       from this software without specific prior written permission.     #
#                                                                         #
# THIS SOFTWARE IS PROVIDED BY UChicago Argonne, LLC AND CONTRIBUTORS     #
# "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT       #
# LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS       #
# FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL UChicago     #
# Argonne, LLC OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT,        #
# INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING,    #
# BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;        #
# LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER        #
# CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT      #
# LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN       #
# ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE         #
# POSSIBILITY OF SUCH DAMAGE.                                             #
# #########################################################################


from PyQt5 import QtCore, QtWidgets


class ReconstructionControlsWidget(QtWidgets.QWidget):

    def __init__(self):
        super(ReconstructionControlsWidget, self).__init__()

        self.initUI()

    def initUI(self):
        button1size = 250
        button2size = 122.5
        button3size = 78.3
        button4size = 58.75
        self.combo = QtWidgets.QComboBox(self)
        self.combo.setMaximumWidth(button1size)
        self.combo.setMinimumWidth(button1size)
        self.method = QtWidgets.QComboBox(self)
        self.method.setMaximumWidth(button1size)
        self.method.setMinimumWidth(button1size)
        self.btn = QtWidgets.QPushButton('Sinogram')
        self.btn.setMaximumWidth(button1size)
        self.btn.setMinimumWidth(button1size)

        self.save = QtWidgets.QPushButton("Save tiff files")
        self.save.setMaximumWidth(button4size)
        self.save.setMinimumWidth(button4size)
        self.save.setHidden(True)
        self.sld = QtWidgets.QSlider(QtCore.Qt.Horizontal, self)
        self.sld.setMaximumWidth(button4size)
        self.sld.setMinimumWidth(button4size)
        self.lbl = QtWidgets.QLabel("")
        self.lbl.setMaximumWidth(button3size)
        self.lbl.setMinimumWidth(button3size)

        self.cbox = QtWidgets.QCheckBox("")
        self.cbox.setMaximumWidth(21)
        self.cbox.setMinimumWidth(20)
        self.lbl2 = QtWidgets.QLabel("Center")
        self.lbl2.setMaximumWidth(52.3)
        self.lbl2.setMinimumWidth(52.3)
        self.centerLbl = QtWidgets.QLineEdit("0")
        self.centerLbl.setMaximumWidth(160)
        self.centerLbl.setMinimumWidth(160)
        self.threshLbl = QtWidgets.QLabel("threshold")
        self.threshLbl.setMaximumWidth(button3size)
        self.threshLbl.setMinimumWidth(button3size)
        self.threshLe = QtWidgets.QLineEdit("")
        self.threshLe.setMaximumWidth(button3size)
        self.threshLe.setMinimumWidth(button3size)
        self.threshBtn = QtWidgets.QPushButton("Apply")
        self.threshBtn.setMaximumWidth(button3size)
        self.threshBtn.setMinimumWidth(button3size)

        self.centerLbl.setEnabled(False)
        self.methodname = ["mlem", "gridrec", "art", "pml_hybrid", "pml_quad"]

        self.mulBtn = QtWidgets.QPushButton("x 10")
        self.mulBtn.setMaximumWidth(button2size)
        self.mulBtn.setMinimumWidth(button2size)
        self.divBtn = QtWidgets.QPushButton("/ 10")
        self.divBtn.setMaximumWidth(button2size)
        self.divBtn.setMinimumWidth(button2size)
        self.maxLbl = QtWidgets.QLabel("Max")
        self.maxLbl.setMaximumWidth(button2size)
        self.maxLbl.setMinimumWidth(button2size)
        self.minLbl = QtWidgets.QLabel("Min")
        self.minLbl.setMaximumWidth(button2size)
        self.minLbl.setMinimumWidth(button2size)
        self.itersName = QtWidgets.QLabel("Iteration")
        self.itersName.setMaximumWidth(button2size)
        self.itersName.setMinimumWidth(button2size)
        self.betaName = QtWidgets.QLabel("Beta")
        self.betaName.setMaximumWidth(button2size)
        self.betaName.setMinimumWidth(button2size)
        self.deltaName = QtWidgets.QLabel("Delta")
        self.deltaName.setMaximumWidth(button2size)
        self.deltaName.setMinimumWidth(button2size)
        self.iters = QtWidgets.QLineEdit("10")
        self.iters.setMaximumWidth(button2size)
        self.iters.setMinimumWidth(button2size)
        self.beta = QtWidgets.QLineEdit("1")
        self.beta.setMaximumWidth(button2size)
        self.beta.setMinimumWidth(button2size)
        self.delta = QtWidgets.QLineEdit("0.01")
        self.delta.setMaximumWidth(button2size)
        self.delta.setMinimumWidth(button2size)
        self.maxText = QtWidgets.QLineEdit()
        self.maxText.setMaximumWidth(button2size)
        self.maxText.setMinimumWidth(button2size)
        self.minText = QtWidgets.QLineEdit()
        self.minText.setMaximumWidth(button2size)
        self.minText.setMinimumWidth(button2size)
       
        centerBox = QtWidgets.QHBoxLayout()
        centerBox.addWidget(self.cbox)
        centerBox.addWidget(self.lbl2)
        centerBox.addWidget(self.centerLbl)
        threshBox = QtWidgets.QHBoxLayout()
        threshBox.addWidget(self.threshLbl)
        threshBox.addWidget(self.threshLe)
        threshBox.addWidget(self.threshBtn)
        mdBox = QtWidgets.QHBoxLayout()
        mdBox.addWidget(self.mulBtn)
        mdBox.addWidget(self.divBtn)
        maxBox = QtWidgets.QHBoxLayout()
        maxBox.addWidget(self.maxLbl)
        maxBox.addWidget(self.maxText)
        minBox = QtWidgets.QHBoxLayout()
        minBox.addWidget(self.minLbl)
        minBox.addWidget(self.minText)
        itersBox = QtWidgets.QHBoxLayout()
        itersBox.addWidget(self.itersName)
        itersBox.addWidget(self.iters)
        betaBox = QtWidgets.QHBoxLayout()
        betaBox.addWidget(self.betaName)
        betaBox.addWidget(self.beta)
        deltaBox = QtWidgets.QHBoxLayout()
        deltaBox.addWidget(self.deltaName)
        deltaBox.addWidget(self.delta)

        for k in range(len(self.methodname)):
            self.method.addItem(self.methodname[k])
        vb = QtWidgets.QVBoxLayout()
        vb.addWidget(self.combo)
        vb.addWidget(self.method)
        vb.addWidget(self.btn)
        vb.addWidget(self.save)
        vb.addLayout(centerBox)
        vb.addLayout(threshBox)
        vb.addWidget(self.sld)
        vb.addWidget(self.lbl)
        vb.addLayout(mdBox)
        vb.addLayout(maxBox)
        vb.addLayout(minBox)
        vb.addLayout(itersBox)
        vb.addLayout(betaBox)
        vb.addLayout(deltaBox)
        self.setLayout(vb)