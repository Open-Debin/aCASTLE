import numpy as np
import torch
from model.trainer.gfsl_trainer import GFSLTrainer
from model.utils import (
    pprint, set_gpu,
    get_command_line_parser,
    postprocess_args,
)
# from ipdb import launch_ipdb_on_exception

if __name__ == '__main__':
    parser = get_command_line_parser()
    args = postprocess_args(parser.parse_args())
    # with launch_ipdb_on_exception():
    pprint(vars(args))

    set_gpu(args.gpu)
    trainer = GFSLTrainer(args)
    trainer.train()
    trainer.evaluate_test()
    trainer.final_record()
    print(args.save_path)



