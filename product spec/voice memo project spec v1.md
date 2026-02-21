voice memo project spec

what i have done so far:
i have recordings of around 5 days of my life with both anker product and also iphone
the main issues with the hardware:
- iphone's voice memo stops automatically when there is an incoming call etc. and no warning it stopped
- anker lasts a long time, and the device is small but there is no easy place to put it on the body, the magnet is not as strong and i'm in constant fear of losing it
- iphone's recording is super obvious on the phone screen and it's not good to have it there because you may want to show your phone screen to someone else
- a separate device definitely makes sense
- need to be easy to keep, no fear of losing it, doesn't look too obvious or threatening
- migrating the files to phones or laptops take a very long time
- for the anker device its a multi-step and the files are stored in a hidden place it takes a few steps to actually 


must have features:
- identify multiple speakers
    - 准确
    - 可以在每天结束的时候询问用户标记当天的说话人（#feature 提供一些说话人的音轨让用户可以和APP对话告知这个是谁，这个人是什么context - 比如我的老板，朋友，同事，做x的同事 etc）
    - 标好的说话人要记录下来这个非常重要，一直使用（#feature 可以有一个纠错的机制，比如可以多次检查一下这个说话人是不是对）
    - #feature 可以在APP里查看每个说话人的音轨，或者可以选择只听某个说话人的音轨
    - 用户自己的声音要识别的特别准不能有错，用户的声音有两种：一种是用户在开会的时候说话，一种是用户在dictate（ie 给指令，或者自己thinking out loud），这两种都很重要 + 特别是指令的部分格外的重要 #feature

- time of recording, metadata
    - 有日记的功能，什么时候在哪里（需要geo 信息）和谁讲了什么话，可以变成日记（#feature 可以在APP里查看每天的日记)
    - 现在的多以录音为单位记录，但我感觉应该以event 为单位记录。在同一个event 上的录音放在一起，可能多个录音file 也可以整合，以日历或者日记的形式让用户看，可能更容易和每天的生活/事件联系到一起（#feature）
    - #feature 录音的时候用户可以标记事件，或者在录音开始前用户可以直接和设备沟通这个是什么事件，等下要讲话的人是谁，大概是个什么内容，这样AI在process的时候就有context 了也减少错误

- audio summary  
    - 人一定是不会一个一个听自己的audio recording的，但不意味着他们不应该存，相反的应该把recording处理好（切成一段一段）并且和transcript匹配好。因为如果要录一天，很有可能会有很多的无效的声音，噪音，或者大段的空白，这些是需要被剪掉的，就是说我们一个核心的feature 应该是把大段大段几十个小时的recordings 剪好成真正有用的recording，有点像剪podcast 一样。这个可能是一个重点开发的东西，可能不简单#feature
    - 飞书的summary 能看，但并不punchy，我也并不想看，overview 的产品应该是更简单的。比如一个仪表盘，记录了今天讲了多少话，和多少人讲话，或者你的情绪如何，主要讨论的内容是哪些，很像健康类硬件产品或者苹果的activities / rings/apple health 的交互 #feature
    - 我觉得人需要的是总结，真的不是会议纪要。可能最后的总结是一个你今天干了什么，开了哪些内容的会，花了多长时间说话，听了多少字，然后会议纪要是链接（如果你想看可以看，但感觉不是很多人会看）。我们的产品不是一个会议纪要工具。会议纪要工具大多是给juniors 用的，比如我自己是不会记会议纪要的，但我会担心忘了很重要的会议里面讲了什么。#feature

- 信息的分类
    - 能想到有几种信息是应该被记录和分类的 #feature
        - 事件。这个设备的主人在什么时间干了什么，开了什么会，听了什么内容，和什么人说了什么话 etc
        - 人物。这个设备的主人生命中有哪些人一直在和他一起开会，喜欢听什么音乐，喜欢听哪些podcast，生活中的人是谁etc
        - facts。全天录制肯定会记录下来很多facts，比如这个人个人的一些facts，比如一些他看到的听到的事情的facts
        - to do。我感觉一个很重要的事情是给用户一个to do list。比如很多会议的时候一些有启发性的东西，应该更多的去check out。或者用户听到podcast 里面的一个概念需要去check out。甚至比如用户开会的时候说到，我应该去找xxx 聊聊 etc。甚至可能可以设计一些手势，比如动作x（摸一下硬件）就是应该follow up，比如动作y（弹两下）就是这个对话很重要
        - 证据？毕竟是一个录音设备，或许有的时候有些对话是可以用来记录下来以后拿出来做证据的。。。
    - 有些信息是对AI 有用的，但信息量对于人来说太多了。这部分信息就应该被整理好，然后用户可以feed 给他在使用的其他AI产品（我们可以build很好的integration with OpenClaw，Chatgpt，Claude etcetc）#feature
    - 有些信息是对人有用的，但这个应该是高度总结和抽象的。每个人都想更多的了解自己，大家都obssessed with knowing more about myself。所以应该是一个日记 + dashboard 的形态 #feature

- do users need their own personalisation?
    - 每个人的习惯不一样，对每个人来说什么样的信息是有效的也不一样
    - 理论上应该一开始有一个rubrics，但前几天使用的时候应该让用户多提供反馈然后update rubrics，让AI 更懂用户
    - 但有一个风险是，修改了以后的rubrics 可能按下葫芦起了瓢，提升了xxx但损害了yyy
    - 所以应该谨慎，什么rubrics 是可以修改的，什么不是。有点类似openclaw 其实非常dynamics，但这个是有问题 + 风险的
    - 需要给用户一个一键回退的机制，比如今天的总结不好，回退到x日#feature

- 产品需要的integrations
    - 支持自己的设备录制（最丝滑的体验），但也可以用其他设备 + iphone
    - 有gps /geo 信息
    - 是不是可以把apple 健康的数据也读到（用户的心率，情绪等）
    - 日历信息
    - email
    - 特别重要的，需要somehow 可以听到用户在听的内容（比如podcast，音乐，视频etc）
    - 所以我们需要的是plaud（可以自己设备录音 + 通过技术获取到用户耳机的声音 + 可以process 外面的file）+ 外部非声音的信息

- 产品：
    - 一个硬件（可以录音 + somehow 收到用户耳机的声音 + 用户可以通过触摸等姿势和他简单互动标记）
    - 一个APP（主要的交互界面）
        - dashboard
        - 日记
        - 交互界面（用户可以在这里和AI 进行交互，纠正说话人，标记事件，标记to do list etc）
    - 一个mac APP 或者webbased APP（更多的交互）因为如果我们的target 是knowledge worker，高级白领，他们大部分时间还是在电脑上

 可能的难点：
 - voice - > asr 质量（多说话人，嘈杂环境质量不好，相对专业的术语，中英混杂，语种切换）
 - 什么是重要的内容
 - 哪些信息应该怎么记录   


 硬件要求：
 - 一定要有GPS（或许也可以通过APP获取手机的定位）
 - 一般用户一天可能需要持续录音的max是15h，（8h睡觉+1h 在家里洗漱或者睡觉前信息量低 + 不方便录）
 - 硬件需要有3个能力：
    - 录音
    - 检测到用户在用耳机听的内容（类似plaud/讯飞耳机）
    - 可以简单方便的通过手势交互（比如双击，单击，滑动etc）

测试设备的问题：
- 用苹果自带录音：
    - 手机录音：有电话会自动停 + 不能同时播放音乐 / podcast 等 + 在屏幕上非常显眼，不方便
    - 电脑录音：同上 + 如果在用电脑录音的同时在打字记笔记，打字的声音会特别明显（但是可能也可以后处理处理掉）
- 用安克/飞书的设备录音：
    - somehow 录音总觉得不如苹果的清楚，有点闷闷的声音
    - 没法录耳机里面的内容
    - pendant 不太好放，稍微厚一点的衣服就不太容易夹住，衣领不是很现实（我大部分衣服的衣领都夹不住这个），夹在lululemon的卫衣的口袋上会很担心掉 + 声音不清楚（是不是因为人在坐着的时候会在桌子下面？）

我目前的测试录音files的问题：
- 有很响的键盘声（或许可以用软件的方法解决）
- 很distant，声音很远
- muffled（闷闷的，声音很不清楚）
- 有比较强的噪声（车里面）
- 有比较强的那种设备碰撞其他物体的杂音（比如在包里一直震动）

最好的设备是什么样的（可能不容易实现）
- 放在包里也能录（iphone 似乎可以，安克的不行，非常muffled）
- 放在兜里也能录的
- 靠手很近也不会capture 太多的键盘声音
- 在振动中也不会capture 很多杂音的

设备应该带在那里？
- 我的instinct 是，应该还是要固定在身体的某一个部位。就我们在设计这个设备的时候应该有一个明确的“如何佩戴”的想法，类似安克的设备虽然很”灵活“，但其实效果并不好，因为用户没法很快的test，而且也不知道哪些位置什么情况会造成录音质量低下
- 是不是应该离键盘远一点（会有很大的键盘声音）（这个就会against戴在手腕上，但或许键盘声音可以处理）
- 应该漏出来（如果在衣服里面可能会有比较严重的muffled的声音问题）
- 坐着的时候应该在桌子之上（桌子下好像会比较严重的影响录音质量）
- 我觉得应该不是很显眼
或许类似腕带，或者戒指 可能确实是最好的formfactor
有没有其他的ideas
