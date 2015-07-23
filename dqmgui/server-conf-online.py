import os.path, socket ; global CONFIGDIR
def reglob(pattern):
  """Extended version of glob that uses regular expressions."""
  from os import listdir
  import re
  cwd = pattern.rsplit('/',1)[0]
  f_pattern= pattern.rsplit('/',1)[-1]
  pat=re.compile(f_pattern)
  g = ["%s/%s" % (cwd,f) for f in listdir(cwd) if pat.match(f)]
  return g

CONFIGDIR = os.path.normcase(os.path.abspath(__file__)).rsplit('/', 1)[0]
BASEDIR   = CONFIGDIR.replace("/current/config/dqmgui", "")
STATEDIR  = "%s/state/dqmgui/online" % BASEDIR
LOGDIR    = "%s/logs/dqmgui/online" % BASEDIR

# Modifiable parameters.
LAYOUTS = reglob("%s/layouts/[^-_]*-layouts.py" % CONFIGDIR)
LAYOUTS += reglob("%s/layouts/shift_[^-_]*_layout.py" % CONFIGDIR)
LAYOUTS += reglob("%s/layouts/.*_overview_layouts.py" % CONFIGDIR)

# Do not modify configuration below this line.
# 1st line: post 07/2015 servers
# 2nd line: server aliases
# 3rd line: pre 07/2015 servers
DQMSERVERS  = ['srv-c2f11-29-01', 'srv-c2f11-29-02',  'srv-c2f11-29-03', 'srv-c2f11-29-04',
               'dqm-prod-local',  'dqm-prod-offsite', 'dqm-integration', 'dqm-test',
               'dqm-C2D07-01',    'dqm-C2D07-02',     'dqm-C2D07-11',    'dqm-C2D07-12',]
HOST        = socket.gethostname().lower()
DOMAIN      = socket.getfqdn().split('.',1)[-1].lower()
HOSTADDR    = socket.getaddrinfo(HOST, None)[0][4][0]
BASEDIR     = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
HOSTALIAS   = HOST
COLLHOST    = '127.0.0.1'
COLLPORT    = DOMAIN == 'cms' and 9190 or 8061
SERVICENAME = 'Online Development'
SERVERPORT  = 8070
BASEURL     = '/dqm/online-dev'
UPLOADDIR   = "%s/uploads" % STATEDIR
FILEREPO    = { "ROOT": "%s/data" % STATEDIR }

# Figure out a preferred alias for this out (if any)
for alias in DQMSERVERS:
  try:
    if len([x for x in socket.getaddrinfo(alias, None) if x[4][0] == HOSTADDR]):
      HOSTALIAS = alias
      break
  except:
    pass

# Specific settings for online DQM fixed servers
# We try to be as explicit as possible here:
if HOSTALIAS == 'dqm-prod-local':
  COLLPORT    = 9090
  SERVERPORT  = 8030
  SERVICENAME = 'Online'
  BASEURL     = '/dqm/online'
  UPLOADDIR   = '/dqmdata/dqm/uploads'
  FILEREPO    = {'Original': '/dqmdata/dqm/repository/original/OnlineData'}
  COLLHOST    = 'srv-c2f11-29-01.cms'

elif HOSTALIAS == 'dqm-prod-offsite':
  COLLPORT    = 9090
  SERVERPORT  = 8030
  SERVICENAME = 'Online'
  BASEURL     = '/dqm/online'
  UPLOADDIR   = '/dqmdata/dqm/uploads'
  FILEREPO    = {'Original': '/dqmdata/dqm/repository/original/OnlineData'}
  COLLHOST    = 'srv-c2f11-29-01.cms'

elif HOSTALIAS == 'dqm-integration':
  COLLPORT    = 9090
  SERVERPORT  = 8030
  SERVICENAME = 'Online Playback'
  BASEURL     = '/dqm/online-playback'

elif HOSTALIAS == 'dqm-test':
  COLLPORT    = 9090
  SERVERPORT  = 8030
  SERVICENAME = 'Online Test'
  BASEURL     = '/dqm/online-test'
  UPLOADDIR   = '/dqmdata/dqm/uploads'
  FILEREPO    = {'Original': '/dqmdata/dqm/repository/original/OnlineData'}
  COLLHOST    = 'srv-c2f11-29-01.cms'

elif HOSTALIAS == 'dqm-C2D07-01':
  COLLPORT    = 9090
  SERVERPORT  = 8030
  SERVICENAME = 'Online'
  BASEURL     = '/dqm/online'
  UPLOADDIR   = '/dqmdata/dqm/uploads'
  FILEREPO    = {'Original': '/dqmdata/dqm/repository/original/OnlineData'}
  COLLHOST    = 'srv-c2f11-29-01.cms'

elif HOSTALIAS == 'dqm-C2D07-02':
  COLLPORT    = 9090
  SERVERPORT  = 8030
  SERVICENAME = 'Online'
  BASEURL     = '/dqm/online'
  UPLOADDIR   = '/dqmdata/dqm/uploads'
  FILEREPO    = {'Original': '/dqmdata/dqm/repository/original/OnlineData'}
  COLLHOST    = 'srv-c2f11-29-01.cms'

elif HOSTALIAS == 'dqm-C2D07-11':
  COLLPORT    = 9090
  SERVERPORT  = 8030
  SERVICENAME = 'Online Playback'
  BASEURL     = '/dqm/online-playback'

elif HOSTALIAS == 'dqm-C2D07-12':
  COLLPORT    = 9090
  SERVERPORT  = 8030
  SERVICENAME = 'Online Test'
  BASEURL     = '/dqm/online-test'
  UPLOADDIR   = '/dqmdata/dqm/uploads'
  FILEREPO    = {'Original': '/dqmdata/dqm/repository/original/OnlineData'}
  COLLHOST    = 'srv-c2f11-29-01.cms'

elif HOSTALIAS == 'srv-c2f11-29-01':
  COLLPORT    = 9090
  SERVERPORT  = 8030
  SERVICENAME = 'Online'
  BASEURL     = '/dqm/online'
  UPLOADDIR   = '/dqmdata/dqm/uploads'
  FILEREPO    = {'Original': '/dqmdata/dqm/repository/original/OnlineData'}
  COLLHOST    = 'localhost'

elif HOSTALIAS == 'srv-c2f11-29-02':
  COLLPORT    = 9090
  SERVERPORT  = 8030
  SERVICENAME = 'Online'
  BASEURL     = '/dqm/online'
  UPLOADDIR   = '/dqmdata/dqm/uploads'
  FILEREPO    = {'Original': '/dqmdata/dqm/repository/original/OnlineData'}
  COLLHOST    = 'srv-c2f11-29-01.cms'

elif HOSTALIAS == 'srv-c2f11-29-03':
  COLLPORT    = 9090
  SERVERPORT  = 8030
  SERVICENAME = 'Online Playback'
  BASEURL     = '/dqm/online-playback'

elif HOSTALIAS == 'srv-c2f11-29-04':
  COLLPORT    = 9090
  SERVERPORT  = 8030
  SERVICENAME = 'Online Test'
  BASEURL     = '/dqm/online-test'
  UPLOADDIR   = '/dqmdata/dqm/uploads'
  FILEREPO    = {'Original': '/dqmdata/dqm/repository/original/OnlineData'}
  COLLHOST    = 'srv-c2f11-29-01.cms'

# Server configuration.
modules = ("Monitoring.DQM.GUI",)

#server.instrument  = 'valgrind --num-callers=999 `cmsvgsupp` --error-limit=no'
#server.instrument  = 'valgrind --tool=helgrind --num-callers=999 --error-limit=no'
#server.instrument  = 'igprof -d -t python -pp'
#server.instrument  = 'igprof -d -t python -mp'
server.localBase   = HOSTALIAS
server.serverDir   = STATEDIR
server.port        = SERVERPORT
server.logFile     = '%s/weblog-%%Y%%m%%d.log' % LOGDIR
server.baseUrl     = BASEURL
server.title       = 'CMS data quality'
server.serviceName = SERVICENAME

server.plugin('render', "%s/style/*.cc" % CONFIGDIR)
server.extend('DQMRenderLink', server.pathOfPlugin('render'))
server.extend('DQMToJSON')
server.extend('DQMFileAccess', "%s/auth/wmcore-auth/header-auth-key" % __file__.rsplit('/', 3)[0],
              UPLOADDIR,FILEREPO)
server.source('DQMUnknown')
server.source('DQMOverlay')
server.source('DQMStripChart')
server.source('DQMLive', "%s:%s" % (COLLHOST,COLLPORT))
server.source('DQMArchive', "%s/ix128" % STATEDIR, '^/Global/')
server.source('DQMLayout')

execfile(CONFIGDIR + "/dqm-services.py")
execfile(CONFIGDIR + "/workspaces-online.py")
