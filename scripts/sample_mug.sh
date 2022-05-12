
# change path to right one 
data_path="/home/kim/Desktop/repos/occupancy_networks/data/ShapeNet_mug/03797390"

while read line || [ -n "$line" ] ; do
    echo "Currently working on $line"
    current_input_path="$data_path/$line"

    echo "sample file into voxel, pcd, points"
    python sample_mesh.py $current_input_path/2_watertight \
      --points_folder $current_input_path
      #--pointcloud_folder $current_input_path \
      #--voxels_folder $current_input_path \
      #--mesh_folder $current_input_path \
done < valid_mugID.txt