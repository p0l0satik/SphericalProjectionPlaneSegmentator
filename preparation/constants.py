# Kitti labels
KITI_ROAD_LABELS = (40, 48, 44, 49)

# Inner dataset structure
PLANES_LABELS = "plane_labels"
KITTI_LABELS = "labels"
POINT_CLOUDS = "velodyne"

# File extensions
POINTCLOUD_EXT = ['.bin', ".pcd"]
LABELS_EXT = [".npy", ".label"]

# RANSAC parameters
RANSAC_N = 3
RANSAC_THRESHOLD = 0.05
RANSAC_N_ITER = 100