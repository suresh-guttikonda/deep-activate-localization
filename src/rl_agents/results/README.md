# deep-activate-localization/src/rl_agents/results

<details close>
  <summary>April 28th - May 4th Summary</summary>

  ### Results
  *blue - training curve, orange - evaluation curve*
  |Experiement | Result     | AverageEpisodeLength      | AverageEpisodeReturn      |
  |------------|------------|------------|-------------|
  |task_obs only (2021-04-30)| [Navigate_Fixed_Goal - (parallel_py_env)](2021-04-30_12-19-33)|![Metrics_AverageEpisodeLength](2021-04-30_12-19-33/images/Metrics_AverageEpisodeLength.svg)|![Metrics_AverageReturn](2021-04-30_12-19-33/images/Metrics_AverageReturn.svg)| -> different train and eval envs with normal_projection_network.NormalProjectionNetwork
  |task_obs only (2021-04-30)| [Navigate_Fixed_Goal - (non-parallel_py_env-1)](2021-04-30_15-00-08)|![Metrics_AverageEpisodeLength](2021-04-30_15-00-08/images/Metrics_AverageEpisodeLength.svg)|![Metrics_AverageReturn](2021-04-30_15-00-08/images/Metrics_AverageReturn.svg)| -> different train and eval envs with normal_projection_network.NormalProjectionNetwork
  |task_obs only (2021-04-30)| [Navigate_Fixed_Goal - (non-parallel_py_env-2)](2021-04-30_20-07-39)|![Metrics_AverageEpisodeLength](2021-04-30_20-07-39/images/Metrics_AverageEpisodeLength.svg)|![Metrics_AverageReturn](2021-04-30_20-07-39/images/Metrics_AverageReturn.svg)| -> same train and eval envs with normal_projection_network.NormalProjectionNetwork
  |rgb_obs only (2021-05-03)| [Navigate_Fixed_Goal - (parallel_py_env)](2021-05-03_14-54-25)|![Metrics_AverageEpisodeLength](2021-05-03_14-54-25/images/Metrics_AverageEpisodeLength.svg)|![Metrics_AverageReturn](2021-05-03_14-54-25/images/Metrics_AverageReturn.svg)| -> different train and eval envs with tanh_normal_projection_network.TanhNormalProjectionNetwork
  |rgb_obs only (2021-05-04)| [Navigate_Fixed_Goal - (non-parallel_py_env)](2021-05-04_07-42-43)|![Metrics_AverageEpisodeLength](2021-05-04_07-42-43/images/Metrics_AverageEpisodeLength.svg)|![Metrics_AverageReturn](2021-05-04_07-42-43/images/Metrics_AverageReturn.svg)| -> different train and eval envs with tanh_normal_projection_network.TanhNormalProjectionNetwork sac_agent.py

</details>

<details close>
  <summary>May 5th - May 11th Summary</summary>

  ### Results
  *blue - training curve, orange - evaluation curve*
  |Experiement | Agent |  Result     | AverageEpisodeLength      | AverageEpisodeReturn      |
  |------------|-------|-----|------------|-------------|
  |task_obs only (2021-05-06)| SAC |[Navigate_Fixed_Goal - (non-parallel_py_env)](2021-05-06_10-06-32)|![Metrics_AverageEpisodeLength](2021-05-06_10-06-32/images/Metrics_AverageEpisodeLength.svg)|![Metrics_AverageReturn](2021-05-06_10-06-32/images/Metrics_AverageReturn.svg)| -> same train and eval envs with normal_projection_network.NormalProjectionNetwork train_eval.py
  |rgb_obs only (2021-05-07)| SAC |[Navigate_Fixed_Goal - (non-parallel_py_env)](2021-05-07_00-07-34)|![Metrics_AverageEpisodeLength](2021-05-07_00-07-34/images/Metrics_AverageEpisodeLength.svg)|![Metrics_AverageReturn](2021-05-07_00-07-34/images/Metrics_AverageReturn.svg)| -> same train and eval envs with tanh_normal_projection_network.TanhNormalProjectionNetwork train_eval.py
  |task_obs only (2021-05-12)| PPOClipAgent |[Navigate_Fixed_Goal - (non-parallel_py_env)](2021-05-12_12-46-55)|![Metrics_AverageEpisodeLength](2021-05-12_12-46-55/images/Metrics_AverageEpisodeLength.svg)|![Metrics_AverageReturn](2021-05-12_12-46-55/images/Metrics_AverageReturn.svg)| -> same train and eval envs with tanh activation non-mini batch training
  |rgb_obs only (2021-05-17)| PPOClipAgent |[Navigate_Fixed_Goal - (non-parallel_py_env)](2021-05-17_08-16-35)|![Metrics_AverageEpisodeLength](2021-05-17_08-16-35/images/Metrics_AverageEpisodeLength.svg)|![Metrics_AverageReturn](2021-05-17_08-16-35/images/Metrics_AverageReturn.svg)| -> same train and eval envs with tanh activation non-mini batch training

</details>


<details close>
  <summary>May 26th - June 2nd Summary</summary>

  ### Results
  ![#1589F0](https://via.placeholder.com/15/1589F0/000000?text=+) - *random agent* ![#f03c15](https://via.placeholder.com/15/f03c15/000000?text=+) - *sac trained agent*\
  reward scale: [-10, 0]\
  env obs: proprio (gt_pose, gt_velocity, est_pose)

  |With Out Transition Noise |With Transition Noise |With Lower Initial Covariance |With More Particles |
  |------------|------------|------------|------------|
  |![Eval_WithOut_Noise](2021-05-29_11-11-00/images/eval_wo_noise.svg)|![Eval_With_Noise](2021-05-29_11-11-00/images/eval_w_noise.svg)|![Eval_Low_Init_Covariance](2021-05-29_11-11-00/images/eval_low_init_covariance.svg)|![Eval_More_Particles](2021-05-29_11-11-00/images/eval_more_particles.svg)|
  |transition_std: ['0', '0']<br/>init_particles_std: ['30', '0.523599']<br/>init_particles_distr: gaussian<br/>num_particles: 1000<br/>alpha_resample_ratio 0.8|transition_std: ['1', '0']<br/>init_particles_std ['30', '0.523599']<br/>init_particles_distr: gaussian<br/>num_particles: 1000<br/>alpha_resample_ratio 0.8|transition_std: ['0.2', '0']<br/>init_particles_std ['15', '0.523599']<br/>init_particles_distr: gaussian<br/>num_particles: 1500<br/>alpha_resample_ratio 0.8|transition_std: ['0.5', '0']<br/>init_particles_std ['30', '0.523599']<br/>init_particles_distr: gaussian<br/>num_particles: 2500<br/>alpha_resample_ratio 0.8|

</details>


<details close>
  <summary>June 3rd - June 9th Summary</summary>

  ### Results
  RMSE vs #th episode ![#1589F0](https://via.placeholder.com/15/1589F0/000000?text=+) - *original* ![#FF8C00](https://via.placeholder.com/15/FF8C00/000000?text=+) - *finetuned*
  * Per Episode Overall Mean RMSE - Manual Trajectories
    |&nbsp; &nbsp; &nbsp; &nbsp; Gauss W/O Transition Noise &nbsp; &nbsp; &nbsp;|&nbsp; &nbsp; &nbsp; &nbsp; Gauss With Transition Noise &nbsp; &nbsp; &nbsp;|Gauss With Noise + Hard Resample|
    |------------|------------|------------|
    |![Gauss_WithOut_Noise](2021-06-07_08-00-00/manual_agent/images/gauss_500_15,0.523_0,0_0.8/eps_mean_rmse.svg)|![Gauss_With_Noise](2021-06-07_08-00-00/manual_agent/images/gauss_500_15,0.523_1,0.087_0.8/eps_mean_rmse.svg)|![Gauss_Noise_Hard_Resample](2021-06-07_08-00-00/manual_agent/images/gauss_500_15,0.523_1,0.087_1.0/eps_mean_rmse.svg)|

    |Gauss W/O Noise + More Particles &nbsp; &nbsp;|Uniform W/O Noise + More Particles &nbsp;|&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;|
    |------------|------------|------------|
    |![Gauss_WithOut_More_Particles](2021-06-07_08-00-00/manual_agent/images/gauss_1500_15,0.523_0,0_0.8/eps_mean_rmse.svg)|![Uniform_WithOut_More_Particles](2021-06-07_08-00-00/manual_agent/images/uniform_1500_75_0,0_0.8/eps_mean_rmse.svg)||
  * Per Episode End RMSE - Manual Trajectories
    |&nbsp; &nbsp; &nbsp; &nbsp; Gauss W/O Transition Noise &nbsp; &nbsp; &nbsp;|&nbsp; &nbsp; &nbsp; &nbsp; Gauss With Transition Noise &nbsp; &nbsp; &nbsp;|Gauss With Noise + Hard Resample|
    |------------|------------|------------|
    |![Gauss_WithOut_Noise](2021-06-07_08-00-00/manual_agent/images/gauss_500_15,0.523_0,0_0.8/eps_final_rmse.svg)|![Gauss_With_Noise](2021-06-07_08-00-00/manual_agent/images/gauss_500_15,0.523_1,0.087_0.8/eps_final_rmse.svg)|![Gauss_Noise_Hard_Resample](2021-06-07_08-00-00/manual_agent/images/gauss_500_15,0.523_1,0.087_1.0/eps_final_rmse.svg)|

    |Gauss W/O Noise + More Particles &nbsp; &nbsp;|Uniform W/O Noise + More Particles &nbsp;|&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;|
    |------------|------------|------------|
    |![Gauss_WithOut_More_Particles](2021-06-07_08-00-00/manual_agent/images/gauss_1500_15,0.523_0,0_0.8/eps_final_rmse.svg)|![Uniform_WithOut_More_Particles](2021-06-07_08-00-00/manual_agent/images/uniform_1500_75_0,0_0.8/eps_final_rmse.svg)||
  * Per Episode Overall Mean RMSE - Random Action Trajectories
    |&nbsp; &nbsp; &nbsp; &nbsp; Gauss W/O Transition Noise &nbsp; &nbsp; &nbsp;|&nbsp; &nbsp; &nbsp; &nbsp; Gauss With Transition Noise &nbsp; &nbsp; &nbsp;|Gauss With Noise + Hard Resample|
    |------------|------------|------------|
    |![Gauss_WithOut_Noise](2021-06-07_08-00-00/rnd_agent/images/gauss_500_15,0.523_0,0_0.8/eps_mean_rmse.svg)|![Gauss_With_Noise](2021-06-07_08-00-00/rnd_agent/images/gauss_500_15,0.523_1,0.087_0.8/eps_mean_rmse.svg)|![Gauss_Noise_Hard_Resample](2021-06-07_08-00-00/rnd_agent/images/gauss_500_15,0.523_1,0.087_1.0/eps_mean_rmse.svg)|

    |Gauss W/O Noise + More Particles &nbsp; &nbsp;|Uniform W/O Noise + More Particles &nbsp;|&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;|
    |------------|------------|------------|
    |![Gauss_WithOut_More_Particles](2021-06-07_08-00-00/rnd_agent/images/gauss_1500_15,0.523_0,0_0.8/eps_mean_rmse.svg)|![Uniform_WithOut_More_Particles](2021-06-07_08-00-00/rnd_agent/images/uniform_1500_75_0,0_0.8/eps_mean_rmse.svg)||
  * Per Episode End RMSE - Random Action Trajectories
    |&nbsp; &nbsp; &nbsp; &nbsp; Gauss W/O Transition Noise &nbsp; &nbsp; &nbsp;|&nbsp; &nbsp; &nbsp; &nbsp; Gauss With Transition Noise &nbsp; &nbsp; &nbsp;|Gauss With Noise + Hard Resample|
    |------------|------------|------------|
    |![Gauss_WithOut_Noise](2021-06-07_08-00-00/rnd_agent/images/gauss_500_15,0.523_0,0_0.8/eps_final_rmse.svg)|![Gauss_With_Noise](2021-06-07_08-00-00/rnd_agent/images/gauss_500_15,0.523_1,0.087_0.8/eps_final_rmse.svg)|![Gauss_Noise_Hard_Resample](2021-06-07_08-00-00/rnd_agent/images/gauss_500_15,0.523_1,0.087_1.0/eps_final_rmse.svg)|

    |Gauss W/O Noise + More Particles &nbsp; &nbsp;|Uniform W/O Noise + More Particles &nbsp;|&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;|
    |------------|------------|------------|
    |![Gauss_WithOut_More_Particles](2021-06-07_08-00-00/rnd_agent/images/gauss_1500_15,0.523_0,0_0.8/eps_final_rmse.svg)|![Uniform_WithOut_More_Particles](2021-06-07_08-00-00/rnd_agent/images/uniform_1500_75_0,0_0.8/eps_final_rmse.svg)||
  * Per Episode Overall Mean RMSE
    |Manual Agent w.r.t Original PFNet |Manual Agent w.r.t Finetuned PFNet |
    |------------|------------|
    |![Manual_Agent_Original_PFNet_EpsMean](2021-06-07_08-00-00/manual_agent/images/box_plots_overall/manual_agent_house_pfnet_eps_mean_rmse.png)|![Manual_Agent_Finetuned_PFNet_EpsMean](2021-06-07_08-00-00/manual_agent/images/box_plots_overall/manual_agent_igibson_pfnet_eps_mean_rmse.png)|

    |Random Agent w.r.t Original PFNet |Random Agent w.r.t Finetuned PFNet |
    |------------|------------|
    |![Random_Agent_Original_PFNet_EpsMean](2021-06-07_08-00-00/rnd_agent/images/box_plots_overall/rnd_agent_house_pfnet_eps_mean_rmse.png)|![Random_Agent_Finetuned_PFNet_EpsMean](2021-06-07_08-00-00/rnd_agent/images/box_plots_overall/rnd_agent_igibson_pfnet_eps_mean_rmse.png)|
  * Per Episode End Mean RMSE
    |Manual Agent w.r.t Original PFNet |Manual Agent w.r.t Finetuned PFNet |
    |------------|------------|
    |![Manual_Agent_Original_PFNet_EpsMean](2021-06-07_08-00-00/manual_agent/images/box_plots_overall/manual_agent_house_pfnet_eps_final_rmse.png)|![Manual_Agent_Finetuned_PFNet_EpsMean](2021-06-07_08-00-00/manual_agent/images/box_plots_overall/manual_agent_igibson_pfnet_eps_final_rmse.png)|

    |Random Agent w.r.t Original PFNet |Random Agent w.r.t Finetuned PFNet |
    |------------|------------|
    |![Random_Agent_Original_PFNet_EpsMean](2021-06-07_08-00-00/rnd_agent/images/box_plots_overall/rnd_agent_house_pfnet_eps_final_rmse.png)|![Random_Agent_Finetuned_PFNet_EpsMean](2021-06-07_08-00-00/rnd_agent/images/box_plots_overall/rnd_agent_igibson_pfnet_eps_final_rmse.png)|
</details>


<details open>
  <summary>June 10th - June 16th Summary</summary>

  ### Results
  * Per Episode Overall Mean RMSE
    |Manual Agent w.r.t Finetuned PFNet |Random Agent w.r.t Finetuned PFNet |
    |------------|------------|
    |![Manual_Agent_Finetuned_PFNet_EpsMean](2021-06-13_22-00-00/manual_agent/images/manual_agent_igibson_pfnet_eps_mean_rmse.png)|![Random_Agent_Finetuned_PFNet_EpsMean](2021-06-13_22-00-00/rnd_agent/images/rnd_agent_igibson_pfnet_eps_mean_rmse.png)|
  * Per Episode End Mean RMSE
    |Manual Agent w.r.t Finetuned PFNet |Random Agent w.r.t Finetuned PFNet |
    |------------|------------|
    |![Manual_Agent_Finetuned_PFNet_EpsEnd](2021-06-13_22-00-00/manual_agent/images/manual_agent_igibson_pfnet_eps_final_rmse.png)|![Random_Agent_Finetuned_PFNet_EpsEnd](2021-06-13_22-00-00/rnd_agent/images/rnd_agent_igibson_pfnet_eps_final_rmse.png)|
  * Episode Success Percentage (success: when last %25 steps has error < 1 meter)
    |Manual Agent w.r.t Finetuned PFNet |Random Agent w.r.t Finetuned PFNet |
    |------------|------------|
    |![Manual_Agent_Finetuned_PFNet_EpsSuccess](2021-06-13_22-00-00/manual_agent/images/manual_agent_igibson_pfnet_eps_success_rate.png)|![Random_Agent_Finetuned_PFNet_EpsSuccess](2021-06-13_22-00-00/rnd_agent/images/rnd_agent_igibson_pfnet_eps_success_rate.png)|

                                                                          
                                                                          <details open>
  <summary>June 24th - June 30th Summary</summary>

  ### Results
  * Per Episode Overall Mean RMSE
    |Manual Agent w.r.t Finetuned PFNet |Random Agent w.r.t Finetuned PFNet |
    |------------|------------|
    |![Manual_Agent_Finetuned_PFNet_EpsMean](2021-06-30_12-00-00/manual_agent/images/manual_agent_igibson_pfnet_eps_mean_rmse.png)|![Random_Agent_Finetuned_PFNet_EpsMean](2021-06-30_12-00-00/rnd_agent/images/rnd_agent_igibson_pfnet_eps_mean_rmse.png)|
  * Per Episode End Mean RMSE
    |Manual Agent w.r.t Finetuned PFNet |Random Agent w.r.t Finetuned PFNet |
    |------------|------------|
    |![Manual_Agent_Finetuned_PFNet_EpsEnd](2021-06-30_12-00-00/manual_agent/images/manual_agent_igibson_pfnet_eps_final_rmse.png)|![Random_Agent_Finetuned_PFNet_EpsEnd](2021-06-30_12-00-00/rnd_agent/images/rnd_agent_igibson_pfnet_eps_final_rmse.png)|
  * Episode Success Percentage (success: when last %25 steps has error < 1 meter)
    |Manual Agent w.r.t Finetuned PFNet |Random Agent w.r.t Finetuned PFNet |
    |------------|------------|
    |![Manual_Agent_Finetuned_PFNet_EpsSuccess](2021-06-30_12-00-00/manual_agent/images/manual_agent_igibson_pfnet_eps_success_rate.png)|![Random_Agent_Finetuned_PFNet_EpsSuccess](2021-06-30_12-00-00/rnd_agent/images/rnd_agent_igibson_pfnet_eps_success_rate.png)|
</details>
