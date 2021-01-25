from app import app
from sanic.response import text, json


@app.route("/")
async def test(request):
    return text("MAIN PAGE")


# Roles
@app.route("/roles", methods=['GET'])
async def get_all_roles(request):
    return text("GET all roles")


@app.route("/roles/create")
async def create_role(request):
    return text("Create new role")


@app.route("/roles/<role_id>", methods=['GET'])
async def get_role(request, role_id):
    return text("GET role by id {}".format(role_id))


@app.route("/roles/<role_id>", methods=['PATCH'])
async def update_role(request, role_id):
    return text("PATCH role on id {}".format(role_id))


@app.route("/roles/<role_id>", methods=['DELETE'])
async def delete_role(request, role_id):
    return text("Delete role on id {}".format(role_id))


# Users
@app.route("/register")
async def register(request):
    return text("Register")


@app.route("/users", methods=['GET'])
async def get_all_users(request):
    return text("GET all users")


@app.route("/users/<user_id>", methods=['GET'])
async def get_user(request, user_id):
    return text("GET user by id {}".format(user_id))


@app.route("/users/<user_id>", methods=['PATCH'])
async def update_user(request, user_id):
    return text("PATCH user on id {}".format(user_id))


@app.route("/users/<user_id>", methods=['DELETE'])
async def delete_user(request, user_id):
    return text("DELETE user on id {}".format(user_id))


# Events
@app.route("/events", methods=['GET'])
async def events_list(request):
    return text("GET list of all events")


@app.route("/events/create")
async def create_event(request):
    return text("CREATE new event")


@app.route("/events/<event_id>", methods=['GET'])
async def get_event(request, event_id):
    return text("GET event by id {}".format(event_id))


@app.route("/events/<event_id>", methods=['PATCH'])
async def update_event(request, event_id):
    return text("PATCH event on id {}".format(event_id))


@app.route("/events/<event_id>", methods=['DELETE'])
async def delete_event(request, event_id):
    return text("Delete event on id {}".format(event_id))


# Stages
@app.route("/events/<event_id>/stages", methods=['GET'])
async def get_stages_per_event(request, event_id):
    return text("GET all stages for event on id {}".format(event_id))


@app.route("/events/<event_id>/stages/create")
async def create_stage(request, event_id):
    return text("CREATE new stage for event on id {}".format(event_id))


@app.route("/stages/<stage_id>", methods=['GET'])
@app.route("/events/<event_id>/stages/<stage_id>", methods=['GET'])
async def get_stage(request, stage_id, event_id=""):
    return text("GET stage by id {}".format(stage_id))


@app.route("/stages/<stage_id>", methods=['PATCH'])
@app.route("/events/<event_id>/stages/<stage_id>", methods=['PATCH'])
async def update_stage(request, stage_id, event_id=""):
    return text("PATCH stage by id {}".format(stage_id))


@app.route("/events/<event_id>/stages/<stage_id>/delete")
async def get_stage(request, event_id, stage_id):
    return text("DELETE stage by id {} from event on id {}".format(stage_id, event_id))


# Performances
@app.route("/events/<event_id>/performances", methods=['GET'])
async def get_performances_per_event(request, event_id):
    return text("GET all performances for event on id {}".format(event_id))


@app.route("/stages/<stage_id>/performances", methods=['GET'])
@app.route("/events/<event_id>/stages/<stage_id>/performances", methods=['GET'])
async def get_performances_per_stage(request, stage_id, event_id=""):
    return text("GET all performances for stage on id {}".format(stage_id))


@app.route("/stages/<stage_id>/performances/create")
@app.route("/events/<event_id>/stages/<stage_id>/performances/create")
async def create_performance(request, stage_id, event_id=""):
    return text("CREATE performance for stage on id {}".format(stage_id))


@app.route("/performances/<performance_id>", methods=['GET'])
@app.route("/stages/<stage_id>/performances/<performance_id>", methods=['GET'])
@app.route("/events/<event_id>/stages/<stage_id>/performances/<performance_id>", methods=['GET'])
async def get_performance(request, performance_id, stage_id="", event_id=""):
    return text("GET performance by id {}".format(performance_id))


@app.route("/performances/<performance_id>", methods=['PATCH'])
@app.route("/stages/<stage_id>/performances/<performance_id>", methods=['PATCH'])
@app.route("/events/<event_id>/stages/<stage_id>/performances/<performance_id>", methods=['PATCH'])
async def update_performance(request, performance_id, stage_id="", event_id=""):
    return text("PATCH performance on id {}".format(performance_id))


@app.route("/performances/<performance_id>", methods=['DELETE'])
@app.route("/stages/<stage_id>/performances/<performance_id>", methods=['DELETE'])
@app.route("/events/<event_id>/stages/<stage_id>/performances/<performance_id>", methods=['DELETE'])
async def delete_performance(request, performance_id, stage_id="", event_id=""):
    return text("DELETE performance on id {}".format(performance_id))


# Materials
@app.route("/events/<event_id>/materials", methods=['GET'])
async def get_materials_per_event(request, event_id):
    return text("GET all materials for event on id {}".format(event_id))


@app.route("/stages/<stage_id>/materials", methods=['GET'])
@app.route("/events/<event_id>/stages/<stage_id>/materials", methods=['GET'])
async def get_materials_per_stage(request, stage_id, event_id=""):
    return text("GET all materials for stage on id {}".format(stage_id))


@app.route("/performances/<performance_id>/materials", methods=['GET'])
@app.route("/stages/<stage_id>/performances/<performance_id>/materials", methods=['GET'])
@app.route("/events/<event_id>/stages/<stage_id>/performances/<performance_id>/materials", methods=['GET'])
async def get_materials_per_performance(request, performance_id, stage_id="", event_id=""):
    return text("GET all materials for performance on id {}".format(performance_id))


@app.route("/performances/<performance_id>/materials/create")
@app.route("/stages/<stage_id>/performances/<performance_id>/materials/create")
@app.route("/events/<event_id>/stages/<stage_id>/performances/<performance_id>/materials/create")
async def create_material(request, performance_id, stage_id="", event_id=""):
    return text("CREATE material for performance on id {}".format(performance_id))


@app.route("/materials/<material_id>", methods=['GET'])
@app.route("/performances/<performance_id>/materials/<material_id>", methods=['GET'])
@app.route("/stages/<stage_id>/performances/<performance_id>/materials/<material_id>", methods=['GET'])
@app.route(
    "/events/<event_id>/stages/<stage_id>/performances/<performance_id>/materials/<material_id>", methods=['GET']
)
async def get_material(request, material_id, performance_id="", stage_id="", event_id=""):
    return text("GET material by id {}".format(material_id))


@app.route("/materials/<material_id>", methods=['PATCH'])
@app.route("/performances/<performance_id>/materials/<material_id>", methods=['PATCH'])
@app.route("/stages/<stage_id>/performances/<performance_id>/materials/<material_id>", methods=['PATCH'])
@app.route(
    "/events/<event_id>/stages/<stage_id>/performances/<performance_id>/materials/<material_id>", methods=['PATCH']
)
async def update_material(request, material_id, performance_id="", stage_id="", event_id=""):
    return text("PATCH material on id {}".format(material_id))


@app.route("/materials/<material_id>>", methods=['DELETE'])
@app.route("/performances/<performance_id>/materials/<material_id>", methods=['DELETE'])
@app.route("/stages/<stage_id>/performances/<performance_id>/materials/<material_id>", methods=['DELETE'])
@app.route(
    "/events/<event_id>/stages/<stage_id>/performances/<performance_id>/materials/<material_id>", methods=['DELETE']
)
async def material(request, material_id, performance_id="", stage_id="", event_id=""):
    return text("DELETE material on id {}".format(material_id))
