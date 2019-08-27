/*
* @file 	:	FreshJuiceTest.java
* @author	: 	renbin.guo	
* @histroy	:   	2017-06-25 11:57:27  renbin.guo created
* @note		:
* @usage	:
* 			
* 			[root@localhost java]# javac  FreshJuiceTest.java 
* 			[root@localhost java]# java FreshJuiceTest
*
* 			[root@localhost javaclass]# java FreshJuiceTest
* 			juice.size = MEDIUM
* 			[root@localhost javaclass]# 
*
*
* 			
*/

/*
	建立一个FreshJuice类，其成员只有一个FreshJuiceSize的枚举类型
 */
class	FreshJuice
{
	enum	FreshJuiceSize
	{
		SMALL,
		MEDIUM,
		LARGE
	}

	FreshJuiceSize size;       // 类的成员
}

/*
		建立一个FreshJuiceTest类，它包含了main函数。
 */
public class FreshJuiceTest 
{

    // 这里的main函数可看做FreshJuiceTest的成员，成员函数而已
    public static void main(String[] args) 
    {
    	// 创建一个FreshJuice对象 ，juice
    	FreshJuice juice = new FreshJuice();

    	// 对juice的成员size进行赋值，需要注意的是
    	// 这里赋值不是我们给定的常数，而是用的一个类的!!
    	juice.size = FreshJuice.FreshJuiceSize.MEDIUM;


    	//System.out.printf("juice.size = %d",juice.size);	//这种用法报错了。
    	System.out.println("juice.size = "+juice.size);

    }
}


