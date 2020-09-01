"""Load project configuration"""

import os
import pathlib
import json

import yaml
import boto3

from chalicelib.commons.errors import ConfigurationError


def load():
    """
    Load app configuration
    :returns: dict config
    """

    stage = os.getenv("STAGE", "dev")

    if stage == "dev":
        return load_local()

    if stage in ("staging", "prod"):
        return load_aws(stage)

    raise ConfigurationError(f"invalid app stage: {stage}")


def load_local():
    """
    Load local config yml file
    :return: (dict)
    """
    path = pathlib.Path(__file__).parent.absolute()
    file = f"{path}/config.yml"

    config = open(file)

    data = yaml.load(config, Loader=yaml.FullLoader)

    if "sentry" not in data.keys():
        data["sentry"] = {"url": None}

    if "elastic" not in data.keys():
        data["elastic"] = {"url": None, "index": None}

    return data


def load_aws(stage):
    """
    Load config from AWS Secret manager depending of the stage
    :returns: dict config
    """

    secret_name = f"crontab/{stage}"
    region_name = "us-east-1"

    session = boto3.session.Session()
    client = session.client(service_name="secretsmanager", region_name=region_name)

    get_secret_value_response = client.get_secret_value(SecretId=secret_name)

    secret = json.loads(get_secret_value_response["SecretString"])

    for key, value in secret.items():
        try:
            secret[key] = json.loads(value)
        except Exception:
            continue

    return secret


CONFIG = load()
