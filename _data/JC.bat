@Rem 进入当前目录
cd /d %~dp0

@Rem 切换到下一级目录
cd JC_Update

@Rem 执行脚本
python testUI.py

@Rem 保存窗口 加 "pause" 或 "cmd/k"
@Rem 关闭窗口 加 "exit"
exit