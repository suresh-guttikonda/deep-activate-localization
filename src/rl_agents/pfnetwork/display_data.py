#!/usr/bin/env python3

import cv2
import matplotlib.cm as cm
import matplotlib.pyplot as plt
from matplotlib.patches import Wedge
import numpy as np
import preprocess, arguments
from scipy.special import softmax

def display_data(params):
    """
    display data with the parsed arguments
    """

    # testing data
    test_ds = preprocess.get_dataflow(params.testfiles, params.batch_size, is_training=False)

    itr = test_ds.as_numpy_iterator()
    raw_record = next(itr)
    data_sample = preprocess.transform_raw_record(raw_record, params)

    b_idx = 2
    t_idx = 10
    batch_size = params.batch_size
    num_particles = params.num_particles
    observation = data_sample['observation'][b_idx]
    odometry = data_sample['odometry'][b_idx]
    true_states = data_sample['true_states'][b_idx]
    global_map = data_sample['global_map'][b_idx]
    init_particles = data_sample['init_particles'][b_idx]
    # init_particle_weights = np.full(shape=(batch_size, num_particles), fill_value=np.log(1.0 / float(num_particles)))[b_idx]
    init_particle_weights = np.random.random(size=(batch_size, num_particles))[b_idx]
    org_map_shape = data_sample['org_map_shapes'][b_idx]
    org_map = global_map[:org_map_shape[0], :org_map_shape[1], :org_map_shape[2]]

    if params.obs_mode == 'rgb-depth':
        rgb, depth = np.split(observation, [3], axis=-1)
        cv2.imwrite('./rgb.png', preprocess.denormalize_observation(rgb[t_idx]))
        cv2.imwrite('./depth.png', cv2.applyColorMap(
            preprocess.denormalize_observation(depth[t_idx]*255/100).astype(np.uint8),
            cv2.COLORMAP_JET))

        rgb_obs = []
        for t_idx in range(0, rgb.shape[0]-1):
            rgb_obs.append(preprocess.denormalize_observation(rgb[t_idx]).astype(np.uint8))
        convert_imgs_to_video(rgb_obs, "rgb_obs.avi")
        depth_obs = []
        for t_idx in range(0, depth.shape[0]-1):
            depth_obs.append(cv2.applyColorMap(preprocess.denormalize_observation(depth[t_idx]*255/100).astype(np.uint8), cv2.COLORMAP_JET))
        convert_imgs_to_video(depth_obs, "depth_obs.avi")
    elif params.obs_mode == 'depth':
        cv2.imwrite('./depth.png', cv2.applyColorMap(
            preprocess.denormalize_observation(observation[t_idx]*255/100).astype(np.uint8),
            cv2.COLORMAP_JET))
        depth_obs = []
        for t_idx in range(0, observation.shape[0]-1):
            depth_obs.append(cv2.applyColorMap(preprocess.denormalize_observation(observation[t_idx]*255/100).astype(np.uint8), cv2.COLORMAP_JET))
        convert_imgs_to_video(depth_obs, "depth_obs.avi")
    else:
        cv2.imwrite('./rgb.png', preprocess.denormalize_observation(observation[t_idx]))
        rgb_obs = []
        for t_idx in range(0, observation.shape[0]-1):
            rgb_obs.append(preprocess.denormalize_observation(observation[t_idx]).astype(np.uint8))
        convert_imgs_to_video(rgb_obs, "rgb_obs.avi")

    # floor map
    fig = plt.figure(figsize=(10, 10))
    plt_ax = fig.add_subplot(111)
    plt_ax.imshow(org_map)

    # init particles
    # HACK: display particles alpha proprtional to their weights
    init_lin_weights = softmax(init_particle_weights)
    th = np.mean(init_lin_weights)
    alphas = np.where(init_lin_weights >= th, 1, 0) * init_lin_weights
    alphas = alphas/np.max(alphas)

    part_x, part_y, part_th = np.split(init_particles, 3, axis=-1)
    rgba_colors = cm.rainbow(init_particle_weights-np.min(init_particle_weights))
    rgba_colors[:, 3] = alphas
    plt_ax.scatter(part_x, part_y, s=10, c=rgba_colors)

    x1, y1, th1 = true_states[0]
    # gt init pose
    heading_len  = robot_radius = 10.0
    xdata = [x1, x1 + (robot_radius + heading_len) * np.cos(th1)]
    ydata = [y1, y1 + (robot_radius + heading_len) * np.sin(th1)]
    position_plt = Wedge((x1, y1), r=robot_radius, theta1=0, theta2=360, color='blue', alpha=0.5)
    plt_ax.add_artist(position_plt)
    plt_ax.plot(xdata, ydata, color='blue', alpha=0.5)

    # # gt trajectory (w.r.t odometry)
    # for t_idx in range(1, true_states.shape[0]):
    #     x2, y2, th2 = true_states[t_idx]
    #     plt_ax.arrow(x1, y1, (x2-x1), (y2-y1), head_width=5, head_length=7, fc='black', ec='black')
    #     x1, y1, th1 = x2, y2, th2

    # gt trajectory (w.r.t gt pose)
    for t_idx in range(0, odometry.shape[0]-1):
        x2, y2, th2 = preprocess.sample_motion_odometry(np.array([x1, y1, th1]),odometry[t_idx])
        plt_ax.arrow(x1, y1, (x2-x1), (y2-y1), head_width=5, head_length=7, fc='black', ec='black')
        x1, y1, th1 = x2, y2, th2

    # plt.show()
    plt.savefig("traj_output.png")

    print('display done')

def convert_imgs_to_video(images, file_path):
    fps = 60
    frame_size = (images[0].shape[0], images[0].shape[1])
    out = cv2.VideoWriter(file_path,
                          cv2.VideoWriter_fourcc(*'XVID'),
                          fps, frame_size)
    for img in images:
        out.write(img)
    out.release()

if __name__ == '__main__':
    params = arguments.parse_args()

    display_data(params)
