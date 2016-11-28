name = 'omtk_cradle'

version = '0.0.1'

description = 'Cradle rig plugin definition for omtk'

requires = ['omtk-0.4']

def commands():
    env.OMTK_PLUGINS.append('{root}')

