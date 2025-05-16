import os

def traverse_directory(path='.'):
    """遍历指定目录并打印所有文件和文件夹"""
    try:
        print(f"正在遍历目录: {os.path.abspath(path)}")
        print("=" * 50)
        
        for root, dirs, files in os.walk(path):
            # 计算当前目录的缩进级别
            level = root.replace(path, '').count(os.sep)
            indent = ' ' * 4 * level
            
            # 打印当前目录
            print(f"{indent}[目录] {os.path.basename(root)}")
            
            # 打印当前目录下的所有文件
            sub_indent = ' ' * 4 * (level + 1)
            for file in files:
                print(f"{sub_indent}{file}")
        
        print("=" * 50)
        print("遍历完成")
        
    except Exception as e:
        print(f"错误: {e}")

if __name__ == "__main__":
    # 可以修改为你想遍历的目录路径
    target_directory = 'E:\gitlab cangku'
    traverse_directory(target_directory)    