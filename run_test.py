import sys
from ultralytics import YOLO

def main():
    # 打印Python解释器的路径，确认我们用的是正确的 venv 环境
    print("--- 步骤 1: 检查Python解释器 ---")
    print(f"当前使用的Python解释器路径: {sys.executable}")
    if 'venv' in sys.executable:
        print("确认成功：正在使用项目内的 venv 环境！")
    else:
        print("警告：未使用正确的 venv 环境，请检查PyCharm解释器配置。")
    print("-" * 50)

    # 尝试加载模型，确认 ultralytics 库可以正常工作
    try:
        print("--- 步骤 2: 测试YOLOv8模型加载 ---")
        model = YOLO('yolov8n.pt')  # 这会自动下载模型
        print("模型加载成功！YOLOv8库可以正常工作！")
        print("-" * 50)
        print("恭喜！您的PyCharm环境已正确配置，可以进行下一步了！")

    except Exception as e:
        print(f"发生错误: {e}")
        print("测试失败。请确认 'ultralytics' 库已在 venv 环境中正确安装。")

if __name__ == '__main__':
    main()