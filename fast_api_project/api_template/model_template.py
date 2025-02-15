model_template = '''from pydantic import BaseModel


# Model for validate request and response template
class {{ router_name.capitalize() }}Request(BaseModel):
    pass


class {{ router_name.capitalize() }}Response(BaseModel):
    pass
'''