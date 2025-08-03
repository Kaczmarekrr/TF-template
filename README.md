# TF-template
Template repository for TensorFlow model development

## Env setup

### Set up pixi
Linux & MacOS
```bash
curl -fsSL https://pixi.sh/install.sh | sh
```


#### After instalation

"train" env is a default env for any operation in this repo.

```bash
pixi shell -e train
```

### ClearML

Please proceed with the [ClearML](https://clear.ml/docs/latest/docs/clearml_sdk/clearml_sdk_setup/) instruction how to init the service.

```bash
clearml-init
```



## Repo structure
```
|
|___docs -> place for additional documentary
|___my_project -> main directory for source code
|            |
|            |___common -> directory for configs
|            |___datasets -> dataset preprocesing and TFRecords creation
|            |___demos -> place for pipeline demonstration
|            |___model_implementation -> model definition and related topics
|            |___model_training -> model training and testing
|pixi.lock
|pixi.toml



```