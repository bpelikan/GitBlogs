
# add -category category_name
# add -tag tag_name

import sys

#print "\n".join(sys.argv)

argCount = len(sys.argv)

if argCount != 3:
	print "For adding category, use 'python add.py -category category_name'"
	print "For adding tag, use 'python add.py -tag tag_name'"
else:
	typeString = sys.argv[1] # -category or -tag
	typeName = sys.argv[2] # category / tag name
	if typeString == "-category":
		catFile = open("../_data/categories.yml", "a")
		catFile.writelines(["\n- slug: " + typeName, "\n  name: " + typeName, "\n  color: " + "'#FFFFFF'" + "\n"])
		catFile.close()

		catFile = open("../blog/category/" + typeName + ".md", "w")
		catFile.writelines(["---", "\nlayout: blog_by_category", "\ncat: " + typeName, "\npermalink: /blog/category/" + typeName + "/", "\n---" + "\n"])
		catFile.close();

		print "Category: " + typeName + " is added successfully."
	elif typeString == "-tag":
		catFile = open("../_data/tags.yml", "a")
		catFile.writelines(["\n- slug: " + typeName, "\n  name: " + typeName + "\n"])
		catFile.close()

		catFile = open("../blog/tag/" + typeName + ".md", "w")
		catFile.writelines(["---", "\nlayout: blog_by_tag" + "\ntag: " + typeName + "\npermalink: /blog/tag/" + typeName + "/", "\n---" + "\n"])
		catFile.close()

		print "Tag: " + typeName + " is added successfully."
	else:
		print "For adding category, use 'python add.py -category category_name'"
		print "For adding tag, use 'python add.py -tag tag_name'"

	
