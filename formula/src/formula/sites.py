from unfold.sites import UnfoldAdminSite

from .forms import LoginForm


class FormulaAdminSite(UnfoldAdminSite):
    login_form = LoginForm
