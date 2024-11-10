#include <iostream>
#include <pcl/point_cloud.h>
#include <pcl/point_types.h>

int main() {
    pcl::PointCloud<pcl::PointXYZ> cloud;
    cloud.width = 5;
    cloud.height = 1;
    cloud.is_dense = false;
    cloud.points.resize(cloud.width * cloud.height);

    for (auto& point : cloud.points) {
        point.x = static_cast<float>(rand()) / RAND_MAX;
        point.y = static_cast<float>(rand()) / RAND_MAX;
        point.z = static_cast<float>(rand()) / RAND_MAX;
    }

    std::cout << "Generated a point cloud with " << cloud.points.size() << " points." << std::endl;
    return 0;
}
