import config, engine
import importlib.util

cfg = config.Config()


def verify_file(file_id):

    script_path = cfg.local_path + '/scripts/'
    file_path = script_path + file_id + '.py'
    spec = importlib.util.spec_from_file_location("Tutor", file_path)
    tutor = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(tutor)
    t = tutor.Tutor

    game = engine.Training('verify', t)
    x = game.training()
    return {"status": "OK"}



if __name__ == '__main__':
    verify_file('client')
