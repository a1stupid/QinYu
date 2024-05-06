import os
from qinyu_common.io import load_json
from qinyu_common.reflection import object_from_classpath

def load_from_meta_file(save_dir: str, verbose=True, **kwargs):
    load_path = save_dir
    metapath = os.path.join(load_path, 'config.json')
    meta: dict = load_json(metapath)
    cls = None
    cls = meta.get('classpath', cls)
    obj = object_from_classpath(cls)
    obj.load(save_dir, verbose=verbose, **kwargs)
    return obj

