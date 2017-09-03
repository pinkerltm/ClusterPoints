# -*- coding: utf-8 -*-

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
	return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
	return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
	return QtGui.QApplication.translate(context, text, disambig)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
	Dialog.setObjectName(_fromUtf8("Dialog"))
	Dialog.setWindowModality(QtCore.Qt.NonModal)
	Dialog.resize(374, 390)
	Dialog.setSizeGripEnabled(True)
	self.gridLayout = QtGui.QGridLayout(Dialog)
	self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
	self.vboxlayout = QtGui.QVBoxLayout()
	self.vboxlayout.setObjectName(_fromUtf8("vboxlayout"))
	self.label_3 = QtGui.QLabel(Dialog)
	self.label_3.setObjectName(_fromUtf8("label_3"))
	self.vboxlayout.addWidget(self.label_3)
	self.inShape = QtGui.QComboBox(Dialog)
	self.inShape.setObjectName(_fromUtf8("inShape"))
	self.vboxlayout.addWidget(self.inShape)
	self.gridLayout.addLayout(self.vboxlayout, 0, 0, 1, 1)
	self.verticalLayout = QtGui.QVBoxLayout()
	self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
	self.useSelectedA = QtGui.QCheckBox(Dialog)
	self.useSelectedA.setObjectName(_fromUtf8("useSelectedA"))
	self.verticalLayout.addWidget(self.useSelectedA)
	self.gridLayout.addLayout(self.verticalLayout, 1, 0, 1, 1)
	self.horizontalLayout = QtGui.QHBoxLayout()
	self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
	self.lblClustertype = QtGui.QLabel(Dialog)
	self.lblClustertype.setObjectName(_fromUtf8("lblClustertype"))
	self.horizontalLayout.addWidget(self.lblClustertype)
	self.cmbClustertype = QtGui.QComboBox(Dialog)
	self.cmbClustertype.setObjectName(_fromUtf8("cmbClustertype"))
	self.cmbClustertype.addItem(_fromUtf8(""))
	self.cmbClustertype.addItem(_fromUtf8(""))
	self.horizontalLayout.addWidget(self.cmbClustertype)
	self.gridLayout.addLayout(self.horizontalLayout, 2, 0, 1, 1)
	self.horizontalLayout0 = QtGui.QHBoxLayout()
	self.horizontalLayout0.setObjectName(_fromUtf8("horizontalLayout0"))
	self.lblLinkage = QtGui.QLabel(Dialog)
	self.lblLinkage.setObjectName(_fromUtf8("lblLinkage"))
	self.horizontalLayout0.addWidget(self.lblLinkage)
	self.cmbLinkage = QtGui.QComboBox(Dialog)
	self.cmbLinkage.setObjectName(_fromUtf8("cmbLinkage"))	  
	self.horizontalLayout0.addWidget(self.cmbLinkage)
	self.gridLayout.addLayout(self.horizontalLayout0, 3, 0, 1, 1)
	self.horizontalLayout1 = QtGui.QHBoxLayout()
	self.horizontalLayout1.setObjectName(_fromUtf8("horizontalLayout1"))
	self.lblDistance = QtGui.QLabel(Dialog)
	self.lblDistance.setObjectName(_fromUtf8("lblDistance"))
	self.horizontalLayout1.addWidget(self.lblDistance)
	self.cmbDistance = QtGui.QComboBox(Dialog)
	self.cmbDistance.setObjectName(_fromUtf8("cmbDistance"))
	self.cmbDistance.addItem(_fromUtf8(""))
	self.cmbDistance.addItem(_fromUtf8(""))
	self.horizontalLayout1.addWidget(self.cmbDistance)
	self.gridLayout.addLayout(self.horizontalLayout1, 4, 0, 1, 1)
	self.horizontalLayout2 = QtGui.QHBoxLayout()
	self.horizontalLayout2.setObjectName(_fromUtf8("horizontalLayout2"))
	self.lblNClust = QtGui.QLabel(Dialog)
	self.lblNClust.setObjectName(_fromUtf8("lblNClust"))
	self.horizontalLayout2.addWidget(self.lblNClust)
	self.spnNClust = QtGui.QSpinBox(Dialog)
	self.spnNClust.setMinimum(2)
	self.spnNClust.setProperty("value", 2)
	self.spnNClust.setObjectName(_fromUtf8("spnNClust"))
	self.horizontalLayout2.addWidget(self.spnNClust)
	self.gridLayout.addLayout(self.horizontalLayout2, 5, 0, 1, 1)
	self.vboxlayout3 = QtGui.QVBoxLayout()
	self.vboxlayout3.setObjectName(_fromUtf8("vboxlayout3"))
	self.label_2 = QtGui.QLabel(Dialog)
	self.label_2.setObjectName(_fromUtf8("label_2"))
	self.vboxlayout3.addWidget(self.label_2)
	self.hboxlayout1 = QtGui.QHBoxLayout()
	self.hboxlayout1.setObjectName(_fromUtf8("hboxlayout1"))
	self.outShape = QtGui.QLineEdit(Dialog)
	self.outShape.setReadOnly(True)
	self.outShape.setObjectName(_fromUtf8("outShape"))
	self.hboxlayout1.addWidget(self.outShape)
	self.toolOut = QtGui.QPushButton(Dialog)
	self.toolOut.setObjectName(_fromUtf8("toolOut"))
	self.hboxlayout1.addWidget(self.toolOut)
	self.vboxlayout3.addLayout(self.hboxlayout1)
	self.gridLayout.addLayout(self.vboxlayout3, 6, 0, 1, 1)
	self.addToCanvasCheck = QtGui.QCheckBox(Dialog)
	self.addToCanvasCheck.setChecked(True)
	self.addToCanvasCheck.setObjectName(_fromUtf8("addToCanvasCheck"))
	self.gridLayout.addWidget(self.addToCanvasCheck, 7, 0, 1, 1)
	self.horizontalLayout3 = QtGui.QHBoxLayout()
	self.horizontalLayout3.setObjectName(_fromUtf8("horizontalLayout3"))
	self.progressBar = QtGui.QProgressBar(Dialog)
	self.progressBar.setProperty("value", 0)
	self.progressBar.setAlignment(QtCore.Qt.AlignCenter)
	self.progressBar.setTextVisible(True)
	self.progressBar.setObjectName(_fromUtf8("progressBar"))
	self.horizontalLayout3.addWidget(self.progressBar)
	self.buttonBox_2 = QtGui.QDialogButtonBox(Dialog)
	self.buttonBox_2.setOrientation(QtCore.Qt.Horizontal)
	self.buttonBox_2.setStandardButtons(QtGui.QDialogButtonBox.Close|QtGui.QDialogButtonBox.Ok)
	self.buttonBox_2.setObjectName(_fromUtf8("buttonBox_2"))
	self.horizontalLayout3.addWidget(self.buttonBox_2)
	self.gridLayout.addLayout(self.horizontalLayout3, 8, 0, 1, 1)

	self.retranslateUi(Dialog)
	QtCore.QObject.connect(self.buttonBox_2, QtCore.SIGNAL(_fromUtf8("accepted()")), Dialog.accept)
	QtCore.QObject.connect(self.buttonBox_2, QtCore.SIGNAL(_fromUtf8("rejected()")), Dialog.close)
	QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
	Dialog.setWindowTitle(_translate("Dialog", "Generate Centroids", None))
	self.label_3.setText(_translate("Dialog", "Input vector layer", None))
	self.useSelectedA.setText(_translate("Dialog", "Use only selected features", None))
	self.lblClustertype.setText(_translate("Dialog", "Cluster type", None))
	self.cmbClustertype.setItemText(0, _translate("Dialog", "K-Means", None))
	self.cmbClustertype.setItemText(1, _translate("Dialog", "Hierarchical", None))
	self.lblLinkage.setText(_translate("Dialog", "Linkage type", None))	     
	self.lblDistance.setText(_translate("Dialog", "Distance type", None))
	self.cmbDistance.setItemText(0, _translate("Dialog", "Euclidean", None))
	self.cmbDistance.setItemText(1, _translate("Dialog", "Manhattan", None))
	self.lblNClust.setText(_translate("Dialog", "Number of clusters", None))
	self.label_2.setText(_translate("Dialog", "Output shapefile", None))
	self.toolOut.setText(_translate("Dialog", "Browse", None))
	self.addToCanvasCheck.setText(_translate("Dialog", "Add result to canvas", None))

