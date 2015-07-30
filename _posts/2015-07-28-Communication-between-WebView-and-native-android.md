---
layout: default
comments: true
category: code
tags: [android, java]
title: Communication between WebView and native android
---
---

[Java和Javascript安全交互](http://jiajixin.cn/2014/09/16/webview-js-safety/)

[android develop javascript bridge example fully explained]()

## Description

In Android project, we sometimes want to rend a page in **WebView**, and need communication between webview and native android side.

**Note:** Go to [here]() for a project as a sample.

## Javascript and Java Bridge

code for javascript interface in native android side:

    public class JavaScriptInterface {
        protected MyActivity parentActivity;
        protected WebView mWebView;
        
        
        public JavaScriptInterface(MyActivity _activity, WebView _webView)  {
            parentActivity = _activity;
            mWebView = _webView;
            
        }
        
        @JavascriptInterface
        public void setResult(int val){
            Log.v("mylog","JavaScriptHandler.setResult is called : " + val);
            this.parentActivity.javascriptCallFinished(val);
        }
        
        @JavascriptInterface
        public void calcSomething(int x, int y){
            this.parentActivity.changeText("Result is : " + (x * y));
        }
    }

Here, we can introduce the main activity `parentActivity` and the webview `mWebView` into the interface for further use.

get webview and config it:

    myWebView = (WebView)this.findViewById(R.id.myWebView);
    myWebView.getSettings().setJavaScriptEnabled(true);
    myWebView.loadUrl("file:///android_asset/index.html");

    myWebView.addJavascriptInterface(new JavaScriptInterface(this, myWebView), "MyHandler");
    if(Build.VERSION.SDK_INT >= Build.VERSION_CODES.KITKAT) {
	    WebView.setWebContentsDebuggingEnabled(true);
	}
	
Then we can use the following way to call javascript function and change html page from java side:

    myWebView.loadUrl("javascript:document.getElementById('test1').innerHTML = 'changed'");
    
And use the following to call java method from javascript side:

    window.MyHandler.setResult(9999)

## code with parameters


We can only send string by `WebView.loadUrl()` function, and the parameters must be put into the *string*:

    myWebView.loadUrl("javascript:window.MyHandler.setResult( addSomething("+val1+","+val2+") )");

## cope with `return` value

### Java return value to Javascript: **sync**

Java can directly return String back to Javascritp, so we can use the following way to get the string from Java:

    var string = window.MyHandler.testString();

### Javascript return value to Java: **async**

As `WebView.loadUrl` does not return anything, so Java can not get results from Javascript. We need other ways to get the result.

## Multi-thread in Java side and Single-thread in Javascript side

### Javascript call Java: sync

When we run the following function, we can get the string returned from java side, and then set it into the html page.

    function testSync() {
    	var string = "default string";
    	string = window.MyHandler.testString();
    	document.getElementById('test1').innerHTML = string;
    }

### Java call Javascript: async

## Security problems