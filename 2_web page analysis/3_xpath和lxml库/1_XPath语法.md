
1、“//”：表示选取所有子节点；如：//div    选取所有的div节点

2、 “/”：表示选取直接子节点；如：/body/div    选取body下的第一个div节点

3、“[]”：表示对节点进行筛选的条件

4、“@”：对节点进行筛选；如：//div[@id="abc"]    筛选所有id为abc的div节点
                    如：//div[@id]    筛选所有拥有id的div
                    如：//book[@price=10]     筛选price为10的book元素

5、“[1]”：下标, 下标是从1开始的；如/body/div[1]  选取第一个div

6、“[last()]”：选取最后一个节点

7、“[position()<3]”：选取位置；如：//div[position()<3]   选取前两个div，即：位置小于3的div

8、“[contains(@element, "str")]”：模糊筛选；如：//div[contains(@class, "abc")]   选取class属性中有“abc”的div标签

9、“*”：通配符；如：/body/*     获取body下所有的标签
   “@*”：     如：//div[@*]   获取所有拥有属性的div

10、“|”：选取多个; 如：/body/div[@class="abc"] | /body/div[@id="def"]   选取body下class=“abc”的div或body下id=“def”的div

11、常用运算符：=、!=、<、<=、>、>=、or、and,not() 可以在“[]”里面使用
