---
layout: default
title: How to Add a Clone function to Function?
---
####add clone functon to Function:
    
    Function.prototype.clone = function() {
        var that = this;
        var temp = function temporary() { return that.apply(this, arguments); };
        for( key in this ) {
            temp[key] = this[key];
        }
        return temp;
    };