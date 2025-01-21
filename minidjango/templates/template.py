import os
from ..settings import TEMPLATES


def render(request, template_name, context:dict):
    for template_dir in TEMPLATES['DIRS']:
        if os.path.exists(template_dir + '/' + template_name):
            with open(template_dir + '/' + template_name) as file:
                template_contxt = file.read()

                for key, value in context.items():
                    template_contxt.replace(f'{{{{key}}}}', str(value))
            return template_contxt
        else:
            return f"Template not found. {template_dir + '/' + template_name} not exist."
