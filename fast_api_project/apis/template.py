import os
from jinja2 import Template
from api_template.router_template import router_template
from api_template.service_template import service_template
from api_template.model_template import model_template

router_template = router_template
service_template = service_template
model_template = model_template


def create_directories(base_dir, router_names):
    os.makedirs(base_dir, exist_ok=True)
    os.makedirs(f'{base_dir}/routers', exist_ok=True)
    os.makedirs(f'{base_dir}/services', exist_ok=True)
    os.makedirs(f'{base_dir}/models', exist_ok=True)
    os.makedirs(f'{base_dir}/query', exist_ok=True)

    for router_name in router_names:
        router_file = os.path.join(base_dir, "routers", f'{router_name}.py')
        with open(router_file, 'w') as f:
            template = Template(router_template)
            f.write(template.render(router_name=router_name, service_name=base_dir))

        service_file = os.path.join(base_dir, "services", f'{router_name}_service.py')
        with open(service_file, 'w') as f:
            template = Template(service_template)
            f.write(template.render(router_name=router_name))

        model_file = os.path.join(base_dir, "models", f'{router_name}_model.py')
        with open(model_file, 'w') as f:
            template = Template(model_template)
            f.write(template.render(router_name=router_name))

        query_file = os.path.join(base_dir, "query", f'query.py')


def generate_project():
    service_name = input('Enter service name: ')
    router_name = input('Enter router names: ').split(',')

    base_dir = service_name
    create_directories(base_dir, router_name)

    with open(os.path.join(base_dir, "main.py"), "w") as f:
        f.write(f"from fastapi import FastAPI\n")
        f.write(f"import uvicorn\n")
        f.write(f"from apis.{service_name}.routers import ")
        f.write(", ".join([f"{name}" for name in router_name]) + "\n\n")
        f.write(f"app = FastAPI()\n\n")
        for router_name in router_name:
            f.write(f"app.include_router({router_name}.router, prefix='{service_name}', tags=['{router_name}'])\n")
        f.write(f"\nhost = '127.0.0.1'\n")
        f.write(f"port = 8000\n\n")
        f.write(f"if __name__ == '__main__':\n")
        f.write(f"\tuvicorn.run('apis.{service_name}.main:app', host=host, port=port, reload=True)")
        print(f" Project '{base_dir}' has been generated successfully!")


if __name__ == "__main__":
    generate_project()
