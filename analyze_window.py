#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
窗口分析工具
用于分析 M3U8 Downloader 的窗口结构和控件信息
"""

import time
from pywinauto import Application

def analyze_window():
    """分析窗口结构"""
    print("=" * 60)
    print("M3U8 Downloader 窗口分析工具")
    print("=" * 60)
    
    # 检查程序是否已运行
    try:
        app = Application(backend="uia").connect(title="M3U8 Downloader")
        print("✓ 已连接到运行的 M3U8 Downloader")
    except:
        print("✗ M3U8 Downloader 未运行，正在启动...")
        try:
            app = Application(backend="uia").start(r"D:\日常软件\M3U8 Downloader\M3U8 Downloader.exe")
            print("✓ M3U8 Downloader 已启动")
            time.sleep(3)  # 等待程序启动
        except Exception as e:
            print(f"✗ 启动失败：{e}")
            return
    
    try:
        # 获取主窗口
        dlg = app.window(title="M3U8 Downloader")
        
        print("\n" + "=" * 60)
        print("窗口基本信息")
        print("=" * 60)
        print(f"窗口标题：{dlg.window_text()}")
        print(f"窗口类名：{dlg.class_name()}")
        print(f"窗口句柄：{dlg.handle}")
        print(f"窗口矩形：{dlg.rectangle()}")
        
        print("\n" + "=" * 60)
        print("控件树结构")
        print("=" * 60)
        
        # 打印完整的控件树
        dlg.print_control_identifiers(depth=None, filename=None)
        
        print("\n" + "=" * 60)
        print("主要控件详情")
        print("=" * 60)
        
        # 查找所有按钮
        try:
            buttons = dlg.descendants(control_type="Button")
            print(f"\n找到 {len(buttons)} 个按钮：")
            for i, btn in enumerate(buttons):
                print(f"  按钮 {i+1}:")
                print(f"    - 文本：{btn.window_text()}")
                print(f"    - 类名：{btn.class_name()}")
                print(f"    - 矩形：{btn.rectangle()}")
        except Exception as e:
            print(f"查找按钮失败：{e}")
        
        # 查找所有编辑框
        try:
            edits = dlg.descendants(control_type="Edit")
            print(f"\n找到 {len(edits)} 个编辑框：")
            for i, edit in enumerate(edits):
                print(f"  编辑框 {i+1}:")
                print(f"    - 文本：{edit.window_text()}")
                print(f"    - 类名：{edit.class_name()}")
                print(f"    - 矩形：{edit.rectangle()}")
        except Exception as e:
            print(f"查找编辑框失败：{e}")
        
        # 查找所有组合框
        try:
            combos = dlg.descendants(control_type="ComboBox")
            print(f"\n找到 {len(combos)} 个组合框：")
            for i, combo in enumerate(combos):
                print(f"  组合框 {i+1}:")
                print(f"    - 文本：{combo.window_text()}")
                print(f"    - 类名：{combo.class_name()}")
                print(f"    - 矩形：{combo.rectangle()}")
        except Exception as e:
            print(f"查找组合框失败：{e}")
        
        # 查找进度条
        try:
            progress = dlg.descendants(control_type="ProgressBar")
            if progress:
                print(f"\n找到 {len(progress)} 个进度条：")
                for i, prog in enumerate(progress):
                    print(f"  进度条 {i+1}:")
                    print(f"    - 类名：{prog.class_name()}")
                    print(f"    - 矩形：{prog.rectangle()}")
        except Exception as e:
            print(f"查找进度条失败：{e}")
        
        print("\n" + "=" * 60)
        print("分析完成")
        print("=" * 60)
        
        # 保持窗口打开，方便查看
        print("\n提示：窗口保持打开状态，按 Ctrl+C 退出")
        try:
            while True:
                time.sleep(1)
        except KeyboardInterrupt:
            print("\n用户中断")
            
    except Exception as e:
        print(f"✗ 分析失败：{e}")
        import traceback
        traceback.print_exc()


if __name__ == "__main__":
    analyze_window()