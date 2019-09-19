## 示例代码

```php
mysql_connect('hostname', 'username', 'password');
// hostname:    mysql服务器的主机名（或IP），如果省略端口号，默认为3306
// username:    登录mysql数据库服务器的用户名
// password：   mysql服务器的用户密码

$con = mysql_connect("pipe-writer","pipe","pipe123",true);
if (!$con){
    die('Could not connect: ' . mysql_error());
}
// 选择数据库
mysql_select_db("pipe", $con);
// sql查询
$result = mysql_query("SELECT * FROM Persons", $con);
// 返回结果
while($row=mysql_fetch_array($result)) { 
    echo $row['FirstName'];
    echo $row['LastName'];
}
// 返回结果中行数
echo mysql_num_rows($result);
```

## 参考

- [PHP MySQL 函数](https://www.w3school.com.cn/php/php_ref_mysql.asp)

