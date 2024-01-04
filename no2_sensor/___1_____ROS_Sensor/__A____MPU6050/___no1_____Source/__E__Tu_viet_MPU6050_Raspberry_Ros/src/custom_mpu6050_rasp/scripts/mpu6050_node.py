from mpu6050 import mpu6050
import time

def read_mpu6050_data():
    address = 0x68  # Địa chỉ I2C của MPU6050
    sensor = mpu6050(address)

    # Đọc dữ liệu từ MPU6050
    accel_data = sensor.get_accel_data()
    gyro_data = sensor.get_gyro_data()

    print("Accelerometer data: {}".format(accel_data))
    print("Gyroscope data: {}".format(gyro_data))
    print("")

if __name__ == "__main__":
    try:
        while True:
            read_mpu6050_data()
            time.sleep(1)  # Đọc dữ liệu mỗi giây
    except KeyboardInterrupt:
        print("Dừng chương trình.")
