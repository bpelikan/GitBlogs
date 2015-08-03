---
layout: default
comments: true
category: code
tags: [productivity]
title: How to write post in github pages
---
---

## Description
This post is **not** for how to deploy the environment of writing posts in github pages, **but** how to use the environment you deployed before.

Assuming that you have deployed the following tools:

In Local:

* Jekyll
* Git
* MarkdownPad

In Remote:

* github repo

## To add a new post

1. git clone *https://github.com/hongchaozhang/GitBlogs.git*
2. go to *gh-pages* branch
3. open **_post** folder, add a new md file named like this: *2015-05-20-How-to-write-post-in-github-pages.md*. Notice: **DO NOT** leave any space in the file title.
4. use **MarkdownPad** in windows or **Macdown** in mac to open the md file you created, and put the yaml title on the top as follows (Note: three dashes at the top and bottom):

    \-\-\-<br>
    layout: default<br>
    comments: true<br>
    category: choose only one from /_data/categories.yml<br>
    tags: [tag1, tag2, ..., tagn] choose from /_data/tags.yml<br>
    title: How to write post in github pages<br>
    \-\-\-<br>
If you don't have a local MarkdownPad, you can use online tools to edit the md file, like [**stackedit**](https://stackedit.io/), a very powerful one. Five star recommended O(∩_∩)O~！

5. Add the content of the post. For Markdown grammar, refer [here](http://wowubuntu.com/markdown/) for Chinese version.
6. After complete the md file, you can directly push the md file to github repo, if you believe it has nothing wrong. 

For an alternative, you can using your local Jekyll to start a server and test the post you wrote. To do this:

1. Open cmd window.
2. Go to you post foler, for me, it is GitBlogs.
3. Start Jekyll server by running: *jekyll serve*
4. Open server address listed in cmd window, for me, it is *localhost:4000/GitBlogs*

## To add a new "category" or "tag"

If we want to add a new tag "java" into our blog, we should:

1. go to /blog/tag/ folder, and add a new file named "java.md";
2. add the following content into the new file:

	\-\-\-<br>
	layout: blog_by_tag<br>
	tag: java<br>
	permalink: /blog/tag/java/<br>
	\-\-\-<br>
3. go to /_data/ folder, and open tags.yml;
4. add the following content into tags.yml file (**NOTE** the indent and spaces):
	
	\- slug: java<br>
	name: java<br> 

For "category", it is similar.
	
## To make the post searchable by Google

Refer [here](http://www.reddit.com/r/web_design/comments/2qq4me/does_google_index_github_pages/).

Google crawls and ranks websites partially based on links to it from other websites. You should consider submitting it to some award websites, show-and-tells, etc to increase the value of the domain.

It can take a few days to a few months to be indexed, depending on several factors. It's recommended that you use the [submit URL](https://www.google.com/webmasters/tools/submit-url) tool, which may help speed up this process.
