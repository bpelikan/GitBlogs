---
layout: default
comments: true
category: code
tags: [productivity]
title: How to deploy MicroStrategy iOS Mobile environment
---
---

Currently, MicroStrategy Mobile code is in [**github**](http://github-mstr.labs.microstrategy.com/). To deploy the environment, you should:

1.  git clone *http://github-mstr.labs.microstrategy.com/MSTRMobile/Mobile.git*
2.  Copy **"Engine"** folder from somewhere else to **"Mobile"** folder you just cloned. **"Engine"** folder can be found in previous clearcase branch.
3.  Open the xcode project here: *Mobile-->Mobile_Client-->iOS-->MicroStrategyMobile-->MicroStrategyMobile.xcodeproj*