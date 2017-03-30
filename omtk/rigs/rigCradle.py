from omtk import constants
from omtk.core import classRig
from omtk.core import className

class CradleNomenclature(className.BaseName):

    root_jnt_name = 'root_jnt'

    def __init__(self, *args, **kwargs):
        super(CradleNomenclature, self).__init__(*args, **kwargs)


class RigCradle(classRig.Rig):
    """
    Custom rig implementation in respect to Cradle Studio nomenclature
    """

    DEFAULT_UPP_AXIS = constants.Axis.y
    LEGACY_ARM_IK_CTRL_ORIENTATION = True
    LEGACY_LEG_IK_CTRL_ORIENTATION = True

    def __init__(self, *args, **kwargs):
        super(RigCradle, self).__init__(*args, **kwargs)
        self._color_ctrl = True

    def _get_nomenclature_cls(self):
        return CradleNomenclature

    def pre_build(self):
        super(RigCradle, self).pre_build(create_master_grp=True, create_layer_jnt=True)
        
def register_plugin():
    return RigCradle