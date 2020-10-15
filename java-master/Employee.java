/*
* @file 	:	Employee.java
* @brief	: 	私有变量只能由成员函数来访问
* @histroy	:   2017-06-25 16:52:39  renbin.guo created
* @note		:
* @usage	:
*/
import java.io.*;
 
public class Employee {
    //salary是静态的私有变量
    private static double salary;

    // DEPARTMENT是一个常量
    public static final String DEPARTMENT = "开发人员";

    public static void main(String args[])
    {
   		salary = 10000;
        System.out.println(DEPARTMENT+"平均工资:"+salary);
    }
}