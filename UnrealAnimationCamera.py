import maya.cmds as mc

windowID = "CameraWindowID"
if mc.window(windowID, q= True, exists = True):
    mc.deleteUI(windowID)

mc.window(windowID,rtf = True, wh = (50,50), title = "Unreal Anim Camera Generator")
mc.showWindow(windowID)
PrimaryLayout = mc.columnLayout()
InfoGatherLayout = mc.rowColumnLayout(nc = 3)
mc.text(l = "Camera To Export: ")
cameraNameTextField = mc.textField(w = 300)
camerAssignBtn = mc.button(l = "<<<", c = "CameraAssignBtnCmd()")
mc.setParent(PrimaryLayout)
mc.rowColumnLayout(nc = 7, cw = (50,50))
mc.text(l = "PositionOffset:   ")
mc.text(l = "X:")
XOffset = mc.floatField()
mc.text(l = "     Y:")
YOffset = mc.floatField()
mc.text(l = "      Z:")
ZOffset = mc.floatField()
mc.setParent(PrimaryLayout)
mc.rowColumnLayout(nc = 3)
CreateButton = mc.button(l = "Create", w= 200, c = "createCameraBtnCmd()")
mc.separator(w = 20, style = "none")
CancelButton = mc.button(l = "cancel", w= 200)

def getSelection():
    selection = mc.ls(sl = True)[0]
    return selection
    
def setTextField(textFieldToSet, Value):
    mc.textField(textFieldToSet, e = True, text = Value)
    
def CameraAssignBtnCmd():
    cam = getSelection()
    setTextField(cameraNameTextField, cam)

def createCameraBtnCmd():
    origionalCam = mc.textField(cameraNameTextField, q = True, text = True)
    ExportCam = mc.camera(n = "Camera_To_Export")[0]
    
    XOffsetValue = mc.floatField(XOffset, q = True, v = True)
    YOffsetValue = mc.floatField(YOffset, q = True, v = True)
    ZOffsetValue = mc.floatField(ZOffset, q = True, v = True)
    
    pointConst = mc.pointConstraint(origionalCam, ExportCam, mo = False)[0]
    
    mc.setAttr(pointConst + ".offsetX", XOffsetValue)
    mc.setAttr(pointConst + ".offsetZ", YOffsetValue)
    mc.setAttr(pointConst + ".offsetY", ZOffsetValue)
    
    orientConst = mc.orientConstraint(origionalCam, ExportCam, mo = False)[0]
    mc.setAttr(orientConst + ".offsetY", 90)