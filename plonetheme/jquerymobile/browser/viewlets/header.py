from zope import component
from plone.app.layout.viewlets import common
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from plonetheme.jquerymobile import i18n
_ = i18n._


class BaseHeaderAction(common.ViewletBase):
    """This is the base header action class
    it generate all nice jquerymobile options you want

    <a href="#panel-left"
       data-role="button"
       data-icon="bars" data-iconpos="notext"></a>
    """
    index = ViewPageTemplateFile("templates/base_header_action.pt")
    href = ""
    icon = ""
    iconpos = "notext"
    label = ""

    def render(self):
        if self.is_available():
            return self.index()
        return ""

    def is_available(self):
        return True


class PanelLeftAction(BaseHeaderAction):
    href = "string:#panel-left"
    icon = "bars"
    iconpos = "notext"
    label = _(u"Open left panel")
    weight = 0

    def is_available(self):
        plone_view = self.context.restrictedTraverse('@@plone')
        portal_state = self.context.restrictedTraverse('@@plone_portal_state')
        isanon = portal_state.anonymous()
        hasportlets = plone_view.have_portlets('plone.leftcolumn')
        return not isanon or hasportlets


class PanelRightAction(BaseHeaderAction):
    href = "string:#panel-right"
    icon = "grid"
    iconpos = "notext"
    label = _(u"Open right panel")
    weight = 10000

    def is_available(self):
        plone_view = self.context.restrictedTraverse('@@plone')
        return plone_view.have_portlets('plone.rightcolumn', self.context)


class SearchRightAction(BaseHeaderAction):
    icon = "search"
    iconpos = "notext"
    label = _(u"Search")

    @property
    def href(self):
        plone_portal_state = component.getMultiAdapter(
            (self.context, self.request),
            name="plone_portal_state"
        )
        return plone_portal_state.navigation_root_url() + '/@@search'


class SiteTitle(common.ViewletBase):
    def update(self):
        portal_state = component.getMultiAdapter(
            (self.context, self.request), name=u'plone_portal_state'
        )
        self.title = portal_state.portal().Title()

    def render(self):
        return self.title
