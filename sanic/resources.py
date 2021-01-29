from sanic.response import text, json
from sanic.views import HTTPMethodView


class MainPageView(HTTPMethodView):

    def get(self, request):
        return text('THIS IS MAIN PAGE')


class RolesView(HTTPMethodView):

    def get(self, request):
        return text('I am get method for Roles')

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

    def get(self, request):
        return text('I am get method for Users')

    async def post(self, request):
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
        return text('I am get method for Events')

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
        return text('I am get method for Stages')

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
        return text('I am get method for Performances')

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
        return text('I am get method for Materials')

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
