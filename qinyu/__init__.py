
def load(save_dir: str, verbose=None, **kwargs):
    from qinyu.utils.component_util import load_from_meta_file
    return load_from_meta_file(save_dir=save_dir, verbose=True, **kwargs)