第一课
1.初识HTMLr context menu（txt文档右键可以直接用Sublime打开）。
    访问packagecontrol.io/installation选中适合版本的simple——Sublime中ctrl+~（查看-显示面板）将代码黏贴到下方代码行。
    prefernces中选择packagecontol——选择install package（ctrl+shift+p）——安装emment（html自动补全，会自动安装PYv8）、安装colorPicker(ctrl+shift+c或ctrl+shift+P输入colorPicker)、sublime Tmpl（模板、安装后文件选项中有new file sublime Tmpl）
    配置sublime Tmpl的模板——prefernces——浏览程序包（B）——sublime Tmpl——templates
    插件禁用与开启：
    右下方tab size 转换缩进为空格
    注释 ctrl+? 缩进Tab 取消缩进shift+Tab



第二课
1.图片标签<img src='http://xxxxx' alt='描述图片（爬虫找这个名字定义）' width'300' height='500' titlte='鼠标放在图片上会显示的字' />
    BMP:占用空间大色彩丰富，点阵图（位图格式）
    JPEG(JPG)：压缩方式通常是破坏数据性压缩，在压缩过程中图像的质量会受到破坏
    GIF：对透明色和多帧动画的支持
    PNG：无损压缩的位图格式，支持Alpha通道的透明/半透明特性
2.列表
    <h1>无序列表</h1> 
    <ul type='circle'>
        <li> 1 </li>
        <li> 2 </li>
    </ul>

    <h1>有序列表</h1>
    <ol type='a'>
        <li> 1 </li>
        <li> 2 </li>
    </ol>

    <h1>自定义列表</h1>
    <dl>
        <dt>1</dt>
        <dd>2</dd>
        <dt>a</dt>  titlte
        <dd>b</dd>
    </dl>
3.表格
    <table border='1'>
        <caption>
            <b>标题</b>
        </caption>
        <tr>行
            <th rowspan='2'（跨行，跨2行）>居中加粗</th>
            <th>居中加粗</th>
        </tr>行
        <tr>行
            <td>列</td>
            <td colspan='2'（跨列，跨2列）>列</td>
        </tr>行
    <table>
4.表格样式、RGB颜色十六转十
    <head>
        <style>
            tbody tr:hover{
                background: red;
                color:white;
            }
        </style>
    </head>
    <table>
        <thead>
            <tr>行
                <th rowspan='2'（跨行，跨2行）>居中加粗</th>
                 <th>居中加粗</th>
            </tr>行
        </thead>
        <tbody> 

        </tbody>

    </table>








ctrl+d 选中单词


第三课


























js是由unicode字符集编写的，完全支持中文。unicode是Ascii和lation-1超集
js注意事项：
    1.js严重区分大小写
    2.每段代码结束后需要加分号，表示他一句代码结束。
    3.构造函数首字母大写，驼峰原则
    4.函数命名首字母小写，驼峰原则
注释：
    //单行注释
    /*多行注释*/       
