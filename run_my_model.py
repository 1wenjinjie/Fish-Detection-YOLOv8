from ultralytics import YOLO
import os

def main():
    # --- 1. 加载您自己的专属模型 ---
    # 请务必确认这个路径和您电脑上的实际路径一致！
    model_path = 'runs/detect/train2/weights/best.pt'
    print(f"正在加载您的专属模型: {model_path}")
    model = YOLO(model_path)
    print("模型加载成功！")

    # --- 2. 指定您想预测的图片 ---
    # 我们可以先用测试集里的一张图片来牛刀小试
    # 您可以从左侧 test/images/ 文件夹里选择任意一张图片，把名字复制过来
    image_to_predict = 'irene-berral-hens-mJwTvRloq-c-unsplash.jpg'
    print(f"准备对图片 '{image_to_predict}' 进行预测...")

    # --- 3. 执行预测 ---
    # save=True 的意思是将画好检测框的图片保存下来
    results = model.predict(source=image_to_predict, conf=0.5, save=True)
    print("预测已执行。")

    # --- 4. 打印结果保存路径 ---
    # ultralytics v8.2之后的版本，可以通过 results[0].save_dir 获取保存路径
    if results and hasattr(results[0], 'save_dir'):
         save_directory = results[0].save_dir
         print(f"预测完成！请在项目文件夹下的 '{save_directory}' 目录中查看结果图片。")
         # 在macOS上自动打开结果文件夹
         os.system(f'open "{save_directory}"')
    else:
         print("预测完成！请在项目文件夹下的 'runs/detect/' 目录中查看结果！")


if __name__ == '__main__':
    main()