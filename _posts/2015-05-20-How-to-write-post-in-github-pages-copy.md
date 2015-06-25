---
layout: default
comments: true
title: How to write post in github pages
---

#{{page.title}}

##Description
插入两个中文看看行不行💖不信

This post is **not** for how to deploy the environment of writing posts in github pages, **but** how to use the environment you deployed before.

Assuming that you have deployed the following tools:

In Local:

* Jekyll
* Git
* MarkdownPad

In Remote:

* github repo

##To add a new post:

1. git clone *https://github.com/hongchaozhang/GitBlogs.git*
2. go to *gh-pages* branch
3. open **\_post** folder, add a new md file named like this: *2015-05-20-How-to-write-post-in-github-pages.md*. Notice: **DO NOT** leave any space in the file title.
4. use **MarkdownPad** to open the md file you created, and put the yaml title on the top as follows:

    \---<br>
    layout: default<br>
    comments: true<br>
    title: How to write post in github pages<br>
    \---<br>
If you don't have a local MarkdownPad, you can use online tools to edit the md file, like [**stackedit**](https://stackedit.io/), a very powerful one. Five star recommended O(∩_∩)O~！

5. Add the content of the post. For Markdown grammar, refer [here](http://wowubuntu.com/markdown/) for Chinese version.
6. After complete the md file, you can directly push the md file to github repo, if you believe it has nothing wrong. 

For an alternative, you can using your local Jekyll to start a server and test the post you wrote. To do this:

1. Open cmd window.
2. Go to you post foler, for me, it is GitBlogs.
3. Start Jekyll server by running: *jekyll serve*
4. Open server address listed in cmd window, for me, it is *localhost:4000/GitBlogs*