print('Ran main.py')

from rlpyt.samplers.serial.sampler import SerialSampler

def build_and_train(game="pong", run_ID=0, cuda_idx=None):
    sampler = # TO DO
    algo = #TO DO
    agent = #TO DO 
    runner = MinibatchRlEval(
        algo = # The algorithm instance.
        agent =  #The learning agent instance
        sampler =  #The sampler instance.
        n_steps = #Total number of environment steps to run in training loop.
        seed = #Random seed to use, if ``None`` will generate randomly.
        affinity = #Hardware component assignments for sampler and algorithm.
        log_interval_steps = # Number of environment steps between logging to csv.
    )
    config = #to do 
    name = # to dO 
    log_dir = #to do 
    with logger_context(log_dir, run_ID, name, config, snapshot_mode="last"):
        runner.train()


if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description='DisTral')
    
    parser.add_argument(
        "-- alpha", type=float, default=None,
        help="Relative amount of KL vs entropy regularization loss, [0,1]")
    parser.add_argument(
        "-- beta", type=float, default=None,
        help="Inverse boltzmann temperature")
    parser.add_argument(
        "-- lr", type=float, default=None,
        help="Learning rate, (0,inf)")
    
    args = parser.parse_args()
    build_and_train(
        #to do
    )
