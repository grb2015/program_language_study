/*
* @file 	:	Puppy.java
* @brief	:	构造函数
* @histroy	:   2017-06-25 16:33:51  renbin.guo created
* @note		:
* @usage	:
*/


/**
 * 	定义一个public 的Puppy类
 */
public class Puppy{

	/*类的成员变量*/
   int puppyAge;

   /*类的构造函数*/
   public Puppy(String name){
      // 这个构造器仅有一个参数：name
      System.out.println("小狗的名字是 : " + name ); 
   }
 
    /*类的成员函数*/
   public void setAge( int age ){
       puppyAge = age;
   }

 	 /*类的成员函数  */
   public int getAge( ){
       System.out.println("小狗的年龄为 : " + puppyAge ); 
       return puppyAge;
   }
 
 	 /*类的成员函数--主函数（进行测试）*/
   public static void main(String []args){
      /* 创建对象 */
      Puppy myPuppy = new Puppy( "tommy" );
      /* 通过方法来设定age */
      myPuppy.setAge( 2 );
      /* 调用另一个方法获取age */
      myPuppy.getAge( );
      /*你也可以像下面这样访问成员变量 */
      System.out.println("变量值 : " + myPuppy.puppyAge ); 
   }
}