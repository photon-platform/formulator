from photon_platform.formulator import *
from rich import print


def main():
    blueprint_file = "demo.yaml"
    blueprint = load_blueprint(blueprint_file)
    print(blueprint)
    form = Formulator(blueprint)
    reply = form.run()
    print(reply)


if __name__ == "__main__":
    main()
