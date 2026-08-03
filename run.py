# -*- coding: utf-8 -*-
"""
run.py —— 问心无愧 App 启动入口
=================================
- 电脑：直接 `python run.py` → 启动 Kivy 窗口
- 手机 Termux：同上
- 无显示器（SSH/远程）：自动降级为命令行模式
"""
import sys
import os

# 把 src/ 加入 path，让 "from core import ..." 能找到
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "src"))

def main():
    # 检测是否有显示器
    has_display = bool(os.environ.get("DISPLAY") or os.environ.get("WAYLAND_DISPLAY"))
    is_android = "ANDROID_ROOT" in os.environ or "ANDROID_DATA" in os.environ

    if has_display or is_android:
        # 有显示器 → 启动 Kivy App
        from main import WenXinApp
        WenXinApp().run()
    else:
        # 无显示器 → 命令行降级模式
        print("=" * 50)
        print("  问心无愧 v1.0 - 命令行模式（无显示器）")
        print("=" * 50)
        print()
        print("提示: 本程序为手机 App 设计，命令行模式仅用于调试。")
        print("     如需完整功能，请在电脑/手机上运行。")
        print()
        # 简单测试
        try:
            from core import _PROXY_LIST, API_NAMES, __version__
            print(f"✅ 核心模块加载成功 v{__version__}")
            print(f"   代理池: {len(_PROXY_LIST)} 条")
            print(f"   接口: {', '.join(API_NAMES.values())}")
        except Exception as e:
            print(f"❌ 核心模块加载失败: {e}")
            sys.exit(1)

        # 简单单次核验
        name = input("姓名（回车=蓝福平）：").strip() or "蓝福平"
        sfz = input("身份证（回车=测试号）：").strip() or "452129197812021073"

        from core import verify_api6, _ins6_warmup_session
        print(f"\n🔥 预热接口⑥...")
        try:
            _ins6_warmup_session(name, sfz, force=True)
        except Exception as e:
            print(f"  预热异常: {e}")

        print(f"▶ 核验中...")
        m, msg, data, cost = verify_api6(name, sfz)
        if m is True:
            print(f"✅ 匹配! [{msg}] 耗时{cost:.0f}ms")
        elif m is False:
            print(f"❌ 不匹配 [{msg}]")
        else:
            print(f"⚠️ 未知 [{msg}]")

if __name__ == "__main__":
    main()
