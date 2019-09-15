## 插入数据 Create

```sql
INSERT INTO table_name (column_list) VALUES (values_list)
```
可以只向部分字段中插入值，而其他字段值为默认值

## 更新数据 Update

```sql
UPDATE table_name
SET column_name1 = value1, column_name2 = value2, ……
[ WHERE <condition> ];
```

## 删除数据 Delete

```sql
DELETE FROM table_name [ WHERE <condition> ];
```
如果省略了Where子句，将删除表中所有行，如果想删除所有行，可以使用速度更快的TRUNCATE TABLE语句。

## 查询数据 Read

SELECT语句关键字的执行顺序
```sql
(7)     SELECT 
(8)     DISTINCT <select_list>
(1)     FROM <left_table>
(3)     <join_type> JOIN <right_table>
(2)     ON <join_condition>
(4)     WHERE <where_condition>
(5)     GROUP BY <group_by_list>
(6)     HAVING <having_condition>
(9)     ORDER BY <order_by_condition>
(10)    LIMIT <limit_number>
```

#### ORDER BY
```
ORDER BY 字段名 ASC(默认) / DESC
```

#### LIMIT
```
LIMIT n         # 显示n条记录
LIMIT m, n      # 从m+1条记录开始显示n条记录
```

#### HAVING
- having语句通常与group by语句联合使用，用来过滤由group by语句返回的记录集
- having语句的存在弥补了where条件子句不能与聚合函数联合使用的不足，**where操作的是表中实际存在的字段，having操作的是聚合函数生成的显示列**

```sql
-- 找出平均攻击力大于105的国家的前2名,显示国家名称和平均攻击力
select country,avg(gongji) from sanguo
group by country
having avg(gongji) > 105
order by avg(gongji) DESC limit 2;
```

## 参考
- [mysql-语句查询执行顺序](https://www.cnblogs.com/52forjie/p/7825613.html)