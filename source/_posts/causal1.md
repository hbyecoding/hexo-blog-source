---
title: 1因果推理初探 没有因果万万不能-DAGs
date: 2023-11-24 00:09:26
katex: true
tags: 因果
---

# 人类对于多任务的轻易掌控，是基于人类长期的知识、经验和习惯形成的

### 研究因果关系最大的一个目标，就是找出事物之间真正的因果关系，去掉那些混杂的伪因果关系。

这里我们先简简单介绍一下脸上的巧克力与诺贝尔奖的例子有研究表明，巧克力消费量越高的国家出现诺贝尔奖得主的概率就会越高但我们拥有常识的话，可以考虑到，很可能巧克力消费量并不是导致诺贝尔奖得主数量的一个原因，或者说原因。
因为一些共鸣，让巧克力销量和诺贝尔奖产生了关联。这些共因我们猜测有可能是经济增长水平程度等等。
假的例子或者说混淆抽烟的人容易，患肺癌头晕的人也容易出现黄手指因为抽烟这个共同原因，黄手指和肺癌产生了关联。我们不难发现手指黄的人，很多都容易被检测出肺癌，但我们不能说黄手指会导致肺癌，他俩并没有因果关系。这个共同原因也被称之为混杂因子（Confounder）。因此让黄手指这个explosure和肺癌outcome出现了一种伪相关，这种伪相关被称为 bias。

因果关系$A \rightarrow Y$和差连接诱导的伪相关混合在一起