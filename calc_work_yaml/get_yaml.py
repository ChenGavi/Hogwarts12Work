import yaml


with open("./data.yaml",'rb') as fo:
    steps = yaml.safe_load(fo)["steps"]
    print(steps)
    #print(steps["data type"])
    for step in steps:
        if isinstance(step, dict):
            if str(type(1)) in step["data type"] and str(type(2)) in step["data type"]:
                print("hello")