# genshin-with-midi-input

用你的 midi 键盘来玩原神的风物之诗琴     
English [here][en]

## quick start

- 安装依赖包:
```
pip install pywin32 pygame
```
- 连上你的 midi 键盘然后等 Windows 自己装驱动
- 开启原神打开诗琴界面
- 用管理员权限打开 cmd，运行这个脚本:
```
python main.py
```

## 鸣谢

灵感来源于[Misaka17032 的 genshin-lyre-auto-play][origin]    
其中的 `press`, `unpress`, `pop_window` 等函数也是从他那里薅的。

[en]: https://github.com/MakDon/genshin-with-midi-input/blob/main/README.md
[cn]: https://github.com/MakDon/genshin-with-midi-input/blob/main/README-cn.md
[origin]: https://github.com/Misaka17032/genshin-lyre-auto-play