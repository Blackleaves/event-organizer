from sanic import Blueprint

from resources import MainPageView, RolesView, RolesDetailView, UsersView, UsersDetailView, EventsView, \
    EventsDetailView, StagesView, StagesDetailView, PerformancesView, PerformancesDetailView, MaterialsView, \
    MaterialsDetailView

main_page = Blueprint('main_page', url_prefix="/")
main_page.add_route(MainPageView.as_view(), '/',  strict_slashes=False)

roles = Blueprint('roles', url_prefix='/roles', strict_slashes=False)
roles.add_route(RolesView.as_view(), '/',  strict_slashes=False)
roles.add_route(RolesDetailView.as_view(), '/<role_id>', strict_slashes=False)

users = Blueprint('users', url_prefix='/users', strict_slashes=False)
users.add_route(UsersView.as_view(), '/',  strict_slashes=False)
users.add_route(UsersDetailView.as_view(), '/<user_id>', strict_slashes=False)

events = Blueprint('events', url_prefix='/events', strict_slashes=False)
events.add_route(EventsView.as_view(), '/',  strict_slashes=False)
events.add_route(EventsDetailView.as_view(), '/<event_id>', strict_slashes=False)

stages = Blueprint('stages', url_prefix='/stages', strict_slashes=False)
stages.add_route(StagesView.as_view(), '/',  strict_slashes=False)
stages.add_route(StagesDetailView.as_view(), '/<stage_id>', strict_slashes=False)

performances = Blueprint('performances', url_prefix='/performances', strict_slashes=False)
performances.add_route(PerformancesView.as_view(), '/',  strict_slashes=False)
performances.add_route(PerformancesDetailView.as_view(), '/<performance_id>', strict_slashes=False)

materials = Blueprint('materials', url_prefix='/materials', strict_slashes=False)
materials.add_route(MaterialsView.as_view(), '/',  strict_slashes=False)
materials.add_route(MaterialsDetailView.as_view(), '/<material_id>', strict_slashes=False)

api = Blueprint.group(main_page, roles, users, events, stages, performances, materials, url_prefix='/')
