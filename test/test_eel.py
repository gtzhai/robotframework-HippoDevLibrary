from HippoDevLibrary.HippoDev import HippoDev
from HippoDevLibrary.HippoSession import HippoSession
import HippoDevLibrary.eel as eel

session = HippoSession()
dev = HippoDev(session)
session.session_connect('USB0::0x049F::0x505E::22ea9d2603fd545::0::INSTR', 'hantek_dso_mso6000bc')
print (session.session_exists('USB0::0x049F::0x505E::22ea9d2603fd545::0::INSTR'))
dev.get_idn('USB0::0x049F::0x505E::22ea9d2603fd545::0::INSTR')
eel.init('./test/web')
eel.hippo_dev = dev
eel.start('hello.html')
session.session_disconnect('USB0::0x049F::0x505E::22ea9d2603fd545::0::INSTR')
session.session_reset_all()