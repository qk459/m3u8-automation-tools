#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
M3U8 Downloader 自动化脚本
使用 pywinauto 库自动化操作 M3U8 Downloader GUI
"""

import time
import os
from pywinauto import Application, keyboard
from pywinauto.timings import Timings

# 配置参数
M3U8_URL = "https://hls.vxdyvk.cn/videos5/7c161fe8110f9abe9601138772227c72/7c161fe8110f9abe9601138772227c72.m3u8?auth_key=1771737023-699a8fbf7825a-0-658d2e2e62d47b81fa741a744671667c&v=3&time=0"
DOWNLOADER_PATH = r"D:\日常软件\M3U8 Downloader\M3U8 Downloader.exe"
OUTPUT_DIR = r"D:\Downloads"

# 设置超时时间（秒）
Timings.fast()
Timings.window_find_timeout = 10
Timings.after_click_wait = 0.5
Timings.after_menu_wait = 0.5
Timings.after_sendkeys_wait = 0.3


def print_log(message):
    """打印日志信息"""
    timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
    print(f"[{timestamp}] {message}")


def check_file_exists(filepath):
    """检查文件是否存在"""
    if not os.path.exists(filepath):
        raise FileNotFoundError(f"找不到文件：{filepath}")
    print_log(f"✓ 文件存在：{filepath}")


def start_downloader():
    """启动 M3U8 Downloader"""
    print_log("正在启动 M3U8 Downloader...")
    
    try:
        # 启动应用程序
        app = Application(backend="uia").start(DOWNLOADER_PATH)
        print_log("✓ M3U8 Downloader 已启动")
        return app
    except Exception as e:
        print_log(f"✗ 启动失败：{e}")
        raise


def connect_to_app():
    """连接到已运行的 M3U8 Downloader"""
    print_log("尝试连接到 M3U8 Downloader...")
    
    try:
        # 尝试通过进程名连接
        app = Application(backend="uia").connect(title="M3U8 Downloader")
        print_log("✓ 已连接到 M3U8 Downloader")
        return app
    except Exception as e:
        print_log(f"✗ 连接失败：{e}")
        return None


def get_window_info(app):
    """获取窗口和控件信息"""
    print_log("正在分析窗口结构...")
    
    try:
        dlg = app.window(title="M3U8 Downloader")
        print_log(f"窗口标题：{dlg.window_text()}")
        print_log(f"窗口句柄：{dlg.handle}")
        
        # 打印控件树
        print_log("\n=== 控件树结构 ===")
        dlg.print_control_identifiers()
        print_log("=== 控件树结构结束 ===\n")
        
        return dlg
    except Exception as e:
        print_log(f"✗ 获取窗口信息失败：{e}")
        return None


def input_m3u8_url(dlg, url):
    """输入 M3U8 URL"""
    print_log(f"正在输入 M3U8 URL：{url}")
    
    try:
        # 方法1：尝试找到 URL 输入框
        # 常见的控件标识符
        edit_control = None
        
        # 尝试多种方式找到输入框
        possible_identifiers = [
            "Edit",
            "Edit0", 
            "Edit1",
            "Edit2",
            "URL",
            "Address",
            "TextBox",
            "ComboBox"
        ]
        
        for identifier in possible_identifiers:
            try:
                edit_control = dlg.child_window(auto_id=identifier)
                if edit_control:
                    print_log(f"✓ 找到输入框：{identifier}")
                    break
            except:
                continue
        
        if edit_control:
            # 清空并输入新 URL
            edit_control.set_focus()
            edit_control.type_keys("^a")  # Ctrl+A 全选
            edit_control.type_keys("{DELETE}")  # 删除
            edit_control.type_keys(url)
            print_log("✓ URL 已输入")
        else:
            # 方法2：使用键盘输入
            print_log("未找到输入框，使用键盘输入...")
            dlg.set_focus()
            keyboard.send_keys("^a")  # Ctrl+A 全选
            keyboard.send_keys("{DELETE}")  # 删除
            keyboard.send_keys(url)
            print_log("✓ URL 已通过键盘输入")
            
    except Exception as e:
        print_log(f"✗ 输入 URL 失败：{e}")
        raise


def click_download_button(dlg):
    """点击下载按钮"""
    print_log("正在点击下载按钮...")
    
    try:
        # 方法1：尝试找到下载按钮
        button = None
        
        possible_buttons = [
            "下载",
            "Download",
            "Button",
            "Button0",
            "Button1",
            "Button2",
            "开始",
            "Start"
        ]
        
        for btn_name in possible_buttons:
            try:
                button = dlg.child_window(title=btn_name, control_type="Button")
                if button:
                    print_log(f"✓ 找到下载按钮：{btn_name}")
                    button.click()
                    print_log("✓ 下载按钮已点击")
                    return True
            except:
                continue
        
        # 方法2：尝试通过控件类型查找
        try:
            buttons = dlg.descendants(control_type="Button")
            if buttons:
                print_log(f"找到 {len(buttons)} 个按钮")
                for btn in buttons:
                    print_log(f"  - {btn.window_text()}")
                # 点击第一个按钮（通常是下载按钮）
                buttons[0].click()
                print_log("✓ 已点击第一个按钮")
                return True
        except:
            pass
        
        # 方法3：使用键盘快捷键
        print_log("未找到下载按钮，尝试使用键盘...")
        dlg.set_focus()
        keyboard.send_keys("{TAB}")  # Tab 到按钮
        time.sleep(0.2)
        keyboard.send_keys("{ENTER}")  # 回车点击
        print_log("✓ 已通过键盘触发下载")
        return True
        
    except Exception as e:
        print_log(f"✗ 点击下载按钮失败：{e}")
        return False


def wait_for_download_complete(dlg, timeout=300):
    """等待下载完成"""
    print_log(f"等待下载完成（超时时间：{timeout}秒）...")
    
    start_time = time.time()
    
    while time.time() - start_time < timeout:
        try:
            # 检查是否有完成提示窗口
            # 这里需要根据实际情况调整
            
            # 方法1：检查主窗口的状态文本
            # status_text = dlg.child_window(auto_id="StatusBar").window_text()
            
            # 方法2：检查是否有弹窗
            # popup = app.window(title="下载完成")
            # if popup.exists():
            #     print_log("✓ 下载完成！")
            #     return True
            
            # 方法3：检查进度条
            # progress = dlg.child_window(auto_id="ProgressBar")
            # if progress:
            #     progress_value = progress.get_value()
            #     print_log(f"下载进度：{progress_value}%")
            
            time.sleep(1)
            
        except Exception as e:
            print_log(f"检查下载状态时出错：{e}")
            time.sleep(1)
    
    print_log("⚠ 下载超时，请手动检查")
    return False


def main():
    """主函数"""
    print_log("=" * 50)
    print_log("M3U8 Downloader 自动化脚本")
    print_log("=" * 50)
    
    try:
        # 检查程序文件
        check_file_exists(DOWNLOADER_PATH)
        
        # 启动或连接到程序
        app = start_downloader()
        time.sleep(3)  # 等待程序完全启动
        
        # 连接到窗口
        app = Application(backend="uia").connect(title="M3U8 Downloader")
        dlg = app.window(title="M3U8 Downloader")
        
        # 获取窗口信息（用于调试）
        get_window_info(app)
        
        # 输入 M3U8 URL
        input_m3u8_url(dlg, M3U8_URL)
        time.sleep(1)
        
        # 点击下载按钮
        if click_download_button(dlg):
            time.sleep(2)
            
            # 等待下载完成（可选）
            # wait_for_download_complete(dlg)
            
            print_log("✓ 下载已开始")
            print_log("\n提示：请手动监控下载进度")
            print_log("脚本将在 30 秒后退出...")
            time.sleep(30)
        else:
            print_log("✗ 无法启动下载")
            
    except Exception as e:
        print_log(f"✗ 脚本执行失败：{e}")
        import traceback
        traceback.print_exc()
    finally:
        print_log("=" * 50)
        print_log("脚本执行结束")
        print_log("=" * 50)


if __name__ == "__main__":
    main()