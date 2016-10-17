name = 'omtk_cradle'

version = '0.0.1'

description = 'Cradle rig plugin definition for omtk'

def commands():
    env.OMTK_PLUGINS.append('{root}')

