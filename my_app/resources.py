from sanic.response import text, json
from sanic.views import HTTPMethodView

from app import db
from models import User, Role, Event, Stage, Performance, Material


class MainPageView(HTTPMethodView):

    def get(self, request):
        return text('THIS IS MAIN PAGE')


class RolesView(HTTPMethodView):

    def get(self, request):
        all_roles = await Role.get(1)
        return text(all_roles)

    async def post(self, request):
        return text('I am post method for Roles')


class RolesDetailView(HTTPMethodView):

    def get(self, request, role_id):
        return text('I am get method for Role by id {}'.format(role_id))

    async def put(self, request, role_id):
        return text('I am put method for Role by id {}'.format(role_id))

    async def patch(self, request, role_id):
        return text('I am patch method for Role by id {}'.format(role_id))

    async def delete(self, request, role_id):
        return text('I am delete method for Role by id {}'.format(role_id))


class UsersView(HTTPMethodView):

    async def get(self, request):
        all_users = await User.get(1)
        return text(all_users)

    async def post(self, request):
        nickname = request.json.get("nickname", None)
        name = request.json.get("name", None)
        email = request.json.get("email", None)
        # description = request.json.get("description", None)
        # role = request.json.get("role", None)
        if not (nickname and email):
            return text('There should be nickname and email at least')
        else:
            user = await User.create(nickname=nickname, name=name, email=email)
        return text('I am post method for Users')


class UsersDetailView(HTTPMethodView):

    def get(self, request, user_id):
        return text('I am get method for User by id {}'.format(user_id))

    async def put(self, request, user_id):
        return text('I am put method for User by id {}'.format(user_id))

    async def patch(self, request, user_id):
        return text('I am patch method for User by id {}'.format(user_id))

    async def delete(self, request, user_id):
        return text('I am delete method for User by id {}'.format(user_id))


class EventsView(HTTPMethodView):

    def get(self, request):
        all_events = await Event.get(1)
        return text(all_events)

    async def post(self, request):
        return text('I am post method for Events')


class EventsDetailView(HTTPMethodView):

    def get(self, request, event_id):
        return text('I am get method for Event by id {}'.format(event_id))

    async def put(self, request, event_id):
        return text('I am put method for Event by id {}'.format(event_id))

    async def patch(self, request, event_id):
        return text('I am patch method for Event by id {}'.format(event_id))

    async def delete(self, request, event_id):
        return text('I am delete method for Event by id {}'.format(event_id))


class StagesView(HTTPMethodView):

    def get(self, request):
        all_stages = await Stage.get(1)
        return text(all_stages)

    async def post(self, request):
        return text('I am post method for Stages')


class StagesDetailView(HTTPMethodView):

    def get(self, request, stage_id):
        return text('I am get method for Stage by id {}'.format(stage_id))

    async def put(self, request, stage_id):
        return text('I am put method for Stage by id {}'.format(stage_id))

    async def patch(self, request, stage_id):
        return text('I am patch method for Stage by id {}'.format(stage_id))

    async def delete(self, request, stage_id):
        return text('I am delete method for Stage by id {}'.format(stage_id))


class PerformancesView(HTTPMethodView):

    def get(self, request):
        all_performances = await Performance.get(1)
        return text(all_performances)

    async def post(self, request):
        return text('I am post method for Performances')


class PerformancesDetailView(HTTPMethodView):

    def get(self, request, performance_id):
        return text('I am get method for Performance by id {}'.format(performance_id))

    async def put(self, request, performance_id):
        return text('I am put method for Performance by id {}'.format(performance_id))

    async def patch(self, request, performance_id):
        return text('I am patch method for Performance by id {}'.format(performance_id))

    async def delete(self, request, performance_id):
        return text('I am delete method for Performance by id {}'.format(performance_id))


class MaterialsView(HTTPMethodView):

    def get(self, request):
        all_materials = await Material.get(1)
        return text(all_materials)

    async def post(self, request):
        return text('I am post method for Materials')


class MaterialsDetailView(HTTPMethodView):

    def get(self, request, material_id):
        return text('I am get method for Material by id {}'.format(material_id))

    async def put(self, request, material_id):
        return text('I am put method for Material by id {}'.format(material_id))

    async def patch(self, request, material_id):
        return text('I am patch method for Material by id {}'.format(material_id))

    async def delete(self, request, material_id):
        return text('I am delete method for Material by id {}'.format(material_id))
