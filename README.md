# M3U8 自动化工具集合

这是一个 M3U8 Downloader 自动化工具集合，包含 Pywinauto 和 AutoIt 脚本，用于自动化操作 M3U8 Downloader 进行视频下载。

## 功能特性

- **Pywinauto 脚本**：使用 Python 的 pywinauto 库自动化操作 M3U8 Downloader GUI
- **AutoIt 脚本**：使用 AutoIt 脚本语言自动化操作 M3U8 Downloader
- **窗口分析工具**：用于分析 M3U8 Downloader 的窗口结构和控件信息

## 文件说明

### 1. `m3u8_automation.py`
- **功能**：使用 Pywinauto 自动化启动 M3U8 Downloader、输入 M3U8 URL 并点击下载按钮
- **依赖**：需要安装 `pywinauto` 库
- **使用方法**：
  ```bash
  # 安装依赖
  pip install pywinauto
  
  # 运行脚本
  python m3u8_automation.py
  ```

### 2. `analyze_window.py`
- **功能**：分析 M3U8 Downloader 的窗口结构和控件信息，帮助定位控件
- **依赖**：需要安装 `pywinauto` 库
- **使用方法**：
  ```bash
  python analyze_window.py
  ```

### 3. `m3u8-downloader.au3`
- **功能**：使用 AutoIt 脚本自动化操作 M3U8 Downloader
- **依赖**：需要安装 AutoIt
- **使用方法**：
  1. 安装 AutoIt (https://www.autoitscript.com/site/autoit/)
  2. 右键点击此文件，选择 "Edit Script" 或 "Run Script"
  3. 如果要编译成 .exe，右键选择 "Compile Script"

## 配置说明

### Pywinauto 脚本配置
在 `m3u8_automation.py` 中修改以下参数：

```python
# 配置参数
M3U8_URL = "https://example.com/playlist.m3u8"  # M3U8 地址
DOWNLOADER_PATH = r"D:\日常软件\M3U8 Downloader\M3U8 Downloader.exe"  # 下载器路径
OUTPUT_DIR = r"D:\Downloads"  # 输出目录
```

### AutoIt 脚本配置
在 `m3u8-downloader.au3` 中修改以下参数：

```autoit
; 配置参数
Global Const $M3U8_URL = "https://example.com/playlist.m3u8"  ; M3U8 地址
Global Const $DOWNLOADER_PATH = "D:\日常软件\M3U8 Downloader\M3U8 Downloader.exe"  ; 下载器路径
Global Const $OUTPUT_DIR = "D:\Downloads"  ; 输出目录
```

## 注意事项

1. **窗口标题**：脚本默认使用 "M3U8 Downloader" 作为窗口标题，如果你的下载器窗口标题不同，请修改脚本中的对应部分
2. **控件识别**：不同版本的 M3U8 Downloader 可能有不同的控件结构，可能需要使用 `analyze_window.py` 分析后调整脚本
3. **依赖安装**：使用 Pywinauto 脚本前需要安装 `pywinauto` 库
4. **权限问题**：确保脚本有足够的权限运行和操作 M3U8 Downloader
5. **网络连接**：确保网络连接正常，M3U8 地址可访问

## 故障排查

### 1. Pywinauto 找不到窗口
- 检查窗口标题是否正确
- 检查 M3U8 Downloader 是否正在运行
- 运行 `analyze_window.py` 查看窗口信息

### 2. 控件点击失败
- 使用 `analyze_window.py` 分析控件结构
- 调整脚本中的控件标识符
- 尝试使用不同的控件查找方法

### 3. AutoIt 脚本问题
- 确保已安装 AutoIt
- 检查 `#include <File.au3>` 是否正确
- 使用 AutoIt Window Info 工具获取控件信息

## 系统要求

- **操作系统**：Windows
- **Python**：3.6+
- **AutoIt**：v3+（使用 AutoIt 脚本时需要）
- **依赖库**：pywinauto（使用 Python 脚本时需要）

## 许可证

本项目采用 MIT 许可证 - 详见 LICENSE 文件

## 贡献

欢迎提交 Issue 和 Pull Request！

## 联系方式

如果有任何问题，请通过 GitHub Issues 联系。