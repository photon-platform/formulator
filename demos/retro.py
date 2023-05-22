from photon_platform.formulator import *
from rich import print


def run_form(blueprint_file):
    blueprint = load_blueprint(blueprint_file)
    #  print(blueprint)
    form = Formulator(blueprint)
    reply = form.run()
    print(reply)


def main():
    run_form("retro-3.yaml")
    #  run_form("flux-capacitor.yaml")
    #  run_form("millenium-falcon.yaml")


if __name__ == "__main__":
    main()
