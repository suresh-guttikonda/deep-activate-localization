# deep-activate-localization/src/rl_agents

#### Steps to train/eval agent in container:
1. Run shell within container image
```
<path_to_sif_file>$ singularity shell --nv --bind /usr/share/glvnd,./src:/mnt/src tensorflow_latest-gpu.sif
```
2. Activate virtual environment
```
~> source /opt/venvs/py3-igibson/bin/activate
```
3. Change to rl_agents dir
```
(py3-igibson) ~> cd /mnt/src/rl_agents/
```
4. Start trainining
```
(py3-igibson) /mnt/src/rl_agents> python -u train_eval.py \
    --root_dir 'train_output' \
    --config_file './configs/turtlebot_point_nav.yaml' \
    --eval_only=False \
    --num_iterations 3000 \
    --initial_collect_steps 500 \
    --use_tf_functions=True \
    --use_parallel_envs=True \
    --collect_steps_per_iteration 1 \
    --num_parallel_environments 1 \
    --num_parallel_environments_eval 1 \
    --replay_buffer_capacity 1000 \
    --train_steps_per_iteration 1 \
    --batch_size 16 \
    --num_eval_episodes 10 \
    --eval_interval 500 \
    --gpu_c 0 \
    --env_mode 'headless' \
    --gpu_g 0 \
    --seed 100
```
5. if above steps are successful, we see training progress as follows
```
.....
I0429 09:27:42.979353 140051197933376 train_eval.py:416] step = 100, loss = -2.514921
.....
```
6. Start evaluation with pretrained policy
```
(py3-igibson) /mnt/src/rl_agents> python -u train_eval.py \
    --root_dir 'results/2021-04-29_21-07-57' \
    --config_file './configs/turtlebot_point_nav.yaml' \
    --eval_only=True \
    --initial_collect_steps 500 \
    --use_tf_functions=True \
    --use_parallel_envs=True \
    --num_parallel_environments 1 \
    --num_parallel_environments_eval 1 \
    --replay_buffer_capacity 1000 \
    --batch_size 16 \
    --num_eval_episodes 10 \
    --gpu_c 0 \
    --env_mode 'gui' \
    --gpu_g 0 \
    --seed 100
```
