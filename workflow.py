from kfp import dsl
from mlrun.platforms import auto_mount
import os
import sys
import mlrun




def kfpipeline(dataset):

    # Fetch the data
    ingest = mlrun.run_function('fetch_data',
        inputs={'dataset': dataset},
        outputs=['dataset'])

    # # Train the model
    # train = funcs["trainer"].as_step(
    #     inputs={"dataset": ingest.outputs['dataset']},
    #     outputs=['model'])


    # # Deploy the model
    # deploy = funcs["serving"].deploy_step(models=[{'key':'cancer-classifier','model_path':train.outputs["model"], 'class_name':'mlrun.frameworks.sklearn.SklearnModelServer'}])
