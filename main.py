__author__ = 'Lorenzo'

from main.layer_zero import deploy_layer_zero
from main.layer_one import deploy_layer_one
from main.layer_two import deploy_layer_two


def algorithm():

    deploy_layer_zero()

    deploy_layer_one()

    deploy_layer_two()


if __name__ == "__main__":
    algorithm()