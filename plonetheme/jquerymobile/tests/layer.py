from plone.app.testing import PloneSandboxLayer
from plone.app.testing import PLONE_FIXTURE
from plone.app.testing import IntegrationTesting, FunctionalTesting
from plone.app.robotframework.testing import AUTOLOGIN_LIBRARY_FIXTURE

from plone.testing import z2


class Layer(PloneSandboxLayer):

    defaultBases = (PLONE_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        # Load ZCML
        import plonetheme.jquerymobile
        self.loadZCML(package=plonetheme.jquerymobile)

#        z2.installProduct(app, 'plonetheme.jquerymobile')

    def setUpPloneSite(self, portal):
        self.applyProfile(portal, 'plonetheme.jquerymobile:default')

#    def tearDownZope(self, app):
#        z2.uninstallProduct(app, 'plonetheme.jquerymobile')


FIXTURE = Layer()
INTEGRATION = IntegrationTesting(bases=(FIXTURE,),
                                 name="plonetheme.jquerymobile:Integration")
FUNCTIONAL = FunctionalTesting(bases=(FIXTURE,),
                               name="plonetheme.jquerymobile:Functional")

ROBOT = FunctionalTesting(
    bases=(AUTOLOGIN_LIBRARY_FIXTURE, FIXTURE, z2.ZSERVER),
    name="plonetheme.jquerymobile:Robot")