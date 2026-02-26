; M3U8 Downloader 自动化脚本
; 使用方法：
; 1. 安装 AutoIt (https://www.autoitscript.com/site/autoit/)
; 2. 右键点击此文件，选择 "Edit Script" 或 "Run Script"
; 3. 如果要编译成 .exe，右键选择 "Compile Script"

#include <File.au3>

; 配置参数
Global Const $M3U8_URL = "https://hls.vxdyvk.cn/videos5/7c161fe8110f9abe9601138772227c72/7c161fe8110f9abe9601138772227c72.m3u8?auth_key=1771737023-699a8fbf7825a-0-658d2e2e62d47b81fa741a744671667c&v=3&time=0"
Global Const $DOWNLOADER_PATH = "D:\日常软件\M3U8 Downloader\M3U8 Downloader.exe"
Global Const $OUTPUT_DIR = "D:\Downloads"

; 主函数
Main()

Func Main()
    ; 检查程序是否存在
    If Not FileExists($DOWNLOADER_PATH) Then
        MsgBox(16, "错误", "找不到 M3U8 Downloader 程序：" & @CRLF & $DOWNLOADER_PATH)
        Exit
    EndIf

    ; 启动 M3U8 Downloader
    ConsoleWrite("正在启动 M3U8 Downloader..." & @CRLF)
    Run($DOWNLOADER_PATH)

    ; 等待窗口出现（最多等待10秒）
    ConsoleWrite("等待窗口出现..." & @CRLF)
    Local $hWnd = WinWait("M3U8 Downloader", "", 10)

    If $hWnd = 0 Then
        MsgBox(16, "错误", "无法找到 M3U8 Downloader 窗口")
        Exit
    EndIf

    ; 激活窗口
    ConsoleWrite("激活窗口..." & @CRLF)
    WinActivate($hWnd)
    WinWaitActive($hWnd, "", 5)

    ; 等待窗口完全加载
    Sleep(2000)

    ; 输入 M3U8 地址
    ConsoleWrite("输入 M3U8 地址..." & @CRLF)
    Send($M3U8_URL)
    Sleep(500)

    ; 尝试多种方法点击下载按钮
    ConsoleWrite("尝试点击下载按钮..." & @CRLF)

    ; 方法1：使用 Tab 键导航
    Send("{TAB}")
    Sleep(200)
    Send("{TAB}")
    Sleep(200)
    Send("{ENTER}")

    ; 方法2：如果上面不行，尝试使用 ControlClick
    ; 需要先使用 AutoIt Window Info 工具获取控件信息
    ; ControlClick("M3U8 Downloader", "", "[CLASS:Button; INSTANCE:1]")

    ; 方法3：直接点击屏幕坐标（需要根据实际情况调整）
    ; MouseClick("left", 500, 300, 1)

    ConsoleWrite("下载已开始..." & @CRLF)

    ; 等待下载完成（这里只是示例，实际需要根据窗口状态判断）
    ; 可以检查进度条、状态文本等
    Sleep(5000)

    ; 检查下载是否完成
    Local $downloadComplete = False
    Local $timeout = 300 ; 5分钟超时
    Local $elapsed = 0

    While $elapsed < $timeout And Not $downloadComplete
        ; 检查是否有"下载完成"或类似的提示窗口
        If WinExists("下载完成") Or WinExists("Download Complete") Or WinExists("成功") Then
            $downloadComplete = True
            ConsoleWrite("下载完成！" & @CRLF)
            ; 关闭完成提示
            WinClose("下载完成")
            WinClose("Download Complete")
            WinClose("成功")
        EndIf

        ; 检查是否有错误提示
        If WinExists("错误") Or WinExists("Error") Or WinExists("失败") Then
            ConsoleWrite("下载失败！" & @CRLF)
            $downloadComplete = True
        EndIf

        Sleep(1000)
        $elapsed += 1
    WEnd

    If Not $downloadComplete Then
        ConsoleWrite("下载超时，请手动检查..." & @CRLF)
    EndIf

    ; 询问是否关闭程序
    Local $closeApp = MsgBox(36, "完成", "下载操作已完成，是否关闭 M3U8 Downloader？", 10)
    If $closeApp = 6 Then ; Yes
        WinClose($hWnd)
    EndIf

    ConsoleWrite("脚本执行完成！" & @CRLF)
EndFunc