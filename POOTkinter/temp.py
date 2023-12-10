Note: For more information, refer to Python Classes and Objects
Instance Method

Instance attributes are those attributes that are not shared by objects. Every object has its own copy of the instance attribute.

For example, consider a class shapes that have many objects like circle, square, triangle, etc. having its own attributes and methods. An instance attribute refers to the properties of that particular object like edge of the triangle being 3, while the edge of the square can be 4.

An instance method can access and even modify the value of attributes of an instance. It has one default parameter:-

    self – It is a keyword which points to the current passed instance. But it need not be passed every time while calling an instance method.