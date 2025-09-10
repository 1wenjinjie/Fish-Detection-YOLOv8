from ultralytics import YOLO

def main():
    # 加载官方的 YOLOv8n 模型
    model = YOLO('yolov8n.pt')

    # 对我们数据集的测试图片文件夹进行预测
    print("开始对 'test/images/' 文件夹中的图片进行预测...")
    results = model.predict(source='test/images/', conf=0.5, save=True)

    # 打印出结果保存的路径
    # 注意：结果文件夹的真实名称可能是 predict, predict2, predict3...
    # ultralytics v8.2之后的版本，可以通过 results[0].save_dir 获取保存路径
    if results and hasattr(results[0], 'save_dir'):
         print(f"预测完成！请在项目文件夹下的 '{results[0].save_dir}' 目录中查看结果图片。")
    else:
         print("预测完成！请在项目文件夹下的 'runs/detect/' 目录中查看结果图片。")


if __name__ == '__main__':
    main()