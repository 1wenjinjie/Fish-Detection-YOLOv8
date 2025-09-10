from ultralytics import YOLO

def main():
    # 加载官方的 yolov8n.pt 模型作为预训练权重
    model = YOLO('yolov8n.pt')

    # 使用 data.yaml 文件开始训练
    # 注意：请确保 data.yaml 文件在您的项目根目录下，并且内容正确
    print("开始训练模型... 这个过程可能会持续很长时间。")
    results = model.train(data='data.yaml', epochs=50, imgsz=640)

    print("训练完成！最好的模型已保存在 'runs/train/' 目录下的weights文件夹中，名为 best.pt。")

if __name__ == '__main__':
    main()