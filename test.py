import numpy as np
import binvox_rw as bv

if __name__=="__main__":
    data = np.load("/home/kim/Desktop/repos/occupancy_networks/data/ShapeNet_mug/03797390/10f6e09036350e92b3f21f1137c3c347/points.npz")
    with open("/home/kim/Desktop/repos/occupancy_networks/data/ShapeNet_mug/03797390/5fe74baba21bba7ca4eec1b19b3a18f8/model.binvox", "rb") as f:
        vox = bv.read_as_3d_array(f) #10155655850468db78d106ce0a280f87
    lst = data.files
    print("voxl")
    print(vox.dims)
    print(vox.scale)
    print(vox.translate)

    for it in lst:
        print(it)
        print(data[it])
