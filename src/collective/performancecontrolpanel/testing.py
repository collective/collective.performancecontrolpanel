from plone.app.testing import PloneSandboxLayer
from plone.app.testing import applyProfile
from plone.app.testing import PLONE_FIXTURE
from plone.app.testing import IntegrationTesting
from plone.app.testing import FunctionalTesting

from plone.testing import z2

from zope.configuration import xmlconfig


class CollectiveperformancecontrolpanelLayer(PloneSandboxLayer):

    defaultBases = (PLONE_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        # Load ZCML
        import collective.performancecontrolpanel
        xmlconfig.file(
            'configure.zcml',
            collective.performancecontrolpanel,
            context=configurationContext
        )

        # Install products that use an old-style initialize() function
        #z2.installProduct(app, 'Products.PloneFormGen')

#    def tearDownZope(self, app):
#        # Uninstall products installed above
#        z2.uninstallProduct(app, 'Products.PloneFormGen')

    def setUpPloneSite(self, portal):
        applyProfile(portal, 'collective.performancecontrolpanel:default')

COLLECTIVE_PERFORMANCECONTROLPANEL_FIXTURE = CollectiveperformancecontrolpanelLayer()
COLLECTIVE_PERFORMANCECONTROLPANEL_INTEGRATION_TESTING = IntegrationTesting(
    bases=(COLLECTIVE_PERFORMANCECONTROLPANEL_FIXTURE,),
    name="CollectiveperformancecontrolpanelLayer:Integration"
)
COLLECTIVE_PERFORMANCECONTROLPANEL_FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(COLLECTIVE_PERFORMANCECONTROLPANEL_FIXTURE, z2.ZSERVER_FIXTURE),
    name="CollectiveperformancecontrolpanelLayer:Functional"
)
