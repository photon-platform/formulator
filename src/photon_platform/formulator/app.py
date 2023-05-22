import click
#  from trogon import tui
import yaml
from .formulator import Formulator, load_blueprint

#  @tui()
@click.command()
@click.option('--blueprint', prompt="blueprint yaml path:", required=True, type=click.Path(exists=True), help='YAML file containing the form blueprint.')
def run(blueprint):
    """Run Formulator with the provided form blueprint."""
    form_blueprint = load_blueprint(blueprint)
    app = Formulator(form_blueprint)
    context = app.run()
    
    # Print context results as YAML
    print(yaml.dump(context))

if __name__ == '__main__':
    run()

