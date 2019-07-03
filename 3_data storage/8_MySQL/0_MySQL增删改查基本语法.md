


        MySQL 增删该查基本语法：

            增：
                insert into 表名[(key1,key2, ...)] values(value1, value2, ...)

            删：
                delete from 表名 [where 条件]

                若没有条件则删除表内所有数据

            改：
                update 表名 set key1=value1,[key2=value2, ...] [where 条件]

                没有条件，则更新此字段的所有的值

            查：
                select 字段1,字段2,...或* from 表名 where 条件

                若是*则代表查询所有字段