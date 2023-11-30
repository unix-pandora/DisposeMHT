# Dispose MHT

<hr>

有时候会从浏览器离线保存一些网页文件，但这些文件是 mht 格式的。该项目是解决：先将它们转为 html，接着从 html 内容中根据 CSS 选择器，提取指定标签中的属性值，再根据获得的值抓取网络资源，保存在本地文件夹之内

<hr>

- Main.Index: core.pivot

<hr>

# Attention

运行项目时，必须进入到 Index 所在的当前目录，执行`python $[Index].py`，而不是执行`python src/$[Index].py`

<hr>