---
layout: default
comments: true
category: code
tags: [ios]
title: Property and its Attributes in Objective-C
---
---



* @synthesize: @synthesize can only be used to property, not iVar.

* atomic / nonatomic

* strong / weak

* assign / retain / copy: go to [here](http://blog.csdn.net/jiarusun000/article/details/6991249) for reference.

* readonly / readwrite

[Here](http://www.cnblogs.com/andyque/archive/2011/08/03/2125728.html) has a detail description. And the useful part:
 
* 什么时候用assign、什么时候用retain和copy呢？推荐做法是NSString用copy,delegate用assign（且一定要用assign，不要问为什么，只管去用就是了，以后你会明白的），非objc数据类型，比如int，float等基本数据类型用assign（默认就是assign），而其它objc类型，比如NSArray，NSDate用retain。
* 当别人使用@property来做内存管理的时候就会有问题了。总结一下，如果你自己实现了getter和setter的话，atomic/nonatomic/retain/assign/copy这些只是给编译的建议，编译会首先会到你的代码里面去找，如果你定义了相应的getter和setter的话，那么好，用你的。如果没有，编译器就会根据atomic/nonatomic/retain/assign/copy这其中你指定的某几个规则去生成相应的getter和setter。 
