from kfp import dsl
from mlrun.platforms import auto_mount
import os
import sys
import mlrun

funcs = {}

# init functions is used to configure function resources and local settings
def init_functions(functions: dict, project=None, secrets=None):
    for f in functions.values():
        f.apply(auto_mount())


def kfpipeline():

    # Fetch the data
    ingest = funcs['fetch_data'].as_step(
        inputs={'dataset': 'store://artifacts/clone-test-shapira/cancer-dataset#0:1e93a7b6-6bbd-4c37-aa5a-c276ff10f49a'},
        outputs=['dataset'])

    # Train the model
    train = funcs["trainer"].as_step(
        inputs={"dataset": ingest.outputs['dataset']},
        outputs=['model'])


    # Deploy the model
    deploy = funcs["serving"].deploy_step(models=[{'key':'cancer-classifier','model_path':train.outputs["model"], 'class_name':'mlrun.frameworks.sklearn.SklearnModelServer'}])
